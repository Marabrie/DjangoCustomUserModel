# Generated by Django 3.2.8 on 2021-10-25 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kafkan_store', '0006_alter_kafkan_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kafkan',
            name='name',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
