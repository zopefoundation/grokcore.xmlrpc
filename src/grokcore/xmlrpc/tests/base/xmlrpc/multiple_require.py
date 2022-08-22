"""
Multiple calls of grok.require in one class are not allowed.

  >>> from grokcore.xmlrpc import testing
  >>> testing.grok(__name__)
  Traceback (most recent call last):
     ...
  martian.error.GrokError: grok.require was called multiple times in \
  <class 'grokcore.xmlrpc.tests.base.xmlrpc.multiple_require.MultipleXMLRPC'>. \
  It may only be set once for a class.
"""  # noqa: E501 line too long
import grokcore.component as grok
import grokcore.security
import zope.interface

import grokcore.xmlrpc


class One(grokcore.security.Permission):
    grok.name('permission.1')


class Two(grokcore.security.Permission):
    grok.name('permission.2')


class MultipleXMLRPC(grokcore.xmlrpc.XMLRPC):
    grok.context(zope.interface.Interface)
    grokcore.security.require(One)
    grokcore.security.require(Two)

    def render(self):
        pass
