from abita.utils.utils import reimport_profile


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
