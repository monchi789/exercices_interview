import httpx
import asyncio
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


URL = 'http://localhost:8003/files/'
DOWNLOADS_PATH = Path('downloads')

files_path = []
async def get_url_files(url):


    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')

    for i in soup.find_all('a'):
        files_path.append(url + i.text)
    
    return files_path

def download_file(url):
    filename = url.split("/")[-1]
    filepath = DOWNLOADS_PATH / filename

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(filepath, 'wb') as file:
            for chuck in response.iter_content(chunk_size=8192):
                file.write(chuck)
    except requests.exceptions.RequestException as e:
        print(e)

files_path = asyncio.run(get_url_files(URL))

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(download_file, files_path))