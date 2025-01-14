from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from bs4 import BeautifulSoup
import requests
from urllib.parse import quote

def search_google(keyword):
    encoded_keyword = quote(keyword)
    search_url = f"https://www.google.com/search?q={encoded_keyword}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    
    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        results = []
        for g in soup.select('.tF2Cxc'):
            title = g.select_one('.DKV0Md').text if g.select_one('.DKV0Md') else None
            link = g.select_one('.yuRUbf a')['href'] if g.select_one('.yuRUbf a') else None
            if title and link:
                results.append({"title": title, "link": link})
        
        return results
    except Exception as e:
        print(f"Error scraping {keyword}: {e}")
        return []


class WebScrapingView(APIView):
    def get(self, request, *args, **kwargs):
        keywords = request.query_params.getlist('keywords')
        if not keywords:
            return Response({"error": "No keywords provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        results = {}
        for keyword in keywords:
            search_results = search_google(keyword)
            if search_results:
                results[keyword] = search_results

        return Response(results, status=status.HTTP_200_OK)



