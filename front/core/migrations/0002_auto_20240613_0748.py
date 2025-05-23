# Generated by Django 3.2.23 on 2024-06-13 07:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_activacion', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('referencia', models.CharField(blank=True, max_length=100, null=True)),
                ('nombre', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='tipo_usuario',
            field=models.CharField(choices=[('0', 'Administrador'), ('1', 'Publicador'), ('2', 'Editor'), ('3', 'Lector')], default='0', max_length=1),
        ),
        migrations.CreateModel(
            name='Regulacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correlativo', models.IntegerField(blank=True, null=True)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('esg', models.CharField(choices=[('-1', 'Sin Asignar'), ('0', 'IMPLEMENTACION'), ('1', 'E'), ('2', 'S'), ('2', 'G'), ('2', 'N/A')], default='-1', max_length=2)),
                ('factibilidad', models.CharField(choices=[('-1', 'Sin Asignar'), ('0', 'IMPLEMENTACION'), ('1', 'BAJO'), ('2', 'MEDIO'), ('3', 'ALTO')], default='-1', max_length=2)),
                ('impacto', models.CharField(choices=[('-1', 'Sin Asignar'), ('0', 'IMPLEMENTACION'), ('1', 'BAJO'), ('2', 'MEDIO'), ('3', 'ALTO')], default='-1', max_length=2)),
                ('priorizacion', models.CharField(choices=[('-1', 'Sin Asignar'), ('0', 'POR DEFINIR'), ('1', 'INCIDENCIA'), ('2', 'INFORMAR')], default='-1', max_length=2)),
                ('servicio', models.CharField(choices=[('-1', 'Sin Asignar'), ('0', 'S'), ('1', 'M'), ('2', 'L')], default='-1', max_length=2)),
                ('tipo_act', models.CharField(blank=True, max_length=200, null=True)),
                ('origen', models.CharField(blank=True, max_length=200, null=True)),
                ('resp_gerencial', models.CharField(blank=True, max_length=200, null=True)),
                ('responsable', models.CharField(blank=True, max_length=200, null=True)),
                ('ambito_afectado', models.CharField(blank=True, max_length=200, null=True)),
                ('foco', models.CharField(blank=True, max_length=200, null=True)),
                ('escala', models.ManyToManyField(blank=True, to='core.Comentario')),
            ],
        ),
    ]
