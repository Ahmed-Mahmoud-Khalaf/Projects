import random
import time

class Task:
    def __init__(self, name, priority, arrival):
        self.name = name
        self.priority = priority
        self.arrival = arrival


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        self.heap.append(task)
        i = len(self.heap) - 1

        while i > 0:
            parent = (i - 1) // 2

            if self.heap[i].priority > self.heap[parent].priority:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def extract_max(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_task = self.heap[0]
        self.heap[0] = self.heap.pop()

        i = 0

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            if left < len(self.heap) and self.heap[left].priority > self.heap[largest].priority:
                largest = left

            if right < len(self.heap) and self.heap[right].priority > self.heap[largest].priority:
                largest = right

            if largest == i:
                break

            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest

        return max_task


tasks = []

for i in range(1, 21):
    tasks.append(
        Task("Task" + str(i), random.randint(1, 100), i)
    )




heap = MaxHeap()

start = time.perf_counter()

for task in tasks:
    heap.insert(task)

heap_time = time.perf_counter() - start


print("Execution Order:")

while len(heap.heap) > 0:
    task = heap.extract_max()

    print(
        task.name,
        "- Priority:",
        task.priority,
        "- Arrival:",
        task.arrival
    )



sorted_list = []

start = time.perf_counter()

for task in tasks:
    sorted_list.append(task)
    sorted_list.sort(key=lambda x: x.priority, reverse=True)

list_time = time.perf_counter() - start



print("\nPerformance Comparison:")
print("Max Heap Insert Time:", heap_time)
print("Sorted List Insert Time:", list_time)

print("\nTime Complexity:")
print("Max Heap Insert: O(log n)")
print("Max Heap Extract-Max: O(log n)")
print("Sorted List insertion: O(n) theoretically when maintaining order")