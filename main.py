

num_list = [1,2,3,4,5]
even_list = [n*2 for n in num_list]
print(num_list)

print(even_list)

letter_list = [l for l in "name"]

name = "Chitra"
letter_list=[ l for l in name]


n_list = [n for n in range(1,5)]
n_list = [n for n in range(1,5) if n/2 ==0]
n_list = [n for n in range(1,5) if n>3]
n_list = [n for n in range(1,5) if n%2==0]
sq_list=[n*n for n in range(1,10)]
sq_list=[n*n for n in range(1,10) if n%2==0]
#new_dict = {key:value for (key, value) in dict.items()}

names=["chitra","Ritwik","Sridhar"]
import random
student_score_dict = {student:random.randint(1,100) for student in names}

passed_student = {k:v for (k,v) in student_score_dict.items() if v>70}
import pandas
student_score_dataframe = pandas.DataFrame(
    list(student_score_dict.items()),
    columns=["Student", "Score"])
print(student_score_dataframe)
for (index,row) in student_score_dataframe.iterrows():
    print(row["Score"])
    print(row["Student"])

