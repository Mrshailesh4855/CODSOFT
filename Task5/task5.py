contacts=[]
def menu():
    print("1.View Contacts")
    print("2.Add Contact")
    print("3.Search Contact")
    print("4.Update Contact")
    print("5.Delete Contact")
    print("6.Exit")
def view_contacts():
    if len(contacts)==0:
        print("No contacts found.")
        return
    for i,c in enumerate(contacts,1):
        print(i,c["name"],"|",c["phone"])
def add_contact():
    name=input("Name:")
    phone=input("Phone:")
    email=input("Email:")
    address=input("Address:")
    contacts.append({"name":name,"phone":phone,"email":email,"address":address})
    print("Added.")
def search_contact():
    q=input("Search:").lower()
    f=False
    for i,c in enumerate(contacts,1):
        if q in c["name"].lower() or q in c["phone"].lower():
            print(i,c["name"],"|",c["phone"])
            f=True
    if not f:
        print("No match.")
def update_contact():
    view_contacts()
    if len(contacts)==0:
        return
    n=int(input("Number:"))
    if n<1 or n>len(contacts):
        print("Invalid.")
        return
    c=contacts[n-1]
    name=input("New Name:")
    phone=input("New Phone:")
    email=input("New Email:")
    address=input("New Address:")
    if name:c["name"]=name
    if phone:c["phone"]=phone
    if email:c["email"]=email
    if address:c["address"]=address
    print("Updated.")
def delete_contact():
    view_contacts()
    if len(contacts)==0:
        return
    n=int(input("Number:"))
    if n<1 or n>len(contacts):
        print("Invalid.")
        return
    contacts.pop(n-1)
    print("Deleted.")
while True:
    menu()
    ch=input("Choose:")
    if ch=="1":view_contacts()
    elif ch=="2":add_contact()
    elif ch=="3":search_contact()
    elif ch=="4":update_contact()
    elif ch=="5":delete_contact()
    elif ch=="6":
        print("Bye")
        break
    else:
        print("Invalid")
