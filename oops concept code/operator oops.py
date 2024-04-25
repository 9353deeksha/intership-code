class A:
    def __init__(self,a):
        self.a=a
    
    def __truediv__(deeksha,pacchu):
        return deeksha.a/pacchu.a
    
deeksha=A(20)
pacchu=A(10)
print(deeksha/pacchu)


class A:
    def __init__(self,a):
        self.a=a
    
    def __mul__(deeksha,pacchu):
        return deeksha.a*pacchu.a
    
deeksha=A(20)
pacchu=A(10)
print(deeksha*pacchu)

class A:
    def __init__(self,a):
        self.a=a
    
    def __add__(deeksha,pacchu):
        return deeksha.a+pacchu.a
    
deeksha=A(20)
pacchu=A(10)
print(deeksha+pacchu)


class A:
    def __init__(self,a):
        self.a=a
    
    def __eq__(deeksha,pacchu):
        return deeksha.a==pacchu.a
    
deeksha=A(20)
pacchu=A(20)
print(deeksha==pacchu)