from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    rate_average = serializers.SerializerMethodField(read_only = True)
    
    class Meta:
        model = Movie
        fields = '__all__'
    
    def get_rate_average(self, obj):
        #Logo apos o obj, estou "batendo" na classe de reviews utilizando o parametro related_name='reviews' declarado na models
        rate_average = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate_average:
            return round(rate_average, 1)
        return None
    
    def validate_release_date(self, value):
        if value.year < 1895:
            raise serializers.ValidationError("O filme não pode ter ano de criação anterior a 1895.")
        return value