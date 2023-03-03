from django.contrib import admin

from .models import MainMenu, MenuItem


@admin.register(MainMenu)
class TreeMainMenuAdmin(admin.ModelAdmin):

    search_fields = ('name',)
    fields = ['name', 'detailed_name', ]
    list_display = ['__str__', 'created', ]
    # list_display = ('name', 'created')
    readonly_fields = ('id', 'created', 'modified', )


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):

    search_fields = ('name',)
    fields = ['name', 'main_menu', 'path', 'parent', ]
    list_display = ['__str__', 'main_menu', 'path', 'parent', 'created', ]
    readonly_fields = ('id', 'created', 'modified',)

    # filter_horizontal = ['main_menu__name', ]
