#overwritting
class a:
    def ab(self):
        print("tranier")
class b:
    def ab(self):
        print("friend")

obj=a().ab()
obj=b().ab()



#overloding
class AA:
    def ab(self,python,java=0):
        if java==0:
            print("trainer",python)
        elif python and java:
            print("tranier",python,java)
        
obj=AA().ab("python")
obj=AA().ab("python","java")