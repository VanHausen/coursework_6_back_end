from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, help_text='Разместите Ваше фото', null=True, upload_to='photos/', verbose_name='фото'),
        ),
    ]
