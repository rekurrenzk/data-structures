from collections import deque

class PrintQueue:
    def __init__(self):
        self.queue = deque()
        self.priority_queue = deque()

    def submit_print_job(self, document):
        self.queue.append(document)
        print(f"Submitted print job: {document}")

    def submit_priority_job(self, document):
        self.priority_queue.append(document)
        print(f"Submitted priority print job: {document}")

    def run_print_job(self):
        if self.priority_queue:
            current_job = self.priority_queue.popleft()
            print(f"Printing priority job: {current_job}")
        elif self.queue:
            current_job = self.queue.popleft()
            print(f"Printing: {current_job}")
        else:
            print("No print jobs in the queue.")

    def show_queue(self):
        print("\nRegular Print Queue:")
        for count, job in enumerate(self.queue, start=1):
            print(f"{count}. {job}")

    def show_priority_queue(self):
        print("\nPriority Print Queue:")
        for count, job in enumerate(self.priority_queue, start=1):
            print(f"{count}. {job}")


print_queue = PrintQueue()

"""
print_queue.submit_print_job("Document1.pdf")
print_queue.submit_print_job("Document2.pdf")
print_queue.show_queue()

print_queue.submit_priority_job("Priority_Document1.pdf")
print_queue.submit_print_job("Document3.pdf")
print_queue.show_queue()
print_queue.show_priority_queue()

print_queue.run_print_job()
print_queue.show_queue()
print_queue.show_priority_queue()
"""