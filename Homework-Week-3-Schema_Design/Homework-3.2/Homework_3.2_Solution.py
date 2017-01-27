# working and sample code for understanding of 'insert_entry', 'get_posts' and 'get_post_by_permalink' functions
# for exact code refer userDOA.py file

import pymongo

# establishing connection
conn = pymongo.MongoClient("mongodb://localhost")
db = conn.blog
posts = db.posts


## insert_entry() function commands
# Build a new post
post = {"title": "title",
        "author": "author",
        "body": "post",
        "permalink":"permalink",
        "tags": ["tag-1", "tag-2", "tag-3"]],
        "comments": [],
        "date": datetime.datetime.utcnow()}

# now insert the post
try:
    # XXX HW 3.2 Work Here to insert the post
    posts.insert_one(post)
    
except:
    print "Error inserting post"


## get_posts() function commands
query = { }
        
try:
    cursor = posts.find(query).sort('date', -1).limit(num_posts)
except:
    print "Error getting post"


## get_post_by_permalink() function commands
query = { 'permalink': permalink }

try:
    post = self.posts.find_one(query)
except:
    print "Error getting post"

print post                                                  # use return post to return value