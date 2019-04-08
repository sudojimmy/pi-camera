#!/usr/bin/python
import argparse
import logging
import socket

parser = argparse.ArgumentParser()
parser.add_argument(
    "--ip",
    default="localhost",
    help="IP address server running on",
    type=str
)

parser.add_argument(
    "--port",
    default=50053,
    help="Port server running on",
    type=int
)

args = parser.parse_args()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = (args.ip, args.port)
logging.info("Connect to: %s:%d" % (args.ip, args.port))

sock.connect(addr)

f = open('pic.jpg', 'w')
try:
    while True:
        data = sock.recv(1024)
        if not data:
            break
        f.write(data)
finally:
    sock.close()

logging.info("DONE");
