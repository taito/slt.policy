from Products.CMFCore.utils import getToolByName
from abita.utils.utils import reimport_profile
from plone.browserlayer.utils import unregister_layer


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


def unregister_layer_ISltPolicyLayer(context):
    """Unregister ISltPolicyLayer"""
    unregister_layer('slt.policy')


# def remove_relatedItems(context):
#     from plone.uuid.interfaces import IUUID
#     from zope.lifecycleevent import modified

#     catalog = getToolByName(context, 'portal_catalog')
#     for brain in catalog(portal_type=['collective.cart.core.Article']):
#         obj = brain.getObject()

#         if hasattr(obj, 'relatedItems'):
#             uuids = []
#             for item in obj.relatedItems:
#                 item_object = item.to_object
#                 if item_object is not None:
#                     uuids.append(IUUID(item_object))

#             setattr(obj, 'related_articles', uuids)
#             del obj.relatedItems

#         modified(obj)
