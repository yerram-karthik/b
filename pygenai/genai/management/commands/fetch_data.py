import requests
from django.core.management.base import BaseCommand
from django.conf import settings


def get_citations(item):
    response_text = item.get('response')
    sources = item.get('sources', [])
    citations = []

    for source in sources:
        if source['context'] in response_text:
            citations.append({'id': source['id'], 'link': source.get('link')})

    return {'response_id': item.get('id'), 'citations': citations}


class Command(BaseCommand):
    help = 'Fetch data from the API'

    def handle(self, *args, **kwargs):
        url = 'https://devapi.beyondchats.com/api/get_message_with_sources'
        page = 1
        citations = []

        while True:
            response = requests.get(url, params={'page': page})
            data = response.json()

            if not data:
                break

            for item in data:
                citations.append(get_citations(item))

            page += 1

        # Save or process citations as needed
        print(citations)
