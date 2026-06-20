#Contact Book
#created by Sathish Kumar
contacts = {}

while True:
    print("\n1.Add Contact")
    print("2.View Contact")
    print("3.Search Contacts")
    print("4.Delete Contact")
    print("5.Exit")

    choice = int(input("Enter your Choice: "))

    if choice == 1:
        name = input("Enter name: ")
        number = input("Enter number: ")
        contacts[name] = number
        print("Contact Added!")

    elif choice == 2:
        for name, number in contacts.items():
            print(name, ":", number)

    elif choice == 3:
        name = input("Enter name to search: ")
        if name in contacts:
            print(name, ":", contacts[name])
        else:
            print("COntact Not Found!")

    elif choice == 4:
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact Deleted!")

    elif choice == 5:
        print("Good Bye!")
        break
    
    else:
        print("Invalid choice!")

