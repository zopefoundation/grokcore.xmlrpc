"""
  >>> from grokcore.xmlrpc import testing
  >>> testing.grok(__name__)
  Traceback (most recent call last):
    ...
  GrokError: <class 'grokcore.xmlrpc.tests.xmlrpc.nomethods.RemoteCaveman'> does not
  define any public methods. Please add methods to this class to enable
  its registration.

"""
import grokcore.component as grok
import grokcore.xmlrpc

class Caveman(grok.Context):
    pass

class RemoteCaveman(grokcore.xmlrpc.XMLRPC):
    pass
