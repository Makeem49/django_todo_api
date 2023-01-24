from rest_framework import generics, permissions, authentication

from .models import Todo
from .serializers import TodoSerializer
from .permissions import IsStaffEdit

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
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsStaffEdit, permissions.IsAuthenticated]


class TodoUpdateAPIView(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]

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
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions,permissions.IsAuthenticatedOrReadOnly]


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