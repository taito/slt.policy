from collective.cart.shopping.tests.base import IntegrationTestCase as BaseIntegrationTestCase
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import unittest


class SltPolicyLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        # Required by Products.CMFPlone:plone-content to setup defaul plone site.
        z2.installProduct(app, 'Products.PythonScripts')
        z2.installProduct(app, 'Products.ATCountryWidget')
        # Load ZCML
        import collective.cart.shopping
        self.loadZCML(package=collective.cart.shopping)
        z2.installProduct(app, 'collective.cart.shopping')
        z2.installProduct(app, 'collective.cart.shipping')
        import z3c.jbot
        self.loadZCML(package=z3c.jbot)
        import plonetheme.sunburst
        self.loadZCML(package=plonetheme.sunburst)
        import slt.theme
        self.loadZCML(package=slt.theme)
        import slt.policy
        self.loadZCML(package=slt.policy)

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        # Install into Plone site using portal_setup

        # Installs all the Plone stuff. Workflows etc. to setup defaul plone site.
        self.applyProfile(portal, 'Products.CMFPlone:plone')

        # Install portal content. Including the Members folder! to setup defaul plone site.
        self.applyProfile(portal, 'Products.CMFPlone:plone-content')

        self.applyProfile(portal, 'plonetheme.sunburst:default')
        self.applyProfile(portal, 'collective.cart.shopping:default')
        self.applyProfile(portal, 'slt.policy:default')

    def tearDownZope(self, app):
        """Tear down Zope."""
        z2.uninstallProduct(app, 'collective.cart.shipping')
        z2.uninstallProduct(app, 'collective.cart.shopping')
        z2.uninstallProduct(app, 'ATCountryWidget')
        z2.uninstallProduct(app, 'Products.PythonScripts')


FIXTURE = SltPolicyLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="SltPolicyLayer:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name="SltPolicyLayer:Functional")


class IntegrationTestCase(BaseIntegrationTestCase):
    """Base class for integration tests."""

    layer = INTEGRATION_TESTING


class FunctionalTestCase(unittest.TestCase):
    """Base class for functional tests."""

    layer = FUNCTIONAL_TESTING
