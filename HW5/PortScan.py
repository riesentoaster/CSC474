import socket
import time
from concurrent.futures import ThreadPoolExecutor
import sys

NUM_THREADS = 100
MAX_PORT = 65535
timeout = None

def scanPort(host, port):
    # print(f"scanning host {host} – port {port}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        res = s.connect_ex((host, port))
        if res == 0:
            try:
                return socket.getservbyport(port, "tcp")
            except:
                return "[unassigned]"
        else:
            return None


def scanPorts(host, ports):
    with ThreadPoolExecutor(NUM_THREADS) as threadPool:
        return [threadPool.submit(scanPort, host, p).result() for p in ports]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 PortScan.py [host]")
        sys.exit(1)
    
    host = sys.argv[1]

    print("Scanning", host)
    print("-------------------------")
    startTime = time.time()
    res = scanPorts(host, range(MAX_PORT+1))
    scanTime = time.time()-startTime

    line = ""
    for i,r in enumerate(res):
        if (i%4096==0):
            print(line)
            line = ""
            line += str(i)
            line += "\t"
        if (r):
            line += "!"
        if (i%255==0):
            line += "."

    print()
    print("Scan finished!")
    print("-------------------------")

    numOfOpenPorts = sum([1 if r else 0 for r in res])
    print(f"{numOfOpenPorts:>10} ports found")
    print(f"{f'{scanTime:.2f}':>10} seconds elapsed")
    print(f"{f'{(MAX_PORT+1)/scanTime:.2f}':>10} ports per second")

    print("Open ports:")
    print("-------------------------")
    for i,r in enumerate(res):
        if (r):
            print(f"{i:>5}: {r}")

    print()
    print("Terminating normally")


        
        
