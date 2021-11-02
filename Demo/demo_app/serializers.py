from rest_framework import serializers

from Demo.demo_app.models import Demo


class SerializerDemo(serializers.ModelSerializer):
    class Meta:
        model = Demo
        fields = "__all__"
