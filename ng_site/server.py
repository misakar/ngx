import json
import asyncio
import websockets
from config import host, port
from types import coroutine

from config import nginx_log_file_path
from tail_f import tail_f
from handle import handle

# async def handle_server(websocket, path):
@coroutine
def handle_server(websocket, path):
    logfile = open(nginx_log_file_path)
    lines = tail_f(logfile)
    log_dicts = handle(lines)

    for log_dict in log_dicts:
        # await websocket.send(str(log_dict))
        yield from websocket.send(str(log_dict))

start_server = websockets.serve(handle_server, host, int(port))

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
