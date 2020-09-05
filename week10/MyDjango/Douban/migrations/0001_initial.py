# Generated by Django 2.2.15 on 2020-09-05 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StatTable',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('mean', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'stat_table',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='QipaoshuiCleaned',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('qptime', models.DateTimeField(blank=True, null=True)),
                ('sentiment', models.IntegerField(blank=True, null=True)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Douban.StatTable')),
            ],
            options={
                'db_table': 'qipaoshui_cleaned',
                'managed': True,
            },
        ),
    ]
