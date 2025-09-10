def menu_driven():
    items = ["phone", "tab", "laptop"]
    while True:
        print("\nMenu:")
        print("1. Add")
        print("2. Remove")
        print("3. Search")
        print("4. Display")
        print("5. Display number of items")
        print("6. Sort")
        print("7.Clear")
        print("8.exit")
        choice = int(input())
        if choice == 1:
            new= input()
            items.append(new)
        elif choice == 2:
            remove = input()
            if remove in items:
                items.remove(remove)
            else:
                print("Element not found")
        elif choice == 3:
            search = input()
            if search in items:
                print("Element found")
            else:
                print("Element not found")
        elif choice == 4:
            print(items)
        elif choice == 5:
            print(len(items))
        elif choice == 6:
            items.sort()
            print(items)
        elif choice==7:
            items.clear()
            print(items)
        elif choice==8:
            print("Invalid choice.")
        break
menu_driven()
