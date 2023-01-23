from rest_framework import serializers

from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    """Method and properties can be specified in this class and also 
    format it properly
    """
    done = serializers.SerializerMethodField(read_only=True) 
    class Meta:
        model = Todo
        fields = [
            "name",
            "created_at",
            "get_target_time",
            "done"
        ]

    def get_done(self, obj):
        # print(obj)
        return obj.is_completed