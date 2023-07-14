#!/usr/bin/env python
# coding: utf-8

# In[6]:


def factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

num = int(input("Enter a number: "))


result = factorial(num)
print(f"The factorial of {num} is: {result}")

