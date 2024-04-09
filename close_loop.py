import asyncio

asyncio.get_event_loop().close()
print(asyncio.get_event_loop().is_closed())
