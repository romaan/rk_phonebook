from indexByEmail import IndexByEmail


class People(object):

    """
    People class responsible to store the persons data
    It also stores necessary indexes for faster search and retrieval
    """
    def __init__(self):
        self.__indexByFirstNLastName = {}
        self.__indexByFirstName = {}
        self.__indexByLastName = {}
        self.__indexByEmail = IndexByEmail()

    @staticmethod
    def __add_to_dict(aDict, k, v):
        if k in aDict:
            aDict[k].append(v)
        else:
            aDict[k] = [v]

    def addPerson(self, firstName, lastName, emailAddresses, phoneNumbers):
        """
        Add a person in address book
        :param firstName: A string representing first name of person
        :param lastName: A string representing last name of person
        :param emailAddresses: A list of strings of email addresses
        :param phoneNumbers: A list of strings of phone numbers
        :return: dictionary of person stored in the system
        """
        if (type(emailAddresses) is not list):
            raise TypeError('Emails expected to be a list')
        if (type(phoneNumbers) is not list):
            raise TypeError('Phone numbers expected to be a list')
        if firstName + lastName in self.__indexByFirstNLastName:
            raise Exception('Person with same first name and last name exists in phone book')
        for email in emailAddresses:
            if len(email) < 1:
                raise Exception('Email expected to be of length 1 or more')
        p = {'firstName': firstName, 'lastName': lastName, 'emailAddresses': emailAddresses, 'phoneNumbers': phoneNumbers}
        self.__class__.__add_to_dict(self.__indexByFirstName, firstName, p)
        self.__class__.__add_to_dict(self.__indexByLastName, lastName, p)
        self.__indexByFirstNLastName[firstName + lastName] = p
        for email in emailAddresses:
            self.__indexByEmail.addEmail(email, firstName + lastName)
        return p

    def findPeople(self, **kwargs):
        """
        Find a person by first name, last name or both first and last name
        :param kwargs: firstName|lastName|firstName and lastName
        :return: None or a list of Person dictionary
        """
        if 'firstName' in kwargs and 'lastName' in kwargs:
            if kwargs['firstName'] + kwargs['lastName'] in self.__indexByFirstNLastName:
                return [self.__indexByFirstNLastName[kwargs['firstName'] + kwargs['lastName']]]
            return None
        elif 'firstName' in kwargs:
            if kwargs['firstName'] in self.__indexByFirstName:
                return self.__indexByFirstName[kwargs['firstName']]
            return None
        elif 'lastName' in kwargs:
            if kwargs['lastName'] in self.__indexByLastName:
                return self.__indexByLastName[kwargs['lastName']]
            return None
        else:
            return None

    def findPerson(self, firstNLastName):
        """
        :param firstNLastName: First and Last Name as a single string
        :return: None if not found else a dictionary of person
        """
        if firstNLastName in self.__indexByFirstNLastName:
            return self.__indexByFirstNLastName[firstNLastName]
        return None

    def findByEmail(self, emailAddress):
        """
        :param emailAddress: emailAddress
        :return: A list of people
        """
        return self.__indexByEmail.getEmail(emailAddress)

