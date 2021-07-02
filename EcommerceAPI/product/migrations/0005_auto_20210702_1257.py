# Generated by Django 3.2.5 on 2021-07-02 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20210702_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('description', models.TextField()),
                ('imageUrl', models.URLField()),
                ('status', models.BooleanField(default=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.category')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ['-date_created'],
            },
        ),
        migrations.DeleteModel(
            name='Electronics',
        ),
    ]
