# Generated by Django 4.2.2 on 2023-07-19 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_core', '0002_alter_cheese_name_alter_sauce_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='pizzas',
            field=models.ManyToManyField(related_name='carts', to='main_core.pizza'),
        ),
    ]