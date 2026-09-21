from django.shortcuts import render, redirect, get_object_or_404
from main.models import Topic
from main.forms import TopicForm
from django.core import serializers
from django.http import HttpResponse

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

def get_topics_json(request):
    topics = Topic.objects.all()

    category = request.GET.get("category", "").strip()
    if category: 
        topics = topics.filter(category=category)

    data = serializers.serialize("json", topics)
    return HttpResponse(data, content_type="application/json")

def show_topics(request): 
    json_response = get_topics_json(request)
    deserialized = serializers.deserialize("json", json_response.content.decode("utf-8"))

    topics = [item.object for item in deserialized]

    context = {
        "topic_list": topics,
        "category": request.GET.get("category", "").strip()
    }
    return render(request, "topics.html", context)

def delete_topic(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    if request.method == "POST":
        topic.delete()
    return redirect("main:show_topics")