import doctest
import http.client
import unittest
import xmlrpc.client

from pkg_resources import resource_listdir

import zope.app.wsgi.testlayer
import zope.testbrowser.wsgi

import grokcore.xmlrpc


class Layer(
        zope.testbrowser.wsgi.TestBrowserLayer,
        zope.app.wsgi.testlayer.BrowserLayer):
    pass


layer = Layer(grokcore.xmlrpc, allowTearDown=True)


class XMLRPCTestTransport(xmlrpc.client.Transport):
    verbose = False
    wsig_app = None

    def request(self, host, handler, request_body, verbose=0):
        request = f"POST {handler} HTTP/1.0\n"
        request += "Content-Length: %i\n" % len(request_body)
        request += "Content-Type: text/xml\n"

        host, extra_headers, x509 = self.get_host_info(host)
        if extra_headers:
            request += "Authorization: {}\n".format(
                dict(extra_headers)["Authorization"])

        request += "\n"
        request += request_body.decode()
        response = zope.app.wsgi.testlayer.http(
            self.wsgi_app(), request.encode())
        errcode = response.getStatus()
        errmsg = response.getStatusString()
        headers = response.getHeaders()

        if errcode != 200:
            raise xmlrpc.client.ProtocolError(
                host + handler,
                errcode, errmsg,
                headers
            )

        res = http.client.HTTPResponse(
            zope.app.wsgi.testlayer.FakeSocket(response.getOutput()))
        res.begin()
        return self.parse_response(res)


def suiteFromPackage(name):
    layer_dir = 'functional'
    files = resource_listdir(__name__, f'{layer_dir}/{name}')
    suite = unittest.TestSuite()
    for filename in files:
        if not filename.endswith('.py'):
            continue
        if filename == '__init__.py':
            continue

        dottedname = 'grokcore.xmlrpc.tests.{}.{}.{}'.format(
            layer_dir, name, filename[:-3])
        transport = XMLRPCTestTransport()
        transport.wsgi_app = layer.make_wsgi_app
        test = doctest.DocTestSuite(
            dottedname,
            extraglobs=dict(
                getRootFolder=layer.getRootFolder,
                transport=transport,
            ),
            optionflags=(
                doctest.ELLIPSIS +
                doctest.NORMALIZE_WHITESPACE +
                doctest.REPORT_NDIFF +
                doctest.IGNORE_EXCEPTION_DETAIL
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
