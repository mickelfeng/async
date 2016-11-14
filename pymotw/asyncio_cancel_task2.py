import asyncio
import functools

async def task_func():
    print('in task function, sleeping')
    try:
        await asyncio.sleep(1)  # await another coroutine
    except asyncio.CancelledError: 
        print('task_func was cancelled')
        raise # raise for main
    return 'the result'

def task_canceller(t):
    # a callback function to cancel the task
    print('in task_canceller')
    t.cancel()
    print('cancelled the task')


async def main(loop):
    print('creating a task')
    task = loop.create_task(task_func())
    loop.call_soon(task_canceller, task)  # add callback
    try:
        await task
    except asyncio.CancelledError:
        print('main() also see the cancell error')

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
