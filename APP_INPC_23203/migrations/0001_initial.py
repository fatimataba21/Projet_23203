# Ce fichier sera généré automatiquement par la commande `python manage.py makemigrations`
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=45)),
                ('label', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45, null=True, blank=True)),
                ('unit_measure', models.CharField(max_length=45, null=True, blank=True)),
                ('product_type', models.ForeignKey(null=True, on_delete=models.SET_NULL, to='APP_INPC_23203.ProductType')),
            ],
        ),
        migrations.CreateModel(
            name='Wilaya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=252)),
            ],
        ),
        migrations.CreateModel(
            name='Moughataa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=45)),
                ('label', models.CharField(max_length=45)),
                ('wilaya', models.ForeignKey(on_delete=models.CASCADE, to='APP_INPC_23203.Wilaya')),
            ],
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=45)),
                ('moughataa', models.ForeignKey(on_delete=models.CASCADE, to='APP_INPC_23203.Moughataa')),
            ],
        ),
        migrations.CreateModel(
            name='PointOfSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=45)),
                ('type', models.CharField(max_length=45)),
                ('gps_lat', models.FloatField(null=True, blank=True)),
                ('gps_lon', models.FloatField(null=True, blank=True)),
                ('commune', models.ForeignKey(on_delete=models.CASCADE, to='APP_INPC_23203.Commune')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('date_from', models.DateField()),
                ('date_to', models.DateField(null=True, blank=True)),
                ('product', models.ForeignKey(on_delete=models.CASCADE, to='APP_INPC_23203.Product')),
                ('point_of_sale', models.ForeignKey(on_delete=models.CASCADE, to='APP_INPC_23203.PointOfSale')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('date_from', models.DateField()),
                ('date_to', models.DateField(null=True, blank=True)),
                ('product', models.ForeignKey(on_delete=models.CASCADE, to='APP_INPC_23203.Product')),
                ('cart_product', models.ForeignKey(on_delete=models.CASCADE, to='APP_INPC_23203.Cart')),
            ],
        ),
    ]
