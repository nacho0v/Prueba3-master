# Generated by Django 4.0.5 on 2022-06-29 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=15)),
                ('appaterno', models.CharField(max_length=50)),
                ('apmaterno', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('vacuna', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
