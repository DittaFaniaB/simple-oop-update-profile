class Profile:
    def __init__(self, first_name,last_name,phone):
        self._first_name = first_name
        self._last_name = last_name
        self._phone = max(int(phone), 0)

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, new_name):
        self._first_name = new_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self,new_name):
        self._last_name = new_name

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, new_phone):
        self._phone = max(int(new_phone), 0)

    def completeProfileInfo(self):
        return f"-Summary-\nFirst Name: {self._first_name} \nLast Name: {self._last_name} \nPhone Number: {self._phone}"

    def fullName(self):
        return "{} {}".format(self._first_name,self._last_name)

    def details(self):
        return f"Full Name: {self.fullName()} \nPhone: {self.phone}"