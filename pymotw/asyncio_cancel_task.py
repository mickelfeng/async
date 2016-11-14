import asyncio

async def task_func():
    print('in task_func')
    return 'the result'

async def main(loop):
    print('ceate a task')
    task = loop.create_task(task_func())

    print('cancel the task')
    task.cancel()

    print('cancelled task {!r}'.format(task))
    try:
        await task  # error
    except asyncio.CancelledError:
        print('caught error from cancelled task: {!r}'.format(task))
    else:
        print('task done result: {!r}'.format(task.result()))

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
