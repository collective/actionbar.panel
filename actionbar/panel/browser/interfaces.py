from zope.interface import Interface
from zope.viewlet.interfaces import IViewletManager
    
class IBottomFeeder(IViewletManager):
    """A viewlet manager that sits at the bottom of the page
    """

class IBottomFeederLayer(Interface):
    """Marker Interface for a custom BrowserLayer
    """
