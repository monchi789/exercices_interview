import asyncio
import httpx
from concurrent.futures import ThreadPoolExecutor

URL = "https://hacker-news.firebaseio.com/v0/newstories.json"

async def get_ids_articles():
    async with httpx.AsyncClient() as client:
        response = await client.get(URL)
        data = response.json()
    return data

