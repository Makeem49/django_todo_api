from rest_framework import serializers

from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    """Method and properties can be specified in this class and also 
    format it properly
    """
    completed = serializers.SerializerMethodField(read_only=True) 
    email = serializers.EmailField(write_only=True)
    class Meta:
        model = Todo
        fields = [
            "email",
            "name",
            "created_at",
            "target_time",
            "completed",
            "is_done"
        ]

    def get_completed(self, obj):
        if hasattr(obj, "id"):
            return obj.is_completed
        return None

    def create(self, validated_data):
        email = validated_data.pop("email")
        print(email)
        return super().create(validated_data)