"""
A permission has to be defined first (using grok.Permission for example)
before it can be used in @grok.require().

  >>> from grokcore.xmlrpc import testing
  >>> testing.grok(__name__)
  Traceback (most recent call last):
  ...
  ConfigurationExecutionError: martian.error.GrokError: Undefined permission
  'doesnt.exist' in <class 'grokcore.xmlrpc.tests.xmlrpc.missing_permission2.MissingPermission'>. Use grok.Permission first.
  ...

"""

import grokcore.component as grok
import grokcore.security
import grokcore.xmlrpc
import zope.interface

class MissingPermission(grokcore.xmlrpc.XMLRPC):
    grok.context(zope.interface.Interface)

    @grokcore.security.require('doesnt.exist')
    def foo(self):
        pass

