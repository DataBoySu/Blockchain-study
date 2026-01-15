import heapq
import random

# -----------------------------
# Event system
# -----------------------------
class Event:
    def __init__(self, time, action, description=""):
        self.time = time
        self.action = action
        self.description = description

    def __lt__(self, other):
        return self.time < other.time


class Simulator:
    def __init__(self):
        self.time = 0.0
        self.event_queue = []

    def schedule(self, delay, action, description=""):
        event_time = self.time + delay
        heapq.heappush(self.event_queue, Event(event_time, action, description))

    def run(self, until):
        while self.event_queue and self.time <= until:
            event = heapq.heappop(self.event_queue)
            self.time = event.time
            event.action()


# -----------------------------
# Sanity test
# -----------------------------
if __name__ == "__main__":
    sim = Simulator()

    def hello():
        print(f"[{sim.time:.2f}] hello")

    sim.schedule(1.0, hello)
    sim.schedule(0.5, hello)
    sim.schedule(2.0, hello)

    sim.run(until=5.0)

# -----------------------------
# Blockchain data
# -----------------------------
class Block:
    def __init__(self, height, parent_id, miner, timestamp):
        self.height = height
        self.parent_id = parent_id
        self.miner = miner
        self.timestamp = timestamp
        self.id = f"{height}-{miner}-{timestamp:.4f}"
