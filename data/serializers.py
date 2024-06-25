from rest_framework import serializers

from data.models import Record, Variable


class VariableSerializer(serializers.ModelSerializer):
    modified_by = serializers.StringRelatedField(read_only=True)

    def save(self, **kwargs):
        self.validated_data["modified_by"] = self.context["request"].user
        return super().save(**kwargs)

    class Meta:
        model = Variable
        fields = ["uuid", "name", "units", "modified_by"]
        read_only_fields = ["uuid"]


class RecordSerializer(serializers.ModelSerializer):
    variable = serializers.CharField(source="variable.name")
    value = serializers.FloatField()
    units = serializers.CharField(read_only=True, source="variable.units")

    def create(self, validated_data):
        try:
            variable_name = validated_data.pop("variable")["name"]
            variable = Variable.objects.get(name=variable_name)
            record = Record.objects.create(
                variable=variable, value=validated_data["value"]
            )
            return record
        except Variable.DoesNotExist:
            raise serializers.ValidationError(
                f"Variable with name {variable_name} does not exist"
            )

    def update(self, instance, validated_data):
        raise NotImplementedError("Updating records is not allowed")

    class Meta:
        model = Record
        fields = ["uuid", "variable", "value", "units", "created_at"]
        read_only_fields = ["uuid", "created_at"]
