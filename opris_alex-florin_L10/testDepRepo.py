import unittest
from infrastructure.department_repo import DepartmentRepository
from domain.departments import Department
from domain.patients import Patient
from infrastructure.patient_repo import PatientRepository

class TestDepRepo(unittest.TestCase):

    def test_creator(self):

        p = []
        l = []
        repo = DepartmentRepository(l, p)

        self.assertEqual(len(repo), 0)

    def test_add_department(self):

        p = []
        pat_repo = PatientRepository(p)
        l = []
        repo = DepartmentRepository(l, pat_repo)

        d = Department(23, "Pediatry", 10, p)

        repo.add_department(d)

        self.assertEqual(len(repo), 1)

    def test_delete_department(self):

        p = []
        pat_repo = PatientRepository(p)
        l = []
        repo = DepartmentRepository(l, pat_repo)

        d1 = Department(23, "Pediatry", 10, p)
        d2 = Department(42, "ORL", 6, p)

        repo.add_department(d1)
        repo.add_department(d2)

        self.assertEqual(len(repo), 2)

        repo.delete_department(0)

        self.assertEqual(len(repo), 1)

    def test_update_department(self):

        p = []
        pat_repo = PatientRepository(p)
        l = []
        repo = DepartmentRepository(l, pat_repo)

        d1 = Department(23, "Pediatry", 10, p)
        d2 = Department(42, "ORL", 6, p)
        d3 = Department(3, "Cardiology", 7, p)

        repo.add_department(d1)
        repo.add_department(d2)

        repo.update_department(0, 3, "Cardiology", 7, p)

        #self.assertEqual(l[0], d3)


if __name__ == '__main__':
    unittest.main()
