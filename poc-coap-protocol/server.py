import aiocoap.resource as resource
import aiocoap
import threading
import logging
import asyncio
import time

class TemperatureGateway(resource.ObservableResource):

    def __init__(self):
        super().__init__()

    async def render_post(self, request):
        print("Received temperature data: %s" % request.payload.decode('ascii'))
        return aiocoap.Message(code=aiocoap.CHANGED, payload=b'%s' % request.payload)

class IlluminationGateway(resource.ObservableResource):

    def __init__(self):
        super().__init__()


    async def render_post(self, request):
        print("Received illumination data: %s" % request.payload.decode('ascii'))
        return aiocoap.Message(code=aiocoap.CHANGED, payload=b'%s' % request.payload)



logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.DEBUG)

def main():
    root = resource.Site()
    temperature_gateway = TemperatureGateway()
    illumination_gateway = IlluminationGateway()

    root.add_resource(['temperature'], temperature_gateway)
    root.add_resource(['illumination'], illumination_gateway)

    asyncio.Task(aiocoap.Context.create_server_context(root, bind=('127.0.0.1', 5683)))

    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()