# async
code for asyncio learning

+ **asyncio**
    - generator
        + ```yield/yield from```
        + can create coroutine
    - coroutine
        + ```async/await```
    - future
        + ```asyncio.Future()```
        + future represents the result of work that has not been completed yet.
    - task
        + ```loop.create_task(task_function())```
        + Tasks are one of the primary ways to interact with the event loop.
        + Tasks wrap coroutines and track when they are complete.
        + Tasks are subclasses of Future
        + so other coroutines can wait for them and each has a result that can be retrieved after the task completes.
+ [*I don't understand asyncio*](http://lucumr.pocoo.org/2016/10/30/i-dont-understand-asyncio/)

![](http://7xj431.com1.z0.glb.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202016-11-13%20%E4%B8%8B%E5%8D%885.22.04.png)
