from django.contrib.auth.models import User  # ✅ Import User model
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

# User registration API
@api_view(['POST'])
def register_user(request):

    first_name = request.data.get('first_name','')
    last_name = request.data.get('last_name','')
    username = first_name + last_name
    email = request.data.get('email')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Couldn\'t generate username. First name is required. Second name is optional, to generate username'}, status=status.HTTP_400_BAD_REQUEST)

    if not email:
        return Response({'error': 'E-mail is required'}, status=status.HTTP_400_BAD_REQUEST)

    if not password:
        return Response({'error': 'Passwordrequired'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=email).exists():
        return Response({'error': 'E-mail already exists'}, status=status.HTTP_400_BAD_REQUEST)



    hashed_password = make_password(password)
    user = User.objects.create(username=username, email= email,password=hashed_password)
    user.save()

    return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)


# User login API
@api_view(['POST'])
def login_user(request):
    print("\n\nReceived Data:", request.data, "\n\n")  # Debugging statement

    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Get user by email
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

    # Authenticate using the retrieved username
    user = authenticate(username=user.username, password=password)

    if not user:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

    # Generate JWT tokens
    refresh = RefreshToken.for_user(user)
    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    })
