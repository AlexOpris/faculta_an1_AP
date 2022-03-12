import unittest
from domain.patients import Patient

class TestPatient(unittest.TestCase):

    def test_create(self):

        p = Patient("Pop", "George", 2325232000, "flu")

        self.assertEqual(p.get_first_name(), "Pop")

        self.assertEqual(p.get_last_name(), "George")

        self.assertEqual(p.get_personal_code(), 2325232000)

        self.assertEqual(p.get_disease(), "flu")

        self.assertEqual(p.get_age(), 20)



if __name__ == '__main__':
    unittest.main()
