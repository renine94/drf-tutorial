from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from user_app.api.serializers import RegistrationSerializer


@api_view(['POST'])
def logout(request):

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({'message': 'successfully logout!'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)

        data = {}

        serializer.is_valid(raise_exception=True)
        account = serializer.save()

        data['response'] = 'Registration Successful!'
        data['username'] = account.username
        data['email'] = account.email

        # token = Token.objects.get(user=account)
        refresh = RefreshToken.for_user(account)
        data['access_token'] = str(refresh.access_token)
        data['refresh_token'] = str(refresh)

        return Response(data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def logout2(request):
    token = RefreshToken(request.data.get('refresh'))
    # Logout 로직 like) token.blacklist()
    return Response({'message': 'successfully Logout!'}, status=status.HTTP_200_OK)
