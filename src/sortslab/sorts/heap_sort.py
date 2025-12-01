def heapify(arr: list[int], i: int | None = None, heap_size: int | None = None) -> None:
    if heap_size is None:
        heap_size = len(arr)
    if i is None:
        i = heap_size - 1
    largest = i
    left = 2 * i + 1
    if left >= heap_size:
        return
    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    right = 2 * i + 2
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, largest, heap_size)

def build_heap(arr: list[int]):
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, i)
    return arr

def heap_sort(arr: list[int]) -> list[int]:
    heap = build_heap(arr)
    for i in range(len(heap) - 1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        heapify(heap, 0, i)
    return heap
