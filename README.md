# quick --args
<i> Quick and easily evaluate command line arguments </i>



Sometimes I just need to get a few arguments from the command line really fast.

And since I hate having to write extensive code just for that purpose, I made this.


#

### ✔ Simplest example - implicit arguments, no constraints
```python
from quick_args import eval_args

args = eval_args()
print(args)

# accessing
if args.flag: ...
if args.positive_int == 0: ...
```
```console
foo@bar:~$ python example.py --flag --free=[1,2] --arbitrary="any type" --boolean=False --positive-int=42
flag: True
free: [1, 2]
arbitrary: any type
boolean: False
positive_int: 42
```

#

### ✔ A bit more control
```python
from quick_args import eval_args

args = eval_args(
	'free',
	flag=None,
	arbitrary=lambda v: True,
	boolean=lambda v: isinstance(v, bool), 
	positive_int=lambda v: isinstance(v, int) and v >= 0)

print(args)
```
```console
foo@bar:~$ python example.py --flag --free=[1,2] --arbitrary="any type" --boolean=False --positive-int=42
free: [1, 2]
flag: True
arbitrary: any type
boolean: False
positive_int: 42
```


● '<b>free</b>': acts exactly like 'arbitrary', but acts as 'flag' if it's not assigned to (i.e., --free). It can either be assigned to anything or to nothing at all. <br>
● '<b>flag</b>': can only be True, and never be assigned to <br>
● '<b>arbitrary</b>': can only be assigned to, but to anything <br>
● '<b>boolean</b>': a basic True or False scenario <br>
● '<b>positive_int</b>': self explanatory <br>


<br>
💡 Observations

● <b>all arguments will be None if they are not passed <br>
● arguments fed in the command line and that aren't passed in to eval_args will still apear, but will act as a 'free' argument. <br></b>
● if you pass an argument name such as 'positive-int', it'll get converted to an attribute named 'positive_int' (hyphen to underline) <br>
