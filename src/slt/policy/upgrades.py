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


# def upgrade_14_to_15(context):
#     """"""
#     from zope.app.intid.interfaces import IIntIds
#     from zope.component import getUtility
#     intids = getUtility(IIntIds)
#     catalog = getToolByName(context, 'portal_catalog')
#     res = {}
#     for brain in catalog(object_provides=[IArticle.__identifier__]):
#         obj = brain.getObject()
#         if hasattr(obj, 'relatedItems'):
#             res.update({obj: [item.to_object for item in obj.relatedItems]})

#     portal = getToolByName(context, 'portal_url').getPortalObject()
#     parent = aq_parent(portal)
#     parent.manage_renameObject('kauppa', 'luontokauppa')

#     for obj in res:
#         intids.unregister(obj)

#     for obj in res:
#         from_id = intids.register(obj)
#         if hasattr(obj, 'relatedItems'):
#             for item in obj.relatedItems:
#                 item._from_id = from_id
#                 index = obj.relatedItems.index(item)
#                 item.to_id = intids.register(res[obj][index])


def unregister_layer_ISltPolicyLayer(context):
    """Unregister ISltPolicyLayer"""
    unregister_layer('slt.policy')


def remove_relatedItems(context):
    from plone.uuid.interfaces import IUUID
    from zope.lifecycleevent import modified

    # catalog = getToolByName(context, 'portal_catalog')
    # catalog.clearFindAndRebuild()

    # intids = getUtility(IIntIds)
    # res = {}
    # res = []
    catalog = getToolByName(context, 'portal_catalog')
    for brain in catalog(portal_type=['collective.cart.core.Article']):
        obj = brain.getObject()
        # modified(obj)

        if hasattr(obj, 'relatedItems'):
            uuids = []
            for item in obj.relatedItems:
                item_object = item.to_object
                if item_object is not None:
                    uuids.append(IUUID(item_object))

            setattr(obj, 'related_articles', uuids)
            del obj.relatedItems
            # obj.relatedItems = []

        modified(obj)

    # for brain in catalog():
    #     obj = brain.getObject()
    #     try:
    #         intids.unregister(obj)
    #     except KeyError:
    #         pass
    #     modified(obj)




            # res.append(obj)

        # import pdb; pdb.set_trace()
        # noLongerProvides(obj, IArticleSchema)
        # obj.vat_rate = float(obj.vat_rate)
        # obj.relatedItems = []
        # alsoProvides(obj, IArticle)
        # modified(obj)
        # obj.reindexObject()
        # res.update({obj: [item.to_object for item in obj.relatedItems]})

    # for obj in res:
    #     intids.unregister(obj)

    # for obj in res:
    #     from_id = intids.register(obj)
    #     if hasattr(obj, 'relatedItems'):
    #         for item in obj.relatedItems:
    #             item._from_id = from_id
    #             index = obj.relatedItems.index(item)
    #             item.to_id = intids.register(res[obj][index])
    #             import pdb; pdb.set_trace()

        # modified(obj)

    #     res.append(obj)

    # catalog = getToolByName(context, 'portal_catalog')
    # catalog.clearFindAndRebuild()

    # for obj in res:
    #     alsoProvides(obj, IArticle)
    #     modified(obj)
