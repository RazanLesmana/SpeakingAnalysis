from django.forms import ModelForm
from main.models import Topic

class TopicForm(ModelForm): 
    class Meta: 
        model = Topic
        fields = ["title", "category", "description"]