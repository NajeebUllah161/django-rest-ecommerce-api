# Generated by Django 3.2.5 on 2021-07-02 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210702_1229'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='electronics',
            options={'ordering': ['-date_created'], 'verbose_name_plural': 'Add Products'},
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]