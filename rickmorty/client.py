
import aiohttp
from typing import List, Dict, Any


class RickMortyClient:    
    BASE_URL = "https://rickandmortyapi.com/api"
    
    def __init__(self):
        self._session = None
    
    async def __aenter__(self):
        self._session = aiohttp.ClientSession()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._session:
            await self._session.close()
    
    async def _fetch_paginated_resource(self, endpoint: str) -> List[Dict[str, Any]]:
        all_results = []
        url = f"{self.BASE_URL}/{endpoint}"
        
        while url:
            async with self._session.get(url) as response:
                data = await response.json()
                all_results.extend(data.get('results', []))
                url = data.get('info', {}).get('next')
        
        return all_results
    
    async def get_all_characters(self) -> List[Dict[str, Any]]:
        return await self._fetch_paginated_resource('character')
    
    async def get_all_locations(self) -> List[Dict[str, Any]]:
        return await self._fetch_paginated_resource('location')
    
    async def get_all_episodes(self) -> List[Dict[str, Any]]:
        return await self._fetch_paginated_resource('episode')
