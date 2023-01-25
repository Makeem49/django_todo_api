from rest_framework import serializers
from rest_framework.reverse import reverse
from datetime import time 

from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    """Method and properties can be specified in this class and also 
    format it properly
    """
    completed = serializers.SerializerMethodField(read_only=True) 
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="todo-detail", lookup_field='pk')

    class Meta:
        model = Todo
        fields = [
            "url",
            "edit_url",
            "name",
            "created_at",
            "target_time",
            "completed",
            "is_done"
        ]

    def get_edit_url(self, obj):
        request = self.context.get('request') # self.request
        if request is None:
            return None
        return reverse('todo-edit', kwargs={"pk" : obj.pk}, request=request)

    def get_completed(self, obj):
        if hasattr(obj, "id"):
            return obj.is_completed
        return None

    def validate_name(self, value):
        request = self.context.get('request')
        user = request.user
        qs = Todo.objects.filter(name__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a product name.")
        return value