# Generated by Django 3.2.23 on 2024-06-24 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_regulacion_fecha_edicion'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cambiar_pass',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
