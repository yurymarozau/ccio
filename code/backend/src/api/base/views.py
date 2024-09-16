from rest_framework import views
from rest_framework.permissions import IsAuthenticated


class BaseAPIView(views.APIView):
    permission_classes = (IsAuthenticated,)
