# 📘 Dynamic Contact Book Using Dictionaries

def is_valid_email(email):
    """Check if the email contains '@' and '.'"""
    return '@' in email and '.' in email

def display_menu():
    print("\n Contact Book Menu")
    print("1. Add New Contact")
    print("2. Update Existing Contact")
    print("3. Retrieve Contact Details")
    print("4. View All Contacts")
    print("5. Exit")

def add_contact(contact_book):
    name = input("Enter contact name: ").title()
    if name in contact_book:
        print(" Contact already exists.")
        return
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    if not is_valid_email(email):
        print(" Invalid email format.")
        return
    contact_book[name] = {"phone": phone, "email": email}
    print(" Contact added successfully.")

def update_contact(contact_book):
    name = input("Enter contact name to update: ").title()
    if name not in contact_book:
        print(" Contact not found.")
        return
    phone = input("Enter new phone number (or press Enter to skip): ")
    email = input("Enter new email (or press Enter to skip): ")

    if phone:
        contact_book[name]["phone"] = phone
    if email:
        if not is_valid_email(email):
            print(" Invalid email format.")
            return
        contact_book[name]["email"] = email

    print(" Contact updated successfully.")

def retrieve_contact(contact_book):
    name = input("Enter contact name to retrieve: ").title()
    if name in contact_book:
        info = contact_book[name]
        print(f" Name: {name}")
        print(f" Phone: {info['phone']}")
        print(f" Email: {info['email']}")
    else:
        print(" Contact not found.")

def view_all_contacts(contact_book):
    if not contact_book:
        print(" No contacts to display.")
        return
    print("\n All Contacts:")
    for name, info in contact_book.items():
        print(f" {name} - {info['phone']},  {info['email']}")

# Main loop
def contact_book_manager():
    contact_book = {
        "Ali": {"phone": "123", "email": "ali@email.com"},
        "Sara": {"phone": "999", "email": "sara@email.com"}
    }

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_contact(contact_book)
        elif choice == "2":
            update_contact(contact_book)
        elif choice == "3":
            retrieve_contact(contact_book)
        elif choice == "4":
            view_all_contacts(contact_book)
        elif choice == "5":
            print(" Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the program
contact_book_manager()

