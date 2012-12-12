from Products.CMFCore.utils import getToolByName
from slt.policy.tests.base import IntegrationTestCase

import mock
import unittest


class TestCase(unittest.TestCase):
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
