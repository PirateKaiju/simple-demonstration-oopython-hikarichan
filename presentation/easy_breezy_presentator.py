class EasyBreezyPresentator(object):
    def __init__(self, msg = "The result is: "):
        self.msg = msg
    
    def simple_print(self, printable):
        print(self.msg + str(printable)) #Something really simple