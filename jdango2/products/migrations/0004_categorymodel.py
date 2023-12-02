# Generated by Django 4.2.5 on 2023-10-06 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_formmodel_alter_productmodel_descriptions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
    ]