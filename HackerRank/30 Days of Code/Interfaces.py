class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    #This is fatster solution.
    def divisorSum(self, n):
        if n == 1: return 1
        sum = 0; i =1
        while i < (n**(1/2)):
            if n % i ==0:
                sum += (i + n/i)
            i +=1
        if n == i**2: sum += i
        return int(sum)
        pass
    # Or I can do it slower but easier, with checking every integer <= n
    ## sum([i for i in range(1,n+1) if (n%i == 0)])

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)