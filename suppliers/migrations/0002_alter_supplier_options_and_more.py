# Generated by Django 5.2.1 on 2025-05-12 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supplier',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='decriotion',
            new_name='description',
        ),
    ]
