
class TestClass:
    def __init__(self, getal_1: int, getal_2: int) -> int:
        self.getal_1 = getal_1
        self.getal_2 = getal_2
        return None

    def som(self):
        return self.getal_1 + self.getal_2

    def verschil(self):
        return self.getal_1 - self.getal_2

def som(a, b):
    return a + b

def main():

    tc1 = TestClass(5, 3)
    tc2 = TestClass(7, 9)

    print('som:', tc1.som())
    print('verschil:', tc1.verschil())
    print(tc2.getal_2)
    return None

main()