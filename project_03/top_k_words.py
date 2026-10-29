class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        i = len(self.heap) - 1

        while i > 0:
            parent = (i - 1) // 2

            if self.heap[i][0] < self.heap[parent][0]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def extract_min(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        min_item = self.heap[0]
        self.heap[0] = self.heap.pop()

        i = 0

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left

            if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

        return min_item


text = input("Enter text: ")
words = text.lower().split()


frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

k = int(input("Enter K: "))

heap = MinHeap()

for word in frequency:
    heap.insert((frequency[word], word))

    if len(heap.heap) > k:
        heap.extract_min()

result = []

while len(heap.heap) > 0:
    result.append(heap.extract_min())

result.reverse()

print("\nTop", k, "Frequent Words:")

for count, word in result:
    print(word, "-", count)