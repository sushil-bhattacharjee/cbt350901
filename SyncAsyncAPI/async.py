import asyncio
from aiohttp import ClientSession
from rich import print as rprint

base_url = 'http://httpbin.org/'

async def count():
    for i in [1,2,3,4,5,6,7,8]:
        rprint(i)
        await asyncio.sleep(1)
        
async def get_delay(seconds):
    endpoint = f'/delay/{seconds}'
    rprint(f'Getting with {seconds} delay ...')
    
    async with ClientSession() as session:
        async with session.get(base_url+endpoint) as response:
            response = await response.read()
            rprint(response)
            
async def main():
    await asyncio.gather(get_delay(5),count())
    
asyncio.run(main())
rprint('Okay! All finished getting.')

