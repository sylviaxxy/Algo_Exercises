# Dijkstra using Priority Queue
import heapq
pqueue = []
heapq.heappush(pqueue, (1, 'A'))
heapq.heappush(pqueue, (7, 'B'))
heapq.heappush(pqueue, (3, 'C'))
heapq.heappush(pqueue, (6, 'D'))
heapq.heappush(pqueue, (2, 'E'))

heapq.heappop(pqueue)
heapq.heappop(pqueue)
heapq.heappop(pqueue)
heapq.heappop(pqueue)
heapq.heappop(pqueue)