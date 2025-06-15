from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Product


@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    if sender.name == 'catalog':
        moderator_group, created = Group.objects.get_or_create(name="Модератор продуктов")

        content_type = ContentType.objects.get_for_model(Product)

        can_unpublish_permission, created = Permission.objects.get_or_create(
            codename='can_unpublish_product',
            name='Can unpublish product',
            content_type=content_type,
        )

        delete_product_permission = Permission.objects.get(
            codename='delete_product',
            content_type=content_type,
        )

        moderator_group.permissions.add(can_unpublish_permission, delete_product_permission)
        moderator_group.save()
        print("Группа 'Модератор продуктов' создана и права назначены.")
