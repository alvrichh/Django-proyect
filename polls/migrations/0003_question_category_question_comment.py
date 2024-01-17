# Generated by Django 4.2.8 on 2024-01-10 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice_created_at_choice_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('General', 'General'), ('Technical', 'Technical'), ('Personal', 'Personal')], default='General', max_length=20),
        ),
        migrations.AddField(
            model_name='question',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]