# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

GENDER_CHOICE=(
    ('M',u'男'),
    ('F',u'女'),
)

# Create your models here.
class Patient(models.Model):
    id_card = models.CharField(u'身份证号码',max_length=20,db_index=True)
    name = models.CharField(u'姓名',max_length=30,blank=False,db_index=True)
    nick_name = models.CharField(u'别名',max_length=30,blank=True,db_index=True)
    gender = models.CharField(u'性别',max_length=1, blank=False, choices=GENDER_CHOICE)
    dob = models.DateTimeField(u'出生日期')
    telephone = models.CharField(u'电话号码', max_length=20,db_index=True)
    create_at = models.DateTimeField(u'注册时间',default=timezone.now)
    last_active_at = models.DateTimeField(u'更新时间',auto_now=True)
    class Meta:
        verbose_name = '患者信息'
        verbose_name_plural = '患者信息'
    
    def __unicode__(self):
        return self.name 

class Family(models.Model):
    ower = models.ForeignKey(Patient,on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    credit =models.IntegerField(default=0)
    
    class Meta:
        verbose_name=u'会员卡'
  
class  Appointment(models.Model):
    patient =models.ForeignKey(Patient,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)