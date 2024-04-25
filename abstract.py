from abc import ABC,abstractmethode

class printable(ABC):
    @abstractmethode
    def print_content(self):
        pass
class Document(printable):
    def print_content(self):
        print("print_content")
        
    
document=Document()
document.print_content()