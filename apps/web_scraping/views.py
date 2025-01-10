from django.http import JsonResponse
from django.views import View
import requests
from bs4 import BeautifulSoup

class WebScrapingView(View):
    def get(self, request):
        keywords = request.GET.getlist('keyword')  # Captura múltiples parámetros 'keyword'
        results = {}

        for keyword in keywords:
            url = f"https://www.google.com/search?q={keyword}"
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')

            results[keyword] = [
                {
                    "title": link.text.strip(),
                    "link": link.get('href'),
                }
                for link in soup.select('a')[:10]  # Cambia el selector según tus necesidades
            ]

        return JsonResponse(results)
