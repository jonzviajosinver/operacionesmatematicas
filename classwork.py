class Fraction():
    ##Atributos##
    Numerator=0
    Denominator=1
    ##Fin de los atributos##


    ##Metodos##

    def __init__(self,Numerator,Denominator):
        self.Numerator=Numerator
        self.Denominator=Denominator

    def print(self):
        print(self.Numerator,"/",self.
        Denominator)

    ##Multiplicación##

    def multiply(self,def_multiplication):
        result_Numerator=self.Numerator*def_multiplication.Numerator
        result_Denominator=self.Denominator*def_multiplication.Denominator
        r=Fraction(result_Numerator,result_Denominator)
        print("El resultado de la multiplicacion de las fracciones es:", result_Numerator,"/",result_Denominator)
        return r

    ##Fin de la multiplicación##

    ##División##
    def division(self,def_division):
        result_Numerator=self.Numerator*def_division.Denominator
        result_Denominator=self.Denominator*def_division.Numerator
        result_division=Fraction(result_Numerator,result_Denominator)
        print("El resultado de la division de las fracciones es:", result_Numerator,"/",result_Denominator)
        return result_division

    ##Fin de la división##

    
    ##Suma##
    def suma(self,def_suma):
        multiplication_one=self.Denominator*Numerator_two
        multiplication_two=self.Numerator*Denominator_two
        result_Denominator=self.Denominator*def_suma.Denominator
        result=multiplication_one+multiplication_two
        result_suma=Fraction(result,result_Denominator)
        print("El resultado de la suma de las fracciones es:", result,"/",result_Denominator)
        return result_suma

    ##Fin de la suma##

    ##Resta##

    def resta(self,def_resta):
        multiplication_one=self.Denominator*Numerator_two
        multiplication_two=self.Numerator*Denominator_two
        result_Denominator=self.Denominator*def_resta.Denominator
        result=multiplication_one-multiplication_two
        result_suma=Fraction(result,result_Denominator)
        print("El resultado de la resta de las fracciones es:", result,"/",result_Denominator)
        return result_suma

    ##Fin de la resta##




print("Ingresar el primer numerador")
Numerator_one=int(input())
print("Ingresar el primer denominador")
Denominator_one=int(input())
result_one=Fraction (Numerator_one,Denominator_one)

Fraction_one=Fraction(Numerator_one,Denominator_one)


print("Ingresar el segundo numerador")
Numerator_two=int(input())
print("I    ngresar el segundo denominador")
Denominator_two=int(input())
result_two=Fraction (Numerator_two,Denominator_two)

Fraction_two=Fraction(Numerator_two,Denominator_two)


r=Fraction_one.multiply(Fraction_two)
r.print

result_division=Fraction_one.division(Fraction_two)
result_division.print

result_suma=Fraction_one.suma(Fraction_two)
result_suma.print

result_resta=Fraction_one.resta(Fraction_two)
result_resta.print