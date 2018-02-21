"""
  >>> from zope.app.wsgi.testlayer import XMLRPCServerProxy
  >>> server = XMLRPCServerProxy("http://localhost/", transport=transport)
  >>> mgr_server = XMLRPCServerProxy("http://mgr:mgrpw@localhost/", transport=transport)

We can access a public method just fine, but a protected method will
raise Unauthorized:

  >>> print(server.stomp())
  Manfred stomped.

  >>> print(server.dance())
  Traceback (most recent call last):
  xmlrpc.client.ProtocolError: <ProtocolError for localhost/: 401 401 Unauthorized>

With manager privileges, the protected method is accessible, however:

  >>> print(mgr_server.dance())
  Manfred doesn't like to dance.

The same applies when a default permission is defined for all XML-RPC
methods in a class:

  >>> print(server.hunt())
  Traceback (most recent call last):
  xmlrpc.client.ProtocolError: <ProtocolError for localhost/: 401 401 Unauthorized>

  >>> print(mgr_server.hunt())
  ME GROK LIKE MAMMOTH!

  >>> print(server.eat())
  MMM, MANFRED TASTE GOOD!

  >>> print(server.rest())
  ME GROK TIRED!
"""
import grokcore.component as grok
import grokcore.xmlrpc
import grokcore.security
import zope.interface

class MammothRPC(grokcore.xmlrpc.XMLRPC):
    grok.context(zope.interface.Interface)

    def stomp(self):
        return 'Manfred stomped.'

    @grokcore.security.require('zope.ManageContent')
    def dance(self):
        return 'Manfred doesn\'t like to dance.'

class CavemanRPC(grokcore.xmlrpc.XMLRPC):
    grok.context(zope.interface.Interface)
    grokcore.security.require('zope.ManageContent')

    def hunt(self):
        return 'ME GROK LIKE MAMMOTH!'

    @grokcore.security.require('zope.View')
    def eat(self):
        return 'MMM, MANFRED TASTE GOOD!'

    @grokcore.security.require(grokcore.security.Public)
    def rest(self):
        return 'ME GROK TIRED!'
