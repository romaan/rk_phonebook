from groups import Groups
from people import People


class Members(object):

    def __init__(self, people, groups):
        self._personToGroup = {}
        self._groupToPerson = {}
        self.__people = people
        self.__groups = groups

    @staticmethod
    def __add_to_dict(aDict, k, v):
        if k in aDict:
            aDict[k].append(v)
        else:
            aDict[k] = [v]

    def addMember(self, groupName, personFirstName, personLastName):
        """
        Add a member to a group
        :param groupName: A group name (string)
        :param personFirstName: Person's first name (string)
        :param personLastName: Person's last name (string)
        :return: True if added, False otherwise
        """
        person = self.__people.findPerson(personFirstName + personLastName)
        group = self.__groups.getGroup(groupName)
        if person and group:
            self.__class__.__add_to_dict(self._personToGroup, person['firstName'] + person['lastName'], group)
            self.__class__.__add_to_dict(self._groupToPerson, group, person['firstName'] + person['lastName'])
            return True
        return False

    def findGroups(self, person):
        """
        Find the groups for a person
        :param person: a dictionary containing person details
        :return: group: None or a dictionary containing group details
        """
        if person in self._personToGroup:
            return self._personToGroup[person]
        return None

    def findPeople(self, group):
        """
        Find the people for a group
        :param group: a dictionary containing group details
        :return: person: None or a dictionary containing person details
        """
        if group in self._groupToPerson:
            return self._groupToPerson[group]
        return None

