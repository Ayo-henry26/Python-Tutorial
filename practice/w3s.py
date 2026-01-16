#Accessing the list
fruits = ["apple", "mango", "banana", "kiwi", "cherry"]
print(fruits[4], "\n")
print(fruits[-3:-1], "")
for fruit in fruits:
    print(fruit)
#Changing the list
newlist = ["red", "gold", "yellow", "green", "blue", "violet"]
print(newlist)
newlist[1] = "orange"
print(newlist)
#To insert new item
newlist.insert(5, "indigo")
print(newlist)
#To append an new item at the end of the list
newlist.append("cyan")
print(newlist)
#To add a list to another list using extend
thislist = ["black", "white", "grey"]
newlist.extend(thislist)
print(newlist)
print(thislist)
#To remove an item from the list using it value
newlist.remove("cyan")
print(newlist)
#To remove item using index number
newlist.pop(9)
print(newlist)
#To delete the list
del thislist
#To clear the entire list
newlist.clear()
print(newlist)

#TUPLES
colors = ("red", "orange", "yellow", "green", "blue")
print(colors[0:5])
if "red" in colors:
    print("It is a primary color")
 
#This is called unpacking a tuple
(strawberry, *banana, blueberry) = colors
print(strawberry)
print(banana)
print(blueberry)
#way of adding an item to a tuple without converting to a list
color = ("indigo","violet")
colors += color
print(colors)

#numbers = [1, 2, 3, 4, 5]
#square_num = []
#for z in numbers:
#    square_num.append(z ** 2)
#print(square_num)

#JOINING IN TUPLE
tuple1 = ("apple", "banana")
tuple2 = ("cherry", "durian")
tuple3 = tuple1 + tuple2
print(tuple3)
tuple4 = tuple3 * 2
print(tuple4)
    
num5 = [100, 75, 50, 25]        
num5.sort()
print(num5)             
num6 = [x for x in num5 if x ==100]
print(num6)
#Using the dict() constructor
thisdict1 = dict(name = "Henry", age = 20, country = "Japan")
print(thisdict1)

thisdict = {
    "name": "Ayo",
    "age": 20,
    "year": 1995
}
print(thisdict)
print(thisdict.get("name"))
#Adding items
thisdict["gender"] = "male"
#Changing items
print(thisdict.update({"year" : 2005}))
if "year" in thisdict:
    print("You are verified")
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())
#Removing Items
thisdict.pop("year")
print(thisdict)

thisdict.popitem()
print(thisdict)

#del thisdict1["name"]
del thisdict1
thisdict.clear()
print(thisdict)

#Looping Through a Dictionary
school = {
"name" : "Havard",
"location" : "USA",
"status" : "Best",
"tuition" : "100000"
}
#To print the KEYS
for k in school:
#OR
#for k in school.keys():
    print(k)
#To print the VALUES
for k in school:
#OR
#for k in school.values():
    print(school[k])

for m, n in school.items():
    print(m, " : ", n)

#Copying a Dictionary
uni = school.copy()
print(uni)
#OR
ver = dict(school)
print(ver)

#Nested Dictionaries
family = {
    "father" : {
        "name" : "Henry",
        "month" : "January"
    },
    "mother" : {
        "name" : "Funmilayo",
        "month" : "May"
    },
    "sister" : {
        "name" : "Blessing",
        "month" : "September"
    }
}
print(family)
#OR
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)
print(myfamily["child1"]["name"])

#Looping through a nested dictionary
for x, obj in family.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y],)
        
        
print("\n")        
#IF, ELSE, AND ELIF STATEMENTS
a = 40
b = 50
if a > b:
    print("That's why I come first")
elif a == b:
    print("We are the same")    
else:
    print("I am bigger than you")    
    
#SHORT HAND IF AND IF....ELSE
#Ternary Operators OR Conditonal Expression
r = 9
t = 10
if r > t: print("Nice")
print("r > t") if r > t else print("r < t")
#It can have multiple else statement
#print("r > t") if r > t else print("r = t") if r == t else print("r < t")
    
#USING THE AND, NOT, and OR LOGICAL OPERATORS 
#AND Keyword
x, y, z = 10, 30, 20
if x < y and y > z:
    print("I am the largest")
    
#OR Keyword
if x < y or y < z:
    print("z is not bigger than me")    
    
#NOT Keyword
if not x > y:
  print("x is too small for me")   

c = 20
if c > 18:
    print("I am above18")
    if c > 20:
        print("I am above 20")
    else:
        print("I am 20")

#USING THE PASS STATEMENT
#it help prevent an error when you have an empty if statement
g = 10
h =11
if g < h:
    pass

#MATCH STATEMENT
day = 9
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")    
    case 4:
        print("Thursday")       
    case 5:
        print("Friday")            
    case 6:
        print("Saturday")               
    case 7:
        print("Sunday")                   
    #For default case
    case _:
        print("It's almost a new week")                
            
#Combined Match Values
days = 3
match days:
    case 1 | 2 | 3 | 4 | 5:
        print("Today's a week day")                                    
    case 6 | 7:
        print("It's Weekend")                        
                                    
#Using match Stastement with if Statement
months = 5
nights = 4
match nights:
     case 1 | 2 | 3 | 4 | 5 if months == 4:
           print("A week day in April")     
     case 1 | 2 | 3 | 4 | 5 if months == 5:
           print("A week day in May")
     case _:
           print("No Match")
           
#WHILE LOOPS 
i = 1
while i < 6:
    print(i)
    i += 1
#Using BREAK STATEMENT
i = 0
while i < 6:
    print(i)  
    if i == 3:
        break
    i += 1
print("\n")    
#Using CONTINUE STATEMENT
i = 0
while i < 5:
    i += 1
    if i % 2 != 0:
        continue
    print(f"The even numbers: {i}")

#FOR LOOPS AND BREAK STATEMENT
faculties = ["CIS", "Art", "Vet", "Pharm"]
#Exiting the loop when the PRINT is a before the IF
for x in faculties:
    print(x)
    if x == "Vet":
        break
print("\n")
#Exiting the loop when the IF is before the PRINT
for x in faculties:
    if x == "Vet":
        break
    print(x)
print("\n")
#FOR LOOPS AND CONTINUE STATEMENT
for x in faculties:
    if x == "Art":
        continue
    print(x)

for x in range(len(faculties)):
    print(x)
#range(start, end, steps)
#FOR LOOP AND ELSE STATEMENT
for y in range(6):
    print(y)
else:
    print("Finally Done")

school = ["unilorin", "unilag", "ui"]
faculty = ["art", "science", "engineeering"]
for x in school:
    for y in faculty:
        print(x, ":", y)
#For loop can also use the pass statement if empty

