# Question 1: How to implement a queue by two stacks?

def queue_pop(stack_1, stack_2):
    while stack_1:
        stack_1.pop()
        stack_2.push()

    print(stack_2.pop())

# Question 2: How to implement the min() function when using stack with time complexity O(1)?
def stack_min(stack_1, stack_2):
    