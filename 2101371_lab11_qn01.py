class calculator:
  def __init__(self):
    num1 = float(input("Enter num1: "))
    num2 = float(input("Enter num2: "))
    self.adder(num1, num2)
    self.subtractor(num1, num2)
    self.multiplier(num1, num2)
    self.divider(num1, num2)
    self.clear()
  

  def adder(self, num1, num2):
    print("Adder: ", num1 + num2)
    return num1+num2
    
  def subtractor(self, num1, num2):
    print("Subtractor(num1 - num2): ", num1 - num2)
    print("Subtractor(num2 - num2): ", num2 - num1)
    return num2 - num1
    
  def multiplier(self, num1, num2):
    print("mulitplier: ",num1*num2)
    return num1*num2

  def divider(self, num1, num2):
    print("divider (num1/num2)" , num1/num2)
    print("divider (num2/num1)" , num2/num1)
    return num2/num1

  def clear(self):
    self.num1 = 0
    self.num2 = 0
    print("Calculator cleared: num1 is " + str(self.num1) + " num2 is " + str(self.num2))


  

    
calculator = calculator()


