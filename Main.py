Attendance=int(input("How many days did you attend Classes:"))
if Attendance>=75:
    print("You are allowed to take the exams")
else:
    Medicalcause=input("Were you sick?:")
    if Medicalcause==("Yes" or "yes" or "YES"):
        print("You can take exams")
    else:
        print("You are not allowed to take exams")