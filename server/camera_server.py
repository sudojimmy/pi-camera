#!/usr/bin/python

import argparse
import logging
import socket

from camera import takePhoto

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

if __name__ == '__main__':
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        addr = (args.ip, args.port)
        logging.info("Server listening on: %s:%d" % (args.ip, args.port))
        sock.bind(addr)
        sock.listen(1)
        while True:
            logging.info("Received connection")
            conn, client = sock.accept()
            try:
                takePhoto()
                f = open('cameraTest.jpg','rb')
                while True:
                    msg = f.read(1024)
                    if not msg:
                        logging.info("Image sent")
                        break
                    conn.send(msg)
            finally:
                conn.close()
                f.close()
    finally:
        sock.close()



