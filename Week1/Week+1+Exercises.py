
# coding: utf-8

# Programming Exercises
# ---
# Dan Siegel
# DSC510

# -----

# Simple Calculations
# ---

# In[1]:


#1. Add two integers together
4+4


# In[4]:


#2. Show how parenthesis changes the order of operations when using multiplication and addition together.
noOrderOfOps = 4+5*6
print("This is the result with no order of operations: ",noOrderOfOps)
orderOfOps = (4+5)*6
print("This is the result with parenthesis to show order of operations: ",orderOfOps)


# In[8]:


#3. Show how to square and cube numbers.
squared = 4**2
print("This is a number squared", squared)
cubed = 4**3
print("This is a number cubed", cubed)


# In[12]:


#4. Assign numbers to variables and then perform mathematical operations (e.g., add, subtract, multiply) using the variables.
var1 = 5
var2 = 6
print("this is var2 minus var1:", (var2-var1))


# In[14]:


#5. Set the variable pi = 3.14159265 and then round it to two decimal places.
pi = 3.14159265
print(pi)
pi=round(pi,2)
print(pi)


# In[15]:


#6. See what happens when you try to divide a number by 0.
5/0


# In[18]:


#7. Add an integer and a floating point number. Is the result a floating point number or an integer?
print("adding an int and a fp number results in an fp number ie:",5+5.0)


# In[20]:


#8. Compute the remainder of an odd number when divided by 2.
print("The remainder, or modulus of 5/2 is:",5%2)


# Working with strings
# ---
# 

# ---

# In[22]:


#1. Enter Hello World! as a string
"Hello World"


# In[23]:


#2. Assign your first name to the variable first_name and your last name to the variable last_name.
first_name = 'Dan'
last_name = 'Siegel'


# In[25]:


#3. Calculate the number of characters in your first name
len(first_name)


# In[27]:


#4. Using string indexing, get the first letter of your first name.
first_name[0]


# In[28]:


#5. Using string indexing, get the last letter in your last name.
first_name[-1]


# In[29]:


#6. See what happens when you add first_name and last_name
first_name + last_name


# In[30]:


#7. See what happens when you multiply your first_name by an integer between 1 and 5.  
first_name * 3


# Working with Lists
# ---
# 

# ---

# In[31]:


#1. Create a list of numbers from 1 to 5 and assign it to the variable L.
L = [1,2,3,4,5]


# In[34]:


#2. Using list indexing, select the second item in the list.
L[1]


# In[36]:


#3. Using slices, get a list containing only the 2nd, 3rd, and 4th numbers.
L[1:4]


# In[37]:


#4. Append a 6 to the end of the list.
L.append(6)


# In[40]:


#5. Using slices, replace the numbers 2 and 3 with 8 and 9
L[1:3]=[8,9]

