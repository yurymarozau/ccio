from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

from rest_framework import permissions


class BasePermission(permissions.BasePermission):
    """Base permission to check if user has specified permission in permission attribute."""

    message = _('permission_denied')
    permission = None

    def has_permission(self, request, view):
        return bool(request.user and request.user.has_perm(self.permission))


class GroupPermissionsService:
    def __init__(self):
        # Import in method because this code can be called in ready method of django application
        # (models are not loaded yet)
        # from apps.example_app.models import ExampleModel

        self.groups_permissions = [
            # {
            #     'group_name': 'example_group_name',
            #     'content_type_model': ExampleModel,
            #     'permissions': ['view_examplemodel', 'delete_examplemodel'],
            # },
        ]

    def add_permissions_to_group(self, sender: AppConfig):
        """
        Method to add permissions to group.
        If group isn't exists, it will create it.
        """

        # Import in method because this code can be called in ready method of django application
        # (models are not loaded yet)
        from django.contrib.auth.models import Group, Permission
        from django.contrib.contenttypes.models import ContentType

        for permission_info in self.groups_permissions:
            group_name = permission_info['group_name']
            content_type_model = permission_info['content_type_model']
            group_permissions = permission_info['permissions']

            group, created = Group.objects.get_or_create(name=group_name)
            content_type = ContentType.objects.get_for_model(content_type_model)

            for permission in group_permissions:
                new_permission = Permission.objects.get(codename=permission, content_type=content_type)
                group.permissions.add(new_permission)

    @classmethod
    def post_migrate_callback(cls, sender: AppConfig, **kwargs):
        """
        Callback for post migrate signal.
        """
        cls().add_permissions_to_group(sender)
