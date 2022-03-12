from infrastructure.repo import VectorRepository
from Controller.controller import VectorController
from ui.console import VectorUI
from domain.vector import MyVector

list = []
repo = VectorRepository(list)


repo.addVector(MyVector(1, "y", 2, [5, 3, 2]))
repo.addVector(MyVector(2, "r", 3, [12]))
repo.addVector(MyVector(3, "b", 1, [25, 13, 26]))
repo.addVector(MyVector(4, "b", 1, [8, 9, 1]))
repo.addVector(MyVector(5, "m", 4, [4]))
repo.addVector(MyVector(6, "b", 4, [23, 42]))
repo.addVector(MyVector(7, "m", 2, [6, 7, 9, 3]))
repo.addVector(MyVector(8, "g", 3, [31, 11]))
repo.addVector(MyVector(9, "g", 1, [21, 30, 10]))
repo.addVector(MyVector(10, "r", 4, [52]))


controller = VectorController(repo)
ui = VectorUI(controller)
ui.start()
