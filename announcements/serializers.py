from rest_framework import serializers
from announcements.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','id', 'email','password','is_active']



class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id','title','description',
                  'category','date','author','tel_number','price','views']
