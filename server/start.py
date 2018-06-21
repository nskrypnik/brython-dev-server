import asyncio
import uvloop

from .webapp import start_web_server
from .watchdog import start_watchdog
from concurrent.futures import ProcessPoolExecutor

# setting uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

executor = ProcessPoolExecutor(max_workers=2)
executor.submit(start_web_server)
executor.submit(start_watchdog)
