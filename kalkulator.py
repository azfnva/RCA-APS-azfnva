class Kalkulator:
    @staticmethod
    def tambah(a, b):
        return a + b

    @staticmethod
    def kurangi(a, b):
        return a - b

    @staticmethod
    def kali(a, b):
        return a * b

    @staticmethod
    def bagi(a, b):
        if b == 0:
            raise ValueError("Division by zero!")
        return a / b