from plone.app.viewletmanager.manager import OrderedViewletManager
from plone.app.layout.viewlets.common import ViewletBase

from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class ActionbarPanelViewlet(ViewletBase):
    """ This viewlet is registered for and rendered inside the IPortalFooter
        viewletmanager. It's sole purpose is to render the
        ActionbarPanelViewletManager.
    """
    index = ViewPageTemplateFile('templates/actionbar_viewlet.pt')
    

class ActionbarPanelViewletManager(OrderedViewletManager):
    """ Any links or widgets that should appear in the actionbar.panel panel must
        be registered as viewlets for this viewletmanager.
    """
    template = ViewPageTemplateFile('templates/actionbar.pt')


class ViewletMixin:
    """ Utility methods for viewlets
    """
    def member(self):
        portal_membership = getToolByName(self.context, 'portal_membership')
        return portal_membership.getAuthenticatedMember()

    def portal_url(self):
        portal_url = getToolByName(self.context, 'portal_url')
        return portal_url()


class ActionViewlet(ViewletBase, ViewletMixin):
    """ """

