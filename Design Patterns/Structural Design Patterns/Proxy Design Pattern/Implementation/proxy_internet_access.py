class OfficeInternetAccess:
    def grant_internet_access(self):
        pass 

class RealInternetAccess(OfficeInternetAccess):
    def __init__(self, emp_name):
        self.__emp_name = emp_name
    
    def grant_internet_access(self):
        print(f'Internet access granted to {self.__emp_name}')

class ProxyInternetAccess(OfficeInternetAccess):
    def __init__(self, emp_name):
        self.__emp_name = emp_name
        self.__real_internet_access = None

    def __get_role(self, emp_name):
        # custom role function
        return len(emp_name)

    def grant_internet_access(self):
        if  self.__get_role(self.__emp_name):
            self.__real_internet_access = RealInternetAccess(self.__emp_name)
            self.__real_internet_access.grant_internet_access()    
        else:
            print('Access Denied for User Role')

office_internet_access = ProxyInternetAccess('Imu Laevo')
office_internet_access.grant_internet_access()