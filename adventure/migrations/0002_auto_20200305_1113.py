# Generated by Django 3.0.4 on 2020-03-05 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='x',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='y',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='room',
            name='e_to',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='room',
            name='n_to',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='s_to',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='w_to',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.DeleteModel(
            name='Player',
        ),
    ]
