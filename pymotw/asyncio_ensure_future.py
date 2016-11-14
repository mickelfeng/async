import asyncio

async def wrapped():
    print('wrapped!')
    return 'result'

async def inner(task):
    print('inner: starting')
    print('inner: waiting for {!r}'.format(task))
    result = await task
    print('inner: task return {!r}'.format(result))

async def starter(loop):
    print('starter: creating task')
    # task = asyncio.ensure_future(wrapped())
    # 使用wrapped就不用传loop进入了
    task = loop.create_task(wrapped())
    print('starter: waiting for inner')
    await inner(task)  # await call a wrapper function
    print('starter: inner returned')

event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    result = event_loop.run_until_complete(starter(event_loop))
finally :
    print('closing event loop')
    event_loop.close()
