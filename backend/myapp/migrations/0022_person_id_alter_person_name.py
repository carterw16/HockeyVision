# Generated by Django 4.2.3 on 2023-08-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_cluster_id_alter_cluster_person'),
    ]

    operations = [

        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.TextField(),
        ),
        migrations.AddField(
            model_name='person',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]