from groups import Groups
from people import People
from members import Members


class AddressBook(object):

    """
    Address Book containing people, groups and members
    It offers APIs for storing, retreiving and searching people and groups
    """

    def __init__(self):
        self._people = People()
        self._groups = Groups()
        self._members = Members(self._people, self._groups)

    def addPerson(self, firstName, lastName, emailAddresses, phoneNumbers):
        """
        Add person to phone book
        :param firstName: First name of the person
        :param lastName: Last name of the person
        :param emailAddresses: List of email addresses
        :param phoneNumbers: List of phone numbers
        :return: A dictionary of person
        :exception If the person with same first name and last name already exists
        :exception If the email and phone number is not a list
        """
        return self._people.addPerson(firstName, lastName, emailAddresses, phoneNumbers)

    def addGroup(self, name):
        """
        Add group to address book
        :param name: Name of the group
        :return: Name of the group
        :exception: if the group already exists
        """
        return self._groups.addGroup(name)

    def addMember(self, groupName, personFirstName, personLastName):
        """
        Add a person to group
        :param groupName: Group name
        :param personFirstName: First name of person
        :param personLastName: Last name of person
        :return: True if saved, Flase otherwise
        """
        return self._members.addMember(groupName, personFirstName, personLastName)

    def getGroupMembers(self, groupName):
        """
        Get the list of group members
        :param groupName: Name of the group
        :return: None if invalid group, else list of people in the group
        """
        group = self._groups.getGroup(groupName)
        if group:
            peopleKeys = self._members.findPeople(group)
            people = []
            for person in peopleKeys:
                people.append(self._people.findPerson(person))
            return people
        return None

    def getGroups(self, firstName, lastName):
        """
        Get the list of groups
        :param firstName: First name of the person
        :param lastName: Last name of the person
        :return: List of group names else None if person does not exist
        """
        person = self._people.findPerson(firstName + lastName)
        if person:
            group = self._members.findGroups(person['firstName'] + person['lastName'])
            return group
        return None

    def findPersonByName(self, **kwargs):
        """
        Find the person by name
        :param kwargs: firstName, lastName or both
        :return: list of people found
        """
        return self._people.findPeople(**kwargs)

    def findPersonByEmail(self, emailAddress):
        """
        Find the person by email
        :param emailAddress: Email address
        :return: List of people with the given email address
        """
        firstNameLastNameList = self._people.findByEmail(emailAddress)
        return [ self._people.findPerson(p) for p in firstNameLastNameList ]
