# Generated by Django 4.2.3 on 2023-08-09 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_cluster_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='game',
            field=models.ForeignKey(blank=True, db_column='game', null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.game'),
        ),
    ]