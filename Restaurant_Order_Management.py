from collections import deque

# Class to represent a single order
class Order:
    def __init__(self, order_id, customer_name, order_items, preparation_time, waiting_time):
        # Input Validation
        if not isinstance(order_id, int) or order_id <= 0:
            raise ValueError("Order ID must be a positive integer.")
        if not isinstance(customer_name, str) or not customer_name.strip():
            raise ValueError("Customer name must be a non-empty string.")
        if not isinstance(order_items, list) or len(order_items) == 0:
            raise ValueError("Order items must be a non-empty list.")
        if not isinstance(preparation_time, int) or preparation_time < 0:
            raise ValueError("Preparation time must be a non-negative integer.")
        if not isinstance(waiting_time, int) or waiting_time < 0:
            raise ValueError("Waiting time must be a non-negative integer.")

        self.order_id = order_id
        self.customer_name = customer_name
        self.order_items = order_items
        self.preparation_time = preparation_time
        self.waiting_time = waiting_time

    def __str__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer_name}, Items: {self.order_items}, Preparation Time: {self.preparation_time}, Waiting Time: {self.waiting_time}"


# Class to represent the kitchen's order queue
class OrderQueue:
    def __init__(self):
        self.queue = deque()

    # Add order to the queue
    def enqueue(self, order):
        if not isinstance(order, Order):
            raise TypeError("Only Order objects can be added to the queue.")
        self.queue.append(order)

    # Remove order from the front of the queue
    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            raise IndexError("Cannot dequeue from an empty queue.")

    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Get the size of the queue
    def size(self):
        return len(self.queue)

    # Display all orders in the queue
    def display(self):
        if self.is_empty():
            print("The queue is empty.")
        else:
            for order in self.queue:
                print(order)

    # Prioritize orders based on preparation time and waiting time
    def prioritize_orders(self):
        self.queue = deque(sorted(self.queue, key=lambda order: (order.preparation_time, order.waiting_time)))

    # Get the next order to be prepared based on priority
    def get_next_order(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None


# Testing the implementation
if __name__ == "__main__":
    try:
        # Create orders
        order1 = Order(1, "Alice", ["Burger", "Fries"], 10, 5)
        order2 = Order(2, "Bob", ["Pizza"], 15, 3)
        order3 = Order(3, "Charlie", ["Salad"], 5, 7)

        # Create the order queue
        kitchen_queue = OrderQueue()

        # Add orders to the queue
        kitchen_queue.enqueue(order1)
        kitchen_queue.enqueue(order2)
        kitchen_queue.enqueue(order3)

        print("--- Orders before prioritization ---")
        kitchen_queue.display()

        # Prioritize orders
        kitchen_queue.prioritize_orders()
        print("\n--- Orders after prioritization ---")
        kitchen_queue.display()

        # Process orders
        print("\n--- Processing Orders ---")
        while not kitchen_queue.is_empty():
            next_order = kitchen_queue.dequeue()
            print(f"Processing {next_order}")

    except Exception as e:
        print(f"Error: {e}")
