'''
from rudp.rudp_client import RUDPClient
from utils import Util
import time
import argparse

def client(addr, filename):
    sock = RUDPClient()
    sock.connect(addr)
    print('Connection established...')
    u = Util(sock)
    u.send(filename)
    status = u.recv().decode('ascii')
    if status != "OK":
        print(status)
        sock.close()
        return
    f = open(filename, 'wb')
    print('Started file transfer...')
    start_time = time.time()
    idx = 0
    while True:
        start = time.time()
        data = u.recv()
        idx += 1
        end = time.time()
        print('Block:', idx, end - start, end='\r')
        if not data:
            print('Finished file transfer...')
            end_time = time.time()
            diff = end_time - start_time
            print('time taken: ', diff, 's')
            break
        f.write(data)
    f.close()
    sock.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser('Simple file client')
    parser.add_argument('--filename', default='test2.mp4', type=str)
    args = parser.parse_args()
    
    client(("127.0.0.1", 8000), args.filename)
'''