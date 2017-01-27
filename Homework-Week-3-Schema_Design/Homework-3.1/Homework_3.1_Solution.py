import pymongo

# establishing connection
connection = pymongo.MongoClient("mongodb://localhost")

# handling db and collection
db = connection.school
students = db.students


# function to count the number of students in the collection 
def students_count():
    print "Total number of students :: "
    query = { }

    try:
        counts = students.find(query).count()
    
    except Exception as ex:
        print "Unexpected Error: ", type(ex), ex

    print counts, "\n"
    return counts

# function
def students_detail(students_count):    
    for i in range(0, students_count):

        query = { '_id':i, 'scores.type':'homework' }
        projection = { 'scores':1, '_id':0 }

        try:
            doc = students.find_one(query, projection)

        except Exception as ex:
            print "Unexpected Error: ", type(ex), ex

        max_score = 0.0
        scores_list = []                                    # a null array list
        for val in doc['scores']:
            if (val['type'] == 'homework'):
                if(max_score < val['score']):
                    max_score = val['score']
            else:
                scores_list.append(val)                     # adding values to array other than 'homework' type

        scores_list.append({"score":max_score, "type":"homework"})
                                                            # adding values to array of than 'homework' type having max score
        # updating scores_list values in database
        students.update_one({'_id':i}, {'$set': {'scores':scores_list}})
    
    
# function call
count = students_count()
students_detail(count)