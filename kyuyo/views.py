from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .models import ZandakaModel, MonthlyModel, SyunyuModel, ZandakaModel

# Create your views here.
def dashborad(request):
    zandaka = ZandakaModel.objects.order_by("id").first()
    syunyu = SyunyuModel.objects.order_by("-id").first()
    syunyu_list = SyunyuModel.objects.all()
    result = 0
    for row in syunyu_list:
        result = result+int(row.syunyu)
    zandaka.zandaka = result
    zandaka.save()
    params = {
        'zandaka': zandaka,
        'syunyu': syunyu,
    }

    return render(request, 'kyuyo/dashborad.html', params)


class KyuyoListView(ListView):
    model = SyunyuModel
    template_name = "kyuyo/syunyu_list.html"

class Syunyu_update(View):
    def get(self, request, *args, **kwargs):
        return redirect('dashborad')

    def post(self, request, *args, **kwargs):
        
        new_obj = SyunyuModel(syunyu=self.request.POST.get('kingaku'))
        new_obj.save()
        return redirect('dashborad')
