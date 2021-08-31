# Generated by Django 2.2.12 on 2020-04-19 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
        ('Applicant', '0002_auto_20200417_1342'),
        ('Manager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newrecruitmodel',
            old_name='contact',
            new_name='cont',
        ),
        migrations.AlterField(
            model_name='newrecruitmodel',
            name='opcode',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='NewInterViewSchModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sch_date', models.DateField()),
                ('application_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Applicant.ApplicationModel')),
                ('emp_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Admin.AdminModel')),
            ],
        ),
    ]
