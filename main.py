from DBmanager import DBManager

def main():

    db = DBManager()
    while True:
        print("---------Welcome---------")
        print()
        print("Press 1 to insert new user")
        print("Press 2 to display all user")
        print("Press 3 to delete user by user ID")
        print("Press 4 to update user by user ID")
        print("Press 5 to exit program")
        print()

        try:
            choice = int(input())
            if choice == 1:
                #insert user
                uID = int(input("Enter user ID: "))
                userName = input("Enter user's First Name or Full Name: ")
                phone = input("Enter user's phone number: ")
                db.insert_user(uID, userName, phone)
            elif choice == 2:
                #display
                db.select_all()
            elif choice == 3:
                #delete
                uID = int(input("Enter user ID to delete: "))                
                db.delete_by_id(uID)
            elif choice == 4:
                #update
                uID = int(input("Enter user ID: "))
                userName = input("Enter user's new Name: ")
                phone = input("Enter user's new phone number: ")
                db.update_by_id(uID, userName, phone)
            elif choice == 5:
                break
            else:
                print("Invalid Input. Try again")
        except Exception as e:
            print(e)
            print("Error. Try again")


if __name__ == "__main__":
    main()