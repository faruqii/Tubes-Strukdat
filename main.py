from tqdm import tqdm
import time


class Contact:
    # Create Contact class
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.next = None

    def __str__(self):
        # Return string representation of Contact class
        return f'{self.name} {self.phone} {self.email}'


class ContactBook:

    def __init__(self):
        # Initialize ContactBook class
        self.first = None
        self.last = None
        self.size = 0

    def is_empty(self):
        return self.first is None

    def add(self, name, phone, email):
        # Add contact to ContactBook class
        contact = Contact(name, phone, email)
        if self.is_empty():
            self.first = contact
            self.last = contact
        else:
            self.last.next = contact
            self.last = contact
        self.size += 1
        print('Contact added')

    def search(self, name):
        if self.is_empty():
            print('Contact Book is empty!')
        else:
            # Prefix Search
            current = self.first
            while current:
                if name in current.name:
                    print(f'Name: {current.name} | Phone: {current.phone} | Email: {current.email}')
                current = current.next

    def remove(self, name):
        # Remove contact from ContactBook class
        current = self.first
        previous = None
        while current:
            if current.name == name:
                if previous:
                    previous.next = current.next
                else:
                    self.first = current.next
                self.size -= 1
                return True
            previous = current
            current = current.next
        return False

    def show_book(self):
        # Print all contacts in ContactBook class
        if self.is_empty():
            print('CONTACT BOOK IS EMPTY')
        else:
            current = self.first
            index = 0
            while current:
                index += 1
                print(f'{index}. Name: {current.name} | Phone: {current.phone} | Email: {current.email}')
                current = current.next

    def run(self):
        while True:
            print('\n========= Menu =========')
            print('1. Add Contact')
            print('2. Search Contact')
            print('3. Remove Contact')
            print('4. Print Contacts')
            print('6. Exit')
            option = int(input('\nSelect an option: '))
            if option == 1:
                name, phone, email = input('\nEnter name, phone and email: ').split(',')
                self.add(name, int(phone), email)
            elif option == 2:
                name = input('Name: ')
                for _ in tqdm(range(101),
                              desc="Searching………",
                              ascii=False, ncols=75):
                    time.sleep(0.01)
                print(f'\nname with {name} found in contact book!\nHere the contact details:')
                self.search(name)
            elif option == 3:
                name = input('Enter Name to search: ')
                auth = input(f'Are you sure you want to remove {name} from contact book? (y/n): ')
                if auth == 'y':
                    if self.remove(name):
                        print('Contact removed')
                    else:
                        print('Contact not found')
                else:
                    print('Contact not removed')
            elif option == 4:
                print()
                print('============ Contact Book  ============')
                self.show_book()
                print('=======================================')
            elif option == 6:
                break
            else:
                print('Invalid option')


class User:

    def __init__(self):
        self.username = "Faruqi"
        self.password = 1202204105

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password


if __name__ == '__main__':
    print('Login First!')
    user = User()
    username = input('Username: ')
    password = int(input('Password: '))
    if username.__eq__(user.get_username()) and password.__eq__(user.get_password()):
        print('Login Successful!')
        contact_book = ContactBook()
        contact_book.run()
    else:
        print('Login Failed!')
