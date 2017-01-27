import pymongo

# establishing connection
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to database
db = connection.students
grades = db.grades

# function to find total number of student of grade type "homework"
def students_count():
    print "Total number of students of grade type 'homework' :: "
    query = { 'type':'homework' }

    try:
        cursor = grades.find(query)

    except Exception as ex:
        print "Unexpected Error", type(ex), ex

    student_id_count = 0
    for doc in cursor:
        if student_id_count < doc['student_id']:
            student_id_count = doc['student_id']

    print student_id_count, "\n"
    find_students_of_type_homework(student_id_count)

# function to find all documents of students having grade type "homework"
def find_students_of_type_homework(student_id_count):
    # print "Documents of students of type 'homework' are :: "
    for id in range(0, student_id_count+1):
        query = { 'student_id':id, 'type':'homework' }

        try:
            cursor = grades.find(query)

        except Exception as ex:
            print "Unexpected Error", type(ex), ex

        min_score = 100.0
        min_doc_id = 0
        for doc in cursor:
            if min_score > doc['score']:
                min_score = doc['score']
                min_doc_id = doc['_id']

        # print min_doc_id, "-->" id, "-->", min_score
        delete_student_document(min_doc_id)
        print "Deleted student_id", id

# function to delete the selected student
def delete_student_document(id):
    # print "Document to delete";
    query = { '_id':id }

    try:
        grades.delete_one(query)
         
    except Exception as ex:
        print "Unexpected Error", type(ex), ex


# function call
students_count()
