from rest_framework import generics, mixins

from .models import Todo
from .serializers import TodoSerializer

class TodoCreateAPIView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data.get("target_time"))
        if serializer.validated_data.get("target_time") is None:
            time = "01:00"

        serializer.save(target_time=time)
        return super().perform_create(serializer)


class TodoDetailAPIView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'


class TodoMixinsViews(
                    mixins.RetrieveModelMixin,  
                    mixins.CreateModelMixin,    
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin, 
                    mixins.UpdateModelMixin,
                    generics.GenericAPIView
                    ):


    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        print(kwargs)
        pk = kwargs.get('pk')
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TodoUpdateAPIView(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        # time = serializer.validated_data.get('get_time')
        return super().perform_update(serializer)


class TodoDeleteAPIView(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        print(instance)
        return super().perform_destroy(instance)


class TodoListAPIView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# Alternative method to creating separating list and create api view wil be to use listcreateapi view 

class TodoListCreateAPIView(generics.ListCreateAPIView):
    """
    Will behave both as generics.CreateAPIView if post method
    and generics.ListAPIView if post method is get. 
     
     """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        # print(serializer.validated_data.get("target_time"))
        time = serializer.validated_data.get("target_time", None)
        if serializer.validated_data.get("target_time") is None:
            time = "01:00"

        serializer.save(target_time=time)
        return super().perform_create(serializer)