from bottle import get,run,post,request,delete

peopleNames = [{'name':'OnurCan' , 'surname' : 'Yucedag','age':'20'},
           {'name': 'Ali', 'surname': 'Avci','age':'21'},
           {'name': 'Sevgi', 'surname': 'Cetin','age':'21'}]

@get(' /people')
def getAll():
    return {'people' : peopleNames}

@get('/people/<name>')
def getOne(name):
    the_name = [person for person in peopleNames if person['name'] == name]
    return {'person' : the_name[0]}

@post('/people/')
def addOne():
    new_person = {'name' : request.json.get('name'),
                  'surname' : request.json.get('surname'),
                  'age' : request.json.get('age')}
    peopleNames.append(new_person)
    return {'people' : peopleNames}
@delete('/people/<name>')
def deleteOne(name):
    deleted_person = [person for person in peopleNames if person['name'] == name] #Searching for name.
    peopleNames.remove(deleted_person[0])
    return {'people' : peopleNames}

run(reloader=True, debug= True)