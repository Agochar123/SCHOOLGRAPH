import matplotlib.pyplot as plt
classes=[1,2,3,4,5,6,7,8,9,10]
no_of_students=[60,65,60,50,55,40,30,35,40,40]
plt.xlabel("GRADES")
plt.ylabel("NUMBER OF STUDENTS ENROLLED")
plt.title("STUDENTS ENROLLED IN DIFFERENT CLASSES")
plt.bar(classes,no_of_students,color="maroon")
plt.show()
