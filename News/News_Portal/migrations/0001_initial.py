# Generated by Django 4.2.2 on 2023-06-15 22:02

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
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('AR', 'статья'), ('NE', 'новость')], default='AR', max_length=2)),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('header', models.CharField(default='заголовок', max_length=255)),
                ('text', models.TextField(default='текст статьи/новости')),
                ('_rating', models.IntegerField(db_column='rating', default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News_Portal.category')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News_Portal.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='Category',
            field=models.ManyToManyField(through='News_Portal.PostCategory', to='News_Portal.category'),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News_Portal.author'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='текст комментария')),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('_rating', models.IntegerField(db_column='rating', default=0)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News_Portal.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
