
# coding: utf-8

# In[1]:


from piazza_api import Piazza
p = Piazza()



# In[2]:


p.user_login('username@ucsd.edu', 'password')
user_profile = p.get_user_profile()
CSE110 = p.network("jebhpmejaa92vh")
CSE110.get_post(10)

posts = CSE110.iter_all_posts(limit=1)
for post in posts:
    print(post)

#>>> from piazza_api import Piazza
#>>> p = Piazza()
#>>> p.user_login()
#Email: ...
#Password: ...
#
#>>> user_profile = p.get_user_profile()
#
#>>> eece210 = p.network("hl5qm84dl4t3x2")
#
#>>> eece210.get_post(100)
#...
#
#>>> posts = eece210.iter_all_posts(limit=10)
#>>> for post in posts:
#...     do_awesome_thing(post)
#
#>>> users = eece210.get_users(["userid1", "userid2"])
#>>> all_users = eece210.get_all_users()
#
#


# In[3]:


for i in post:
    print(i)


# In[16]:


print(type(post['history'][1]))

print(post['history'][1])

for i in post['history'][1]:
    print(i)
print(post['history'][1]['subject'])
print(post['history'][1]['content'])

