"""

Context-determination follows the same rules as for adapters. We just check
whether it's hooked up at all:

  >>> from grokcore.xmlrpc import testing
  >>> testing.grok(__name__)
  Traceback (most recent call last):
  ...
  martian.error.GrokError: No module-level context for \
  <class 'grokcore.xmlrpc.tests.base.xmlrpc.nocontext.HomeRPC'>, please use the \
  'context' directive.

"""  # noqa: E501 line too long
import grokcore.xmlrpc


class HomeRPC(grokcore.xmlrpc.XMLRPC):

    def foo(self):
        pass
