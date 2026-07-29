from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import UserCreateSerializer
from ..wallets.serializers import WalletCreateSerializer

User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    """
    POST /api/users
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

class WalletCreateView(APIView):
    """
    POST /api/users/<int:userId>/wallet
    """
    def post(self, request, userId):
        user = get_object_or_404(User, pk=userId)
        if hasattr(user, 'wallet'):
            return Response(
                {"error": "User already has a wallet."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        wallet = create_wallet_for_user(user)
        
        # 4. Oluşan cüzdanı serialize et ve dön
        serializer = WalletCreateSerializer(wallet)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
