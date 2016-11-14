import asyncio
import functools

def callback(future, n):
    # a callback function, when future done,
    # it will be executed
    print('{future} - future done: {result}'.format(
            future = n, result = future.result()
        )
    )

async def register_callbacks(all_done):
    print('registing callback functions')
    all_done.add_done_callback(functools.partial(callback, n=1))  # partial 第一个参数
    all_done.add_done_callback(functools.partial(callback, n=2))

async def main(all_done):
    await register_callbacks(all_done)
    print('setting result to future')
    all_done.set_result('the result')

event_loop = asyncio.get_event_loop()
all_done = asyncio.Future()
try:
    event_loop.run_until_complete(main(all_done))
finally:
    event_loop.close()
