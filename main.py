

# The list data has some methods:
"""
list.append(x) this is equal to a[len(a):] = [x]
"""


# Stack (LIFO)

    # It supports two primary operations: push and pop
        # Push adds an item to the top of the stack and pop removes the topmost

# let us write a simple undo mechanism uses a stack to store actions

class ActionManager:

    def __init__(self):
        self.stack = []
        self.latest = []

    def action_process(self, action):
        self.stack.append(action)
        print(f"action called:\n < {action} >")

        if len(self.latest) < 10:
            self.latest.append(action)
        else:
            self.latest[0].pop()
            self.latest[len(self.latest):].append(action)

    def action_history(self):
        print()
        if self.stack:
            print(f"so far '{len(self.stack)}' action proceeded!")
            print(self.stack)
        elif self.latest:
            print(f"so far '{len(self.latest)}' action proceeded!")
            print(self.latest)

    def latest_action(self):
        print()
        latest_applied_action = self.latest[-1]
        print(f"the latest action:\n < {latest_applied_action} >")

    def latest_action_return(self):
        print()
        latest_action = self.latest[-1]
        self.stack.append(latest_action)
        print(f"< {self.latest[-1]} > is returned!")

    def latest_action_delete(self):
        print()
        latest_action = self.latest[-1]
        self.stack.pop()
        print(f"THE LATEST < {latest_action} > ACTION IS DELETED!")


action_manager = ActionManager()