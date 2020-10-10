# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class AreaEn(models.Model):
    area_id = models.AutoField(primary_key=True)
    area_parent_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    area_code = models.CharField(max_length=20, blank=True, null=True)
    area_name = models.CharField(max_length=50, blank=True, null=True)
    area_level = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area_en'




class Indicator(models.Model):
    indicator_id = models.AutoField(primary_key=True)
    indicator_name = models.CharField(max_length=255, blank=True, null=True)
    classification = models.ForeignKey('IndicatorClassification', models.DO_NOTHING, blank=True, null=True)
    indicator_order = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indicator'


class IndicatorClassification(models.Model):
    classification_id = models.AutoField(primary_key=True)
    classification_parent_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    classification_name = models.CharField(max_length=90, blank=True, null=True)
    classification_order = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indicator_classification'


class IndicatorUnitSubgroup(models.Model):
    iusnid = models.AutoField(primary_key=True)
    indicator = models.ForeignKey(Indicator, models.DO_NOTHING)
    unit = models.ForeignKey('Unit', models.DO_NOTHING)
    subgroup = models.ForeignKey('Subgroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'indicator_unit_subgroup'


class Subgroup(models.Model):
    subgroup_id = models.AutoField(primary_key=True)
    subgroup_name = models.CharField(max_length=20, blank=True, null=True)
    subgroup_order = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subgroup'



class Timeperiod(models.Model):
    timeperiod_id = models.AutoField(primary_key=True)
    timeperiod = models.CharField(max_length=90, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timeperiod'


class Unit(models.Model):
    unit_id = models.AutoField(primary_key=True)
    unit_name = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unit'


class UtData(models.Model):
    data_id = models.AutoField(primary_key=True)
    iusnid = models.ForeignKey(IndicatorUnitSubgroup, models.DO_NOTHING, db_column='iusnid')
    timeperiod = models.ForeignKey(Timeperiod, models.DO_NOTHING)
    area = models.ForeignKey(AreaEn, models.DO_NOTHING)
    indicator = models.ForeignKey(Indicator, models.DO_NOTHING)
    unit = models.ForeignKey(Unit, models.DO_NOTHING)
    subgroup = models.ForeignKey(Subgroup, models.DO_NOTHING)
    data_value = models.DecimalField(max_digits=255, decimal_places=5, blank=True, null=True)

    def __str__(self):
        return "data_id: {}".format(self.data_id)

    class Meta:
        managed = False
        db_table = 'ut_data'

class NiStDtbPoly(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    id_field = models.CharField(db_column='id_', max_length=20, blank=True, null=True)  # Field renamed because it ended with '_'.
    dt_name = models.CharField(max_length=40, blank=True, null=True)
    st_name = models.CharField(max_length=40, blank=True, null=True)
    parts_field = models.IntegerField(db_column='parts_', blank=True, null=True)  # Field renamed because it ended with '_'.
    points_field = models.IntegerField(db_column='points_', blank=True, null=True)  # Field renamed because it ended with '_'.
    length_field = models.FloatField(db_column='length_', blank=True, null=True)  # Field renamed because it ended with '_'.
    area_field = models.FloatField(db_column='area_', blank=True, null=True)  # Field renamed because it ended with '_'.
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ni_st_dtb_poly'