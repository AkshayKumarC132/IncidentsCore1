# Generated by Django 5.1.1 on 2024-10-17 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='integrationmspconfig',
            name='access_token',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='integrationmspconfig',
            name='expires_in',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='integrationmspconfig',
            name='refresh_token',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
