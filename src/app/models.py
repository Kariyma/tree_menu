import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    """Class mixin for field s with DateTimeField type."""

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta(object):
        """Class Meta for TimeStampedMixin."""

        abstract = True


class UUIDMixin(models.Model):
    """Class mixin for field s with uuid4 type."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta(object):
        """Class Meta for UUIDMixin."""

        abstract = True


class MainMenu(UUIDMixin, TimeStampedMixin):
    """Class for the MainMenu model."""

    name = models.CharField(_('Name'), max_length=settings.MAX_TEXT_FIELD_LENGTH, blank=True, null=False)
    detailed_name = models.TextField(
        _('Detailed name'),
        max_length=settings.MAX_TEXT_FIELD_LENGTH,
        blank=True,
        null=False,
    )

    class Meta(object):
        """Class Meta for MainMenu."""

        db_table = 'content"."main_menu'
        verbose_name = _('Main menu')
        verbose_name_plural = _('Main menus')
        indexes = [models.Index(fields=['name'])]

    def __str__(self):
        """Represent class MainMenu as string.

        Returns:
            result
        """
        return self.name


class MenuItem(UUIDMixin, TimeStampedMixin):
    """Class for the MenuItem model."""

    name = models.CharField(_('Name'), max_length=settings.MAX_TEXT_FIELD_LENGTH, blank=True, null=False)
    main_menu = models.ForeignKey(
        MainMenu,
        on_delete=models.CASCADE,
        verbose_name=_('Main menu'),
        blank=False,
        null=False
    )
    path = models.CharField(_('Path'), max_length=settings.MAX_TEXT_FIELD_LENGTH, blank=True, null=False)

    parent = models.ForeignKey(
        'self',
        verbose_name=_('Parent menu item'),
        on_delete=models.SET_DEFAULT,
        null=True,
        blank=True,
        default=0
    )

    class Meta(object):
        """Class Meta for MenuItem."""

        db_table = 'content"."menu_item'
        verbose_name = _('Menu item')
        verbose_name_plural = _('Menu items')
        indexes = [models.Index(fields=['name'])]

    def __str__(self):
        """Represent class MenuItem as string.

        Returns:
            result
        """
        return self.name
