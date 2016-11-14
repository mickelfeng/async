import asyncio

def markdown(future, result):
    print('setting future result to {!r}'.format(result))
    future.set_result(result)

event_loop = asyncio.get_event_loop()
try:
    all_done = asyncio.Future()
    print('scheduling mark down')
    # add callback function in order
    event_loop.call_soon(markdown, all_done, 'the result')
    print('entering event loop')
    result = event_loop.run_until_complete(all_done)
    print('return result: {!r}'.format(result))
finally:
    print('closing event loop')
    event_loop.close()

# future executed done!
print('future result: {!r}'.format(all_done.result()))
