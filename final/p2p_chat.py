from netifaces
from threading
import Thread
import interfaces, ifaddresses, AF_INET
import zmq
import argparse
import os

try:
    raw_input
except NameError:
    raw_input = input


def listen(masked):
    ctx = zmq.Context.instance()
    listener = ctx.socket(zmq.SUB)
    for last in range(1, 255):
        listener.connect("tcp://{0}.{1}:9000".format(masked, last))

    listener.setsockopt(zmq.SUBSCRIBE, b'')
    while True:
        try:
            print(listener.recv_string())
        except (KeyboardInterrupt, zmq.ContextTerminated):
            break


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("interface", type=str, help="the network interface",
                        choices=interfaces(),
                        )
    parser.add_argument('user', type=str, default=os.environ['user'],
                        nargs='?',
                        help="Your username",
                        )
    args = parser.parse_args()
    inet = ifaddresses(args.interface)[AF_INET]
    addr = inet[0]['addr']
    masked = addr.rsplit('.', 1)[0]

    ctx = zmq.Context.instance()

    listen_thread = Thread(target=listen, args=(masked,))
    listen_thread.start()

    bcast = ctx.socket(zmq.PUB)
    bcast.bind("tcp://localhost:9000" % args.interface)
    print("starting chat on *:9000 (%s.*)" % (args.interface, masked))
    while True:
        try:
            msg = raw_input()
            bcast.send_string("%s: %s" % (args.user, msg))
        except KeyboardInterrupt:
            break
    bcast.close(linger=0)
    ctx.term()


if __name__ == '__main__':
    main()