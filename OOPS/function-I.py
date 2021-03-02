#Function to take input marks of students in list ‘marksList’ with total strength ‘numStudent’
def inputMarks(numStudent):
    marksList=list() 
    for i in range(numStudent):
        m1=int(input("Enter marks for student "+str(i+1)+":"))      #EDIT converted the input to integer
        marksList.append(m1)        # Statement 1 : Appending marks for each student in subject marks list
    return marksList


#Function to validate the input marks i.e. marks should be between 0 to 100.
#returns TRUE if list of marks is valid otherwise returns FALSE
def validateMarks(marks):
	for i in marks: # Traverse each element 
		if not isinstance(i,(int,float)) or i < 0 or i > 100:    # Statement 2 : Checking if entered marks are in float and int type and within range 0 to 100
			return False
	return True

#Main Script
TotalMarks=[]
numStudent=int(input("Enter Total Number of students:"))
print("Enter Marks for 1st subject")
marks1=inputMarks(numStudent)
print("Enter Marks for 2nd subject")
marks2=inputMarks(numStudent)

if not validateMarks(marks1) or not validateMarks(marks2):   # Statement 3 : Validating the marks for both subjects
	print("Invalid Marks")
else: 
    for i in range(numStudent):                      # Statement 4 : for num of students traversing on all marks
        TotalMarks.append(marks1[i] + marks2[i])     # Statement 5 : adding both the subject marks and appending them to TotalMarks

print(TotalMarks)