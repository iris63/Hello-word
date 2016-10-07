
# coding: utf-8

# In[8]:

#donuts
#Given an int count of a number of donuts, return a string of the form 'Number of donuts: ', where  is the number 
#passed in. However, if the count is 10 or more, then use the word 'many' instead of the actual count.

#So donuts(5) returns 'Number of donuts: 5' and donuts(23) returns 'Number of donuts: many'

def donuts(count):
    if count >=10 : nombre="many"
    else: nombre=str(count)
    retour = "Number of donuts: "  +nombre  
    return retour


# In[29]:

#both_ends
#Given a string s, return a string made of the first 2 and the last 2 chars of the original string, 
#so 'spring' yields 'spng'. However, if the string length is less than 2, return instead the empty string.
def both_ends(s):
    longueur=len(s)
    if longueur<2:retour=""
    else: retour=s[:2]+s[(longueur-2):]   
    return retour


# In[33]:

#fix_start
#Given a string s, return a string where all occurences of its first char have been changed to '*', 
#except do not change the first char itself.
#e.g. 'babble' yields 'ba**le'
#Assume that the string is length 1 or more. Hint: s.replace(stra, strb) returns a version of string s where all instances of stra have been replaced by strb.
def fix_start(s):
    car1=s[0]
    retour=car1+s[1:].replace(car1, '*')
    return retour


# In[56]:

#MixUp
#Given strings a and b, return a single string with a and b separated by a space '<a> <b>', 
#except swap the first 2 chars of each string.
#e.g.
#'mix', pod' -> 'pox mid'
#'dog', 'dinner' -> 'dig donner'
#Assume a and b are length 2 or more.
def mix_up(a, b):
    retour=b[:2]+a[2:]+" "+a[:2]+b[2:]
    return retour


# In[58]:

def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)


# In[5]:


def main():
    print 'donuts'
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print
    print 'both_ends'
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

  
    print
    print 'fix_start'
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print
    print 'mix_up'
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')



# In[59]:

main()


# In[ ]:



