# Generated by Django 2.2.12 on 2020-04-19 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Applicant', '0002_auto_20200417_1342'),
        ('Interviewer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewInterviewModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interviewid', models.IntegerField()),
                ('interviewer', models.IntegerField()),
                ('result', models.CharField(max_length=30)),
                ('applicationid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Applicant.ApplicationModel')),
            ],
        ),
        migrations.DeleteModel(
            name='InterviewModel',
        ),
    ]
