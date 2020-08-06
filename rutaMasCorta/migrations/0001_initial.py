# Generated by Django 2.2.15 on 2020-08-06 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rows', models.IntegerField(max_length=2)),
            ],
            options={
                'verbose_name': 'rows',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nodo_Origen', models.CharField(max_length=2)),
            ],
            options={
                'verbose_name': 'Nodo_Origen',
            },
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nodo_Destino', models.CharField(max_length=2)),
            ],
            options={
                'verbose_name': 'Nodo_Destino',
            },
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Peso', models.IntegerField(max_length=2)),
            ],
            options={
                'verbose_name': 'Peso',
            },
        ),
    ]
