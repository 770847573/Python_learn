from mymodule import say_Hi,__version__
import mymodule
say_Hi()
print(__version__)
print(dir(mymodule))
a = 1
print(dir())
del a
print(dir())
