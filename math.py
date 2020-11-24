from fractions import Fraction
from time import sleep

class Convert:
    def __init__(self,Num=str):
        self.Num = Num

    #Change the Fraction To Decimal
    def FractionToDecimal(self):
        print(f'Answer: {float(Fraction(self.Num))}')
        print(f'Explanation: Divide {self.Num} the denomnator and numerator.')

    #Change the Decimal to Fraction
    def DecimalToFraction(self):
        print(f'Answer: {Fraction(self.Num)}')
        print(f'Place decimal point by 2 and you will find out the answer if it is in 10th,100th, and 1000th then simplify your answer.')

    #Change Fraction to Decimal
    def FractionToPercent(self):
        a = float(Fraction(self.Num))
        print(f'Answer: {int(a * 100)}%')
        print(f'Explain: Convert {self.Num} to percent, by dividing the numerator by denominator then multiply by 100')

    def DecimalToPercent(self):
        a = self.Num * 100
        print(f'Answer: {a}%')
        print(f'Multiply {self.Num} to 100 and move decimal point two places to the right and put % sign.')

    def PercentToDecimal(self):
        a = self.Num.strip('%')
        b = len(a)
        if b == 2:
            d = int(a) /100
            print(f'Answer: {d}')
            print(f'Explanation: Convert {self.Num} and it will be {a} and divided by 100, and will be {d}.')
        elif b == 3:
            d = int(a) /1000
            print(f'Answer: {d}')
            print(f'Explanation: Convert {self.Num} and it will be {a} and divided by 100, and will be {d}.')
    def PercentToFraction(self):
        a = self.Num.strip('%')
        b = len(a)
        if b == 2:
            d = Fraction(a)/100
            print(f'Answer: {d}')
            print(f'Explaination: {self.Num} = {a} divided by {a}/100 which is the answer is {d}.')
        elif b == 3:
            d = Fraction(a)/1000
            print(f'Answer: {d}')
            print(f'Explaination: {self.Num} = {a} divided by {a}/1000 which is the answer is {d}.')
        elif b == 4:
            d = Fraction(a)/1000
            print(f'Answer: {d}')
            print(f'Explaination: {self.Num} = {a} divided by {a}/1000 which is the answer is {d}.')

    def __str__(self):
        return 'This is My Math Project'


def decimaltopercent(n):
    a = n * 100
    print(f'Answer: {a}%')

def main():
    print("""
    List of Available Converters
    
    [1]. Fraction To Decimal
    [2]. Decimal To Fraction
    [3]. Fraction to Percent
    [4]. Decimal to Percent
    [5]. Percent to Decimal
    [6]. Percent to Fraction
    [10]. Exit
    """)
    while True:
        Ask = input("Please Choose: ")
        if Ask == '1':
            try:

                fraction_ask = input("Your number Please: ")
                c = Convert(fraction_ask)
                a = c.FractionToDecimal()
            except ValueError:
                print("Oops.. Value Error, please try again")
                sleep(2)
                quit()
        elif Ask == '2':
            try:

                fraction_ask = input("Your Number Please: ")
                c = Convert(fraction_ask)
                a = c.DecimalToFraction()
            except ValueError:
                print("Oops.. Value Error, please try again")
                sleep(2)
                quit()
        elif Ask == '3':
            try:

                fraction_ask = input("Your Number Please: ")
                c = Convert(fraction_ask)
                a = c.FractionToPercent()
            except ValueError:
                print("Oops.. Value Error, please try again")
                sleep(2)
                quit()
        elif Ask == '4':
            try:

                fraction_ask = float(input("Your Number Please: "))
                a = decimaltopercent(fraction_ask)
            except ValueError:
                print("Oops.. Value Error, please try again")
                sleep(2)
                quit()
        elif Ask == '10':
            print("Thank you for using our service!")
            sleep(2)
            quit()
        elif Ask == '5':
            fraction_ask = input("Your Number Please: ")
            c = Convert(fraction_ask)
            c.PercentToDecimal()
        elif Ask == '6':
            try:

                fraction_ask = input("Your Number Please: ")
                c = Convert(fraction_ask)
                c.PercentToFraction()
            except:
                print("My Solver Can't solve this equation")
        else:
            print("You've Entered A Wrong Number, Please try again.")
main()
