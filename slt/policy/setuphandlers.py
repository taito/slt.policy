from Products.CMFCore.utils import getToolByName


import logging


logger = logging.getLogger(__name__)


def exclude_from_nav(context):
    """Object exclude from nav."""
    portal = context.getSite()
    ids = ['Members', 'events', 'news']
    for oid in ids:
        obj = portal.get(oid)
        logger.info('Excluding from navigation: {}'.format('/'.join(obj.getPhysicalPath())))
        obj.setExcludeFromNav(True)
        obj.reindexObject()


def remove_front_page(context):
    portal = context.getSite()
    logger.info('Removing front-page.')
    portal.manage_delObjects(['front-page'])


def set_firstweekday(context):
    portal = context.getSite()
    tool = getToolByName(portal, 'portal_calendar')
    logger.info('Setting first weekday for calendar to Monday.')
    tool.firstweekday = 0


def uninstall_package(context, packages):
    """Uninstall packages.

    :param packages: List of package names.
    :type packages: list
    """
    portal = context.getSite()
    installer = getToolByName(portal, 'portal_quickinstaller')
    packages = [
        package for package in packages if installer.isProductInstalled(package)]
    logger.info('Uninstalling {}'.format(', '.join(packages)))
    installer.uninstallProducts(packages)


def setupVarious(context):

    if context.readDataFile('slt.policy_various.txt') is None:
        return

    exclude_from_nav(context)
    remove_front_page(context)
    set_firstweekday(context)
    uninstall_package(context, ['plonetheme.classic'])
