import httpx
import asyncio
from fastapi import FastAPI
from users import User
import uuid


app = FastAPI()

URL = 'https://randomuser.me/api/?results=5000'

async def fetch(client):
    try:
        response = await client.get(URL, timeout=10)

        if response.status_code != 200:
            return []

        return response.json().get('results', [])

    except:
        return []

@app.get('/', response_model=list[User])
async def main():
    async with httpx.AsyncClient() as client:

        tasks = [fetch(client) for _ in range(3)]
        results = await asyncio.gather(*tasks)

    data = [user for sublist in results for user in sublist]

    cleaned_data = [
        {
            'id': str(i + 1),
            'gender': user['gender'],
            'first_name': user['name']['first'],
            'last_name': user['name']['last'],
            'email': user['email'],
            'age': user['dob']['age']
        }
        for i, user in enumerate(data)
    ]

    return cleaned_data