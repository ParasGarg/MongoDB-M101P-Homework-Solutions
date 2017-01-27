# working and sample code for understanding of 'add_comment' function
# for exact code refer userDOA.py file

import pymongo

# establishing connection
conn = pymongo.MongoClient("mongodb://localhost")
db = conn.blog
posts = db.posts

comment = {'author': "Mongo", 'body': "Hello Mongodb!"} # comment doc is passed in the add_comment function

query = { 'permalink': "my_blog" }                      
post_find = posts.find_one(query)                       # finding post in which comment is be added 

comment_list = post_find['comments']                    # storing comments in a list
comment_list.append(comment)                            # appending new comment in the list

update = { '$set':{ 'comments': comment_list } }         
posts.update_one(query, update, upsert=True)            # updating the document by the new list     

post_find = self.posts.find_one(query)                  # finding post in which comment is be added                       

print post_find                                         # use return rather then print