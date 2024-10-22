from rest_framework.decorators import action
from rest_framework.response import Response 
from rest_framework import viewsets, status
from .models import Rule
from .serializers import RuleSerializer, EvaluateRuleSerializer
from .rule_engine_logic import tokenize_rule, parse_expression, evaluate_rule
from django.shortcuts import render
from .utils import validate_rule_string  # Import the validation function

def index(request):
    return render(request, 'rule_engine/index.html')


class RuleViewSet(viewsets.ModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer

    def create(self, request, *args, **kwargs):
        rule_string = request.data.get('rule_string')
        
        if not rule_string:
            return Response({"error": "No rule string provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Validate the rule string
        is_valid, error_message = validate_rule_string(rule_string)
        if not is_valid:
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Tokenize and parse the rule string into an AST
            tokens = tokenize_rule(rule_string)
            ast = parse_expression(tokens)
            
            # Optionally save the rule to the database
            rule = Rule.objects.create(rule_string=rule_string)
            serializer = self.get_serializer(rule)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, *args, **kwargs):
        rule_instance = self.get_object()
        rule_string = request.data.get('rule_string')

        if not rule_string:
            return Response({"error": "No rule string provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Validate the new rule string
        is_valid, error_message = validate_rule_string(rule_string)
        if not is_valid:
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Tokenize and parse the new rule string into an AST
            tokens = tokenize_rule(rule_string)
            ast = parse_expression(tokens)

            # Update the rule instance
            rule_instance.rule_string = rule_string
            rule_instance.save()
            
            serializer = self.get_serializer(rule_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        rule = self.get_object()
        rule.delete()
        return Response({"message": "Rule deleted successfully"}, status=status.HTTP_204_NO_CONTENT)    

   
    @action(detail=False, methods=['POST'])
    def evaluate_rule(self, request, *args, **kwargs):
        user_data = request.data.get('user_data')
        rule_id = request.data.get('rule_id')

        if not user_data or not rule_id:
            return Response({"error": "User data and rule_id are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            rule_instance = Rule.objects.get(id=rule_id)
        except Rule.DoesNotExist:
            return Response({"error": "Rule not found"}, status=status.HTTP_404_NOT_FOUND)

        # Tokenize and parse the rule string into an AST
        tokens = tokenize_rule(rule_instance.rule_string)
        ast = parse_expression(tokens)

        # Evaluate the rule
        evaluation_result = evaluate_rule(ast, user_data)
        return Response({"result": evaluation_result}, status=status.HTTP_200_OK)

   