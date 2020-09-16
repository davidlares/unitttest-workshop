from phonebook import PhoneBook
import unittest

# test class
class PhoneBookTest(unittest.TestCase):

    # before every test
    def setUp(self) -> None:
        self.phonebook = PhoneBook()

    # after every test - good for releasesnio
    def tearDown(self) -> None:
        pass

    # all cases starts with test_
    def test_lookup_by_name(self):
        #phonebook = PhoneBook()
        self.phonebook.add("David", "12345")
        # number = phonebook.lookup("David")
        number = self.phonebook.lookup("David")
        # assertion case
        self.assertEqual("12345", number)

    def test_missing_name(self):
        phonebook = PhoneBook()
        # phonebook without args -> passes because the phonebook it is an dictionary
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    @unittest.skip("WIP") # skip WIP - Work in Progress
    def test_empty_phonebook_is_consistent(self):
        # phonebook = PhoneBook()
        self.assertTrue(self.phonebook.is_consistent())

    # solution to avoid bad design test (arrange, act, assert)

    def test_is_consistent_with_different_entries(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Anna", "012345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_entries(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Sue", "12345")
        self.assertFalse(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_prefix(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Sue", "123")
        self.assertFalse(self.phonebook.is_consistent())
