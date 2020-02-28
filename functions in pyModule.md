### Q. How to list all functions in a Python module?

### A.  help(modulename) or  dir(modulename)

-------------------
Once you've imported the module, you can just do:

 help(modulename)
 
... To get the docs on all the functions at once, interactively. Or you can use:

 dir(modulename)
 
... To simply list the names of all the functions and variables defined in the module.

```
ex) 
dir(Komoran)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'morphs', 'nouns', 'pos']
```
Reference : 
[Q. How to list all functions in a Python module?
](https://stackoverflow.com/questions/139180/how-to-list-all-functions-in-a-python-module)
