from rest_framework import serializers


class NestedRangeSerializer(serializers.Serializer):
    """
    Serializer for nested ranges for { integer_number, float_number, list_choice}
    """
    range = serializers.CharField(required=True)
    name = serializers.CharField(required=True)


class SchemaSerializer(serializers.Serializer):
    """
    Serializer for the Mock Data Schema
    """
    count = serializers.IntegerField(min_value=1, max_value=100)
    city = serializers.CharField(required=False)
    country_code = serializers.CharField(required=False)
    country_name = serializers.CharField(required=False)
    currency = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    state = serializers.CharField(required=False)
    street_address = serializers.CharField(required=False)
    zip_code = serializers.CharField(required=False)
    # Fields below are generated and not stored
    integer_number = NestedRangeSerializer()
    float_number = NestedRangeSerializer()
    list_choice = NestedRangeSerializer()
    boolean_valie = serializers.CharField(required=False)
    unique_identifier = serializers.CharField(required=False)
