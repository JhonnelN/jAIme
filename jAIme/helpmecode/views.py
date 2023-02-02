from django.shortcuts import render
from django.http import JsonResponse
import requests
from rest_framework.views import APIView
from rest_framework import permissions
from jAIme.settings import OPENAI_API_KEY


class Question(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        data = request.data
        code = data.get('code')
        prompt =data.get('prompt')
        api_key = OPENAI_API_KEY
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "model": "text-davinci-002",
            "prompt": prompt,
            "temperature": 0.5,
            "max_tokens": 512,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }
        response = requests.post("https://api.openai.com/v1/engines/explaincode/jobs",
                                headers=headers, json=data)
        print(response.text)
        if response.status_code == 200:
            response_json = response.json()
            explanation = response_json['choices'][0]['text']
            return JsonResponse({'explanation': explanation})
        else:
            return JsonResponse({'error': 'Failed to get explanation'})
  
