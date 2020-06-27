#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# # 1D Array

# In[23]:


a = np.array([1,2])
a


# # 2D Array

# In[20]:


a1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
a1


# # ndim -> gives the dimension of array

# In[12]:


a1.ndim


# In[14]:


a.ndim


# # itemsize -> to know the size of each item in an array

# In[18]:


a3.itemsize


# In[21]:


a1.itemsize


# In[25]:


a.itemsize


# # dtype -> to know the data type of an array and also used for typecasting (changing the int array to float array)

# In[26]:


a.dtype


# In[27]:


a3.dtype


# In[28]:


a4 = np.array([[1,2,3],[4,5,6]])
a4.dtype


# In[36]:


a4 = np.array([[1,2,3],[4,5,6]], dtype = np.float64)
a4.dtype


# # size -> Gives the total nuber of elements in an array

# In[37]:


a.size


# In[38]:


a1.size


# In[40]:


a3.size


# In[41]:


a4.size 


# # shape -> GIves the number of rows and columns like (rows,columns)

# In[42]:


a.shape


# In[49]:


a


# In[43]:


a1.shape


# In[48]:


a1


# In[44]:


a3.shape


# In[45]:


a3


# In[46]:


a4.shape


# In[47]:


a4


# # zeros -> append the designed array with 0s with shape given like (2,3)

# In[51]:


a5 = np.zeros((2,3), dtype = np.int)
a5


# # ones -> append array with 1 with shape given like (3,3)

# In[54]:


a6 = np.ones((6,6), dtype = np.int)
a6


# # arange -> defines a range of numbers... Ceiling value or the max value entered is not counted in this

# In[55]:


a7 = np.arange(0,10)
a7


# # linspace -> providing the number of digits specified within a range and the generated numbers are linealr spaced from each other

# In[58]:


a8 = np.linspace(1,11,10)
a8


# # reshape -> change the shape of array like from(3,2) to (2,3)

# In[63]:


a9 = np.array([[1,2],[3,4], [5,6]])


# In[64]:


a9.shape


# In[65]:


a9.reshape(2,3)


# In[66]:


a9.reshape(1,6)


# # ravel -> it just flatten the n dimensional array to 1D array and does not make any changes in the original array. So if we want to store the result of the flatten array, then we will have to store it in a differnet variable.

# In[67]:


a9


# In[68]:


a9.ravel()


# In[69]:


a9


# In[70]:


b = a9.ravel()
b


# In[71]:


a9


# In[72]:


b


# # min -> returns the minimum element, max -> returns the maximum element, sum -> returns the sum of the array

# In[73]:


a9.min()


# In[74]:


a9.max()


# In[75]:


a9.min


# In[76]:


a9.sum()


# # axis -> defines the changes to m be made either in column or row; 0 : Columns, 1: Rows

# In[77]:


a9


# In[78]:


a9.sum(axis = 1)


# In[79]:


a9.sum(axis = 0)


# # np.sqrt(object) -> gives square root of an array

# In[80]:


np.sqrt(a9)


# # std -> returns the standard deviation

# In[81]:


a9.std()


# # operations in numpy arrays

# In[93]:


array1 = np.array([[1,2], [4,5]])
array2 = np.array([[4,5], [7,8]])


# In[86]:


array1+array2


# In[87]:


array1-array2


# In[88]:


array1*array2


# In[90]:


array1/array2


# In[94]:


array1.dot(array2)

