number =int(raw_input("enter number:"))
word =str(raw_input("enter word:"))


if number == 0 or number > 1:
     print ("%s %ss." % (number,word))
else:
    print("%s %s." % (number,word))

if word[-3:] == "ife":
    print( word[:-3] + "ives")
elif word[-2:] == "sh":
    print(word[:-2] + "shes" )
elif word[-2:] == "ch":
    print(word[:-2] + "ches")
elif word[-2:] == "us":
    print(word[:-2] + "i")
elif word[-2:] == "ay":
    print(word[:-2] + "ays")
elif word[-2:] == "oy":
    print(word[:-2] + "oys")
elif word[-2:] == "ey":
    print(word[:-2] + "eys")
elif word[-2:] == "uy":
    print(word[:-2] + "uys")
elif word[-1:] == "y":
    print(word[:-1] + "ies")
else:
    print(word + "s")
