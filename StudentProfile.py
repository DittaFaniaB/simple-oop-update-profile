from Profile import *
class StudentProfile(Profile):
    def __init__(self,first_name,last_name,phone,gpa):
        super().__init__(first_name,last_name,phone)
        self._gpa = gpa
    
    @property
    def gpa(self):
        return self._gpa
    
    @gpa.setter
    def gpa(self, new_gpa):
        self._gpa = new_gpa
    
    def cpga_info(self):
        profile = Profile(self.first_name,self.last_name,self.phone)
        return f"CGPA of {profile.fullName()} is {self.gpa}"

    def completeProfileInfo(self):
        return f"-Summary-\nFirst Name: {self.first_name} \nLast Name: {self.last_name} \nPhone Number: {self.phone} \nGPA : {self.gpa}"