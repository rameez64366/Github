# names=["Alex","Eleanor","Beth","Rameez", "Kevin"]
# import random
#
# student_scores={name:random.randint(1,100) for name in names}
# print(student_scores)
#
#
# passed_students={name:student_scores[name] for name in student_scores if student_scores[name]>50}
#
# print(passed_students)

# import pandas
# classroom={
#     "student":["angela","rameez","pathu","cello","kevin"],
#     "scores":[80,60,50,66,56]
# }
#
# classroom_proper=pandas.DataFrame(classroom)
# print(classroom_proper)
# for (index,row) in classroom_proper.iterrows():
#     if row.scores==66:
#         print(row.student)
import random

def driving(age:int)->bool:
    if age>18:
        can_drive=True
    else:
        can_drive=False
    return can_drive

driving(21)







































