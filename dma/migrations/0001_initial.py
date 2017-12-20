# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-20 05:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=128, null=True, unique=True)),
                ('metabinding', models.CharField(blank=True, db_column='MetaBinding', max_length=20, null=True)),
                ('districtid', models.IntegerField(blank=True, db_column='DistrictId', null=True)),
            ],
            options={
                'db_table': 'community',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DmaZone',
            fields=[
                ('dma_id', models.AutoField(primary_key=True, serialize=False)),
                ('zone_name', models.CharField(blank=True, max_length=64, null=True, unique=True, verbose_name='\u5206\u533a\u540d\u79f0')),
                ('zone_area', models.FloatField(blank=True, null=True, verbose_name='\u5206\u533a\u9762\u79ef\uff08\u5e73\u65b9\u516c\u91cc\uff09')),
                ('zone_water_in', models.FloatField(blank=True, null=True, verbose_name='\u5206\u533a\u8fdb\u6c34\u91cf\uff08 m3\uff09')),
                ('registed_user', models.FloatField(blank=True, null=True, verbose_name='\u6ce8\u518c\u7528\u6237\u603b\u6570\uff08\u4e07\u6237\uff09')),
                ('pipeline_length', models.FloatField(blank=True, null=True, verbose_name='\u7ba1\u7ebf\u957f\u5ea6\uff08 km\uff09')),
                ('sub_zone_num', models.FloatField(blank=True, null=True, verbose_name='\u4e0b\u4e00\u7ea7\u5206\u533a\u6570\u91cf\uff08\u4e2a\uff09')),
                ('dma_num', models.FloatField(blank=True, null=True, verbose_name='\u5206\u533a\u4e2d DMA \u6570\u91cf\uff08\u4e2a\uff09')),
                ('measure_per_actual', models.FloatField(blank=True, null=True, verbose_name='\u6c34\u8868\u6284\u89c1\u7387\uff08 %\uff09')),
                ('measure_precision', models.FloatField(blank=True, null=True, verbose_name='\u6284\u8868\u51c6\u786e\u7387\uff08 %\uff09')),
                ('zone_sale', models.FloatField(blank=True, null=True, verbose_name='\u5206\u533a\u9500\u552e\u6c34\u91cf\uff08 m3\uff09')),
                ('nightflow_min', models.FloatField(blank=True, null=True, verbose_name='\u591c\u95f4\u6700\u5c0f\u6d41\u91cf\uff08 m3\uff09')),
                ('online_presspoint_num', models.FloatField(blank=True, null=True, verbose_name='\u5728\u7ebf\u538b\u529b\u70b9\u6570\u91cf\uff08\u4e2a\uff09')),
                ('online_flowmeter_num', models.FloatField(blank=True, null=True, verbose_name='\u5728\u7ebf\u6d41\u91cf\u8ba1\u6570\u91cf\uff08\u4e2a\uff09')),
                ('online_water_quality_m_num', models.FloatField(blank=True, null=True, verbose_name='\u5728\u7ebf\u6c34\u8d28\u76d1\u6d4b\u70b9\u6570\u91cf\uff08\u4e2a\uff09')),
                ('charge_watermeter_num', models.FloatField(blank=True, null=True, verbose_name='\u6536\u8d39\u7528\u8fdc\u4f20\u6c34\u8868\u6570\u91cf\uff08\u53ea\uff09')),
                ('charge_waterwater_percent', models.FloatField(blank=True, null=True, verbose_name='\u6536\u8d39\u7528\u8fdc\u4f20\u6c34\u8868\u6c34\u91cf\u5360\u5206\u533a\u9500 \u6c34\u91cf\u6bd4\uff08 %\uff09')),
                ('zone_detect_leak_num', models.FloatField(blank=True, null=True, verbose_name='\u5206\u533a\u63a2\u51fa\u6f0f\u70b9\u603b\u6570\uff08\u4e2a\uff09')),
                ('leak_water', models.FloatField(blank=True, null=True, verbose_name='\u6f0f\u5931\u6c34\u91cf\uff08 m3\uff09')),
                ('leak_obscur_water', models.FloatField(blank=True, null=True, verbose_name='\u6697\u6f0f\u6c34\u91cf\uff08 m3\uff09')),
                ('leak_obvious_water', models.FloatField(blank=True, null=True, verbose_name='\u660e\u6f0f\u6c34\u91cf\uff08 m3\uff09')),
                ('leak_rate', models.FloatField(blank=True, null=True, verbose_name='\u6f0f\u635f\u7387\uff08 %\uff09')),
                ('pressure_quality', models.FloatField(blank=True, null=True, verbose_name='\u538b\u529b\u5408\u683c\u7387\uff08 %\uff09')),
                ('water_quality', models.FloatField(blank=True, null=True, verbose_name='\u6c34\u8d28\u5408\u683c\u7387\uff08 %\uff09')),
                ('zone_inner_pressure', models.FloatField(blank=True, null=True, verbose_name='\u5206\u533a\u5185\u538b\u529b\uff08 MPa\uff09')),
                ('slug', models.SlugField()),
            ],
            options={
                'db_table': 'dmazone',
            },
        ),
        migrations.CreateModel(
            name='FlowShareDayTax',
            fields=[
                ('pid', models.IntegerField(db_column='PID', primary_key=True, serialize=False)),
                ('readtime', models.CharField(db_column='ReadTime', max_length=20)),
                ('simid', models.CharField(db_column='SIMID', max_length=20)),
                ('flux', models.FloatField(blank=True, db_column='Flux', null=True)),
                ('plustotalflux', models.FloatField(blank=True, db_column='PlusTotalFlux', null=True)),
                ('reversetotalflux', models.FloatField(blank=True, db_column='ReverseTotalFlux', null=True)),
                ('warning', models.CharField(db_column='Warning', max_length=50)),
                ('warningdesc', models.CharField(db_column='WarningDesc', max_length=20)),
            ],
            options={
                'db_table': 'flow_share_day_tax',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='HdbTianhouBig',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('rvalue', models.CharField(blank=True, db_column='RValue', max_length=30, null=True)),
                ('fvalue', models.CharField(blank=True, db_column='FValue', max_length=30, null=True)),
                ('meterstate', models.CharField(blank=True, db_column='MeterState', max_length=30, null=True)),
                ('commstate', models.CharField(blank=True, db_column='CommState', max_length=30, null=True)),
                ('rtime', models.CharField(blank=True, db_column='RTime', max_length=30, null=True)),
                ('lastrvalue', models.CharField(blank=True, db_column='LastRValue', max_length=30, null=True)),
                ('lastrtime', models.CharField(blank=True, db_column='LastRTime', max_length=30, null=True)),
                ('dosage', models.CharField(blank=True, db_column='Dosage', max_length=30, null=True)),
                ('watermeterid', models.IntegerField(blank=True, db_column='WaterMeterId', null=True)),
            ],
            options={
                'db_table': 'hdb_tianhou_big',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PressShareDayTax',
            fields=[
                ('pid', models.IntegerField(db_column='PID', primary_key=True, serialize=False)),
                ('readtime', models.CharField(db_column='ReadTime', max_length=20)),
                ('simid', models.CharField(db_column='SIMID', max_length=20)),
                ('pressure', models.FloatField(blank=True, db_column='Pressure', null=True)),
                ('warning', models.CharField(db_column='Warning', max_length=50)),
                ('warningdesc', models.CharField(db_column='WarningDesc', max_length=20)),
            ],
            options={
                'db_table': 'press_share_day_tax',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tblfminfo',
            fields=[
                ('precinctname', models.CharField(db_column='PrecinctName', max_length=50)),
                ('filialename', models.CharField(db_column='FilialeName', max_length=50)),
                ('usertype', models.CharField(db_column='UserType', max_length=20)),
                ('userid', models.CharField(db_column='UserID', max_length=20)),
                ('username', models.CharField(db_column='UserName', max_length=50)),
                ('useraddress', models.CharField(db_column='UserAddress', max_length=50)),
                ('simid', models.CharField(db_column='SIMID', max_length=20, primary_key=True, serialize=False)),
                ('fmtype', models.CharField(db_column='FMType', max_length=50)),
                ('fmaddress', models.CharField(db_column='FMAddress', max_length=20)),
                ('installdate', models.CharField(db_column='InstallDate', max_length=20)),
                ('install_jd', models.CharField(db_column='Install_JD', max_length=10)),
                ('install_wd', models.CharField(db_column='Install_WD', max_length=10)),
                ('updatetime', models.CharField(db_column='UpdateTime', max_length=20)),
                ('lastreadtime', models.CharField(db_column='LastReadTime', max_length=20)),
                ('lastflux', models.FloatField(blank=True, db_column='LastFlux', null=True)),
                ('lasttotalflux', models.FloatField(blank=True, db_column='LastTotalFlux', null=True)),
                ('lastpressure', models.FloatField(blank=True, db_column='LastPressure', null=True)),
                ('lastwarning', models.CharField(db_column='LastWarning', max_length=50)),
                ('lastwarningdesc', models.CharField(db_column='LastWarningDesc', max_length=20)),
                ('lastwarningtime', models.CharField(db_column='LastWarningTime', max_length=20)),
                ('lastreadpressuretime', models.CharField(db_column='LastReadPressureTime', max_length=20)),
                ('lastreadfluxtime', models.CharField(db_column='LastReadFluxTime', max_length=20)),
            ],
            options={
                'db_table': 'tblfminfo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Watermeter',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('numbersth', models.CharField(blank=True, db_column='NumberSth', max_length=30, null=True)),
                ('buildingname', models.CharField(blank=True, db_column='BuildingName', max_length=128, null=True)),
                ('roomname', models.CharField(blank=True, db_column='RoomName', max_length=128, null=True)),
                ('nodeaddr', models.CharField(blank=True, db_column='NodeAddr', max_length=30, null=True)),
                ('wateraddr', models.CharField(blank=True, db_column='WaterAddr', max_length=30, null=True)),
                ('rvalue', models.CharField(blank=True, db_column='RValue', max_length=30, null=True)),
                ('fvalue', models.CharField(blank=True, db_column='FValue', max_length=30, null=True)),
                ('metertype', models.CharField(blank=True, db_column='MeterType', max_length=30, null=True)),
                ('meterstate', models.CharField(blank=True, db_column='MeterState', max_length=30, null=True)),
                ('commstate', models.CharField(blank=True, db_column='CommState', max_length=30, null=True)),
                ('rtime', models.CharField(blank=True, db_column='RTime', max_length=30, null=True)),
                ('lastrvalue', models.CharField(blank=True, db_column='LastRValue', max_length=30, null=True)),
                ('lastrtime', models.CharField(blank=True, db_column='LastRTime', max_length=30, null=True)),
                ('dosage', models.CharField(blank=True, db_column='Dosage', max_length=30, null=True)),
                ('islargecalibermeter', models.IntegerField(blank=True, db_column='IsLargeCaliberMeter', null=True)),
                ('communityid', models.IntegerField(blank=True, db_column='CommunityId', null=True)),
                ('metabinding', models.CharField(blank=True, db_column='MetaBinding', max_length=20, null=True)),
            ],
            options={
                'db_table': 'watermeter',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Wbalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('totoal_in', models.FloatField(blank=True, null=True)),
                ('auth_use', models.FloatField(blank=True, null=True)),
                ('loss', models.FloatField(blank=True, null=True)),
                ('charge_auth', models.FloatField(blank=True, null=True)),
                ('uncharge_auth', models.FloatField(blank=True, null=True)),
                ('charge_measure', models.FloatField(blank=True, null=True)),
                ('charge_unmeasure', models.FloatField(blank=True, null=True)),
                ('uncharge_measure', models.FloatField(blank=True, null=True)),
                ('uncharge_unmeasure', models.FloatField(blank=True, null=True)),
                ('apparent_loss', models.FloatField(blank=True, null=True)),
                ('actual_loss', models.FloatField(blank=True, null=True)),
                ('unauth_use', models.FloatField(blank=True, null=True)),
                ('statistic_error', models.FloatField(blank=True, null=True)),
                ('money_back', models.FloatField(blank=True, null=True)),
                ('money_waste', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'wbalance',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ZoneTree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField()),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='dma.ZoneTree')),
            ],
            options={
                'db_table': 'zonetree',
            },
        ),
        migrations.AlterUniqueTogether(
            name='watermeter',
            unique_together=set([('nodeaddr', 'wateraddr')]),
        ),
        migrations.AddField(
            model_name='dmazone',
            name='zone',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dmazone', to='dma.ZoneTree', verbose_name='\u5206\u533a\u9009\u62e9'),
        ),
        migrations.AlterUniqueTogether(
            name='zonetree',
            unique_together=set([('slug', 'parent')]),
        ),
        migrations.AlterUniqueTogether(
            name='dmazone',
            unique_together=set([('slug', 'zone')]),
        ),
    ]
