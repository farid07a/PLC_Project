from Modules.FamilyDoctor import FamilyDoctor


class Doctor(FamilyDoctor):

    def what_specialisation(self):
        print("I am Doctor")

    def studies_years(self):
        print("Override method")
