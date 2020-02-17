import main

while 1:
    print("\n\n\n")
    print("*---"*20)
    print("\t\t\t\t\t\t\tMain Menu")
    print("*---"*20)
    print("\n\n")

    print("\t\t\t1.New Site\n")
    print("\t\t\t2.Update\n")
    print("\t\t\t9.Exit\n")

    choice = input("\tEnter your choice =>\t")

    if choice == '1':
        p=main.main()

    elif choice == '2':
        print("This feature is under development\nTry again later")

    elif choice == '9':
        exit(1)
