# Generated by Django 4.1.5 on 2023-01-04 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2)),
                ('start_time', models.TimeField()),
            ],
            options={
                'db_table': 'classrooms',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('salary', models.FloatField(default=0.0)),
            ],
            options={
                'db_table': 'teachers',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('idClassroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.classroom')),
            ],
            options={
                'db_table': 'students',
            },
        ),
        migrations.AddField(
            model_name='classroom',
            name='idTeacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='administration.teacher'),
        ),
        migrations.CreateModel(
            name='OrderedAlumn',
            fields=[
            ],
            options={
                'ordering': ['last_name'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('administration.student',),
        ),
    ]
