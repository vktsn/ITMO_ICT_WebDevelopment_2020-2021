# Generated by Django 3.1.2 on 2020-10-23 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Наименование')),
            ],
        ),
        migrations.CreateModel(
            name='SkillOfWarrior',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(verbose_name='Уровень освоения умения')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warriors.skill', verbose_name='Умение')),
            ],
        ),
        migrations.CreateModel(
            name='Warrior',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.CharField(choices=[('s', 'student'), ('d', 'developer'), ('t', 'teamlead')], max_length=1, verbose_name='Pacca')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('level', models.IntegerField(default=0, verbose_name='Level')),
                ('profession', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='warriors.profession', verbose_name='Profession')),
                ('skill', models.ManyToManyField(related_name='warrior_skills', through='warriors.SkillOfWarrior', to='warriors.Skill')),
            ],
        ),
        migrations.AddField(
            model_name='skillofwarrior',
            name='warrior',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warriors.warrior', verbose_name='Воин'),
        ),
    ]
