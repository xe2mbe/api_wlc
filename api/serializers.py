from .models import guestUser
from rest_framework import serializers

class guestUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = guestUser
    # fields = ['id', 'netuser', 'netpass', 'wlanID', 'lifetime', 'description']
    fields = '__all__'