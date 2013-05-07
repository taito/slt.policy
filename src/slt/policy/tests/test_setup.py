from Products.CMFCore.utils import getToolByName
from abita.utils.utils import get_record
from sll.basepolicy.tests.test_setup import get_action
from sll.basepolicy.tests.test_setup import get_property
from sll.basepolicy.tests.test_setup import get_roles
from sll.basepolicy.tests.test_setup import get_workflow
from slt.policy.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_installed__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('slt.policy'))

    def test_actions__user__information__i18n_domain(self):
        action = get_action(self.portal, 'user', 'information')
        self.assertEqual(action.i18n_domain, 'slt.policy')

    def test_actions__user__information__meta_type(self):
        action = get_action(self.portal, 'user', 'information')
        self.assertEqual(action.meta_type, 'CMF Action')

    def test_actions__user__information__title(self):
        action = get_action(self.portal, 'user', 'information')
        self.assertEqual(action.title, 'Personal Information')

    def test_actions__user__information__descripion(self):
        action = get_action(self.portal, 'user', 'information')
        self.assertEqual(action.description, '')

    def test_actions__user__information__url_expr(self):
        action = get_action(self.portal, 'user', 'information')
        self.assertEqual(action.url_expr,
            'string:${globals_view/navigationRootUrl}/@@personal-information')

    def test_actions__user__information__available_expr(self):
        action = get_action(self.portal, 'user', 'information')
        self.assertEqual(action.available_expr, 'python:member is not None')

    def test_actions__user__information__permissions(self):
        action = get_action(self.portal, 'user', 'information')
        self.assertEqual(action.permissions, ('View',))

    def test_actions__user__information__visible(self):
        action = get_action(self.portal, 'user', 'information')
        self.assertTrue(action.visible)

    def test_actions__user__preferences__permissions(self):
        action = get_action(self.portal, 'user', 'preferences')
        self.assertEqual(action.permissions, ('slt.theme: View Personal Preferences',))

    def test_actions__user__preferences__visible(self):
        action = get_action(self.portal, 'user', 'preferences')
        self.assertTrue(action.visible)

    def test_actions__user__addresses__i18n_domain(self):
        action = get_action(self.portal, 'user', 'addresses')
        self.assertEqual(action.i18n_domain, 'slt.policy')

    def test_actions__user__addresses__meta_type(self):
        action = get_action(self.portal, 'user', 'addresses')
        self.assertEqual(action.meta_type, 'CMF Action')

    def test_actions__user__addresses__title(self):
        action = get_action(self.portal, 'user', 'addresses')
        self.assertEqual(action.title, 'Addresses')

    def test_actions__user__addresses__descripion(self):
        action = get_action(self.portal, 'user', 'addresses')
        self.assertEqual(action.description, '')

    def test_actions__user__addresses__url_expr(self):
        action = get_action(self.portal, 'user', 'addresses')
        self.assertEqual(action.url_expr,
            'string:${portal/portal_membership/getHomeUrl}/@@address-listing')

    def test_actions__user__addresses__available_expr(self):
        action = get_action(self.portal, 'user', 'addresses')
        self.assertEqual(action.available_expr, 'python:member is not None')

    def test_actions__user__addresses__permissions(self):
        action = get_action(self.portal, 'user', 'addresses')
        self.assertEqual(action.permissions, ('View',))

    def test_actions__user__addresses__visible(self):
        action = get_action(self.portal, 'user', 'addresses')
        self.assertTrue(action.visible)

    def test_actions__user__orders__i18n_domain(self):
        action = get_action(self.portal, 'user', 'orders')
        self.assertEqual(action.i18n_domain, 'slt.policy')

    def test_actions__user__orders__meta_type(self):
        action = get_action(self.portal, 'user', 'orders')
        self.assertEqual(action.meta_type, 'CMF Action')

    def test_actions__user__orders__title(self):
        action = get_action(self.portal, 'user', 'orders')
        self.assertEqual(action.title, 'Orders')

    def test_actions__user__orders__descripion(self):
        action = get_action(self.portal, 'user', 'orders')
        self.assertEqual(action.description, '')

    def test_actions__user__orders__url_expr(self):
        action = get_action(self.portal, 'user', 'orders')
        self.assertEqual(action.url_expr, 'string:${portal/portal_membership/getHomeUrl}')

    def test_actions__user__orders__available_expr(self):
        action = get_action(self.portal, 'user', 'orders')
        self.assertEqual(action.available_expr, 'python:member is not None')

    def test_actions__user__orders__permissions(self):
        action = get_action(self.portal, 'user', 'orders')
        self.assertEqual(action.permissions, ('View',))

    def test_actions__user__orders__visible(self):
        action = get_action(self.portal, 'user', 'orders')
        self.assertTrue(action.visible)

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-slt.policy:default'), u'18')

    def test_metadata__dependency__sll_basepolicy(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('sll.basepolicy'))

    def test_metadata__dependency__slt_theme(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('slt.theme'))

    def test_properties__default_page(self):
        self.assertEqual(self.portal.getProperty('default_page'), 'slt-view')

    def test_properties__description(self):
        self.assertEqual(self.portal.getProperty('description'),
            'Suomen Luonnonsuojelun Tuki Oy')

    def test_properties__email_from_address(self):
        self.assertEqual(
            self.portal.getProperty('email_from_address'),
            'webmaster@sll.fi')

    def test_properties__email_from_name(self):
        self.assertEqual(self.portal.getProperty('email_from_name'),
            'Suomen Luonnonsuojelun Tuki Oy')

    def test_properties__title(self):
        self.assertEqual(self.portal.getProperty('title'), 'Luonnonsuojelukauppa')

    def test_propertiestool__navtree_properties__metaTypesNotToList(self):
        additional_ctypes = ('Document', 'News Item', 'slt.content.MemberArea')
        ctypes = get_property(self.portal, 'navtree_properties', 'metaTypesNotToList')
        for ctype in additional_ctypes:
            self.assertIn(ctype, ctypes)

    def test_propertiestool__site_properties__icon_visibility(self):
        self.assertEqual(get_property(self.portal, 'site_properties', 'icon_visibility'), 'disabled')

    def test_propertiestool__site_properties__types_not_searched(self):
        additional_ctypes = ('Document', 'Event', 'File', 'Image', 'Link', 'News Item', 'slt.content.MemberArea')
        ctypes = get_property(self.portal, 'site_properties', 'types_not_searched')
        for ctype in additional_ctypes:
            self.assertIn(ctype, ctypes)

    def get_record(self, name):
        """Get record by name.
        :param name: Name of record.
        :type name: basestring

        :rtype: plone.registry.record.Record
        """
        from plone.registry.interfaces import IRegistry
        from zope.component import getUtility
        return getUtility(IRegistry).records.get(name)

    def test_registry_record__collective_cart_shopping_notification_cc_email__value(self):
        record = self.get_record('collective.cart.shopping.notification_cc_email')
        self.assertEqual(record.value, u'lk-tilaukset@sll.fi')

    def test_registry_record_hexagonit_socialbutton_config(self):
        record = get_record('hexagonit.socialbutton.config')
        self.assertEqual(record.value, {
            u'twitter': {u'content_types': u'Document,Folder,FormFolder,Plone Site,News Item,Event,collective.cart.core.Article,collective.cart.shopping.ArticleContainer', u'view_permission_only': u'True', u'view_models': u'*', u'enabled': u'True', u'viewlet_manager': u'plone.belowcontent'},
            u'facebook': {u'content_types': u'Document,Folder,FormFolder,Plone Site,News Item,Event,collective.cart.core.Article,collective.cart.shopping.ArticleContainer', u'view_permission_only': u'True', u'view_models': u'*', u'enabled': u'True', u'viewlet_manager': u'plone.belowcontent'},
            u'google-plus': {u'content_types': u'Document,Folder,FormFolder,Plone Site,News Item,Event,collective.cart.core.Article,collective.cart.shopping.ArticleContainer', u'view_permission_only': u'True', u'view_models': u'*', u'enabled': u'True', u'viewlet_manager': u'plone.belowcontent'},
        })

    def test_rolemap__Add_portal_member__rolesOfPermission(self):
        permission = "Add portal member"
        self.assertEqual(get_roles(self.portal, permission), [
            'Anonymous',
            'Manager',
            'Site Administrator'])

    def test_rolemap__Add_portal_member__acquiredRolesAreUsedBy(self):
        permission = "Add portal member"
        self.assertEqual(self.portal.acquiredRolesAreUsedBy(permission), '')

    def test_rolemap__Portlets_Manage_own_portlets__rolesOfPermission(self):
        permission = "Portlets: Manage own portlets"
        self.assertEqual(get_roles(self.portal, permission), [
            'Manager',
            'Site Administrator'])

    def test_rolemap__Portlets_Manage_own_portlets__acquiredRolesAreUsedBy(self):
        permission = "Portlets: Manage own portlets"
        self.assertEqual(self.portal.acquiredRolesAreUsedBy(permission), 'CHECKED')

    def test_rolemap__slt_theme_View_Personal_Preferences__rolesOfPermission(self):
        permission = "slt.theme: View Personal Preferences"
        self.assertEqual(get_roles(self.portal, permission), [
            'Contributor',
            'Editor',
            'Manager',
            'Site Administrator'])

    def test_rolemap__slt_theme_View_Personal_Preferences__acquiredRolesAreUsedBy(self):
        permission = "slt.theme: View Personal Preferences"
        self.assertEqual(self.portal.acquiredRolesAreUsedBy(permission), 'CHECKED')

    def test_rolemap__slt_theme_Manage_feed_for_shop_top__rolesOfPermission(self):
        permission = "slt.theme: Manage feed for shop top"
        self.assertEqual(get_roles(self.portal, permission), [
            'Contributor',
            'Editor',
            'Manager',
            'Site Administrator'])

    def test_rolemap__slt_theme_Manage_feed_for_shop_top__acquiredRolesAreUsedBy(self):
        permission = "slt.theme: Manage feed for shop top"
        self.assertEqual(self.portal.acquiredRolesAreUsedBy(permission), 'CHECKED')

    def test_setuphandlers__create_containers(self):
        self.assertIsNotNone(self.portal.get('tilaukset'))
        self.assertEqual(self.portal.get('tilaukset').Type(), u'Order Container')
        self.assertIsNotNone(self.portal.get('toimitustavat'))
        self.assertEqual(self.portal.get('toimitustavat').Type(), u'Shipping Method Container')

    def test_setuphandlers__set_member_content_type(self):
        membership = getToolByName(self.portal, 'portal_membership')
        self.assertEqual(membership.memberarea_type, 'slt.content.MemberArea')
        self.assertTrue(membership.getMemberareaCreationFlag())

    def test_setuphandlers__provideIShoppingSiteRoot(self):
        from collective.cart.core.interfaces import IShoppingSiteRoot
        self.assertTrue(IShoppingSiteRoot.providedBy(self.portal))

    def test_workflow__type__collective_cart_shopping_CustomerInfo(self):
        workflow = getToolByName(self.portal, 'portal_workflow')
        self.assertEqual(workflow.getChainForPortalType('collective.cart.shopping.CustomerInfo'),
            ('member_workflow', ))

    def test_workflow__type__slt_content_MemberArea(self):
        workflow = getToolByName(self.portal, 'portal_workflow')
        self.assertEqual(workflow.getChainForPortalType('slt.content.MemberArea'),
            ('member_workflow', ))

    def test_workflows__member_workflow__description(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        self.assertEqual(workflow.description, 'Private state only for member.')

    def test_workflows__member_workflow__initial_state(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        self.assertEqual(workflow.initial_state, 'private')

    def test_workflows__member_workflow__manager_bypass(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        self.assertFalse(workflow.manager_bypass)

    def test_workflows__member_workflow__state_variable(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        self.assertEqual(workflow.state_var, 'review_state')

    def test_workflows__member_workflow__title(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        self.assertEqual(workflow.title, 'Member Workflow')

    def test_workflows__member_workflow__permissions(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        self.assertEqual(workflow.permissions, (
            'Access contents information',
            'Copy or Move',
            'List folder contents',
            'Modify portal content',
            'View'))

    def test_workflows__member_workflow__states__private__title(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        state = workflow.states.private
        self.assertEqual(state.title, 'Private')

    def test_workflows__member_workflow__states__private__description(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        state = workflow.states.private
        self.assertEqual(state.description, 'Can only be seen and edited by the owner.')

    def test_workflows__member_workflow__states__private__permission__Access_contents_information(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        state = workflow.states.private
        self.assertEqual(state.getPermissionInfo('Access contents information'), {
            'acquired': 0,
            'roles': ['Manager', 'Owner', 'Site Administrator'],
        })

    def test_workflows__member_workflow__states__private__permission__Copy_or_Move(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        state = workflow.states.private
        self.assertEqual(state.getPermissionInfo('Copy or Move'), {
            'acquired': 0,
            'roles': ['Manager', 'Site Administrator'],
        })

    def test_workflows__member_workflow__states__private__permission__List_folder_contents(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        state = workflow.states.private
        self.assertEqual(state.getPermissionInfo('List folder contents'), {
            'acquired': 0,
            'roles': ['Manager', 'Site Administrator'],
        })

    def test_workflows__member_workflow__states__private__permission__Modify_portal_content(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        state = workflow.states.private
        self.assertEqual(state.getPermissionInfo('Modify portal content'), {
            'acquired': 0,
            'roles': ['Manager', 'Owner', 'Site Administrator'],
        })

    def test_workflows__member_workflow__states__private__permission__View(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        state = workflow.states.private
        self.assertEqual(state.getPermissionInfo('View'), {
            'acquired': 0,
            'roles': ['Manager', 'Owner', 'Site Administrator'],
        })

    def test_workflows__member_workflow__variables__action__for_catalog(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.action
        self.assertFalse(variable.for_catalog)

    def test_workflows__member_workflow__variables__action__for_status(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.action
        self.assertTrue(variable.for_status)

    def test_workflows__member_workflow__variables__action__updata_always(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.action
        self.assertTrue(variable.update_always)

    def test_workflows__member_workflow__variables__action__description(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.action
        self.assertEqual(variable.description, 'Previous transition')

    def test_workflows__member_workflow__variables__action__default(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.action
        self.assertEqual(variable.getDefaultExprText(), 'transition/getId|nothing')

    def test_workflows__member_workflow__variables__action__guard(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.action
        self.assertIsNone(variable.info_guard)

    def test_workflows__member_workflow__variables__actor__for_catalog(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.actor
        self.assertFalse(variable.for_catalog)

    def test_workflows__member_workflow__variables__actor__for_status(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.actor
        self.assertTrue(variable.for_status)

    def test_workflows__member_workflow__variables__actor__updata_always(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.actor
        self.assertTrue(variable.update_always)

    def test_workflows__member_workflow__variables__actor__description(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.actor
        self.assertEqual(variable.description, 'The ID of the user who performed the last transition')

    def test_workflows__member_workflow__variables__actor__default(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.actor
        self.assertEqual(variable.getDefaultExprText(), 'user/getId')

    def test_workflows__member_workflow__variables__actor__guard(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.actor
        self.assertIsNone(variable.info_guard)

    def test_workflows__member_workflow__variables__comments__for_catalog(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.comments
        self.assertFalse(variable.for_catalog)

    def test_workflows__member_workflow__variables__comments__for_status(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.comments
        self.assertTrue(variable.for_status)

    def test_workflows__member_workflow__variables__comments__updata_always(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.comments
        self.assertTrue(variable.update_always)

    def test_workflows__member_workflow__variables__comments__description(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.comments
        self.assertEqual(variable.description, 'Comment about the last transition')

    def test_workflows__member_workflow__variables__comments__default(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.comments
        self.assertEqual(variable.getDefaultExprText(),
            "python:state_change.kwargs.get('comment', '')")

    def test_workflows__member_workflow__variables__comments__guard(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.comments
        self.assertIsNone(variable.info_guard)

    def test_workflows__member_workflow__variables__review_history__for_catalog(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.review_history
        self.assertFalse(variable.for_catalog)

    def test_workflows__member_workflow__variables__review_history__for_status(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.review_history
        self.assertFalse(variable.for_status)

    def test_workflows__member_workflow__variables__review_history__updata_always(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.review_history
        self.assertFalse(variable.update_always)

    def test_workflows__member_workflow__variables__review_history__description(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.review_history
        self.assertEqual(variable.description, 'Provides access to workflow history')

    def test_workflows__member_workflow__variables__review_history__default(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.review_history
        self.assertEqual(variable.getDefaultExprText(),
            "state_change/getHistory")

    def test_workflows__member_workflow__variables__review_history__guard(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.review_history
        self.assertEqual(variable.info_guard.permissions,
            ('Request review', 'Review portal content'))

    def test_workflows__member_workflow__variables__time__for_catalog(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.time
        self.assertFalse(variable.for_catalog)

    def test_workflows__member_workflow__variables__time__for_status(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.time
        self.assertTrue(variable.for_status)

    def test_workflows__member_workflow__variables__time__updata_always(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.time
        self.assertTrue(variable.update_always)

    def test_workflows__member_workflow__variables__time__description(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.time
        self.assertEqual(variable.description, 'When the previous transition was performed')

    def test_workflows__member_workflow__variables__time__default(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.time
        self.assertEqual(variable.getDefaultExprText(),
            "state_change/getDateTime")

    def test_workflows__member_workflow__variables__time__guard(self):
        workflow = get_workflow(self.portal, 'member_workflow')
        variable = workflow.variables.time
        self.assertIsNone(variable.info_guard)

    def uninstall_package(self):
        """Uninstall package: slt.policy."""
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['slt.policy'])

    def test_uninstall__package(self):
        self.uninstall_package()
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertFalse(installer.isProductInstalled('slt.policy'))
