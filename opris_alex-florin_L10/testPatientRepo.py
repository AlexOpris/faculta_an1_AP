import unittest
from infrastructure.patient_repo import PatientRepository
from domain.patients import Patient
from domain.departments import Department

class TestPatientRepo(unittest.TestCase):

    def test_creator(self):

        l = []
        repo = PatientRepository(l)


        self.assertEqual(len(repo), 0)

    def test_add_patient(self):

        l = []
        repo = PatientRepository(l)

        p1 = Patient("Pop", "George", 2342315233, "Arrhythmia")

        repo.add_patient(p1)

        self.assertEqual(len(l), 1)

    def test_delete_patient(self):

        l = []
        repo = PatientRepository(l)

        p1 = Patient("Pop", "George", 2323415231, "Arrhythmia")
        p2 = Patient("Tatar", "Andrei", 5234253216, "Atherosclerosis")

        repo.add_patient(p1)
        repo.add_patient(p2)

        self.assertEqual(len(l), 2)

        repo.delete_patient(1)

        self.assertEqual(len(l), 1)

    def test_update_patient(self):

        l = []
        repo = PatientRepository(l)

        p1 = Patient("Pop", "George", 8645634623, "Arrhythmia")
        p2 = Patient("Tatar", "Andrei", 7534432756, "Atherosclerosis")
        p3 = Patient("Sabou", "Mihaela", 4322190533, "Coronary artery disease")

        repo.add_patient(p1)
        repo.add_patient(p2)

        repo.update_patient(1, "Sabou", "Mihaela", 5323214243, "Coronary artery disease")






if __name__ == '__main__':
    unittest.main()
