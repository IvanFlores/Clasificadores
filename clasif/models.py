from django.db import models
from django.utils import timezone


class Tareas(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'clasif_tareas'

class Arancel(models.Model):
    id = models.IntegerField(primary_key=True)
    cod_arancel = models.CharField(max_length=15, blank=True, null=True)
    subpartida = models.CharField(max_length=15, blank=True, null=True)
    sid = models.CharField(max_length=5, blank=True, null=True)
    desc_grupo = models.CharField(max_length=1000, blank=True, null=True)
    descripcion = models.CharField(max_length=1000, blank=True, null=True)
    cod_ccp = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arancel'


class Caeb(models.Model):
    id = models.IntegerField(primary_key=True)
    seccion = models.CharField(max_length=1, blank=True, null=True)
    nivel = models.SmallIntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=10, blank=True, null=True)
    cod = models.CharField(max_length=10, blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    descrip2 = models.CharField(max_length=5000, blank=True, null=True)
    detalle = models.CharField(max_length=10000, blank=True, null=True)
    os = models.NullBooleanField()
    desc_os = models.CharField(max_length=250, blank=True, null=True)
    fecha_cierre_fiscal = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caeb'


class Nandina(models.Model):
    id = models.IntegerField(primary_key=True)
    cod_nandina = models.CharField(max_length=15, blank=True, null=True)
    desc_nandina = models.CharField(max_length=1000, blank=True, null=True)
    cod_ccp = models.CharField(max_length=15, blank=True, null=True)
    obs = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nandina'


class Productos(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=10, blank=True, null=True)
    nivel = models.SmallIntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=1000, blank=True, null=True)
    obs = models.CharField(max_length=500, blank=True, null=True)
    obsadic = models.CharField(max_length=500, blank=True, null=True)
    sinonimos = models.CharField(max_length=1000, blank=True, null=True)
    tipo = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'


class RelCaebCaeb(models.Model):
    id = models.IntegerField(primary_key=True)
    caeb1 = models.CharField(max_length=15, blank=True, null=True)
    caeb2 = models.CharField(max_length=15, blank=True, null=True)
    tiporel = models.SmallIntegerField(blank=True, null=True)
    obs = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_caeb_caeb'


class RelCcpCaeb(models.Model):
    id = models.IntegerField(primary_key=True)
    codproducto = models.CharField(max_length=15, blank=True, null=True)
    codcaeb = models.CharField(max_length=15, blank=True, null=True)
    obs = models.CharField(max_length=250, blank=True, null=True)
    rel = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_ccp_caeb'


class Sinonimos(models.Model):
    id = models.IntegerField(primary_key=True)
    palabras = models.CharField(max_length=500, blank=True, null=True)
    numacep = models.SmallIntegerField(blank=True, null=True)
    sinonimos = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sinonimos'