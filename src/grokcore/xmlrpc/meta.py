#############################################################################
#
# Copyright (c) 2006-2007 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Grokkers for Grok-configured components.

This `meta` module contains the actual grokker mechanisms for which the
Grok web framework is named.  A directive in the adjacent `meta.zcml`
file directs the `martian` library to scan this file, where it discovers
and registers the grokkers you see below.  The grokkers are then active
and available as `martian` recursively examines the packages and modules
of a Grok-based web application.

"""
from zope.publisher.interfaces.xmlrpc import IXMLRPCRequest
from grokcore.view import make_checker

import martian
import grokcore.component
import grokcore.component.util
import grokcore.security
import grokcore.xmlrpc

from zope import interface, component
from zope.publisher.xmlrpc import XMLRPCView
from zope.location import Location


class MethodPublisher(XMLRPCView, Location):
    """Copied from zope.app.publisher.xmlrpc to get rid of that dependency.
    """
    def __getParent(self):
        return hasattr(self, '_parent') and self._parent or self.context

    def __setParent(self, parent):
        self._parent = parent

    __parent__ = property(__getParent, __setParent)


class XMLRPCGrokker(martian.MethodGrokker):
    """Grokker for methods of a `grok.XMLRPC` subclass.

    When an application defines a `grok.XMLRPC` view, we do not actually
    register the view with the Component Architecture.  Instead, we grok
    each of its methods separately, placing them each inside of a new
    class that we create on-the-fly by calling `type()`.  We make each
    method the `__call__()` method of its new class, since that is how
    Zope always invokes views.  And it is this new class that is then
    made the object of the two configuration actions that we schedule:
    one to activate it as an XML-RPC adapter for the context, and the
    other to prepare a security check for the adapter.

    """
    martian.component(grokcore.xmlrpc.XMLRPC)
    martian.directive(grokcore.component.context)
    martian.directive(grokcore.security.require, name='permission')

    def execute(self, factory, method, config, context, permission, **kw):
        name = method.__name__

        # Make sure that the class inherits MethodPublisher, so that the
        # views have a location
        method_view = type(
            factory.__name__, (factory, MethodPublisher),
            {'__call__': method})

        adapts = (context, IXMLRPCRequest)
        config.action(
            discriminator=('adapter', adapts, interface.Interface, name),
            callable=grokcore.component.util.provideAdapter,
            args=(method_view, adapts, interface.Interface, name),
            )
        config.action(
            discriminator=('protectName', method_view, '__call__'),
            callable=make_checker,
            args=(factory, method_view, permission),
            )
        return True
