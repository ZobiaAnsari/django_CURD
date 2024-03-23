from rest_framework  import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length = 100)

    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self,instace,validated_data):
        instace.name = validated_data.get('name',instace.name)
        print(instace.name)
        instace.roll = validated_data.get('roll',instace.roll)
        instace.city = validated_data.get('city',instace.city)
        instace.save()
        return instace