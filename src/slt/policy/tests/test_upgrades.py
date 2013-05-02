from slt.policy.tests.base import IntegrationTestCase

import mock


class TestCase(IntegrationTestCase):
    """TestCase for upgrade steps."""

    @mock.patch('slt.policy.upgrades.reimport_profile')
    def test_reimport_actions(self, reimport_profile):
        context = mock.Mock()
        from slt.policy.upgrades import reimport_actions
        reimport_actions(context)
        reimport_profile.assert_called_with(context, 'profile-slt.policy:default', 'actions')

    @mock.patch('slt.policy.upgrades.reimport_profile')
    def test_reimport_memberdata_properties(self, reimport_profile):
        context = mock.Mock()
        from slt.policy.upgrades import reimport_memberdata_properties
        reimport_memberdata_properties(context)
        reimport_profile.assert_called_with(context, 'profile-slt.policy:default', 'memberdata-properties')

    @mock.patch('slt.policy.upgrades.reimport_profile')
    def test_reimport_properties(self, reimport_profile):
        context = mock.Mock()
        from slt.policy.upgrades import reimport_properties
        reimport_properties(context)
        reimport_profile.assert_called_with(context, 'profile-slt.policy:default', 'properties')

    @mock.patch('slt.policy.upgrades.reimport_profile')
    def test_reimport_propertiestool(self, reimport_profile):
        context = mock.Mock()
        from slt.policy.upgrades import reimport_propertiestool
        reimport_propertiestool(context)
        reimport_profile.assert_called_with(context, 'profile-slt.policy:default', 'propertiestool')

    @mock.patch('slt.policy.upgrades.reimport_profile')
    def test_reimport_registry(self, reimport_profile):
        context = mock.Mock()
        from slt.policy.upgrades import reimport_registry
        reimport_registry(context)
        reimport_profile.assert_called_with(context, 'profile-slt.policy:default', 'plone.app.registry')

    @mock.patch('slt.policy.upgrades.reimport_profile')
    def test_reimport_rolemap(self, reimport_profile):
        context = mock.Mock()
        from slt.policy.upgrades import reimport_rolemap
        reimport_rolemap(context)
        reimport_profile.assert_called_with(context, 'profile-slt.policy:default', 'rolemap')

    @mock.patch('slt.policy.upgrades.reimport_profile')
    def test_reimport_typeinfo(self, reimport_profile):
        context = mock.Mock()
        from slt.policy.upgrades import reimport_typeinfo
        reimport_typeinfo(context)
        reimport_profile.assert_called_with(context, 'profile-slt.policy:default', 'typeinfo')

    @mock.patch('slt.policy.upgrades.reimport_profile')
    def test_reimport_workflow(self, reimport_profile):
        context = mock.Mock()
        from slt.policy.upgrades import reimport_workflow
        reimport_workflow(context)
        reimport_profile.assert_called_with(context, 'profile-slt.policy:default', 'workflow')

    # @mock.patch('slt.policy.upgrades.aq_parent')
    # def test_upgrade_14_to_15(self, aq_parent):
    #     from z3c.relationfield.relation import RelationValue
    #     from zope.app.intid.interfaces import IIntIds
    #     from zope.component import getUtility

    #     # Create articles
    #     article1 = self.create_content('collective.cart.core.Article', id='article1', money=self.money('12.40'), vat_rate=24.0)
    #     article2 = self.create_content('collective.cart.core.Article', id='article2', money=self.money('12.40'), vat_rate=24.0)
    #     # Relate article2 to article1
    #     intids = getUtility(IIntIds)

    #     to_id = intids.register(article2)
    #     relation_value = RelationValue(to_id)
    #     from_id = intids.register(article1)
    #     relation_value._from_id = from_id
    #     self.assertEqual(relation_value.from_id, from_id)
    #     article1.relatedItems = [relation_value]

    #     from slt.policy.upgrades import upgrade_14_to_15
    #     upgrade_14_to_15(self.portal)

    #     aq_parent().manage_renameObject.assert_called_with('kauppa', 'luontokauppa')

    #     item = article1.relatedItems[0]
    #     self.assertEqual(item.to_id, to_id)
    #     self.assertNotEqual(item.from_id, from_id)

    @mock.patch('slt.policy.upgrades.unregister_layer')
    def test_unregister_layer_ISltPolicyLayer(self, unregister_layer):
        from slt.policy.upgrades import unregister_layer_ISltPolicyLayer
        unregister_layer_ISltPolicyLayer(self.portal)
        unregister_layer.assert_called_with('slt.policy')
