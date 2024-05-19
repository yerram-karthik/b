from django.shortcuts import render
from django.http import JsonResponse
import requests
import json


def fetch_data():
    url = 'https://devapi.beyondchats.com/api/get_message_with_sources'
    page = 1
    citations = []

    while True:
        response = requests.get(url, params={'page': page})
        try:
            print(f"Raw response content for page {page}: {response.text}")  # Debugging line
            data = response.json()
            print(f"Decoded JSON data for page {page}: {data}")  # Debugging line
        except ValueError as e:
            print(f"Error decoding JSON for page {page}: {e}")
            break

        if not data or 'data' not in data:
            break

        messages = data['data']
        for message in messages:
            citations.extend(process_message(message))

        page += 1

    return citations


def process_message(message):
    citations = []
    response_text = message.get('response', '')
    sources = message.get('source', [])

    for source in sources:
        context = source.get('context', '')
        link = source.get('link', '')
        if context and context in response_text:
            citations.append({'response_id': message.get('id'), 'context': context, 'link': link})

    return citations


def citations_view(request):
    try:
        citations = fetch_data()
        return JsonResponse(citations, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def index(request):
    return render(request, 'genai/index.html')
