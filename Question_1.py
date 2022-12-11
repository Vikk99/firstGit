#!/usr/bin/env python
# coding: utf-8

# In[14]:


import re

number = input("Enter your mobile number")

pattern= "^\+?\d{0,3}\s?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}?"

if re.match(pattern, number):
    print(f"{number} is valid mobile number")
else:
    print(f"{number} is not a valid mobile number")


# In[ ]:





# In[ ]:




