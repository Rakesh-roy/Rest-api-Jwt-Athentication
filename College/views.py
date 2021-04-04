from django.contrib.auth.models import User, Group
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from College.models import StudentModel, TeacherModel
from College.serializers import StudentSerializer, TeacherSerializer, RegisterSerializer


class AddStudents(CreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]


class ListStudents(ListAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]


class AddTeachers(CreateAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ListTeachers(ListAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]


#sign up View
class RegisterView(APIView):
    def post(self, request):
        try:
            qs = RegisterSerializer(data=request.data)
            if qs.is_valid():
                user = qs.save()
                group = Group.objects.get(name='students')
                user.groups.add(group)
                message = {'message': 'Registered Successfully'}
            else:
                message = {'error': qs.errors}
        except:
            pass
        return Response(message)
