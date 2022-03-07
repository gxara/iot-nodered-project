# client_put.py
import asyncio
import random
import json
from aiocoap import *

async def main():
    context = await Context.create_client_context()
    payload = json.dumps({
        "celsius": random.randint(0, 30)
    }).encode('ascii')

    request = Message(code=POST, payload=payload, uri="coap://127.0.0.1/temperature")

    response = await context.request(request).response
    print('Result: %s\n%r'%(response.code, response.payload))

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())