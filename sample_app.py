import asyncio
import json
from rickmorty import RickMortyClient


async def main():
    async with RickMortyClient() as client:
        characters = await client.get_all_characters()
        with open('characters.json', 'w', encoding='utf-8') as f:
            json.dump(characters, f, indent=2, ensure_ascii=False)
        
        locations = await client.get_all_locations()
        with open('locations.json', 'w', encoding='utf-8') as f:
            json.dump(locations, f, indent=2, ensure_ascii=False)
        
        episodes = await client.get_all_episodes()
        with open('episodes.json', 'w', encoding='utf-8') as f:
            json.dump(episodes, f, indent=2, ensure_ascii=False)
    
    print("All data fetched successfully!")
    print(f"- Characters: {len(characters)}")
    print(f"- Locations:  {len(locations)}")
    print(f"- Episodes:   {len(episodes)}")


if __name__ == "__main__":
    asyncio.run(main())
