set1 = {"delhi", 'gurgaon', 'gujarat', 'mumbai', 'delhi', 'gurgaon', 'odissa', 'mumbai'}

#ADD
set1.add("smh")
print(set1)

#REMOVE or DISCARD
#DISCARD BECAUSE IT'S MORE SECURE
set1.remove("smh")
print(set1)
set1.discard("odissa")
print(set1)

#COPY
set2 = set1.copy()
print(set2==set1)
print(set2 is set1)

#CLEAR
set2.clear()
print(set2)

#SETMATH
math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}
combine = math_students|biology_students
print(combine)
common = math_students & biology_students
print(common)