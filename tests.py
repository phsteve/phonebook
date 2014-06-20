import unittest
import phonebook

class TestStuff(unittest.TestCase):

    def setUp(self):
        self.pb = phonebook.Phonebook()
        self.pb.add('joe', 8675309)

    def test_retrieve(self):
        try:
            self.pb.retrieve('joe')
        except phonebook.InvalidNameError:
            self.fail('retrieve is broken!')
        self.assertRaises(phonebook.NameNotFoundError, self.pb.retrieve, 'noe')

    def test_add(self):
        self.pb.add('bob', 1234567)
        test_bob = phonebook.Entry('bob', 1234567)
        self.assertEquals(self.pb.retrieve('bob'), test_bob)

    def test_change(self):
        self.pb.change('joe', 8675308)
        self.assertEquals(self.pb.retrieve('joe').number, 8675308)

        self.assertRaises(phonebook.NameNotFoundError, self.pb.change, 'nonexistant', 1234567)

    def test_lookup(self):
        test_joe = phonebook.Entry('joe', 8675309)
        jo_results = self.pb.lookup('jo')
        self.assertEquals(jo_results.split("\n")[0], str(test_joe))

        oe_results = self.pb.lookup('oe')
        self.assertEquals(oe_results.split("\n")[0], str(test_joe))

if __name__ == '__main__':
    unittest.main()
