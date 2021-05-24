from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """ serilaizes a name field for testing our API view"""

    name = serializers.CharField(max_length=10)
