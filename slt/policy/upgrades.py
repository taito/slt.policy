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
