import asyncio

from config import nginx_log_file_path
from tail_f import tail_f
from handle import handle


logfile = open(nginx_log_file_path)
lines = tail_f(logfile)
log_dicts = handle(lines)

def show():
    yield log_dicts

# event_loop = asyncio.get_event_loop()
# try:
#     event_loop.run_until_complete(show())
# finally:
#     event_loop.close()
# show()
for log_dict in log_dicts:
    print(log_dict)
