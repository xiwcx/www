# Generated by Django 2.1.4 on 2018-12-28 01:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=500)),
                ('height', models.IntegerField()),
                ('upload', models.ImageField(height_field='height', upload_to='', width_field='width')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('width', models.IntegerField()),
            ],
            options={
                'db_table': 'image',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('markdown', models.TextField()),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=20)),
                ('hero', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.Image')),
            ],
            options={
                'db_table': 'post',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('markdown', models.TextField()),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('type', models.CharField(choices=[('code', 'Code'), ('art', 'Art')], default=None, max_length=20)),
                ('hero', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.Image')),
            ],
            options={
                'db_table': 'work',
            },
        ),
        migrations.AddField(
            model_name='image',
            name='related_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='content.Post'),
        ),
        migrations.AddField(
            model_name='image',
            name='related_work',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='content.Work'),
        ),
    ]
