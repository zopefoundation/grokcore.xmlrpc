##############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
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
"""Grok publication factories and classes.

These factories, and the publication classes they return, make Grok
security different from the way that security normal operates during
Zope publication.  Instead of security proxies being wrapped around
every object generated during traversal, and then wrapped around the
final object before it is viewed, only a single security check is done
when Grok is in charge: a check to see whether the view selected at the
end of the traversal process is, in fact, permitted to display the
object.

"""
from grokcore.view.publication import ZopePublicationSansProxy
from zope.app.publication.http import BaseHTTPPublication
from zope.app.publication.requestpublicationfactories import XMLRPCFactory


class GrokXMLRPCPublication(ZopePublicationSansProxy, BaseHTTPPublication):
    """Combines `BaseHTTPPublication` with the Grok sans-proxy mixin."""


class GrokXMLRPCFactory(XMLRPCFactory):
    """Returns the classes Grok uses for browser requests and publication.

    When an instance of this class is called, it returns a 2-element
    tuple containing:

    - The request class that Grok uses for XML-RPC requests.
    - The publication class that Grok uses to publish to a XML-RPC.

    """
    def __call__(self):
        request, publication = super(GrokXMLRPCFactory, self).__call__()
        return request, GrokXMLRPCPublication
