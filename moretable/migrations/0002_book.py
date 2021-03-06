# Generated by Django 2.2.1 on 2020-02-15 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moretable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='书籍名字')),
                ('pub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moretable.Publish')),
            ],
            options={
                'verbose_name_plural': '书籍',
                'db_table': 'book',
            },
        ),
    ]
