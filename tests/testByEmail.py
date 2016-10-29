import unittest
from addressbook.indexByEmail import IndexByEmail


class TestNode(unittest.TestCase):

    def setUp(self):
        """
        Set up with email address and FirstNameLastName values
        """
        self.email_1 = ('romaank@gmail.com', 'RomaanKhadeer')
        self.email_2 = ('rahul@gmail.com', 'RahulGupta')
        self.email_3 = ('rosey@gmail.com', 'RoseyInsan')
        self.email_4 = ('romaank@gmail.com', 'RomaanAhmed')

    def testAddEmailIndex(self):
        """
        Test to ensure n-ary indexes are created
        """
        idxEmail = IndexByEmail()
        idxEmail.addEmail(self.email_1[0], self.email_1[1])
        idxEmail.addEmail(self.email_2[0], self.email_2[1])
        idxEmail.addEmail(self.email_3[0], self.email_3[1])
        for email in (self.email_1[0], self.email_2[0], self.email_3[0]):
            node = idxEmail.tree
            for ch in email:
                self.assertTrue(ch in node.nodes)
                node = node.nodes[ch]

    def testEmailIndexWithValues(self):
        """
        Test to ensure n-ary indexes are created and FirstNameNLastNames are inserted into left nodes' list
        """
        idxEmail = IndexByEmail()
        idxEmail.addEmail(self.email_1[0], self.email_1[1])
        idxEmail.addEmail(self.email_2[0], self.email_2[1])
        idxEmail.addEmail(self.email_3[0], self.email_3[1])
        idxEmail.addEmail(self.email_4[0], self.email_4[1])
        node = idxEmail.tree
        email = self.email_1[0]
        for ch in email:
            node = node.nodes[ch]
        self.assertEqual(len(node.values), 2)
        self.assertEqual(set(node.values), set([self.email_1[1], self.email_4[1]]))

    def testGetNoNames(self):
        """
        Test to ensure we get the no names as we do not have matching email
        """
        idxEmail = IndexByEmail()
        idxEmail.addEmail(self.email_1[0], self.email_1[1])
        idxEmail.addEmail(self.email_2[0], self.email_2[1])
        idxEmail.addEmail(self.email_3[0], self.email_3[1])
        idxEmail.addEmail(self.email_4[0], self.email_4[1])
        search = 'rxxxx'
        ret = idxEmail.getEmail(search)
        self.assertTrue(ret == None, "Expected result as None")


    def testGetNames(self):
        """
        Test to ensure we get the names
        """
        idxEmail = IndexByEmail()
        idxEmail.addEmail(self.email_1[0], self.email_1[1])
        idxEmail.addEmail(self.email_2[0], self.email_2[1])
        idxEmail.addEmail(self.email_3[0], self.email_3[1])
        idxEmail.addEmail(self.email_4[0], self.email_4[1])
        search = 'ro'
        ret = idxEmail.getEmail(search)
        self.assertTrue(type(ret) == list)
        self.assertEqual(len(ret), 3, "Expected result with 3 values")
        self.assertEqual(set(ret), set([self.email_1[1], self.email_3[1], self.email_4[1]]))