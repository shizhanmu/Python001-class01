# 参考：https://docs.python.org/zh-cn/3/library/subprocess.html

import subprocess
import fire
from concurrent.futures import ThreadPoolExecutor

def ping_one(ip_address):
    re = subprocess.run(["ping",ip_address, "-t", "2"], capture_output=True)
    # re = subprocess.run(["ping",ip_address, "-t", "2"])
    if re.returncode == 0:
        print(ip_address)

def ping_func(n, f, ip):
    # ip = '39.97.180.1-39.97.180.10'
    if f == 'ping':
        start_ip, stop_ip = ip.split('-')
        start_last_num = start_ip.split('.')[-1]
        stop_last_num = stop_ip.split('.')[-1]
        start_head = start_ip.rstrip(start_last_num).rstrip('.')
        seed = [start_head + '.' + str(num) for num in range(int(start_last_num), int(stop_last_num)+1)]

        with ThreadPoolExecutor(n) as executor:
            executor.map(ping_one, seed)
    else:
        print("You can call ping or tcp function, anything else is prohibited!")

fire.Fire(ping_func)
