# Public APIs

## Create a phone book

```python
from addressbook.addressbook import AddressBook
phoneBook = AddressBook()
```

Creates and returns an instance of phone book

## Add a person to the address book

```python
person = phoneBook.addPerson(firstName, lastName, emailAddresses, phoneNumbers)
```

- firstName - First name of the person (a string)
- lastName - Last name of the person (a string)
- emailAddresses - List of strings of email address (list of non empty strings)
- phoneNumbers - List of strings of phone numbers (list of strings)

phoneBook's addPerson method creates a person

> Please note that First name and Last name are together treated as a unique key, hence the system will not allow
> the user to create another person with same First and Last name.

> Exceptions are thrown if email addresses or phone numbers are not list.
> Exceptions are thrown if email addresses is empty string

returns a dictionary of the person.

## Add a group to address book

```python
group = phoneBook.addGroup(groupName)
```

- groupName - Name of the group to be created (a string)

phoneBook's addGroup method creates a group

returns the string if successfully created else throws an exception

## Add a person to group

```python
membership = phoneBook.addMember(groupName, personFirstName, personLastName)
```

- groupName - Name of the group to be created (string)
- personFirstName - First name of the person (string)
- personLastName - Last name of the person (string)

phoneBook's addMember method creates a membership for the person

returns False if group or person does not exist else True after the membership is saved

## Get list of person in a group

```python
people = phoneBook.getGroupMembers(groupName)
```

- groupName - Name of the group (string)

phoneBook's getGroupMembers returns a list of dictionary of people. It returns None if the group name is invalid


## Get list of groups for a person

```python
groups = phoneBook.getGroupMembers(firstName, lastName)
```

- firstName - First name of the person (string)
- lastName - Last name of the person (string)

phoneBook's getGroupMembers returns a list of dictionary of groups. It returns None if the person's first and last name is invalid


## Get list of person by name (first name or last name or both)

```python
people = phoneBook.findPersonByName(**kwargs)
```

phoneBook's findPersonByName expects named parameters. They can take `firstName` or `lastName` or (`firstName` and `lastName`) as the parameters

- firstName - First name of the person (string)
- lastName - Last name of the person (string)

phoneBook's findPersonByName returns a list of people. It returns None if an invalid parameter is passed

## Get list of person by prefix or complete email address

```python
people = phoneBook.findPersonByEmail(email)
```

- email - Email of the people (string or prefix string)

phoneBook's findPersonByName returns a list of people who have been using the mentioned email or prefix email.


# Design to find person by email address

Let me take an example to explain my design approach. Given an email address like: 'romaank@company.com', I start by reading each character in the reverse order.

Hence I read the character as following:

```python
['m','o','c','.','l','i', ...... 'o', 'r']
```

Now the 'm' first character is inserted into my m-array. And m-array looks like the following:

> [] -> [m]

After reading the second character, I create an index entry for 'om' , and my index n-array will contain

> [] -> [m (FirstLastName), o -> [m (FirstLastName)] ]

Again, I read the third element 'c' and I create an index entry for 'com' and my index n-array will contain

> [] -> [m (FirstLastName), o -> [m (FirstLastName)], [c -> [o -> [m (FirstLastName)]]]

Like wise I create the index while reading backwards for every element.

While retriving the data if user searces for string, say, 'com' or 'compan', we search searching from the root node and traverse to a node that contains 'com' or 'compan' and then read all the subnodes for the values under the traversed node.

# Directory structure

The directory is organised as follows:

- addressbook = Contains the source code
- tests = Contains all the test cases
- requirements.txt = Contains the package names that needs to be installed
- LICENSE = Declaration that this is unlicensed
- README.md = This file that explains the APIs, directory structure and design approach for the asked question, how do I implement an efficient search to match a substring in the given list of strings
- setup.sh = Run the file to setup the project

# Run tests

```sh
python -m unittest discover tests # Assuming you are in the parent of tests directory
```

# Setup the project

- Clone the repository
- Ensure your present working directory has setup.sh and you have executable permission
- Run ./setup.sh