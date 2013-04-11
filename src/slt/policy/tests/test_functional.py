# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from Testing import ZopeTestCase as ztc
from hexagonit.testing.browser import Browser
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import TEST_USER_PASSWORD
from plone.app.testing import setRoles
from plone.testing import layered
from slt.policy.tests.base import FUNCTIONAL_TESTING
from zope.lifecycleevent import modified
from zope.testing import renormalizing

import doctest
import manuel.codeblock
import manuel.doctest
import manuel.testing
import re
import transaction
import unittest

FLAGS = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS | doctest.REPORT_NDIFF | doctest.REPORT_ONLY_FIRST_FAILURE

CHECKER = renormalizing.RENormalizing([
    # Normalize the generated UUID values to always compare equal.
    (re.compile(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'), '<UUID>'),
])


# def prink(e):
#     print eval('"""{0}"""'.format(str(e)))


def setUp(self):
    layer = self.globs['layer']
    browser = Browser(layer['app'])
    portal = layer['portal']
    # Update global variables within the tests.
    self.globs.update({
        'TEST_USER_NAME': TEST_USER_NAME,
        'TEST_USER_PASSWORD': TEST_USER_PASSWORD,
        'portal': portal,
        'browser': browser,
    })
    ztc.utils.setupCoreSessions(layer['app'])
    browser.setBaseUrl(portal.absolute_url())

    browser.handleErrors = True
    portal.error_log._ignored_exceptions = ()

    setRoles(portal, TEST_USER_ID, ['Manager'])

    # Set the site back in English mode to make testing easier.
    portal.portal_languages.manage_setLanguageSettings('en', ['en', 'fi'])

    workflow = getToolByName(portal, 'portal_workflow')

    # Add two shipping method
    shipping_method_container = portal['toimitustavat']
    shipping_method1 = shipping_method_container[shipping_method_container.invokeFactory('ShippingMethod', 'shippingmethod1',
        title='ShippingMethöd1', vat=24.0)]
    modified(shipping_method1)
    workflow.doActionFor(shipping_method1, 'publish')
    shipping_method2 = shipping_method_container[shipping_method_container.invokeFactory('ShippingMethod', 'shippingmethod2',
        title='ShippingMethöd2', vat=24.0)]
    modified(shipping_method2)
    workflow.doActionFor(shipping_method2, 'publish')

    regtool = getToolByName(portal, 'portal_registration')
    regtool.addMember('member1', 'member1')
    setRoles(portal, 'member1', ['Member'])

    # ## Setup MockMailHost
    from Products.CMFPlone.tests.utils import MockMailHost
    from Products.MailHost.interfaces import IMailHost
    from zope.component import getSiteManager
    portal._original_MailHost = portal.MailHost
    portal.MailHost = mailhost = MockMailHost('MailHost')
    sm = getSiteManager(context=portal)
    sm.unregisterUtility(provided=IMailHost)
    sm.registerUtility(mailhost, provided=IMailHost)
    self.globs.update({
        'mailhost': portal.MailHost,
        # 'prink': prink,
    })

    transaction.commit()


def DocFileSuite(testfile, flags=FLAGS, setUp=setUp, layer=FUNCTIONAL_TESTING):
    """Returns a test suite configured with a test layer.

    :param testfile: Path to a doctest file.
    :type testfile: str

    :param flags: Doctest test flags.
    :type flags: int

    :param setUp: Test set up function.
    :type setUp: callable

    :param layer: Test layer
    :type layer: object

    :rtype: `manuel.testing.TestSuite`
    """
    m = manuel.doctest.Manuel(optionflags=flags, checker=CHECKER)
    m += manuel.codeblock.Manuel()

    return layered(
        manuel.testing.TestSuite(m, testfile, setUp=setUp, globs=dict(layer=layer)),
        layer=layer)


def test_suite():
    return unittest.TestSuite([
        DocFileSuite('functional/address.txt'),
        DocFileSuite('functional/browser.txt'),
        DocFileSuite('functional/manager.txt')])
