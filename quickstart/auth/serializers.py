from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        meta = ['username', 'email']




# class MyModelSerializer(serializers.ModelSerializer):

#     creator = serializers.ReadOnlyField(source='creator.username')
#     creator_id = serializers.ReadOnlyField(source='creator.id')
#     image_url = serializers.ImageField(required=False)

#     class Meta:
#         model = MyModel
#         fields = ['id', 'creator', 'creator_id', 'title', 'description', 'image_url']
