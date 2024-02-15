# views.py
from rest_framework import viewsets
from .models import Pricing,Item
from .serializers import PricingSerializer
from rest_framework.response import Response
from django.http import JsonResponse
import decimal

class PricingViewSet(viewsets.ViewSet):
    def list(self, request):
        zone = str(request.query_params.get('zone'))
        organization_id = request.query_params.get('organization_id')
        item_id = request.query_params.get('item_id')
        base_distance = int(request.query_params.get('base_distance',  0))

        # Fetch the relevant Pricing instance based on the provided parameters
        pricing = Pricing.objects.filter(zone=zone, item_id=item_id, organization_id=organization_id).first()
        # Correctly filter for the specific item by its id
        item = Item.objects.filter(id=item_id).first()

# Check the typeof attribute on the item instance
        if int(item.typeof) ==  1:
            km_price_extra =  decimal.Decimal(1.5)
            fix_price = 10 # 10
            extra_distance = base_distance - 5  # Assuming base_distance is the total distance
            calculated_price = max(0,(km_price_extra*extra_distance+fix_price))
        else:
            km_price =  1
            fix_price = 10
            extra_distance = base_distance - 5  # Assuming base_distance is the total distance
            calculated_price = max(0,(km_price*extra_distance+fix_price))


        if pricing:
            
            return Response({'total_price': calculated_price})
        else:
            return Response({'error': 'No matching pricing found'}, status=404)