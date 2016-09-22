import pyaudio
import struct
import wave
from boto import kinesis
from collections import deque
import Queue
from threading import Thread
import json
import time
from get_coffee_status import get_coffee_status
import event_types

q = Queue.Queue()
k = kinesis.connect_to_region("us-east-1")


def write(w, data):
    count = len(data) / 2
    fmt = "%dh" % (count)
    shorts = struct.unpack(fmt, data)
    for s in shorts:
        w.write(str(s) + "\n")

def algo(data):
    status, rms = get_coffee_status(data)
    print '{} rms:{}'.format(status, rms)
    return status

def worker():
    prev_state = ""
    while True:
        data = q.get()
        count = len(data) / 2
        fmt = "%dh" % (count)
        shorts = struct.unpack(fmt, data)
        current_state = algo(shorts)
        if prev_state != current_state:
            k.put_record("coffee", json.dumps({"timestamp": int(time.time()), "state": current_state}), "1")
            prev_state = current_state

        q.task_done()


if __name__ == "__main__":
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, 
                    channels=1, 
                    rate=1000, 
                    input=True,
                    output=False)

    t = Thread(target=worker)
    t.daemon = True
    t.start()

    w = open("/tmp/bennyca.txt", "w")

    buf = deque([])
    for i in range(0, 4):
        buf.append(stream.read(500))
        write(w, buf[i])

    while True:
        q.put(buf[0] + buf[1] + buf[2] + buf[3])
        buf.rotate(-1)
        buf[3] = stream.read(500)
        write(w, buf[3])

    q.join()
    w.close()