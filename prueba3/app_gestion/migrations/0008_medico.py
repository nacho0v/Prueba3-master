# Generated by Django 4.0.5 on 2022-07-10 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestion', '0007_alter_persona_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('med_rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('med_nombre', models.CharField(max_length=15)),
                ('med_appaterno', models.CharField(max_length=50)),
                ('med_apmaterno', models.CharField(max_length=50)),
                ('med_fecha', models.CharField(max_length=20)),
            ],
        ),
    ]