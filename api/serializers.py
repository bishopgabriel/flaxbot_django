from rest_framework import serializers
from wbapp.models import UserProfile

class UserProfileSerialize(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        # To get all data, the fields can be changed to fields = '__all__'
        fields = ["id", "username", "address", "phone", "email"]