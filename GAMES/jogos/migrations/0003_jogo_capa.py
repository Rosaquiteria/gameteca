# Generated by Django 3.2.7 on 2021-09-15 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogos', '0002_jogo_publicado'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogo',
            name='capa',
            field=models.ImageField(blank=True, upload_to='capas/%d/%m/%y'),
        ),
    ]