class Counter():
    def __init__(self):
        self.wrd = input("Enter A Word: ")

        self.wrd = self.wrd.lower()

        self.vow_count = 0
        self.con_count = 0
        self.num_count = 0
        self.space = 0
        self.special = 0
        self.vowels = ['a','e','i','o','u']

        self._count()
        self._output()

    def _count(self):
        for self.let in self.wrd:
            self._ascii = ord(self.let)
            if self.let in self.vowels:
                self.vow_count+=1
            elif 65 <= self._ascii <= 90 or 97 <= self._ascii <= 122:
                self.con_count+=1
            elif self._ascii == 32:
                self.space+=1
            elif 47 <= self._ascii <= 56:
                self.num_count+=1
            else:
                self.special+=1

    def _output(self):
        print("\nOutput:-")
        print(f"The Number Of Vowels in this string is {self.vow_count}.")
        print(f"The Number of Consonants In This String Is {self.con_count}.")
        print(f"The Number of Digits In This String Is {self.num_count}.")
        print(f"The Number of Spaces In This String Is {self.space}.")
        print(f"The Number of Special Characters In This String Is {self.special}.")

if __name__=="__main__":
    Counter()
