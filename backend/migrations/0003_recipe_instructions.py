# Generated by Django 4.1.3 on 2022-11-23 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZeroFoodWaste', '0002_recipe_delete_recipes'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=models.JSONField(default=''),
            preserve_default=False,
        ),
    ]
