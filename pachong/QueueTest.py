import Queue
initial_page = "https://www.jd.com"
url_queue = Queue.Queue()
url_queue.put(initial_page)

while True:
        print(url_queue)
