#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A simple http client using requests.

Note here that the requests.get() call blocks our main thread
(which is the same as the event loop thread) and doesn't let
the event loop executor to switch between coroutines.
"""

import asyncio
import requests

async def get_users():
    response = requests.get('http://localhost:8080/users')
    users = response.json()
    return users

async def main():
    tasks = []
    for _i in range(3):
        tasks.append(get_users())

    users = await asyncio.gather(*tasks)
    for user in users:
        print('users:', user)

if __name__ == "__main__":
    asyncio.run(main())
