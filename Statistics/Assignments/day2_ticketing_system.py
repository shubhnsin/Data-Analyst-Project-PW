# ------------------------------------------------------------
# Day 2: Data Structures and Their Applications
# Task:
# Create a simple ticketing system using a Queue.
# The system should:
# 1. Add new ticket requests (enqueue)
# 2. Process tickets in FIFO order (dequeue)
# 3. Show the next ticket to be processed
# 4. Display the total number of pending tickets
# ------------------------------------------------------------

from collections import deque  # deque allows fast insert and remove operations


class TicketQueue:
    def __init__(self):
        # Initialize an empty queue
        self.queue = deque()

    def enqueue(self, ticket_name):
        # Add a new ticket at the end of the queue
        # This simulates a new customer request
        print(f"[New Request] Ticket '{ticket_name}' added.")
        self.queue.append(ticket_name)

    def dequeue(self):
        # Process the first ticket in the queue
        # Queue follows FIFO (First In First Out)
        if len(self.queue) == 0:
            print("[Error] No tickets to process.")
            return None

        # Remove and return the first ticket
        ticket = self.queue.popleft()
        print(f"[Processing] Now serving ticket: '{ticket}'")
        return ticket

    def view_next(self):
        # Display the next ticket without removing it
        if len(self.queue) > 0:
            print(f"[Next] The next ticket is: '{self.queue[0]}'")
        else:
            print("[Info] Queue is empty.")

    def total_tickets(self):
        # Display total number of tickets in the queue
        count = len(self.queue)
        print(f"[Status] Total tickets pending: {count}")
        return count


# Program execution starts here
if __name__ == "__main__":
    print("--- Day 2: Ticketing System Using Queue ---\n")

    # Create an object of the TicketQueue class
    system = TicketQueue()

    # Step 1: Add ticket requests to the queue
    system.enqueue("Issue #101: Login Failure")
    system.enqueue("Issue #102: Payment Error")
    system.enqueue("Issue #103: Page Not Loading")

    # Step 2: Check the next ticket and total tickets
    system.view_next()
    system.total_tickets()

    # Step 3: Process ticket requests
    system.dequeue()
    system.dequeue()

    # Step 4: Check remaining tickets
    system.total_tickets()
