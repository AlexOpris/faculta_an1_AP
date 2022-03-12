from infrastructure.patient_repo import PatientRepository
from infrastructure.department_repo import DepartmentRepository
from domain.departments import Department
from domain.patients import Patient
from ui.console import UI
from application.controller import Controller


pat_list = []
pat_repo = PatientRepository(pat_list)
dep_list = []
dep_repo = DepartmentRepository(dep_list, pat_repo)


controller = Controller(dep_repo)
ui = UI(controller)
ui.start()



