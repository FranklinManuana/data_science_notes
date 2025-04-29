def instructorWithLongestName(instructors):
    longest_name = ""
    for i in range(len(instructors)):
        if len(instructors[i].get("name")) > len(longest_name):
            longest_name = instructors[i].get("name")
            longest= i 
    return instructors[longest]
   
  
  
print(instructorWithLongestName([
  {"name": "Samuel", "course": "iOS"},
  {"name": "Jeremiah", "course": "Data"},
  {"name": "Ophilia", "course": "Web"},
  {"name": "Donald", "course": "Web"}
]))
