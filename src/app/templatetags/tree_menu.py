import re

from django import template
from django.conf import settings
from django.http import HttpRequest
from django.template import RequestContext
from django.urls import NoReverseMatch, reverse

from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('app/menu.html', takes_context=True)
def draw_menu(context: RequestContext, name: str = '', parent: int = 0):
    """Draw tree menu.

    Arguments:
        context:
        name:
        parent
    """

    if parent != 0 and 'menu' in context:
        menu = context['menu']
    else:

        is_url = re.compile(settings.URL_PATTERN)

        # Get path if request exist
        current_path = context['request'].path \
            if 'request' in context and isinstance(context['request'], HttpRequest) \
            else ''

        data = MenuItem.objects.select_related()\
            .filter(main_menu__name=name)\
            .order_by('pk')

        menu = []

        for item in data:

            path = item.path.strip()

            target = '_self'

            if is_url.match(path):
                url = path
                target = '_blank'
            else:
                try:
                    url = reverse(path)
                except NoReverseMatch:
                    url = path

            menu.append({
                'id': item.pk,
                'url': url,
                'target': target,
                'name': item.name,
                'parent': item.parent_id or 0,
                'active': True if url == current_path else False,
            })

    return {
        'menu': menu,
        'current_menu': (item for item in menu if 'parent' in item and item['parent'] == parent),
    }
