class A:
    def duster(self):
        print("duster")
class B(A):
    def chalk(self):
        print("chalk")

deeksha=A()
pacchu=B()
#deeksha.chalk()
pacchu.duster()
deeksha.duster()
pacchu.chalk()