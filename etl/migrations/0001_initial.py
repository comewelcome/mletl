# Generated by Django 5.1.3 on 2024-11-08 04:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='datasets/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('processed', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            options={
                'ordering': ['-uploaded_at'],
            },
        ),
        migrations.CreateModel(
            name='DataTransformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transformation_type', models.CharField(choices=[('missing', 'Handle Missing Values'), ('normalize', 'Normalize Data'), ('encode', 'Encode Categorical'), ('scale', 'Scale Features')], max_length=20)),
                ('parameters', models.JSONField(default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etl.dataset')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
