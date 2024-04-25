class A:
      def __display(self):
        print("display")
class B:
    def __fan(self):
        print("fan on")

print(A().__display())


class A:
      def __init__(self):
          self.__display()
      def __display(self):
        print("display")
class B:
    def __fan(self):
        print("fan on")

A()


class A:
      def deeksha(self):
          self.__display()
      def __display(self):
        print("display")
class B:
    def __fan(self):
        print("fan on")

A().deeksha( )