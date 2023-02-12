from django.shortcuts import render
from django.http import JsonResponse
import requests
import openai
from rest_framework.views import APIView
from rest_framework import permissions
from jAIme.settings import OPENAI_API_KEY

class Question(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    openai.api_key = OPENAI_API_KEY
    def post(self, request, *args, **kwargs):
        data = request.data
        #code = data.get('code')
        prompt = data.get('prompt')
        model = "code-davinci-002"

        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            temperature=0.5,
            max_tokens=512,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["\"\"\""]
        )

        if response:
            return JsonResponse({'response': response})
        else:
            return JsonResponse({'error': 'Failed to get explanation'})
