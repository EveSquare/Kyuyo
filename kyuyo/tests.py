from django.test import TestCase

from .models import MonthlyModel
from datetime import datetime

# Create your tests here.
def add_monthly(date):
    now = datetime.now()
    obj = MonthlyModel.objects.order_by('-id').first()
    db_date = obj.updated_at

    print(now - datetime)

    return

add_monthly()