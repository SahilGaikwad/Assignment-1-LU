#Assignment 1 -LU
Name="Sahil Gaikwad"
age =19 
Branch="computer Enginerring"
college_name ="PHCET"
sem = 3
Subject =["EM-3","CG","DS","DLCOA","DSGT","JAVA"]
marks=91.67

print("My name is %s i am %s year old pursuing %s at %s,My subject for sem: %s are %s and i secured %s"\
    %(Name,age,Branch,college_name,sem,Subject,marks))

print("My name is {} i am {} year old pursuing {} at {},My subject for sem: {} are {} and i secured {}"\
    .format(Name,age,Branch,college_name,sem,Subject,marks))

print("My name is {5} i am {6} year old pursuing {0} at {1},My subject for sem: {2} are {3} and i secured {4}"\
    .format(Branch,college_name,sem,Subject,marks,Name,age))

print(f"My name is {Name} i am {age} year old pursuing {Branch} at {college_name},\
My subject for sem: {sem} are {Subject} and i secured {marks}")


