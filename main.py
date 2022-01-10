from tqdm import tqdm
import time
import sys


class Contact:
    # Contact has attributes name, phone, and email
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.next = None

    def __str__(self):
        # Return string representation of Contact class
        return f'{self.name} {self.phone} {self.email}'


class ContactApp:
    # Application is CRUD app allow user to add contact, read contact, update contact, and delete contact.
    def __init__(self, head=None, tail=None, size=0):
        self.head = head  # head is the first node of the linked list
        self.tail = tail  # tail is the last node of the linked list
        self.size = size  # size is the number of nodes in the linked list

    def is_empty(self):
        # This Function is use for check if linked list is empty
        return self.head is None

    def add(self, name, phone, email):
        # Add contact to ContactBook class
        contact = Contact(name, phone, email)
        if self.is_empty():
            self.head = contact  # If linked list is empty, head and tail will be the same
            self.tail = contact
        else:
            self.tail.next = contact  # If linked list is not empty, tail will be the new node
            self.tail = contact 
        self.size += 1  # Increase size by 1
        print('Contact added')

    def search(self, name):
        # Search name in contact book
        if self.is_empty():
            print('Contact Book is empty!')
        else:
            # Prefix Search
            current = self.head 
            while current:
                if name in current.name: 
                    print(f'Name: {current.name} | Phone: {current.phone} | Email: {current.email}')
                current = current.next

    def remove(self, name):
        # Remove contact from ContactBook class
        if self.is_empty():
            print('Contact Book is empty!')
        current = self.head
        previous = None
        while current:
            if current.name == name: 
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                self.size -= 1
                return True
            previous = current
            current = current.next
        return False

    def update_contact(self, name):
        # Update contact in Contact Book class
        current = self.head
        while current:
            if current.name == name: 
                updated_name, updated_phone, updated_email = input('\nEnter name, phone and email: ').split(',')
                current.name = updated_name
                current.phone = updated_phone
                current.email = updated_email
                return True
            current = current.next
        return False

    def merge(self, head1, head2):
        # Merge two sorted linked list
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        if head1.name < head2.name:
            head1.next = self.merge(head1.next, head2)
            return head1
        else:
            head2.next = self.merge(head1, head2.next)
            return head2

    def merge_sort(self, head):
        # Merge Sort
        # Contact Book should be ascending order
        if head is None or head.next is None:
            return head
        middle = self.get_middle(head)
        next_of_middle = middle.next
        middle.next = None
        left = self.merge_sort(head)
        right = self.merge_sort(next_of_middle)
        sorted_list = self.merge(left, right)
        return sorted_list

    def get_middle(self, head):
        # Get middle node of linked list
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def show_book(self):
        # Print all contacts in ContactBook class
        if self.is_empty():
            print('\t\t\t\t\tCONTACT BOOK IS EMPTY')
        else:
            current = self.merge_sort(self.head)
            index = 0
            while current:
                index += 1
                print(f'{index}. Name: {current.name} | Phone: {current.phone} | Email: {current.email}')
                current = current.next

    def run(self):
        # Run the Application
        while True:
            print('\n========= Menu =========')
            print('1. Add Contact')
            print('2. Search Contact')
            print('3. Remove Contact')
            print('4. Update Contact')
            print('5. Print Contacts')
            print('0. Exit')
            option = int(input('\nSelect an option: '))
            if option == 1:
                name, phone, email = input('\nEnter name, phone and email: ').split(',')
                self.add(name, phone, email)
            elif option == 2:
                name = input('Enter Name to Search: ')
                for _ in tqdm(range(101),
                              desc="Searching Contact………",
                              ascii=False, ncols=75):
                    time.sleep(0.01)
                print(f'\nName with {name} found in contact book!\nHere the contact details:')
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
                name = input('Enter Name to Update: ')
                if self.update_contact(name):
                    print('Contact updated')
                else:
                    print('Contact not found')
            elif option == 5:
                print()
                print('======================== Contact Book  ========================')
                self.show_book()
                print('===============================================================')
            elif option == 0:
                print('Thank You!')
                sys.exit(0)
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
    # This is Where Code is Running
    number_of_attempts = 3
    attempts = 0
    login_success = False
    for _ in range(number_of_attempts):
        print('=========== Contact Book Application ===========')
        print('Login First!')
        user = User()
        try:
            username = input('Username: ')
            password = int(input('Password: '))
            if username.__eq__(user.get_username()) and password.__eq__(user.get_password()):
                # __eq__() is same as .equals() in java
                user_auth = input('Are You Sure To Login? (Y/N): ')
                if user_auth == 'Y':
                    print('Login Successful!')
                    login_success = True
                    contact_book = ContactApp()
                    contact_book.run()
                elif user_auth == 'N':
                    print('Thank You!')
                    break
                else:
                    print('Invalid Choice!')
            else:
                attempts += 1
                if number_of_attempts - attempts != 0:
                    print(f'Login Failed! You Have Login {number_of_attempts - attempts} Attempt Remaining!\n')
        except ValueError:
            print('Password Must be Integer!!')
            print('Login Again!\n')
    if login_success is False and number_of_attempts == attempts:
        print('You Have Reached Maximum of Login Attempt!')
