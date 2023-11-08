from collections import deque

class RequestAllocate:
    def __init__(self):
        self.queue = deque()
        self.prior_queue = deque()

    def prior(self, req):
        if self.queue:
            moved_request = self.queue.popleft()
            self.prior_queue.append(moved_request)
            print(f"Moved standard request to priority: <{moved_request}>")


        self.prior_queue.append(req)
        print(f"Priority request initialized: <{req}>")

    def standard_queue(self, req):
        self.queue.append(req)
        print(f"Request <{req}> added to the standard queue")

    def queue_history(self):
        print("Standard Queue History:")
        for req in self.queue:
            print(f"<{req}>")
        print("Priority Queue History:")
        for req in self.prior_queue:
            print(f"<{req}>")


request_allocate = RequestAllocate()

"""
request_allocate.standard_queue("SYN")
request_allocate.prior("HTTP")
request_allocate.standard_queue("FTP")

request_allocate.queue_history()
"""