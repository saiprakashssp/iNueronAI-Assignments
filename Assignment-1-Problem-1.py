#!/usr/bin/env python
# coding: utf-8

# In[33]:


"""Problem-1: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). 
The numbers obtained should be printed in a comma-separated sequence on a single line. """


# In[34]:


def num_divisible_by_Seven_and_not_multiple_of_five(start_val,stop_val):
    for i in range(start_val,stop_val):
        if i%7==0 and i!=i*5:
            print(i, end = "\t")
        else:
            pass
num_divisible_by_Seven_and_not_multiple_of_five(2000,3201)





