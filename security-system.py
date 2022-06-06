#Security System of Organisation
#Groups with different security access:
#   - Intern
#   - Cyber Security
#   - Admin
#Student = No access
#Cyber Security = Access with Limitation
#Admin = Full Security Access
#_______________________________________#

#Display Message
print("Welcome to Security System Acess\nPlease answer all questions to access Security System\n")
input("Press Enter to begin")

#Ask user which group
print("There are three groups: Intern, Cyber Security, Admin")
group = input("Please enter the group you are in: ")

#Check if group is not equal to Student, Cyber Security or Admin
if(group != "Intern" and group != "Cyber Security" and group != "Admin"):
    #Display Security Breach
    print("Security Breach")
else:
    if(group == "Intern"):
        print("You have no access to Security System!")
    if(group == "Cyber Security"):
        print("You have Access to Security System with some limitation!")
    if(group == "Admin"):
        print("You have full Access to Security System!")