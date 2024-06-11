from flask import Flask, redirect
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

app = Flask(__name__)

def get_first_iframe_url(page_url):
    try:
        response = requests.get(page_url)
        response.raise_for_status()  # Certifique-se de levantar uma exceção se a requisição falhar
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        iframe_tag = soup.find('iframe', class_='metaframe rptss', src=True)
        if iframe_tag:
            return iframe_tag['src']
        else:
            print(f"No iframe tag found on the page: {page_url}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page URL: {e}")
        return None

@app.route('/get/dorama/<path:url>')
def redirect_to_dorama(url):
    # Decodificar a URL
    full_url = unquote(url)
    print(f"Full URL after unquote: {full_url}")

    iframe_url = get_first_iframe_url(full_url)
    if iframe_url:
        print(f"Found iframe URL: {iframe_url}")
        return redirect(iframe_url)
    else:
        return "Iframe URL not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
          
