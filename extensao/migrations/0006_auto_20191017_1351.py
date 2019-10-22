# Generated by Django 2.0 on 2019-10-17 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('extensao', '0005_auto_20191017_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoOferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_oferta', models.CharField(max_length=50, verbose_name='Tipo da Oferta')),
            ],
            options={
                'verbose_name': 'Tipo da Oferta',
                'verbose_name_plural': 'Tipo de Oferta',
            },
        ),
        migrations.AlterModelOptions(
            name='oferta',
            options={'verbose_name_plural': 'Ofertas'},
        ),
        migrations.AddField(
            model_name='oferta',
            name='tipo_oferta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='extensao.TipoOferta'),
            preserve_default=False,
        ),
    ]