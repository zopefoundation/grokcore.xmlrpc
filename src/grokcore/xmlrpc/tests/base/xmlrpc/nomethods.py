"""
  >>> from grokcore.xmlrpc import testing
  >>> testing.grok(__name__)
  Traceback (most recent call last):
    ...
  martian.error.GrokError: \
  <class 'grokcore.xmlrpc.tests.base.xmlrpc.nomethods.RemoteCaveman'> does not \
  define any public methods. Please add methods to this class to enable \
  its registration.

"""  # noqa: E501 line too long
import grokcore.component as grok
import grokcore.xmlrpc


class Caveman(grok.Context):
    pass


class RemoteCaveman(grokcore.xmlrpc.XMLRPC):
    pass
