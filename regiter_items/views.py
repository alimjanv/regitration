from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({
                "message": "Login successful",
                "username": user.username
            })
        else:
            return Response({
                "error": "Invalid username or password"
            }, status=400)


class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"})
