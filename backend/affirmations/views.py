from django.shortcuts import render
import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI

# OpenAI client
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

# Create your views here.
@csrf_exempt
def generate_affirmation(request):
    # POST Method?
    if request.method != "POST":
        return JsonResponse({"error": "Only POST accepted"}, status=405)

    # Parse JSON Body
    try:
        data = json.loads(request.body)
        name = data.get('name', '').strip()
        feeling = data.get('feeling', '').strip()

        if not name or not feeling:
            return JsonResponse({'error': "Please fill out your name and how you are feeling."}, status=400)
    except:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    # OpenAI Response
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": f'''You are an empathetic affirmation therapist for {name}. Keep your resnonses between 2 and 4 
                sentances. Dont give medical or legal advice. If the uses suggests self harm, advice seeking profesional help''',
            },
            {
                "role":"user",
                "content":f"This is what the user is feeling:\n\n{feeling}"
            }
        ],
        max_tokens=100
    )
    # Extract & Return
    affirmation = response.choices[0].message.content
    return JsonResponse({'affirmation': affirmation})

