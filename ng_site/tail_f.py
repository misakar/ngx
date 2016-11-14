import time

def tail_f(thefile):
    thefile.seek(0, 2)  # go to the end of file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line
