from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import SchemaSerializer
from .utils import (
    dynamic_random_data,
    DynamicFieldName,
    FieldName, query_random_data,
    verbose_to_enum, create_kwargs,
    needs_nested_range,
)


class Mockify(APIView):
    """
    View to generate random data from a Schema and a count
    - No authentication or permission is required at the moment
    """

    def post(self, request, format=None):
        """
        POST at /mockify/api/ with Schema Object
        """
        schema_serializer = SchemaSerializer(data=request.data)

        if schema_serializer.is_valid():
            schema = request.data
            count = request.data.pop('count', None)
            try:
                my_kwargs = create_kwargs(request.data)
            except Exception:
                return Response(
                    data='Provided arguments are invalid',
                    status=status.HTTP_400_BAD_REQUEST
                )
            queried_data = {}
            for verbose_field in schema.keys():
                field = verbose_to_enum(verbose_field)
                if isinstance(field, FieldName):
                    queried_data[verbose_field] = query_random_data(
                        field, count)
                else:
                    queried_data[verbose_field] = dynamic_random_data(
                        field, count, **my_kwargs)
            data = []
            for i in range(count):
                obj = {}
                for key in queried_data.keys():
                    if needs_nested_range(key):
                        obj[schema[key]['name']] = queried_data[key][i]
                    else:
                        obj[schema[key]] = queried_data[key][i]
                data.append(obj)
            return Response(
                data=data,
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                data=schema_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
