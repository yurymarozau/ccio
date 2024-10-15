# Generated by Django 5.1.1 on 2024-10-15 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_chain_chainrpc_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chain',
            name='gecko_logo_large_url',
            field=models.URLField(max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='chain',
            name='gecko_logo_small_url',
            field=models.URLField(max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='chain',
            name='gecko_logo_thumb_url',
            field=models.URLField(max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='chain',
            name='info_url',
            field=models.URLField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='chainrpc',
            name='url',
            field=models.URLField(max_length=2048, unique=True),
        ),
        migrations.AlterField(
            model_name='token',
            name='logo_uri',
            field=models.URLField(max_length=2048, null=True),
        ),
    ]
