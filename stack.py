stack =[]
#Push
def add(s,num):
    s.append(num)
    return s
#Pop
def remove(s):
    if len(s) == 0:
        return "Stack is Empty"
    else:
         s.pop()
         return s
#IsEmpty
def isEmpty(s):
    if len(s) == 0:
        return True
    else:
        return False
# Peek
def peek(s):
    if len(s) == 0:
        return "stack is Empty"
    else:
        return s[-1]
    
#Size
def size(s):
    return len(s)

print(isEmpty(stack))
print(stack)
add(stack,1)
print(stack)
print(isEmpty(stack))
print(peek(stack))
print(remove(stack))
print(remove(stack))
print(remove(stack))
print(add(stack,1))
print(remove(stack))
