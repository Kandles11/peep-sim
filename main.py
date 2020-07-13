import random, os

clear = lambda: os.system('cls')

log = open("log.txt","w+")



class Person :
    def __init__(self, firstName, lastName, age, hunger, thirst, energy, status, social):
        self.firstName= firstName
        self.lastName = lastName
        self.name = firstName + " " + lastName
        self.age = age
        self.hunger = hunger
        self.thirst = thirst
        self.energy = energy
        self.status = status
        self.social = social
        self.relationships = {

        }

people = []

firstNames = ["Mason", "Aaron", "Abel", "Jasmine", "Hunter", "Mike", "Micheal", "Carrie", "Kynlee", "Mary", "Kenneth", "Jeff", "Bob"]
lastNames = ["Thomas", "Smith", "Hubbard", "Ramsey", "Whitney", "Perez", "Hilton", "Meyer", "Boone", "Kim", "Grey", "Black", "Blue"]

def createPerson():
    people.append(Person(random.choice(firstNames), random.choice(lastNames), random.randint(10,50), 100, 100, 50, "sleep", 100))

def mainLoop():
    
    for person in people:
        if person.status == "sleep":
            person.hunger -=.5
            person.thirst -=.5
            person.energy += 3
            log.write(str(person.name + " is asleep! Energy: " + str(person.energy) + "\n"))
            if person.energy >= 90:
                person.status = "awake"
                log.write(str(person.name + " is now awake!\n"))
            continue

        person.hunger -= 1
        person.thirst -= 1
        person.social -= .5

        if person.hunger <= 30:
            eat(person)

        if person.thirst <= 50:
            drink(person)

        if person.social <= 70:
            socialize(person)

        

def eat(person):
    person.hunger += random.randint(60,70)
    log.write(str(person.name + " ate food! Hunger: " + str(person.hunger) + "\n"))

def drink(person):
    person.thirst += random.randint(30,40)
    log.write(str(person.name + " drank water! Thirst: " + str(person.thirst) + "\n"))

def socialize(person):
    socializePersonChoice = socializePersonChooser()
    log.write(str(person.name + " socialized with " + str(socializePersonChoice.name) + "! social score: " + str(person.social) + "\n"))
    person.social = 100

def socializePersonChooser():
    return random.choice(people)


def startSim():
    clear()
    for i in range(10):
        createPerson()
    for person in people:
        for personB in people:
            
        person.relationships[str(person.name)]
    for i in range(100):
        log.write(str("TIME UNIT " + str(i) + "\n"))
        mainLoop()
    for person in people:
        print(person.name, "-", "hunger:", str(person.hunger), "thirst:", str(person.thirst))


startSim()
