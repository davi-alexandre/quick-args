# quick --args
<i> Quick and easily evaluate command line arguments </i>



Sometimes I just need to get a few arguments from the command line really fast.

And since I hate having to write extensive code just for that purpose, I made this.


✔ Example:
```python
from quick_args import eval_args


args = eval_args(
	no_equals=None,
	reprocess=lambda v: isinstance(v, bool), 
	read_limit=lambda v: isinstance(v, int) and v > 0)

if args.reprocess: pass
if args.read_limit == 1: pass

print(args)
```
```console
foo@bar:~$ python example.py --no-equals --reprocess=True --read-limit=2
no_equals: True
reprocess: True
read_limit: 2
```
