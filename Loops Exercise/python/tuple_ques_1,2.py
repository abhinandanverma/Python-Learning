# #Q1.
# student=[]
# stu1=input("Enter the student 1:")
# stu2=input("Enter the student 2:")
# stu3=input("Enter the student 3:")
# student.append(stu1)
# student.append(stu2)
# student.append(stu3)
# print(student)

# Q2.
list=[1,2,1]
#list=[1,2,3]
copy_list=list.copy()
copy_list.reverse()
if(copy_list==list):
    print("palindrome")
else:
    print("not palindrome")    

#Q3.
garde=("A","B","A","B","c","A")
print(garde.count("A"))