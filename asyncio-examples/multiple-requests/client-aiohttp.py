#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A simple http client using aiohttp."""

import asyncio
import aiohttp

async def get_users():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:8080/users') as response:
            users = await response.json()
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
