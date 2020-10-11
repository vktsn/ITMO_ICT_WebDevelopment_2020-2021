# Generated by Django 3.1.2 on 2020-10-05 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.TextField()),
                ('model', models.TextField()),
                ('color', models.TextField()),
                ('number', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('surname', models.TextField()),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.person')),
            ],
        ),
        migrations.CreateModel(
            name='DriverLicence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('date', models.DateTimeField()),
                ('category', models.CharField(choices=[('A', 'Moto'), ('B', 'Car'), ('C', 'Truck'), ('D', 'Bus')], max_length=1)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.person')),
            ],
        ),
    ]
