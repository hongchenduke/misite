# testaa.py
import os,sys
import time
from concurrent.futures.thread import ThreadPoolExecutor
paths = [
    "paths111111111",
    "paths222222222",
]

def cc(path):
    print(time.time(), path)

threads = ThreadPoolExecutor(max_workers=6)

threads.map(cc,paths)
