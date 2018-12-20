# Generated by Django 2.1.4 on 2018-12-18 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('none', models.IntegerField(default=-1000)),
                ('name', models.CharField(blank=True, max_length=122100, null=True)),
                ('rating', models.CharField(blank=True, max_length=122100, null=True)),
                ('gape', models.CharField(blank=True, max_length=122100, null=True)),
                ('edu_dob', models.CharField(blank=True, max_length=122100, null=True)),
                ('exp_dob', models.CharField(blank=True, max_length=122100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('none', models.IntegerField(default=-1000)),
                ('name', models.CharField(blank=True, max_length=122100, null=True)),
                ('rating', models.CharField(blank=True, max_length=122100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(blank=True, max_length=122100, null=True)),
                ('rating', models.CharField(blank=True, max_length=122100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('none', models.IntegerField(default=-1000)),
                ('name', models.CharField(blank=True, max_length=122100, null=True)),
                ('rating', models.CharField(blank=True, max_length=122100, null=True)),
                ('artist', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='cvs', to='sync.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('none', models.IntegerField(default=-1000)),
                ('name', models.CharField(blank=True, max_length=122100, null=True)),
                ('rating', models.CharField(blank=True, max_length=122100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(blank=True, max_length=122100, null=True)),
                ('rating', models.CharField(blank=True, max_length=122100, null=True)),
                ('company', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='artists', to='sync.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('none', models.IntegerField(default=-1000)),
                ('name', models.CharField(blank=True, max_length=122100, null=True)),
                ('rating', models.CharField(blank=True, max_length=122100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('none', models.IntegerField(default=-1000)),
                ('name', models.CharField(blank=True, max_length=122100, null=True)),
                ('rating', models.CharField(blank=True, max_length=122100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('none', models.IntegerField(default=-1000)),
                ('name', models.CharField(blank=True, max_length=122100, null=True)),
                ('rating', models.CharField(blank=True, max_length=122100, null=True)),
                ('gape', models.CharField(blank=True, max_length=122100, null=True)),
                ('edu_dob', models.CharField(blank=True, max_length=122100, null=True)),
                ('exp_dob', models.CharField(blank=True, max_length=122100, null=True)),
                ('company', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='requirements', to='sync.Company')),
                ('courses', models.ManyToManyField(blank=True, related_name='requirements', to='sync.Course')),
                ('exps', models.ManyToManyField(blank=True, related_name='requirements', to='sync.Exp')),
                ('qualities', models.ManyToManyField(blank=True, related_name='requirements', to='sync.Quality')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='degree',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='sync.Degree'),
        ),
        migrations.AddField(
            model_name='course',
            name='institute',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='sync.Institute'),
        ),
        migrations.AddField(
            model_name='artist',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='artists', to='sync.Course'),
        ),
        migrations.AddField(
            model_name='artist',
            name='exps',
            field=models.ManyToManyField(blank=True, related_name='artists', to='sync.Exp'),
        ),
        migrations.AddField(
            model_name='artist',
            name='qualities',
            field=models.ManyToManyField(blank=True, related_name='artists', to='sync.Quality'),
        ),
        migrations.AddField(
            model_name='artist',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='artists', to=settings.AUTH_USER_MODEL),
        ),
    ]