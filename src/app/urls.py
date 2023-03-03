from django.urls import path

from .views import base

urlpatterns = [
    path('main/', base, {'name': 'Main'}, name='main'),
    path('about_us/', base, {'name': 'About company'}, name='About'),
    path('top_level/', base, {'name': 'Top Level'}, name='Top_level'),
    path('links/', base, {'name': 'Links'}, name='Links'),
    path('top_level/sub-item_14', base, {'name': 'Sub-item 14'}, name='Sub-item_14'),
    path('top_level/sub-item_15', base, {'name': 'Sub-item 15'}, name='Sub-item_15'),
    path('top_level/sub-item_15/item_16', base, {'name': 'Sub-item 16'}, name='Sub-item_16'),
    path('top_level/sub-item_15/item_17', base, {'name': 'Item 17'}, name='Item_17'),
    path('top_level/sub-item_15/item_18', base, {'name': 'Item 18'}, name='Item_18'),
    path('top_level/sub-item_15/item_16/item_19', base, {'name': 'Item 19'}, name='item_19'),
]
