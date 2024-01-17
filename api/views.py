from rest_framework.response import Response
from rest_framework.decorators import api_view
from wbapp.models import UserProfile
from .serializers import UserProfileSerialize


@api_view(['GET'])
def get_user_data(request):
    user_profile = UserProfile.objects.get(username=request.username)
    serialize = UserProfileSerialize(user_profile, many=False)
    return Response(serialize.data)