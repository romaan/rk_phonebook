import unittest
from faker import Faker
from addressbook.addressbook import AddressBook


class TestAddressBookFindApi(unittest.TestCase):

    def setUp(self):
        self.fake = Faker()
        self.addrBook = AddressBook()
        self.groups = []
        self.people = []

    def _createPeopleNGroup(self, numberOfpeople, numberOfgroup):
        """
        Helper function to create a few people and a few groups
        :param numberOfpeople: Number of people
        :param numberOfgroup: Number of groups
        """
        i = 0
        while i < numberOfpeople:
            firstName = self.fake.first_name()
            lastName = self.fake.last_name()
            emailAddresses = [self.fake.email(), self.fake.email(), self.fake.email()]
            phoneNumbers = [self.fake.phone_number(), self.fake.phone_number()]
            self.people.append(self.addrBook.addPerson(firstName=firstName, lastName=lastName,
                                             emailAddresses=emailAddresses,
                                             phoneNumbers=phoneNumbers))
            i += 1

        i = 0
        while i < numberOfgroup:
            groupName = self.fake.company()
            self.groups.append(self.addrBook.addGroup(groupName))
            i += 1

    def testFindGroupMembers(self):
        """
        Test find a group member
        """
        # Create 10 people and 3 groups
        self._createPeopleNGroup(10, 3)
        i = 0
        while i < 3:
            self.addrBook.addMember(self.groups[0], self.people[i]['firstName'], self.people[i]['lastName'])
            i += 1

        people = self.addrBook.getGroupMembers(self.groups[0])
        self.assertEquals(len(people), 3, "Expecting 3 people to be in the group")

    def testFindPersonGroups(self):
        """
        Test find a persons group
        """
        self._createPeopleNGroup(1, 4)
        i = 0
        while i < 3:
            self.addrBook.addMember(self.groups[i], self.people[0]['firstName'], self.people[0]['lastName'])
            i += 1
        groups = self.addrBook.getGroups(self.people[0]['firstName'], self.people[0]['lastName'])
        self.assertEqual(len(self.addrBook._groups._groups), 4, "Expecting total of 4 groups")
        self.assertEqual(len(groups), 3, "Expecting a person to be in 3 groups")


    def testFindPersonByFirstName(self):
        """
        Test finding person by first name
        """
        self._createPeopleNGroup(10, 0)
        people = self.addrBook.findPersonByName(firstName=self.people[0]['firstName'])
        self.assertTrue(type(people) == list and len(people) >= 1, "Expecting a list of people with 1 or more items")
        self.assertTrue(people[0]['firstName'] == self.people[0]['firstName'])

    def testFindPersonByLastName(self):
        """
        Test finding person by last name
        """
        self._createPeopleNGroup(10, 0)
        people = self.addrBook.findPersonByName(lastName=self.people[0]['lastName'])
        self.assertTrue(type(people) == list and len(people) >= 1, "Expecting a list of people with 1 or more items")
        self.assertTrue(people[0]['lastName'] == self.people[0]['lastName'])

    def testFindPersonByFirstNLastName(self):
        """
        Test finding a person by first and last name
        """
        self._createPeopleNGroup(10, 0)
        people = self.addrBook.findPersonByName(firstName=self.people[0]['firstName'],
                                                lastName=self.people[0]['lastName'])
        self.assertTrue(type(people) == list and len(people) == 1, "Expecting a list of people with 1 item only")
        self.assertTrue(people[0]['firstName'] == self.people[0]['firstName'], "Expecting first name with predefined first name")
        self.assertTrue(people[0]['lastName'] == self.people[0]['lastName'], "Expecting last name with predefined last name")

    def testFindPersonByEmail(self):
        """
        Test finding the person by email
        """
        self._createPeopleNGroup(10, 0)
        people = self.addrBook.findPersonByEmail(self.people[0]['emailAddresses'][0])
        self.assertEqual(len(people), 1)
        self.assertTrue(people[0]['firstName'] == self.people[0]['firstName'] and people[0]['lastName'] == self.people[0]['lastName'], "Expected person with predefined name")
