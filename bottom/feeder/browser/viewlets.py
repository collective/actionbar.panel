from zope.interface import implements
from zope.viewlet.interfaces import IViewlet

from plone.app.viewletmanager.manager import OrderedViewletManager

from Products.CMFPlone.utils import safe_unicode
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class BottomFeederViewlet(BrowserView):
    """ """
    template = ViewPageTemplateFile('templates/bottomfeeder_viewlet.pt')
    
    def __init__(self, context, request, view, manager):
        super(BottomFeederViewlet, self).__init__(context, request)
        self.__parent__ = view
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager

    def render(self):
        return self.template()


class BottomFeederViewletManager(OrderedViewletManager):
    """ """
    template = ViewPageTemplateFile('templates/bottomfeeder.pt')

    def member(self):
        portal_membership = getToolByName(self.context, 'portal_membership')
        return portal_membership.getAuthenticatedMember()

    def portal_url(self):
        portal_url = getToolByName(self.context, 'portal_url')
        return portal_url()

    def render(self):
        return self.template()


class RecentActivityViewlet(BrowserView):
    implements(IViewlet)

    def __init__(self, context, request, view, manager):
        super(RecentActivityViewlet, self).__init__(context, request)
        self.__parent__ = view
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager

    def update(self):
        pass

    def render(self):
        snippet = safe_unicode("HELLO")
        return snippet

