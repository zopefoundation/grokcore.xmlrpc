##############################################################################
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
"""Base classes for Grok application components.

When an application developer builds a Grok-based application, the
classes they define each typically inherit from one of the base classes
provided here.

"""

import grokcore.view

from zope import interface


class XMLRPC(grokcore.view.ViewSupport):
    """Base class for XML-RPC endpoints in Grok applications.

    When an application creates a subclass of `grok.XMLRPC`, it is
    creating an XML-RPC view.  Like other Grok views, each `grok.XMLRPC`
    component can either use an explicit `grok.context()` directive to
    specify the kind of object it wraps, or else Grok will look through
    the same module for exactly one `grok.Model` or `grok.Container` (or
    other `IGrokContext` implementor) and make that class its context
    instead.

    Every object that is an instance of the wrapped class or interface
    becomes a legitimate XML-RPC server URL, offering as available
    procedures whatever methods have been defined inside of that
    `grok.XMLRPC` component.  When a method is called over XML-RPC, any
    parameters are translated into normal Python data types and supplied
    as normal positional arguments.  When the method returns a value or
    raises an exception, the result is converted back into an XML-RPC
    response for the client.  In both directions, values are marshalled
    transparently to and from XML-RPC data structures.

    During the execution of an XML-RPC method, the object whose URL was
    used for the XML-RPC call is available as ``self.context``.

    """
    interface.implements(grokcore.view.IGrokSecurityView)
