"""
A permission has to be defined first (using grok.Permission for example)
before it can be used in grok.require() in an XMLRPC class.

  >>> from grokcore.xmlrpc import testing

  # PY2 - remove '+IGNORE_EXCEPTION_DETAIL'  when dropping Python 2 support:
  >>> testing.grok(__name__)  # doctest: +IGNORE_EXCEPTION_DETAIL
  Traceback (most recent call last):
  ...
  zope.configuration.config.ConfigurationExecutionError: \
  martian.error.GrokError: Undefined permission 'doesnt.exist' in \
  <class 'grokcore.xmlrpc.tests.base.xmlrpc.missing_permission.MissingPermission'>.\
  Use grok.Permission first...

"""  # noqa: E501 line too long

import zope.interface
import grokcore.xmlrpc
import grokcore.security
import grokcore.component as grok


class MissingPermission(grokcore.xmlrpc.XMLRPC):
    grok.context(zope.interface.Interface)
    grokcore.security.require('doesnt.exist')

    def foo(self):
        pass
