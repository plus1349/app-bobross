from collections import OrderedDict

from rest_framework.serializers import ModelSerializer as BaseModelSerializer

from bobross.utils import camelcase


class ModelSerializer(BaseModelSerializer):
    def to_representation(self, instance):
        to_representation = super().to_representation(instance)
        representation_list = list(filter(lambda field: field[1] not in ['', [], None], to_representation.items()))
        camelcased_representation = [(camelcase(field[0]), field[1]) for field in representation_list]
        return OrderedDict(camelcased_representation)
