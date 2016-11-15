import time

def tail_f(thefile):
    thefile.seek(0, 2)  # go to the end of file
    while True:
        line = thefile.readline()
        # 现在是主动去询问
        # 使用websocket, 可以改成服务器主动发送
        if not line:
            time.sleep(0.1)
            continue
        yield line
