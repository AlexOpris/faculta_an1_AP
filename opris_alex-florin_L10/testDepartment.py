import unittest
from domain.departments import Department
from domain.patients import Patient

class TestDepartment(unittest.TestCase):

    def test_create(self):

        p = []
        p1 = Patient("Pop", "George", 2312322186, "Arrhythmia")
        p2 = Patient("Tatar", "Andrei", 5686590765, "Atherosclerosis")
        p.append(p1)
        p.append(p2)

        d = Department(3, "Cardiology", 7, p)

        self.assertEqual(d.get_id(), 3)

        self.assertEqual(d.get_name(), "Cardiology")

        self.assertEqual(d.get_nr_beds(), 7)

        #self.assertEqual(d.get_list_patients(), d)


if __name__ == '__main__':
    unittest.main()
