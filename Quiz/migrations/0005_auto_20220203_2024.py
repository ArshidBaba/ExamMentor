# Generated by Django 3.2.12 on 2022-02-03 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0004_auto_20220203_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Category', to='Quiz.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='questions',
            name='title',
            field=models.CharField(default='Question', max_length=255, verbose_name='Title'),
        ),
    ]
