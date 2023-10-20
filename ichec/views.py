from django.shortcuts import render
from .settings import APP_NAME
from .models import Course, Master

TEMPLATE_PATH = f"{APP_NAME}/"

HOME_PATH = TEMPLATE_PATH + "index.html"
MASTERS_PATH = TEMPLATE_PATH + "masters.html"
MASTER_DETAIL_PATH = TEMPLATE_PATH + "master-detail.html"

# Create your views here.
def home(request):
    return render(request, HOME_PATH, {})

def masters(request):
    if request.method == "GET":
        masters = Master.objects.all()
        num_masters = masters.count()
        return render(request, MASTERS_PATH, {
            "masters": masters,
            "num_masters": num_masters
        })

def master_detail(request, pk):
    master = Master.objects.get(pk=pk)
    return render(request, MASTER_DETAIL_PATH, {
        "master": master,
        "courses": master.get_courses()
    })