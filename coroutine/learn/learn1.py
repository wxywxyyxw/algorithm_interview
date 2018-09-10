# import asyncio
# from time import sleep
#
# # Define a coroutine that takes in a future
# async def myCoroutine():
#     sleep(5)
#     print("My Coroutine")
#
#
#
# # Spin up a quick and simple event loop
# # and run until completed
# loop = asyncio.get_event_loop()
# try:
#     loop.run_until_complete(myCoroutine())
# finally:
#     loop.close()


# import asyncio
# import time
#
# async def myWork():
#     print("Starting Work")
#     time.sleep(5)
#     print("Finishing Work")
#
# loop = asyncio.get_event_loop()
# try:
#     loop.run_until_complete(myWork())
# finally:
#     loop.close()


# import asyncio
#
# async def work():
#     while True:
#         await asyncio.sleep(1)
#         print("Task Executed")
#
# loop = asyncio.get_event_loop()
# try:
#     asyncio.ensure_future(work())
#     loop.run_forever()
# except KeyboardInterrupt:
#     pass
# finally:
#     print("Closing Loop")
#     loop.close()

import asyncio
import time

# async def firstWorker():
#     while True:
#         await asyncio.sleep(1)
#         print("First Worker Executed")
#
# async def secondWorker():
#     while True:
#         await asyncio.sleep(1)
#         print("Second Worker Executed")
#
#
# loop = asyncio.get_event_loop()
# try:
#     asyncio.ensure_future(firstWorker())
#     asyncio.ensure_future(secondWorker())
#     loop.run_forever()
# except KeyboardInterrupt:
#     pass
# finally:
#     print("Closing Loop")
#     loop.close()

