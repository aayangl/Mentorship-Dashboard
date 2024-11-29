from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='qualification',
            field=models.CharField(default='Not Specified', max_length=200),
        ),
    ]
