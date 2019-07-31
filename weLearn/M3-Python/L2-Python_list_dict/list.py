students = ["Alice", "Javi", "Damien "]
students.append("Delilah")
print(students)

students = ["Alice", "Javi","Damien"]
students.insert(1, "Zoe")
print(students)

students = ["Alice", "Javi", "Damien", "Javi"]
students.remove("Javi")
print(students, "\r\n")

smith_siblings = ["Emily", "Monique","Giovanni", "Brianna", "javi", "Peter Griffin","Sans Undertale \r\n"]
for name in smith_siblings:
    print(name + " Smith")

smith_siblings = ["Emily", "Monique","Giovanni", "Brianna", "javi", "Peter Griffin","Sans Undertale \r\n"]
for index in range(len(smith_siblings)):
    smith_siblings[index] = smith_siblings[index] + " Smith"
print(smith_siblings)

#superheroes = ["Captain", "Wonder Woman", "Storm", "Kamala Khan", "BumbleBee", "Jessica Jones"]
#demoted_hero = str(raw_input("What superhero do you want to eliminate from the top 5?"))
#if demoted_hero in superheroes:
    #superheroes.remove(demoted_hero)
    #print("Top 5 heroes:", superheroes)
#else:
    #print("Hero not found.")

names = ["Rickon", "Bran", "Arya", "Sans", "Jon", "Robb"]
print(names[::-1])
print(names[4:2:-1])

states ={"NY": "New York","CA": "California", "TX": "Texas"}
for abbreviation in states:
    print(abbreviation + " is short for " + states[abbreviation])
