from rest_framework import serializers
from main1.models import Pricing,Item


class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pricing
        fields =('organization_id', 'item_id', 'zone', 'base_distance_in_km', 'km_price', 'fix_price')



class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('item_id','type')