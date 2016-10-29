class Groups(object):

    """
    Groups holds the dictionary of groupName -> groups
    """

    def __init__(self):
        # Each group is stored as a dictionary of groupName to enable faster retrieval and search
        self._groups = {}

    def addGroup(self, name):
        """
        Add a new group to address book
        :param name: A string representing a group name
        :return: The name of group that is stored in dictionary as key
        :exception: If the group already exists with same name
        """
        if name in self._groups:
            raise Exception('Group already exists')
        self._groups[name] = None
        return name

    def getGroup(self, name):
        """
        Get a group if exists, None otherwise
        :param name: A string representing a group name
        :return: None or Group Name
        """
        if name in self._groups:
            return name
        return None

