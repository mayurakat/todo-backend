from datetime import datetime
from rest_framework import generics, permissions, status,authentication
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task, Category, ContextEntry
from .serializers import TaskSerializer, CategorySerializer, ContextEntrySerializer
from .openai_utils import get_ai_task_suggestions 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer
from django.http import QueryDict   



class TaskListCreateView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        # Ensure the user is set to the request user
        if isinstance(request.data, QueryDict):
            request.data = request.data.copy()
        request.data['user'] = request.user.id
        return super().create(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

class ContextEntryListCreateView(generics.ListCreateAPIView):
    serializer_class = ContextEntrySerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        return ContextEntry.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        # Ensure the user is set to the request user
        if isinstance(request.data, QueryDict):
            request.data = request.data.copy()
        request.data['user'] = request.user.id
        return super().create(request, *args, **kwargs)

class AISuggestionsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request):
        # Fetch context entries for the user
        context_entries = ContextEntry.objects.filter(user=request.user,created_at__gte=datetime.today().date())

        suggestions = get_ai_task_suggestions(context_entries.values_list('content', flat=True))
        return Response(suggestions, status=status.HTTP_200_OK)
    

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request):
        request.auth.delete()  # Delete the token
        return Response(status=status.HTTP_204_NO_CONTENT)