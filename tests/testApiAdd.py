import unittest
from faker import Faker
from addressbook.addressbook import AddressBook


class TestAddressBookAddApi(unittest.TestCase):

    def setUp(self):
        self.fake = Faker()
        self.addrBook = AddressBook()

    def testAddPerson(self):
        """
        Test adding a person to phone book
        """
        firstName = self.fake.first_name()
        lastName = self.fake.last_name()
        emailAddresses = [self.fake.email(), self.fake.email(), self.fake.email()]
        phoneNumbers = [self.fake.phone_number(), self.fake.phone_number()]
        ret = self.addrBook.addPerson(firstName=firstName, lastName=lastName,
                               emailAddresses=emailAddresses,
                                      phoneNumbers=phoneNumbers)
        self.assertEqual(type(ret), dict, "Expecting a person dictionary")
        self.assertTrue(ret['firstName'] == firstName and ret['lastName'] == lastName)
        self.assertTrue(set(ret['emailAddresses']) == set(emailAddresses), "Incorrect email addresses")
        self.assertTrue(set(ret['phoneNumbers']) == set(phoneNumbers), "Incorrect phone number")
        self.assertEqual(len(self.addrBook._people._People__indexByFirstName), 1, "Data not indexed by first name")
        self.assertEqual(len(self.addrBook._people._People__indexByLastName), 1, "Data not indexed by last name")
        self.assertEqual(len(self.addrBook._people._People__indexByFirstNLastName), 1, "Data not indexed by first and last name")

    def testAddPersonExceptionDuplicatePerson(self):
        """
        Test adding a person to phone book
        """
        firstName = self.fake.first_name()
        lastName = self.fake.last_name()
        emailAddresses = [self.fake.email(), self.fake.email(), self.fake.email()]
        phoneNumbers = [self.fake.phone_number(), self.fake.phone_number()]
        ret = self.addrBook.addPerson(firstName=firstName, lastName=lastName,
                               emailAddresses=emailAddresses,
                                      phoneNumbers=phoneNumbers)
        self.assertEqual(type(ret), dict, "Expecting a person dictionary")
        with self.assertRaises(Exception):
            self.addrBook.addPerson(firstName=firstName, lastName=lastName,
                                      emailAddresses=emailAddresses,
                                      phoneNumbers=phoneNumbers)


    def testAddGroup(self):
        """
        Test adding a group to phone book
        """
        groupName = self.fake.company()
        ret = self.addrBook.addGroup(groupName)
        self.assertEqual(ret, groupName, "Expecting a group name")
        self.assertEqual(len(self.addrBook._groups._groups), 1, "Group not indexed")

    def testAddGroupMembers(self):
        """
        Test adding members to group
        """
        groupName = self.fake.company()
        firstName = self.fake.first_name()
        lastName = self.fake.last_name()
        emailAddresses = [self.fake.email(), self.fake.email(), self.fake.email()]
        phoneNumbers = [self.fake.phone_number(), self.fake.phone_number()]
        person = self.addrBook.addPerson(firstName=firstName, lastName=lastName,
                                emailAddresses=emailAddresses,
                                phoneNumbers=phoneNumbers)
        group = self.addrBook.addGroup(groupName)
        ret = self.addrBook.addMember(group, person['firstName'], person['lastName'])
        self.assertTrue(ret)
        self.assertEqual(len(self.addrBook._members._personToGroup), 1, "Relation person to group not saved")
        self.assertEqual(len(self.addrBook._members._groupToPerson), 1, "Relation group to person not saved")