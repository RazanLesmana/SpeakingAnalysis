from django.urls import path
from main.views import show_main, create_topic, get_topics_json
from main.views import show_topics, delete_topic

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("topics/add/", create_topic, name="create_topic"),
    path("api/topics/", get_topics_json, name="get_topics_json"),
    path("topics/", show_topics, name="show_topics"),
    path("topics/<uuid:topic_id>/delete/", delete_topic, name="delete_topic")
]