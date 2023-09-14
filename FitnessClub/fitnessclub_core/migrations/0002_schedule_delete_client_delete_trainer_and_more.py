# Generated by Django 4.2.1 on 2023-06-04 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitnessclub_core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_time', models.TimeField(default='09:00', help_text='Gym opening time')),
                ('close_time', models.TimeField(default='21:00', help_text='Gym closing time')),
                ('is_works_on_weekends', models.BooleanField(default=False, help_text='Is it works on weekends')),
            ],
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Trainer',
        ),
        migrations.RemoveField(
            model_name='gym',
            name='close_time',
        ),
        migrations.RemoveField(
            model_name='gym',
            name='open_time',
        ),
        migrations.AddField(
            model_name='gym',
            name='gym_membership',
            field=models.ManyToManyField(help_text='Gym membership of the gym', to='fitnessclub_core.gymmembership'),
        ),
        migrations.AlterField(
            model_name='gymmembership',
            name='cost',
            field=models.IntegerField(help_text='Cost of the gym membership'),
        ),
        migrations.AddField(
            model_name='gym',
            name='schedule',
            field=models.ForeignKey(help_text='Schedule of the gym', null=True, on_delete=django.db.models.deletion.CASCADE, to='fitnessclub_core.schedule'),
        ),
    ]
