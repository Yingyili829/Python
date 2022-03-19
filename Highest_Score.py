#for loop
#max()





student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)


#Write your code below this row 👇

#method_1
#print(max(student_scores))

#method_2
highest_score=0
for score in student_scores:
    if score >= highest_score:
        highest_score =score
print(f"the highest score is : {highest_score}")