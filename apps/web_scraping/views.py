from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def search_google_selenium(keyword):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    # Configuración del driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(f"https://www.google.com/search?q={keyword}")
    time.sleep(2)  # Esperar a que la página cargue

    results = []
    try:
        elements = driver.find_elements(By.CSS_SELECTOR, '.tF2Cxc')  # Actualiza el selector si es necesario
        for element in elements:
            title = element.find_element(By.CSS_SELECTOR, 'h3').text
            link = element.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
            results.append({"title": title, "link": link})
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

    return results


# Función para realizar búsquedas utilizando SerpAPI
def search_with_serpapi(keywords):
    api_key = "122bba01c878282881097ad940b526831debab821948ea7b1bac1c7486dabb93"  # Reemplaza con tu API Key de SerpAPI
    base_url = "https://serpapi.com/search.json"

    results = {}

    for keyword in keywords:
        params = {
            "q": keyword,  # Palabra clave a buscar
            "hl": "es",  # Idioma (español)
            "gl": "pe",  # País (Perú)
            "api_key": api_key,
        }
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()

            # Extraer resultados relevantes de SerpAPI
            keyword_results = [
                {
                    "title": result.get("title"),
                    "link": result.get("link"),
                }
                for result in data.get("organic_results", [])
            ]

            results[keyword] = keyword_results
        except Exception as e:
            print(f"Error fetching data for keyword '{keyword}': {e}")

    return results

# Vista de la API
class WebScrapingView(APIView):
    def get(self, request, *args, **kwargs):
        # Obtener las palabras clave desde los parámetros de la consulta
        keywords = request.query_params.getlist("keywords")

        if not keywords:
            return Response({"error": "No keywords provided."}, status=status.HTTP_400_BAD_REQUEST)

        # Realizar la búsqueda con SerpAPI
        results = search_with_serpapi(keywords)

        if not results:
            return Response({"error": "No results found."}, status=status.HTTP_404_NOT_FOUND)

        return Response(results, status=status.HTTP_200_OK)
