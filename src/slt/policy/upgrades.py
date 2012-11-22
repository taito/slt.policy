from Products.CMFCore.utils import getToolByName

import logging


PROFILE_ID = 'profile-slt.policy:default'


def update_rolemap(context, logger=None):
    """Update rolemap"""
    if logger is None:
        logger = logging.getLogger(__name__)
    setup = getToolByName(context, 'portal_setup')
    logger.info('Reimporting rolemap.')
    setup.runImportStepFromProfile(PROFILE_ID, 'rolemap', run_dependencies=False, purge_old=False)


def update_typeinfo(context, logger=None):
    """Update typeinfo"""
    if logger is None:
        logger = logging.getLogger(__name__)
    setup = getToolByName(context, 'portal_setup')
    logger.info('Reimporting typeinfo.')
    setup.runImportStepFromProfile(
        'profile-collective.cart.shopping:default', 'typeinfo', run_dependencies=False, purge_old=False)


def update_registry(context, logger=None):
    """Update registry"""
    if logger is None:
        logger = logging.getLogger(__name__)
    setup = getToolByName(context, 'portal_setup')
    logger.info('Reimporting registy.')
    setup.runImportStepFromProfile(
        PROFILE_ID, 'plone.app.registry', run_dependencies=False, purge_old=False)


def update_memberdata_properties(context, logger=None):
    """Update memberdata properties"""
    if logger is None:
        logger = logging.getLogger(__name__)
    setup = getToolByName(context, 'portal_setup')
    logger.info('Reimporting memberdata_properties.')
    setup.runImportStepFromProfile(
        PROFILE_ID, 'memberdata-properties', run_dependencies=False, purge_old=False)


def update_actions(context, logger=None):
    """Update actions"""
    if logger is None:
        logger = logging.getLogger(__name__)
    setup = getToolByName(context, 'portal_setup')
    logger.info('Reimporting actions.')
    setup.runImportStepFromProfile(PROFILE_ID, 'actions', run_dependencies=False, purge_old=False)


def update_properties(context, logger=None):
    """Update properties"""
    if logger is None:
        logger = logging.getLogger(__name__)
    setup = getToolByName(context, 'portal_setup')
    logger.info('Reimporting properties.')
    setup.runImportStepFromProfile(
        PROFILE_ID, 'properties', run_dependencies=False, purge_old=False)


def update_propertiestool(context, logger=None):
    """Update propertiestool"""
    if logger is None:
        logger = logging.getLogger(__name__)
    setup = getToolByName(context, 'portal_setup')
    logger.info('Reimporting propertiestool.')
    setup.runImportStepFromProfile(
        PROFILE_ID, 'propertiestool', run_dependencies=False, purge_old=False)


def update_workflows(context, logger=None):
    """Update workflows"""
    if logger is None:
        logger = logging.getLogger(__name__)
    setup = getToolByName(context, 'portal_setup')
    logger.info('Reimporting workflows.')
    setup.runImportStepFromProfile(
        PROFILE_ID, 'workflow', run_dependencies=False, purge_old=False)
