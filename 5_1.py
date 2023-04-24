class StringVar:
    def __init__(self):
         self.s = ''
    def set (self, info):
        self.s = info
    def get (self):
        return self.s
s = StringVar()
print(s.set('some information'))
print(s.get())