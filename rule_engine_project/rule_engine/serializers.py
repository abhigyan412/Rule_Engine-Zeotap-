from rest_framework import serializers
from .models import Rule

class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = ['id', 'rule_string', 'created_at']

        def update(self, instance, validated_data):
         instance.rule_string = validated_data.get('rule_string', instance.rule_string)
         instance.save()
         return instance
        
class EvaluateRuleSerializer(serializers.Serializer):
     rule_id = serializers.IntegerField()
     user_data = serializers.DictField()
    
