student_lists = [{'name': 'Alex', 'grades': [0, 1, 2, 4, 5]}, {'name': 'Peter', 'grades': [4, 5, 4, 4, 5]}, {'name': 'Fedor', 'grades': []}, {'name': 'Vanya', 'grades': [5, 3, 5, 4, 5]} ]
best_students = []
#def filter_students(some_list):
for i in student_lists:
    #number = i['grades']
    if sum(i['grades'])/5 >4:
        best_students.append(i['name'])
print(best_students)
    

    