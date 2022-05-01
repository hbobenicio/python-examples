import asyncio

from aiohttp import web

from delayer.config import config

async def handle(request):
    sleep_time = int(request.query.get('t', "1"))
    await asyncio.sleep(sleep_time)
    return web.Response(text=f'slept for {sleep_time}s')

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

if __name__ == '__main__':
    web.run_app(app, host=config.host, port=config.port)
