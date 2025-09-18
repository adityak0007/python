class Employee:
    def __init__(self):
        print("employee name")

    def __del__(self):
        print("employee removed")

obj = Employee()
del obj
