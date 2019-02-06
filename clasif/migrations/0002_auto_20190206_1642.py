# Generated by Django 2.1.5 on 2019-02-06 16:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clasif', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arancel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cod_arancel', models.CharField(blank=True, max_length=15, null=True)),
                ('subpartida', models.CharField(blank=True, max_length=15, null=True)),
                ('sid', models.CharField(blank=True, max_length=5, null=True)),
                ('desc_grupo', models.CharField(blank=True, max_length=1000, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=1000, null=True)),
                ('cod_ccp', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'arancel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Caeb',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('seccion', models.CharField(blank=True, max_length=1, null=True)),
                ('nivel', models.SmallIntegerField(blank=True, null=True)),
                ('codigo', models.CharField(blank=True, max_length=10, null=True)),
                ('cod', models.CharField(blank=True, max_length=10, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True)),
                ('descrip2', models.CharField(blank=True, max_length=5000, null=True)),
                ('detalle', models.CharField(blank=True, max_length=10000, null=True)),
                ('os', models.NullBooleanField()),
                ('desc_os', models.CharField(blank=True, max_length=250, null=True)),
                ('fecha_cierre_fiscal', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'caeb',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nandina',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cod_nandina', models.CharField(blank=True, max_length=15, null=True)),
                ('desc_nandina', models.CharField(blank=True, max_length=1000, null=True)),
                ('cod_ccp', models.CharField(blank=True, max_length=15, null=True)),
                ('obs', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'nandina',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(blank=True, max_length=10, null=True)),
                ('nivel', models.SmallIntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=1000, null=True)),
                ('obs', models.CharField(blank=True, max_length=500, null=True)),
                ('obsadic', models.CharField(blank=True, max_length=500, null=True)),
                ('sinonimos', models.CharField(blank=True, max_length=1000, null=True)),
                ('tipo', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'productos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RelCaebCaeb',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('caeb1', models.CharField(blank=True, max_length=15, null=True)),
                ('caeb2', models.CharField(blank=True, max_length=15, null=True)),
                ('tiporel', models.SmallIntegerField(blank=True, null=True)),
                ('obs', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'rel_caeb_caeb',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RelCcpCaeb',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codproducto', models.CharField(blank=True, max_length=15, null=True)),
                ('codcaeb', models.CharField(blank=True, max_length=15, null=True)),
                ('obs', models.CharField(blank=True, max_length=250, null=True)),
                ('rel', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rel_ccp_caeb',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sinonimos',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('palabras', models.CharField(blank=True, max_length=500, null=True)),
                ('numacep', models.SmallIntegerField(blank=True, null=True)),
                ('sinonimos', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'sinonimos',
                'managed': False,
            },
        ),
        migrations.RenameModel(
            old_name='Post',
            new_name='Tareas',
        ),
    ]
