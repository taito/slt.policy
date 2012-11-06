from Products.CMFCore.utils import getToolByName
from slt.policy.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_installed__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('slt.policy'))

    def get_action(self, category, name):
        """Get action by category and name."""
        actions = getToolByName(self.portal, 'portal_actions')
        return getattr(getattr(actions, category), name)

    def test_actions__user__dashboard(self):
        action = self.get_action('user', 'dashboard')
        self.assertFalse(action.visible)

    def test_actions__user__information__i18n_domain(self):
        action = self.get_action('user', 'information')
        self.assertEqual(action.i18n_domain, 'plone')

    def test_actions__user__information__meta_type(self):
        action = self.get_action('user', 'information')
        self.assertEqual(action.meta_type, 'CMF Action')

    def test_actions__user__information__title(self):
        action = self.get_action('user', 'information')
        self.assertEqual(action.title, 'Personal Information')

    def test_actions__user__information__descripion(self):
        action = self.get_action('user', 'information')
        self.assertEqual(action.description, '')

    def test_actions__user__information__url_expr(self):
        action = self.get_action('user', 'information')
        self.assertEqual(action.url_expr,
            'string:${globals_view/navigationRootUrl}/@@personal-information')

    def test_actions__user__information__available_expr(self):
        action = self.get_action('user', 'information')
        self.assertEqual(action.available_expr, 'python:member is not None')

    def test_actions__user__information__permissions(self):
        action = self.get_action('user', 'information')
        self.assertEqual(action.permissions, ('View',))

    def test_actions__user__information__visible(self):
        action = self.get_action('user', 'information')
        self.assertTrue(action.visible)

    def test_actions__user__preferences__permissions(self):
        action = self.get_action('user', 'preferences')
        self.assertEqual(action.permissions, ('slt.theme: View Personal Preferences',))

    def test_actions__user__preferences__visible(self):
        action = self.get_action('user', 'preferences')
        self.assertTrue(action.visible)

    def test_browserlayer(self):
        from slt.policy.browser.interfaces import ISltPolicyLayer
        from plone.browserlayer import utils
        self.assertIn(ISltPolicyLayer, utils.registered_layers())

    def test_jsregistry__popupforms(self):
        javascripts = getToolByName(self.portal, 'portal_javascripts')
        resource = javascripts.getResource('popupforms.js')
        self.assertFalse(resource.getEnabled())

    def test_mailhost__smtp_host(self):
        mailhost = getToolByName(self.portal, 'MailHost')
        self.assertEqual(mailhost.smtp_host, 'sll.fi')

    def test_mailhost__smtp_port(self):
        mailhost = getToolByName(self.portal, 'MailHost')
        self.assertEqual(mailhost.smtp_port, 25)

    def test_memberdata_properties(self):
        memberdata = getToolByName(self.portal, 'portal_memberdata')
        ids = ['registration_number', ]
        for pid in ids:
            self.assertTrue(memberdata.hasProperty(pid))

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-slt.policy:default'), u'4')

    def test_metadata__installed__abita_development(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('abita.development'))

    def test_metadata__installed__hexagonit_socialbutton(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('hexagonit.socialbutton'))

    def test_metadata__installed__slt_theme(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('slt.theme'))

    def test_properties__title(self):
        self.assertEqual(self.portal.getProperty('title'), 'Luonnonsuojelukauppa')

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

    def test_properties__default_page(self):
        self.assertEqual(self.portal.getProperty('default_page'), 'view')

    def test_properties__validate_email(self):
        self.assertTrue(self.portal.getProperty('validate_email'))

    def get_navtree_property(self, name):
        """Get property from navtree_properties based on the name."""
        properties = getToolByName(self.portal, 'portal_properties')
        navtree_properties = getattr(properties, 'navtree_properties')
        return navtree_properties.getProperty(name)

    def test_propertiestool__navtree_properties__metaTypesNotToList(self):
        ctypes = (
            'Collection', 'Document', 'Event', 'File', 'Image', 'Link', 'News Item', 'Topic')
        for ctype in ctypes:
            self.assertIn(ctype, self.get_navtree_property('metaTypesNotToList'))
        self.assertEqual(len(self.get_navtree_property('metaTypesNotToList')), len(ctypes) + 26)

    def get_site_property(self, name):
        """Get property from site_properties based on the name."""
        properties = getToolByName(self.portal, 'portal_properties')
        site_properties = getattr(properties, 'site_properties')
        return site_properties.getProperty(name)

    def test_propertiestool__site_properties__available_editors(self):
        self.assertEqual(self.get_site_property('available_editors'), ('TinyMCE',))

    def test_propertiestool__site_properties__default_editor(self):
        self.assertEqual(self.get_site_property('default_editor'), 'TinyMCE')

    def test_propertiestool__site_properties__default_language(self):
        self.assertEqual(self.get_site_property('default_language'), 'fi')

    def test_propertiestool__site_properties__disable_folder_sections(self):
        self.assertTrue(self.get_site_property('disable_folder_sections'))

    def test_propertiestool__site_properties__enable_sitemap(self):
        self.assertTrue(self.get_site_property('enable_sitemap'))

    def test_propertiestool__site_properties__external_links_open_new_window(self):
        self.assertEqual(self.get_site_property('external_links_open_new_window'), 'true')

    def test_propertiestool__site_properties__icon_visibility(self):
        self.assertEqual(self.get_site_property('icon_visibility'), 'authenticated')

    def test_propertiestool__site_properties__types_not_searched(self):
        ctypes = (
            'Collection', 'Document', 'Event', 'File', 'Image', 'Link', 'News Item', 'Topic')
        for ctype in ctypes:
            self.assertIn(ctype, self.get_site_property('types_not_searched'))
        self.assertEqual(len(self.get_site_property('types_not_searched')), len(ctypes) + 27)

    def test_propertiestool__site_properties__use_email_as_login(self):
        self.assertTrue(self.get_site_property('use_email_as_login'))

    def test_propertiestool__site_properties__visible_ids(self):
        self.assertTrue(self.get_site_property('visible_ids'))

    def get_record(self, name):
        from zope.component import getUtility
        from plone.registry.interfaces import IRegistry
        return getUtility(IRegistry).records.get(name)

    def test_registry_record_hexagonit_socialbutton_codes(self):
        record = self.get_record('hexagonit.socialbutton.codes')
        self.assertEqual(record.value, {
            u'twitter': {u'code_text': u'<a class="social-button twitter" title="Twitter" href="https://twitter.com/share?text=${title}?url=${url}">\n<img src="${portal_url}/++resource++hexagonit.socialbutton/twitter.gif" />\n</a>'},
            u'facebook': {u'code_text': u'<a class="social-button facebook" title="Facebook" target="_blank" href="http://www.facebook.com/sharer.php?t=${title}&u=${url}">\n<img src="${portal_url}/++resource++hexagonit.socialbutton/facebook.gif" />\n</a>'},
            u'google-plus': {u'code_text': u'<a class="social-button googleplus" title="Google+" href="https://plusone.google.com/_/+1/confirm?hl=${lang}&title=${title}&url=${url}">\n<img src="${portal_url}/++resource++hexagonit.socialbutton/google-plus.gif" />\n</a>'},
        })

    def test_registry_record_hexagonit_socialbutton_config(self):
        record = self.get_record('hexagonit.socialbutton.config')
        self.assertEqual(record.value, {
            u'twitter': {u'content_types': u'Document,Folder,Plone Site,News Item,collective.cart.core.Article,collective.cart.shopping.ArticleContainer', u'view_permission_only': u'True', u'view_models': u'*', u'enabled': u'True', u'viewlet_manager': u'plone.belowcontent'},
            u'facebook': {u'content_types': u'Document,Folder,Plone Site,News Item,collective.cart.core.Article,collective.cart.shopping.ArticleContainer', u'view_permission_only': u'True', u'view_models': u'*', u'enabled': u'True', u'viewlet_manager': u'plone.belowcontent'},
            u'google-plus': {u'content_types': u'Document,Folder,Plone Site,News Item,collective.cart.core.Article,collective.cart.shopping.ArticleContainer', u'view_permission_only': u'True', u'view_models': u'*', u'enabled': u'True', u'viewlet_manager': u'plone.belowcontent'},
        })

    def test_rolemap__Add_portal_member__rolesOfPermission(self):
        permission = "Add portal member"
        roles = [item['name'] for item in self.portal.rolesOfPermission(
            permission) if item['selected'] == 'SELECTED']
        roles.sort()
        self.assertEqual(roles, [
            'Anonymous',
            'Manager',
            'Site Administrator'])

    def test_rolemap__Add_portal_member__acquiredRolesAreUsedBy(self):
        permission = "Add portal member"
        self.assertEqual(self.portal.acquiredRolesAreUsedBy(permission), '')

    def test_rolemap__Portlets_View_dashboard__rolesOfPermission(self):
        permission = "Portlets: View dashboard"
        roles = [item['name'] for item in self.portal.rolesOfPermission(
            permission) if item['selected'] == 'SELECTED']
        roles.sort()
        self.assertEqual(roles, ['Manager', 'Site Administrator'])

    def test_rolemap__Portlets_View_dashboard__acquiredRolesAreUsedBy(self):
        permission = "Portlets: View dashboard"
        self.assertEqual(self.portal.acquiredRolesAreUsedBy(permission), 'CHECKED')

    def test_rolemap__Portlets_Manage_own_portlets__rolesOfPermission(self):
        permission = "Portlets: Manage own portlets"
        roles = [item['name'] for item in self.portal.rolesOfPermission(
            permission) if item['selected'] == 'SELECTED']
        roles.sort()
        self.assertEqual(roles, ['Manager', 'Site Administrator'])

    def test_rolemap__Portlets_Manage_own_portlets__acquiredRolesAreUsedBy(self):
        permission = "Portlets: Manage own portlets"
        self.assertEqual(self.portal.acquiredRolesAreUsedBy(permission), 'CHECKED')

    def test_rolemap__slt_theme_View_Personal_Preferences__rolesOfPermission(self):
        permission = "slt.theme: View Personal Preferences"
        roles = [item['name'] for item in self.portal.rolesOfPermission(
            permission) if item['selected'] == 'SELECTED']
        roles.sort()
        self.assertEqual(roles, [
            'Contributor',
            'Editor',
            'Manager',
            'Site Administrator'])

    def test_rolemap__slt_theme_View_Personal_Preferences__acquiredRolesAreUsedBy(self):
        permission = "slt.theme: View Personal Preferences"
        self.assertEqual(self.portal.acquiredRolesAreUsedBy(permission), 'CHECKED')

    def test_rolemap__slt_theme_Manage_feed_for_shop_top__rolesOfPermission(self):
        permission = "slt.theme: Manage feed for shop top"
        roles = [item['name'] for item in self.portal.rolesOfPermission(
            permission) if item['selected'] == 'SELECTED']
        roles.sort()
        self.assertEqual(roles, [
            'Contributor',
            'Editor',
            'Manager',
            'Site Administrator'])

    def test_rolemap__slt_theme_Manage_feed_for_shop_top__acquiredRolesAreUsedBy(self):
        permission = "slt.theme: Manage feed for shop top"
        self.assertEqual(self.portal.acquiredRolesAreUsedBy(permission), 'CHECKED')

    def test_setuphandlers__exclude_from_nav(self):
        ids = ['Members', 'events', 'news']
        for oid in ids:
            self.assertTrue(self.portal[oid].getExcludeFromNav())

    def test_setuphanlders__remove_front_page(self):
        self.assertIsNone(self.portal.get('front-page'))

    def test_setuphandlers__set_firstweekday(self):
        calendar = getToolByName(self.portal, 'portal_calendar')
        self.assertEqual(calendar.firstweekday, 0)

    def test_setuphandlers__uninstall_package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertFalse(installer.isProductInstalled('plonetheme.classic'))

    def test_setuphandlers__create_containers(self):
        self.assertIsNotNone(self.portal.get('tilaukset'))
        self.assertEqual(self.portal.get('tilaukset').Type(), u'Cart Container')
        self.assertIsNotNone(self.portal.get('toimitustavat'))
        self.assertEqual(self.portal.get('toimitustavat').Type(), u'Shipping Method Container')

    def test_setuphandlers__set_member_content_type(self):
        membership = getToolByName(self.portal, 'portal_membership')
        self.assertEqual(membership.memberarea_type, 'slt.content.MemberArea')
        self.assertTrue(membership.getMemberareaCreationFlag())

    def test_setuphandlers__provideIShoppingSiteRoot(self):
        from collective.cart.core.interfaces import IShoppingSiteRoot
        self.assertTrue(IShoppingSiteRoot.providedBy(self.portal))

    def test_tinymce__link_using_uids(self):
        tinymce = getToolByName(self.portal, 'portal_tinymce')
        self.assertTrue(tinymce.link_using_uids)

    def uninstall_package(self):
        """Uninstall package: slt.policy."""
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['slt.policy'])

    def test_uninstall__package(self):
        self.uninstall_package()
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertFalse(installer.isProductInstalled('slt.policy'))

    def test_uninstall__browserlayer(self):
        self.uninstall_package()
        from slt.policy.browser.interfaces import ISltPolicyLayer
        from plone.browserlayer import utils
        self.assertNotIn(ISltPolicyLayer, utils.registered_layers())

    def test_uninstall__jsregistry__popupforms(self):
        self.uninstall_package()
        javascripts = getToolByName(self.portal, 'portal_javascripts')
        resource = javascripts.getResource('popupforms.js')
        self.assertFalse(resource.getEnabled())

    def test_uninstall__mailhost__smtp_host(self):
        self.uninstall_package()
        mailhost = getToolByName(self.portal, 'MailHost')
        self.assertEqual(mailhost.smtp_host, 'sll.fi')

    def test_uninstall__mailhost__smtp_port(self):
        self.uninstall_package()
        mailhost = getToolByName(self.portal, 'MailHost')
        self.assertEqual(mailhost.smtp_port, 25)

    def test_uninstall__metadata__installed__abita_development(self):
        self.uninstall_package()
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('abita.development'))

    def test_uninstall__metadata__installed__hexagonit_socialbutton(self):
        self.uninstall_package()
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('hexagonit.socialbutton'))

    def test_uninstall__metadata__installed__slt_theme(self):
        self.uninstall_package()
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('slt.theme'))

    def test_uninstall__properties__title(self):
        self.uninstall_package()
        self.assertEqual(self.portal.getProperty('title'), 'Luonnonsuojelukauppa')

    def test_uninstall__properties__description(self):
        self.uninstall_package()
        self.assertEqual(self.portal.getProperty('description'),
            'Suomen Luonnonsuojelun Tuki Oy')

    def test_uninstall__properties__email_from_address(self):
        self.uninstall_package()
        self.assertEqual(
            self.portal.getProperty('email_from_address'),
            'webmaster@sll.fi')

    def test_uninstall__properties__email_from_name(self):
        self.uninstall_package()
        self.assertEqual(self.portal.getProperty('email_from_name'),
            'Suomen Luonnonsuojelun Tuki Oy')

    def test_unintall__properties___default_page(self):
        self.uninstall_package()
        self.assertEqual(self.portal.getProperty('default_page'), 'view')

    def test_uninstall__properties___validate_email(self):
        self.uninstall_package()
        self.assertTrue(self.portal.getProperty('validate_email'))

    def test_uninstall__propertiestool__navtree_properties__metaTypesNotToList(self):
        self.uninstall_package()
        ctypes = (
            'Collection', 'Document', 'Event', 'File', 'Image', 'Link', 'News Item', 'Topic')
        for ctype in ctypes:
            self.assertIn(ctype, self.get_navtree_property('metaTypesNotToList'))
        self.assertEqual(len(self.get_navtree_property('metaTypesNotToList')), len(ctypes) + 26)

    def test_uninstall__propertiestool__site_properties__available_editors(self):
        self.uninstall_package()
        self.assertEqual(self.get_site_property('available_editors'), ('TinyMCE',))

    def test_uninstall__propertiestool__site_properties__default_editor(self):
        self.uninstall_package()
        self.assertEqual(self.get_site_property('default_editor'), 'TinyMCE')

    def test_uninstall__propertiestool__site_properties__default_language(self):
        self.uninstall_package()
        self.assertEqual(self.get_site_property('default_language'), 'fi')

    def test_uninstall__propertiestool__site_properties__disable_folder_sections(self):
        self.uninstall_package()
        self.assertTrue(self.get_site_property('disable_folder_sections'))

    def test_uninstall__propertiestool__site_properties__enable_sitemap(self):
        self.uninstall_package()
        self.assertTrue(self.get_site_property('enable_sitemap'))

    def test_uninstall__propertiestool__site_properties__external_links_open_new_window(self):
        self.uninstall_package()
        self.assertEqual(self.get_site_property('external_links_open_new_window'), 'true')

    def test_uninstall__propertiestool__site_properties__icon_visibility(self):
        self.uninstall_package()
        self.assertEqual(self.get_site_property('icon_visibility'), 'authenticated')

    def test_uninstall__propertiestool__site_properties__types_not_searched(self):
        self.uninstall_package()
        ctypes = (
            'Collection', 'Document', 'Event', 'File', 'Image', 'Link', 'News Item', 'Topic')
        for ctype in ctypes:
            self.assertIn(ctype, self.get_site_property('types_not_searched'))
        self.assertEqual(len(self.get_site_property('types_not_searched')), len(ctypes) + 27)

    def test_uninstall__propertiestool__site_properties__use_email_as_login(self):
        self.uninstall_package()
        self.assertTrue(self.get_site_property('use_email_as_login'))

    def test_uninstall__propertiestool__site_properties__visible_ids(self):
        self.uninstall_package()
        self.assertTrue(self.get_site_property('visible_ids'))

    def test_uninstall__rolemap__Add_portal_member__acquiredRolesAreUsedBy(self):
        permission = "Add portal member"
        self.assertEqual(self.portal.acquiredRolesAreUsedBy(permission), '')

    def test_uninstall__setuphandlers__exclude_from_nav(self):
        ids = ['Members', 'events', 'news']
        for oid in ids:
            self.assertTrue(self.portal[oid].getExcludeFromNav())
