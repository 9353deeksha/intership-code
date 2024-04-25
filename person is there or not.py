def deeksha():
    print("deeksha")
def pacchu():
    print("pacchu")
def laxmi():
    print("laxmi")
def default():
    print("the person is not here")

def teacher():
    someotherperson=int(input("enter the funtion name"))
    switch_data={1:deeksha,2:pacchu,3:laxmi}
    result=switch_data.get(someotherperson,default)
    result()
teacher()