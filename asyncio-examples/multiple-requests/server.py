#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A simple http server using aiohttp.

Note here the difference between time.sleep (blocking) and asyncio.sleep (non-blocking).

Remember that we must avoid blocking the event loop thread to let the event loop
switch the execution context to other coroutines.
"""

import asyncio
from aiohttp import web

async def list_users_handler(request):
    await asyncio.sleep(3)
    return web.json_response(
        ['Fulano', 'Beltrano', 'Cicrano']
    )

if __name__ == '__main__':
    app = web.Application()

    app.add_routes([
        web.get('/users', list_users_handler)
    ])

    web.run_app(app)
