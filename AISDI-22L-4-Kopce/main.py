from heaps import insert, extract

heap = [-1]
insert(heap, 5, 2)
print(heap[1:])
insert(heap, 2, 2)
print(heap[1:])
insert(heap, 3, 2)
print(heap[1:])
insert(heap, 7, 2)
print(heap[1:])
insert(heap, 9, 2)
print(heap[1:])
extract(heap, 2)
print(heap[1:])
extract(heap, 2)
print(heap[1:])
extract(heap, 2)
print(heap[1:])
