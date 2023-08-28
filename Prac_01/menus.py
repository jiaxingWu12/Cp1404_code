name = input("Enter name:")
choice = input(">>> ").upper()
while choice != "Q":
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

    if choice == 'H':
        print("Hello", name)
    elif choice == 'G':
        print("Goodbye", name)
    else:
        print("Invalid choice")
    choice = input(">>> ").upper()
print("End")



