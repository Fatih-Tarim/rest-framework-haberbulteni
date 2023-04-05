from rest_framework import serializers
from haberler.models import Makale


class MakaleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    yazar = serializers.CharField()
    baslik = serializers.CharField()
    aciklama = serializers.CharField()
    metin = serializers.CharField()
    sehir = serializers.CharField()
    yayimlanma_tarihi = serializers.DateTimeField()
    aktif = serializers.BooleanField()
    yaratilma_tarihi = serializers.DateTimeField(read_only=True)
    guncellenme_tarihi = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Makale.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.yazar = validated_data.get('yazar', instance.yazar)
        instance.baslik = validated_data.get('baslik', instance.baslik)
        instance.aciklama = validated_data.get('aciklama', instance.aciklama)
        instance.metin = validated_data.get('metin', instance.metin)
        instance.sehir = validated_data.get('sehir', instance.sehir)
        instance.yayimlanma_tarihi = validated_data.get('yayimlanma_tarihi', instance.yayimlanma_tarihi)
        instance.aktif = validated_data.get('aktif', instance.aktif)
        instance.yaratilma_tarihi = validated_data.get('yaratilma_tarihi', instance.yaratilma_tarihi)
        instance.güncellenme_tarihi = validated_data.get('güncellenme_tarihi', instance.güncellenme_tarihi)
        instance.save()
        return instance
        
    def validate(self, data): #Object Level Validate
        if data['baslik'] == data['aciklama']:
            raise serializers.ValidationError('Başlık ve açıklama alanları aynı olamaz!')
        return data

    def validate_baslik(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(f'Başlık 10 karakterden küçük olamaz. Girilen değer len {len(value)} karakter')
        return value