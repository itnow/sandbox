# Stack
stack = [0] * n
size = 0
def push(x):
    global size
    stack[size] = x
    size += 1
def pop():
    global size
    size -= 1
    return stack[size]

# Queue
# Cyclic buffer is used http://en.wikipedia.org/wiki/Circular_buffer
n = 4
queue = [0] * n
head, tail = 0, 0
def push(x):
    global tail
    tail = (tail + 1) % n
    queue[tail] = x
def pop():
    global head
    head = (head + 1) % n
    return queue[head]
def size():
    return (tail - head + n) % n
def empty():
    return head == tail
