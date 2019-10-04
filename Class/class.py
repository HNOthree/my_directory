class Hogehoge:
 def __init__(self,value):
  self.value = value
 def plus (self,x):
  return(self.value+x)

a = Hogehoge(123)
print(a.plus(654))
print(a.plus(0))
print(a.plus(1)) 