import unittest
from zope import component

from Testing import ZopeTestCase as ztc

from Products.Archetypes.Schema.factory import instanceSchemaFactory
from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase import layer

from plone import browserlayer

from bottom.feeder.browser.viewlets import BottomFeederViewlet
from bottom.feeder.browser.viewlets import HomeViewlet
from bottom.feeder.browser.viewlets import UserViewlet
from bottom.feeder.browser.viewlets import PersonalizeViewlet
from bottom.feeder.browser.viewlets import MembersViewlet
from bottom.feeder.browser.viewlets import NewsViewlet
from bottom.feeder.browser.interfaces import IBottomFeederLayer

import bottom.feeder
ztc.installProduct('bottom.feeder')
ztc.installPackage(bottom.feeder)
SiteLayer = layer.PloneSite

class BottomFeederLayer(SiteLayer):

    @classmethod
    def setUp(cls):
        PRODUCTS = ['bottom.feeder', ]
        ptc.setupPloneSite(products=PRODUCTS)

        fiveconfigure.debug_mode = True
        zcml.load_config('configure.zcml', bottom.feeder)
        fiveconfigure.debug_mode = False

        browserlayer.utils.register_layer(
                                IBottomFeederLayer, 
                                name='bottom.feeder')

        component.provideAdapter(instanceSchemaFactory)
        SiteLayer.setUp()

class TestCase(ptc.PloneTestCase):
    """Base class used for test cases
    """
    layer = BottomFeederLayer


class TestViewlets(TestCase):
    """ """

    def test_bottomfeederviewlet(self):
        """ """
        request = self.app.REQUEST
        context = self.portal
        viewlet = BottomFeederViewlet(context, request, None, None)
        # XXX: This throws a componentProviderLookupError, so for some reason
        # the BottomFeederViewletManager is not being registered for the tests.
        # I, however, have no idea why :(
        # self.assertEqual(type(viewlet.render(), str))

    def test_homeviewlet(self):
        """ """
        request = self.app.REQUEST
        context = self.portal
        viewlet = HomeViewlet(context, request, None, None)
        viewlet.update()

    def test_userviewlet(self):
        """ """
        request = self.app.REQUEST
        context = self.portal
        viewlet = UserViewlet(context, request, None, None)
        viewlet.update()

    def test_personalizeviewlet(self):
        """ """
        request = self.app.REQUEST
        context = self.portal
        viewlet = PersonalizeViewlet(context, request, None, None)
        viewlet.update()

    def test_membersviewlet(self):
        """ """
        request = self.app.REQUEST
        context = self.portal
        viewlet = MembersViewlet(context, request, None, None)
        viewlet.update()

    def test_newsviewlet(self):
        """ """
        request = self.app.REQUEST
        context = self.portal
        viewlet = NewsViewlet(context, request, None, None)
        viewlet.update()


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestViewlets))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')


