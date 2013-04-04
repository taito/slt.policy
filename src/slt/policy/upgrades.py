from Acquisition import aq_parent
from Products.CMFCore.utils import getToolByName
from abita.utils.utils import reimport_profile
from collective.cart.core.interfaces import IArticle


PROFILE_ID = 'profile-slt.policy:default'


def reimport_actions(context):
    """Update actions"""
    reimport_profile(context, PROFILE_ID, 'actions')


def reimport_memberdata_properties(context):
    """Update memberdata properties"""
    reimport_profile(context, PROFILE_ID, 'memberdata-properties')


def reimport_properties(context):
    """Update properties"""
    reimport_profile(context, PROFILE_ID, 'properties')


def reimport_propertiestool(context):
    """Update propertiestool"""
    reimport_profile(context, PROFILE_ID, 'propertiestool')


def reimport_registry(context):
    """Update registry"""
    reimport_profile(context, PROFILE_ID, 'plone.app.registry')


def reimport_rolemap(context):
    """Update rolemap"""
    reimport_profile(context, PROFILE_ID, 'rolemap')


def reimport_typeinfo(context):
    """Update typeinfo"""
    reimport_profile(context, PROFILE_ID, 'typeinfo')


def reimport_workflow(context):
    """Update workflow"""
    reimport_profile(context, PROFILE_ID, 'workflow')


def upgrade_13_to_14(context):
    """"""
    from zope.app.intid.interfaces import IIntIds
    from zope.component import getUtility
    intids = getUtility(IIntIds)
    catalog = getToolByName(context, 'portal_catalog')
    res = {}
    for brain in catalog(object_provides=[IArticle.__identifier__]):
        obj = brain.getObject()
        if hasattr(obj, 'relatedItems'):
            res.update({obj: [item.to_object for item in obj.relatedItems]})

    portal = getToolByName(context, 'portal_url').getPortalObject()
    parent = aq_parent(portal)
    parent.manage_renameObject('slt', 'kauppa')

    for obj in res:
        intids.unregister(obj)

    for obj in res:
        from_id = intids.register(obj)
        if hasattr(obj, 'relatedItems'):
            for item in obj.relatedItems:
                item._from_id = from_id
                index = obj.relatedItems.index(item)
                item.to_id = intids.register(res[obj][index])
