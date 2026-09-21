from django.shortcuts import render, redirect
from main.models import Topic
from main.forms import TopicForm

def show_main(request):
    context = {
        "topic": Topic.objects.order_by("?").first(),
    }
    return render(request, "index.html", context) #bisa diganti nanti

def create_topic(request):
    form = TopicForm(request.POST or None)

    if request.method == "POST" and form.is_valid:
        form.save()
        return redirect("main:show_main")

    context = {"form": form}
    return render(request, "topic_form.html", context)