"""
A permission has to be defined first (using grok.Permission for
example) before it can be used in grok.require() in an XMLRPC
class. However, this is *not* the the case for a default permission
that is never used.

  >>> from grokcore.xmlrpc import testing
  >>> testing.grok(__name__)

"""

import grokcore.component as grok
import grokcore.security
import grokcore.xmlrpc
import zope.interface

class Foo(grokcore.security.Permission):
    grok.name('foo')

class MissingPermission(grokcore.xmlrpc.XMLRPC):
    grok.context(zope.interface.Interface)
    grokcore.security.require('doesnt.exist')

    @grokcore.security.require(Foo)
    def foo(self):
        pass
