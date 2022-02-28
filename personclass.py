class person:
    def __init__(self, name, address, phone):
        self.name = name
        self.address =  address
        self.phone = phone

class customer(person):
    def __init__(self, name, address, phone, cust_phone, mail_list):

        person.__init__(self, name, address, phone)
        
        self.__cust_phone = cust_phone
        self.__mail_list = mail_list

    def print_person(self):
        print(self.name)
        print(self.address)
        print(self.phone)
        print(self.__cust_phone)
        print(self.__mail_list)

        