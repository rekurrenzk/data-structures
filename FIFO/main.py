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
            print(f"printing priority job: {current_job}")

        elif self.queue:
            current_job = self.queue.popleft()
            print(f"printing: {current_job}")

        else:
            print("No print jobs in the queue.")


    def show_queue(self):
        print("\nRegular Print Queue:\n")
        for count, job in enumerate(self.queue, start=1):
            print(f"{count}. {job}")

    def show_priority_queue(self):

        print("\nPriority Print Queue:")
        for count, job in enumerate(self.priority_queue, start=1):
            print(f"{count}. {job}")



print_queue = PrintQueue()
