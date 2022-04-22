#	Author: Davi Alexandre
#	Date: 10/2021


from sys import argv


class MyArgs:
	def __init__(self, free:'identifiers', constrained:'identifiers and a predicate'):
		self._args = {arg:(lambda v: True) for arg in free}
		for arg, predicate in constrained.items():
			self._args[arg] = predicate
		for arg in self._args.keys():
			if arg != '_args':
				setattr(self, arg, None)
	def __str__(self):
		msg = ''
		for arg in self._args.keys():
			msg += arg + ': ' + str(getattr(self, arg)) + '\n'
		return msg

def eval_args(*free, **constrained):
	args = MyArgs(free, constrained)
	identifiers = list(free) + list(constrained.keys())
	for arg in argv[1:]:
		if not arg[:2].startswith('--') or arg == '--':
			continue
		arg = arg[2:]
		if not '=' in arg:
			# no attribution
			arg = arg.replace('-', '_')
			if arg in constrained.keys():
				if constrained[arg] == None:
					key = arg
					value = 'True'
				else:
					continue
			else:
				key = arg
				value = 'True'
		else:
			# attribution
			key, value = arg.split('=')
			key = key.replace('-', '_')
		if key not in identifiers:
			# unlisted argument name
			args._args[key] = lambda x: True
		try:
			value = eval(value)
		except:
			value = eval("'" + str(value) + "'")

		predicate = args._args[key] if key != arg.replace('-', '_') else (lambda x: x)
		if not predicate(value):
			raise Exception(
				f"The argument <{key}> does not satisfy "
				f"it's predicate for the value <{value}>")
		setattr(args, key, value)
	return args
