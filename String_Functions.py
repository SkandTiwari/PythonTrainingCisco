'''There are various function s for string manupulation, Some of the results with examples are given below'''


course = "Network Automation"


print(f'The {course} network automation is cool!') #fstring or format string

print(course.upper())  #upper and lowe case conversion
print(course.lower())


tempstr = course.find('N')  ##find() returns index of a number
print(tempstr)

print("Network" in course) #returns a boolean value wether string      patten exist in the given string



temp = "I love scripting"
print(temp.replace('l', 'a')) #replaces the 'l' with 'o'

print(temp.replace("love", "hate"))  #string replacement

