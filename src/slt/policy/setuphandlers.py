from Products.CMFCore.utils import getToolByName
from collective.cart.core.interfaces import IShoppingSiteRoot
from plone.dexterity.utils import createContentInContainer
from zope.interface import alsoProvides
from zope.lifecycleevent import modified

import logging


logger = logging.getLogger(__name__)


def create_containers(context):
    portal = context.getSite()
    logger.info('Creating cart container named: Tilaukset.')
    container = createContentInContainer(portal, 'collective.cart.core.CartContainer',
        title="Tilaukset", checkConstraints=False)
    modified(container)
    logger.info('Creating shipping method container named: Toimitustavat.')
    container = createContentInContainer(portal, 'collective.cart.shipping.ShippingMethodContainer',
        title='Toimitustavat', checkConstraints=False)
    modified(container)


def set_member_content_type(context):
    """Set member content type to slt.content.MemberArea."""
    portal = context.getSite()
    membership = getToolByName(portal, 'portal_membership')
    logger.info('Setting member area type to slt.content.Member.')
    membership.setMemberAreaType('slt.content.MemberArea')
    membership.memberareaCreationFlag = True


def provideIShoppingSiteRoot(context):
    """Provide IShoppingSiteRoot for plone root."""
    portal = context.getSite()
    alsoProvides(portal, IShoppingSiteRoot)
    portal.reindexObject(idxs=['object_provides'])


def setupVarious(context):

    if context.readDataFile('slt.policy_various.txt') is None:
        return

    create_containers(context)
    set_member_content_type(context)
    provideIShoppingSiteRoot(context)
