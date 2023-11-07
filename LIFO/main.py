
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
        self.history = []

    def action_process(self, action):

        self.stack.append(action)
        print(f"\naction proceed: <{action}>\n")

        if len(self.history) < 10:
            self.history.append(action)

        elif len(self.history) == 10:
            self.history.pop()

        else:
            pass

    def action_history(self):
        if self.stack:
            print("\nTHE COMMAND HISTORY: \n")
            for all_actions in self.stack:
                print("<", all_actions, ">")
        else:
            print("no action has found on the records!")

    def action_return(self):
        if self.history:
            self.stack.append(self.history[-1])
            print(f"\nthe latest command's recalled: <{self.history[-1]}>")
        else:
            print("no old command found!")
            return

    def action_delete(self):
        latest_command = self.stack[-1]
        if self.stack:
            self.stack.pop()
            print(f"\nthe latest command deleted: <{latest_command}>")


action_manager = ActionManager()
