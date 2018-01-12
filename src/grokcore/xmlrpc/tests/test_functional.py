import doctest
import grokcore.xmlrpc
import re
import unittest
import zope.app.wsgi.testlayer
import zope.testbrowser.wsgi

from pkg_resources import resource_listdir
from zope.app.wsgi._compat import httpclient, xmlrpcclient
from zope.testing import renormalizing


class Layer(
        zope.testbrowser.wsgi.TestBrowserLayer,
        zope.app.wsgi.testlayer.BrowserLayer):
    pass


layer = Layer(grokcore.xmlrpc, allowTearDown=True)


checker = renormalizing.RENormalizing([
    # Accommodate to exception wrapping in newer versions of mechanize
    (re.compile(r'httperror_seek_wrapper:', re.M), 'HTTPError:'),
    ])


class XMLRPCTestTransport(xmlrpcclient.Transport):
    verbose = False
    wsig_app = None

    def request(self, host, handler, request_body, verbose=0):
        request = "POST %s HTTP/1.0\n" % (handler,)
        request += "Content-Length: %i\n" % len(request_body)
        request += "Content-Type: text/xml\n"

        host, extra_headers, x509 = self.get_host_info(host)
        if extra_headers:
            request += "Authorization: %s\n" % (
                dict(extra_headers)["Authorization"],)

        request += "\n"
        request += request_body.decode()
        response = zope.app.wsgi.testlayer.http(
            self.wsgi_app(), request.encode())
        errcode = response.getStatus()
        errmsg = response.getStatusString()
        headers = response.getHeaders()

        if errcode != 200:
            raise xmlrpcclient.ProtocolError(
                host + handler,
                errcode, errmsg,
                headers
                )

        res = httpclient.HTTPResponse(
            zope.app.wsgi.testlayer.FakeSocket(response.getOutput()))
        res.begin()
        return self.parse_response(res)


def suiteFromPackage(name):
    layer_dir = 'functional'
    files = resource_listdir(__name__, '{}/{}'.format(layer_dir, name))
    suite = unittest.TestSuite()
    for filename in files:
        if not filename.endswith('.py'):
            continue
        if filename == '__init__.py':
            continue

        dottedname = 'grokcore.xmlrpc.tests.%s.%s.%s' % (
            layer_dir, name, filename[:-3])
        transport = XMLRPCTestTransport()
        transport.wsgi_app = layer.make_wsgi_app
        test = doctest.DocTestSuite(
            dottedname,
            checker=checker,
            extraglobs=dict(
                getRootFolder=layer.getRootFolder,
                transport=transport,
                ),
            optionflags=(
                doctest.ELLIPSIS +
                doctest.NORMALIZE_WHITESPACE +
                doctest.REPORT_NDIFF +
                renormalizing.IGNORE_EXCEPTION_MODULE_IN_PYTHON2
                ))
        test.layer = layer

        suite.addTest(test)
    return suite


def test_suite():
    suite = unittest.TestSuite()
    for name in ['xmlrpc']:
        suite.addTest(suiteFromPackage(name))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
