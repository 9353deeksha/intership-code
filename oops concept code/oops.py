with open('example.txt','w+')as file:
    file.write('deeksha')
    print(file.tell())
    print(file.read())
    
with open('example.txt','w+')as file:
    file.write('deeksha')
    print(file.seek(1))
    print(file.read())    
    
with open('example.txt','r+')as file:
    print(file.read())
    file.write("hello")     
  
    