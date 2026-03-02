queue=[]
#Enqueue
def add(q,num):
    q.append(num)
    return q
#Dequeue
def remove(q):
    q.pop(0)
    return q
#isEmpty
def isEmpty(q):
    if len(q) ==0:
        return True
    else:
        return False
#Peek
def peek(q):
    if len(q)==0:
        return "the Queue is Empty"
    else:
        return q[0]
#size
def size(q):
    return len(q)

print(isEmpty(queue))
print(queue)
print(add(queue,5))
print(remove(queue))
print(size(queue))
print(peek(queue))
print(add(queue,9))
print(add(queue,6))
print(add(queue,7))
print(queue)
print(peek(queue))
print(remove(queue))

