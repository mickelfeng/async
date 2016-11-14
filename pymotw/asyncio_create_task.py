import asyncio

async def task_func():
    print('in task')
    return "the result"

async def main(loop):
    print('create a task')
    task = loop.create_task(task_func())  # a wrapper of a coroutine!
    print('waiting for task: {!r}'.format(task))
    result = await task  # intresting!
    print('task done: {!r}'.format(task))
    print('return value: {!r}'.format(result))

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
