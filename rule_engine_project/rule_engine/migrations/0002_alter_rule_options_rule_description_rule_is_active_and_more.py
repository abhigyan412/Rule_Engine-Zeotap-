# Generated by Django 5.1.1 on 2024-10-22 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rule_engine', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rule',
            options={'ordering': ['created_at'], 'verbose_name': 'Rule', 'verbose_name_plural': 'Rules'},
        ),
        migrations.AddField(
            model_name='rule',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='rule',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='rule',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
