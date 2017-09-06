
def names(users):
    print "Students"
    for b in range(0, len(users["Students"])):
        name = " ".join(users["Students"][b].values())
        print b+1, "-", name.upper(), "-", len(name)-1
    print "Instructors"
    for j in range(0, len(users["Instructors"])):
        name = " ".join(users["Instructors"][j].values())
        print j+1, "-", name.upper(), "-", len(name)-1
users = {
    "Students": [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    "Instructors": [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}

names(users)
