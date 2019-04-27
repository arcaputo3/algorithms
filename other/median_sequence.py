""" Various median finding methods. """

import heapq

class MaxHeapObj(object):
    """ Max Heap Wrapper """
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val

    def __str__(self):
        return str(self.val)


class MinHeap(object):
    """ MinHeap Implementation """
    def __init__(self):
        self.h = []

    def heappush(self, x):
        heapq.heappush(self.h, x)

    def heappop(self):
        return heapq.heappop(self.h)

    def __getitem__(self, i):
        return self.h[i]

    def __len__(self):
        return len(self.h)


class MaxHeap(MinHeap):
    """ MaxHeap Implementation """
    def heappush(self, x):
        heapq.heappush(self.h,MaxHeapObj(x))

    def heappop(self):
        return heapq.heappop(self.h).val

    def __getitem__(self, i):
        return self.h[i].val


class MedianHeap():
    """
        Left: MaxHeap, Right: MinHeap

            o                o
           / \              / \

    """
    def __init__(self, arr=[]):
        """ Optional: pass an array to initialize. """
        self._min_heap = MinHeap()
        self._max_heap = MaxHeap()
        for i in arr:
            self.insert(i)

    def insert(self, item):
        """ Inserts item into MedianHeap. """
        # Empty case
        if not self._min_heap and not self._max_heap:
            self._max_heap.heappush(item)

        elif self._max_heap:
        # Ensure minmax invariant
            if item >= self._max_heap[0]:
                self._min_heap.heappush(item)
            else:
                self._max_heap.heappush(item)

            # Keep difference in lengths less than 2
            if len(self._min_heap) > len(self._max_heap) + 1:
                self._max_heap.heappush(
                    self._min_heap.heappop()
                )
            elif len(self._max_heap) > len(self._min_heap) + 1:
                self._min_heap.heappush(
                    self._max_heap.heappop()
                )

    def median(self):
        """ Returns current median. """
        if self._min_heap and self._max_heap:
            # Even number of items case
            if len(self._min_heap) == len(self._max_heap):
                return (self._min_heap[0] + self._max_heap[0])/2
            # o.w. return head of heap with more items
            elif len(self._min_heap) == len(self._max_heap) + 1:
                return self._min_heap[0]
            else:
                return self._max_heap[0]
        # Single item case - max_heap filled first
        if self._max_heap:
            return self._max_heap[0]
        return None

    def __len__(self):
        """ Returns total length of MedianHeap """
        return len(self._max_heap) + len(self._min_heap)

    def len(self):
        """ Returns length of items in left and right heaps resp. """
        return {
            'left_max': len(self._max_heap),
            'right_min': len(self._min_heap)
        }


if __name__ == "__main__":
    # Test Cases
    med_heap = MedianHeap(range(101, -1, -1c))
    print(med_heap.median())
    print(len(med_heap))
    print(med_heap.len())
