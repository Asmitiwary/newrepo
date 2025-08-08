from rest_framework import serializers
from .models import Expense
class ExpenseSerializer(serializers.Serializer):
    class Meta:
        model=Expense
        fields='__all__'

