# Generated by Django 3.2.5 on 2021-07-02 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bikes',
            options={'ordering': ['-date_created'], 'verbose_name_plural': 'Bikes'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='electronics',
            options={'ordering': ['-date_created'], 'verbose_name_plural': 'Electronics'},
        ),
        migrations.AlterModelOptions(
            name='fashion_and_beauty',
            options={'ordering': ['-date_created'], 'verbose_name_plural': 'Fashion_and_beauty'},
        ),
        migrations.AlterModelOptions(
            name='furniture',
            options={'ordering': ['-date_created'], 'verbose_name_plural': 'Furniture'},
        ),
        migrations.AlterModelOptions(
            name='mobiles',
            options={'ordering': ['-date_created'], 'verbose_name_plural': 'Mobiles'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['-date_created'], 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='sports_and_hobbies',
            options={'ordering': ['-date_created'], 'verbose_name_plural': 'Sports_and_hobbies'},
        ),
        migrations.AlterModelOptions(
            name='vehicles',
            options={'ordering': ['-date_created'], 'verbose_name_plural': 'Vehicles'},
        ),
    ]