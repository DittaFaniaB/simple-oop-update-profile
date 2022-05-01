from Profile import *
class TeacherProfile(Profile):
    def __init__(self,first_name,last_name,phone,attendance,payable_amount):
        super().__init__(first_name,last_name,phone)
        self._attendance = attendance
        self._payable_amount = payable_amount
    
    @property
    def attendance(self):
        return self._attendance
    
    @attendance.setter
    def attendance(self, new_atn):
        self._attendance = int(new_atn)
    
    @property
    def payable_amount(self):
        return self._payable_amount
    
    @payable_amount.setter
    def payable_amount(self,amnt):
        self._payable_amount = int(amnt)
    
    def teachersPaymentCalc(self):
        payment = self._attendance * self._payable_amount
        return payment

    def teachersPaymentInfo(self):
        teacher_profile = Profile(self.first_name,self.last_name,self.phone)
        return f"Fee amount of {teacher_profile.fullName()} is {self.teachersPaymentCalc()}"
    
    def completeProfileInfo(self):
        return f"-Summary-\nFirst Name: {self._first_name} \nLast Name: {self._last_name} \nPhone Number: {self._phone} \nAttendance : {self._attendance } \nPayable Amount: {self._payable_amount} \nFee : {self.teachersPaymentCalc()}" 