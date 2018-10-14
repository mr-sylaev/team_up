from apps.users.models import ItUser
from rest_framework import serializers


class ItUserSerializer(serializers.HyperlinkedModelSerializer):
    age = serializers.SerializerMethodField()
    tracks = serializers.StringRelatedField(many=True)

    class Meta:
        model = ItUser
        fields = (
            'first_name',
            'last_name',
            'specialty__title',
            'age',
            'skills',
            'edu',
        )

    def get_age(self, obj):
        return obj.get_age()
