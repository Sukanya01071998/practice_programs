class A:
    def __init__(self):
        print("In A")
class B:
    def __init__(self):
        print("In B")
class C:
    def __init__(self):
        super().__init__()
        print("In C")
c=C()

