from zope.interface import implements
from zope.viewlet.interfaces import IViewlet


from plone.app.viewletmanager.manager import OrderedViewletManager

from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class BottomFeederViewlet(BrowserView):
    """ This viewlet is registered for and rendered inside the IPortalFooter
        viewletmanager. It's sole purpose is to render the
        BottomFeederViewletManager.
    """
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
    """ Any links or widgets that should appear in the bottom.feeder panel must
        be registered as viewlets for this viewletmanager.
    """
    template = ViewPageTemplateFile('templates/bottomfeeder.pt')


class ViewletMixin:
    """ Utility methods for viewlets
    """
    def member(self):
        portal_membership = getToolByName(self.context, 'portal_membership')
        return portal_membership.getAuthenticatedMember()

    def portal_url(self):
        portal_url = getToolByName(self.context, 'portal_url')
        return portal_url()



class HomeViewlet(BrowserView, ViewletMixin):
    """ """
    implements(IViewlet)

    def __init__(self, context, request, view, manager):
        super(HomeViewlet, self).__init__(context, request)
        self.__parent__ = view
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager

    def update(self):
        pass


class UserViewlet(BrowserView, ViewletMixin):
    """ """
    implements(IViewlet)

    def __init__(self, context, request, view, manager):
        super(UserViewlet, self).__init__(context, request)
        self.__parent__ = view
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager

    def update(self):
        pass


class PersonalizeViewlet(BrowserView, ViewletMixin):
    """ """
    implements(IViewlet)

    def __init__(self, context, request, view, manager):
        super(PersonalizeViewlet, self).__init__(context, request)
        self.__parent__ = view
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager

    def update(self):
        pass


class MembersViewlet(BrowserView, ViewletMixin):
    """ """
    implements(IViewlet)

    def __init__(self, context, request, view, manager):
        super(MembersViewlet, self).__init__(context, request)
        self.__parent__ = view
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager

    def update(self):
        pass


class NewsViewlet(BrowserView, ViewletMixin):
    """ """
    implements(IViewlet)

    def __init__(self, context, request, view, manager):
        super(NewsViewlet, self).__init__(context, request)
        self.__parent__ = view
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager

    def update(self):
        pass


