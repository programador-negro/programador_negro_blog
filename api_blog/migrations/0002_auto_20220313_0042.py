# Generated by Django 3.0.7 on 2022-03-13 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_blog.Types'),
        ),
    ]
