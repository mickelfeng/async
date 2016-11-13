import asyncio

def callback():
    print('callback invoked')

def stopper(loop):
    print('stopper invoked')
    loop.stop()

event_loop = asyncio.get_event_loop()
try:
    print('registering callbacks')
    # the callbacks are invoked in the order they are scheduled
    event_loop.call_soon(callback)
    event_loop.call_soon(stopper, event_loop)
    print('entering event loop')
    event_loop.run_forever()
finally:
    print('closing event loop')
    event_loop.close()

