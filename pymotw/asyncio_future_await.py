import asyncio

def markdown(future, result):
    """
    execute the future object
    """
    print('setting result to {!r}'.format(result))
    future.set_result(result)

async def main(loop):
    """
    main coroutine function
    set callback for event loop
    """
    all_done = asyncio.Future()  # a future object in coroutine
    loop.call_soon(markdown, all_done, 'the result')
    result = await all_done
    print('return result: {!r}'.format(result))

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
