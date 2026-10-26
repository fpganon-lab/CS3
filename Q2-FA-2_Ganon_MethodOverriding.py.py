class Patient:
    def __init__(self, name: str, bill_amount: int) -> None:
        self.__name: str = name
        self.__bill_amount: int = bill_amount

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_bill_amount(self) -> int:
        return self.__bill_amount

    def set_bill_amount(self, bill_amount: int) -> None:
        self.__bill_amount = bill_amount

    def calculate_bill(self: int)
        return self.__bill_amount


class Senior_patient(Patient):
    def calculate_bill(self) -> int:
        return self.get_bill_amount() * 80 // 100

class PhilHealthPatient(Patient):
    def calculate_bill(self) -> int:
        return self.get_bill_amount() * 85 // 100

patient1 = Patient("Juan Dela Cruz", 15000)
patient2 = Senior_patient("Maria Santos", 15000)
patient3 = PhilHealthPatient("Pedro Reyes", 15000)

print("\nHospital Billing System\n")

for patient in (patient1, patient2, patient3):
    print(f"Patient Name: {patient.get_name()}")
    print(f"Original Bill: {patient.get_bill_amount()}")
    print(f"Final Bill: {patient.calculate_bill()}\n")
