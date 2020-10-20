#!/usr/bin/env python
# coding: utf-8

# In[8]:


from math import pi 


# In[10]:


def sphere_volume_with_diameter_in_cm(d):
                                      radius = d/2
                                      volume = ((4*pi *radius * radius * radius)/3)
                                      print("Volume of the Sphere" , volume)
sphere_volume_with_diameter_in_cm(12)






