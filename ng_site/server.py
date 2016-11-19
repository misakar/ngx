import time
import json
import asyncio
import websockets
from config import host, port

from config import nginx_log_file_path
from tail_f import tail_f
from handle import handle

# async def handle_server(websocket, path):
@asyncio.coroutine
def handle_server(websocket, path):
    request_count = 0
    logfile = open(nginx_log_file_path)
    lines = tail_f(logfile)
    log_dicts = handle(lines)

    start = time.time()
    for log_dict in log_dicts:
        # await websocket.send(str(log_dict))
        request_count += 1
        during_time = time.time() - start
        log_dict.update({
            'request_per_second': round(
                (request_count / during_time), 2
            )
        })
        yield from websocket.send(str(json.dumps(log_dict)))


start_server = websockets.serve(handle_server, host, int(port))
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
