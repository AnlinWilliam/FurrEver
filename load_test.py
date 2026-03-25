import requests
import threading
import time

URL = "http://localhost:5000/"   # endpoint to test
NUM_USERS = 20                       # simulated users

def send_request():
    try:
        start = time.time()
        r = requests.get(URL)
        end = time.time()

        print("Status:", r.status_code,
              "Response Time:", round(end-start,3),"sec")

    except Exception as e:
        print("Error:", e)

threads = []

for i in range(NUM_USERS):
    t = threading.Thread(target=send_request)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Load test completed")