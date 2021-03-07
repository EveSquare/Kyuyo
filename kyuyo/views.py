from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .models import ZandakaModel, MonthlyModel, SyunyuModel, ZandakaModel

from datetime import datetime
import pytz
# Create your views here.
# メイン画面
def dashborad(request):
    zandaka = ZandakaModel.objects.order_by("id").first()
    syunyu = SyunyuModel.objects.order_by("-id").first()
    syunyu_list = SyunyuModel.objects.all()
    result = 0
    for row in syunyu_list:
        result = result+int(row.syunyu)

    progress_month = add_monthly()
    monthly_total = MonthlyModel.objects.order_by('-id').first().total
    getugaku = result + monthly_total

    if progress_month:
        tmp = 0
        for i in range(int(progress_month)):
            month_spend = MonthlyModel.objects.order_by('-id').first()
            print(int(month_spend.syogaku))
            tmp = int(month_spend.syogaku) + int(month_spend.subscription)

        monthly_total = int(month_spend.total) + int(tmp)
        month_spend.total = int(month_spend.total) + int(tmp)
        month_spend.save()

        getugaku = result + monthly_total

    zandaka.zandaka = result
    zandaka.save()

    

    params = {
        'zandaka': zandaka,
        'getugaku': getugaku,
        'syunyu': syunyu,
        'monthly_total': monthly_total,
    }

    return render(request, 'kyuyo/dashborad.html', params)


# 追加した収入のリスト表示
class KyuyoListView(ListView):
    model = SyunyuModel
    template_name = "kyuyo/syunyu_list.html"

# POSTがあった時、値を収入とし残高に追加
class Syunyu_update(View):
    def get(self, request, *args, **kwargs):
        return redirect('dashborad')

    def post(self, request, *args, **kwargs):

        if self.request.POST.get('kingaku'):
            new_obj = SyunyuModel(syunyu=self.request.POST.get('kingaku'))
            new_obj.save()
            return redirect('dashborad')
        else:
            return redirect('dashborad')

def add_monthly():
    now = datetime.now()
    obj = MonthlyModel.objects.order_by('-id').first()
    db_date = obj.updated_at

    def diff_month(d1, d2):
        if d1 > d2:
            d1, d2 = d2, d1
        return (d2.year - d1.year)*12 + d2.month - d1.month 
    
    result = diff_month(datetime(now.year, now.month, now.day), datetime(db_date.year, db_date.month, db_date.day))

    if result:
        obj.updated_at = now.astimezone(pytz.timezone('Asia/Tokyo'))
        obj.save()
        return result

    return False