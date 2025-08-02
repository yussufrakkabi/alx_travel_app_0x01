from rest_framework import serializers
from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Listing model. This serializer automatically generates fields
    based on the Listing model and includes all fields by default.
    """
    class Meta:
        model = Listing
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    listing = ListingSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'
