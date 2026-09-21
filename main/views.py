from django.shortcuts import render
from main.models import Topic

def show_main(request):
    context = {
        "topic": Topic.objects.order_by("?").first(),
    }
    return render(request, "index.html", context) #bisa diganti nanti