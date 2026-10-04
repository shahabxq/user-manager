import json
import os

if os.path.exists("data3.json"):
    with open("data3.json","r") as file:
        data=json.load(file)
else:
    data = {"users":[]}
    with open("data3.json","w") as file:
        json.dump(data,file,indent=4)


def add_user():
    while True:
        try:
            name= input ("your name: ").strip()
            if name !="":
                break
            print("name nabayad khali bashad")
        except:
            None
        
    while True:
        try:

            age = int(input("your age:  "))
            break
        except:
            print("faghat adad bede")
    new_user={"name":name, "age":age}
    data["users"].append(new_user)
    with open("data3.json","w")as file:
        json.dump(data,file,indent=4)
    print("user add!")


def show_users():
    for number,user in enumerate(data["users"],start=1):
        print(f"{number} . {user['name']} - {user ['age']} years old")


def delete_user ():
    show_users()
    while True:
        try:

            target= int (input("kodom number delete konam? "))
            if 1 <= target <= len(data["users"]):
                break
            print("in adad vojod nadarad")
        except:
            print("adad bede")
    hadaf = target -1
    data ["users"].pop (hadaf)
    with open("data3.json","w") as file:
        json.dump(data,file,indent=4)
    print( "user deleted!")


def edite_user():
    show_users()
    while True:
        try:
            add=int (input("addbede kodom "))
            if 1 <= add <= len(data["users"]):
                break
            print( 'user ba in adad vojod nadarad')
        except:
            print("faghat adad bede")
    hadaf=add-1
    new_name=input("new name? ")
    while True:
        try:
            new_age= int(input("new_age? "))
            break
        except:
            ("adad faghat")
    data["users"][hadaf]["name"]=new_name
    data["users"][hadaf]["age"]=new_age
    with open("data3.json","w") as file:
        json.dump(data,file,indent=4)
    print ("user edite shod")


def search_user():
    name = input ("search name: ")
    fund=False
    for user in data["users"]:
        if user["name"].lower()== name.lower():
            print(user)
            fund=True
    if fund == False:
        print("user peyda nashod")

while True:
    print("1.add user")
    print ("2.show users")
    print ("3.exit")
    print ("4.delete user")
    print ("5.edite")
    print ("6.search user")
    while True:
        try:
            choice= int(input("choice?: "))
            break
        except:
            print("adad vared konid")
    if choice==1:
        add_user()
    elif choice==2:
        show_users()
    elif choice==3:
        print("ok bye")
        break
    elif choice==4:
        delete_user()
    elif choice==5:
        edite_user()
    elif choice==6:
        print("ok")
        search_user()