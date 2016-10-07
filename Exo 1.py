
# coding: utf-8

# In[16]:

#A. match_ends
#Given a list of strings, return the count of the number of strings where the string length is 2 or more 
# and the first and last chars of the string are the same.

def match_ends(words):
    nombre_element=0
    longueur_list= len(words)  
    for i in range(0,longueur_list,1):
        mot=words[i]
        if len(mot)>=2 and mot[0]== mot[-1] : nombre_element=nombre_element+1       
    return nombre_element


# In[17]:

#front_x
#Given a list of strings, return a list with the strings in sorted order, except group all the strings that 
#begin with 'x' first.
#e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
#Hint: this can be done by making 2 lists and sorting each of them before combining them.
def front_x(words):   
    lista=sorted(words)
    for i in range(0,len(words) ,1):
        mot=words[i]
        if  (mot[0]== "x" or mot[0]== "X") : lista.remove(mot) 
       
    listx=sorted(words)
    for i in range(0,len(words) ,1):
        mot=words[i]
        if  not(mot[0]== "x") and not(mot[0]== "X") : listx.remove(mot) 
     
    listx.extend(lista)
    
    return listx



# In[18]:

#sort_last
#Given a list of non-empty tuples, return a list sorted in increasing order by the last element in each tuple.
#e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
#Hint: use a custom key= function to extract the last element form each tuple.

def sort_last(tuples):
    tri=sorted(tuples,key=lambda dernier: dernier[-1])
    return tri



# In[19]:

#Simple provided test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)


# In[20]:

def main():
    print 'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print
    print 'front_x'
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
        ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
        ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])
    
    print
    print 'sort_last'
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


# In[21]:

main()


# In[50]:

#remove_adjacent
#Given a list of numbers, return a list where all adjacent == elements have been reduced to a single element, 
#so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or modify the passed in list.
def remove_adjacent(nums):

    new_list=[]
        
    for i in range(0,len(nums) ,1):
        if not(nums[i] in new_list)  : new_list.append(nums[i])
           
    return new_list





# In[51]:

print remove_adjacent([1, 2, 2, 3])


# In[27]:

#linear_merge
#Given two lists sorted in increasing order, create and return a merged list of all the elements in sorted order. 
#You may modify the passed in lists. 
#Ideally, the solution should work in "linear" time, making a single pass of both lists.

def linear_merge(list1, list2):    
    new_list=sorted(list1+list2)
    return new_list
  


# In[24]:

def main():
    print 'remove_adjacent'
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print
    print 'linear_merge'
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
        ['aa', 'aa', 'aa', 'bb', 'bb'])


# In[52]:

main()


# In[ ]:



