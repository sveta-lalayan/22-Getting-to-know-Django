# Generated by Django 5.1.3 on 2024-12-05 11:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ["name", "description"],
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                help_text="Выберите категорию",
                on_delete=django.db.models.deletion.CASCADE,
                to="catalog.category",
                verbose_name="категория",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateField(
                auto_now_add=True,
                help_text="Дата создания",
                verbose_name="дата создания",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateField(
                auto_now=True,
                help_text="Дата изменения",
                verbose_name="дата последнего изменения",
            ),
        ),
    ]
