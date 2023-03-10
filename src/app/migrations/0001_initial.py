# Generated by Django 4.1.7 on 2023-02-28 11:06

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunSQL('create schema if not exists content;'),
        migrations.CreateModel(
            name='MainMenu',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, max_length=255, verbose_name='Name')),
                ('detailed_name', models.TextField(blank=True, max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Main menu',
                'verbose_name_plural': 'Main menus',
                'db_table': 'content"."main_menu',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, max_length=255, verbose_name='Name')),
                ('path', models.CharField(blank=True, max_length=255, verbose_name='Path')),
                ('main_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.mainmenu', verbose_name='Main menu')),
                ('parent', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.menuitem', verbose_name='Parent menu item')),
            ],
            options={
                'verbose_name': 'Menu item',
                'verbose_name_plural': 'Menu items',
                'db_table': 'content"."menu_item',
            },
        ),
        migrations.AddIndex(
            model_name='mainmenu',
            index=models.Index(fields=['name'], name='main_menu_name_362271_idx'),
        ),
        migrations.AddIndex(
            model_name='menuitem',
            index=models.Index(fields=['name'], name='menu_item_name_ecb6ca_idx'),
        ),
    ]
