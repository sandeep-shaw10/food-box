from tqdm import tqdm, trange
import time

def loader(delay):
    for _ in trange(delay):
        time.sleep(0.01)
