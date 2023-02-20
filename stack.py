stack = []

def push_stack(n):
    stack.append(n)
    print("pushed!")

def pop_stack():
    if len(stack) == 0:
        print("stack underflow!")
    print("poped!")
    return stack.pop()

def top_of_stack():
    print(stack[len(stack)-1])


# Driver Code

push_stack(9)
push_stack(10)
push_stack(3)
top_of_stack()
print(pop_stack())
top_of_stack()