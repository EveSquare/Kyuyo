from django.db import models

# Create your models here.
class ZandakaModel(models.Model):
    zandaka = models.IntegerField(
                    blank=True,
                    null=True,
                    verbose_name='残高',
    )
    created_at = models.DateTimeField(null=True,blank=True,auto_now_add=True)
    updated_at = models.DateTimeField(null=True,blank=True,auto_now=True)
    # class Meta:
    #     db_table = '残高'
    def __str__(self):
        return '残高'

class SyunyuModel(models.Model):
    syunyu = models.IntegerField(
                    blank=True,
                    null=True,
                    verbose_name='収入',
    )

    # class Meta:
    #     db_table = '収入'

class MonthlyModel(models.Model):

    syogaku = models.IntegerField(
                    blank=True,
                    null=True,
                    verbose_name='奨学',
                    default=-54000,
    )

    subscription = models.IntegerField(
                    blank=True,
                    null=True,
                    verbose_name='サブスク',
                    default=-540,
    )

    # class Meta:
    #     db_table = '月額'

class ExpenseModel(models.Model):

    spend = models.IntegerField(
                    blank=True,
                    null=True,
                    verbose_name='支出',
    )

    # class Meta:
    #     db_table = '支出'