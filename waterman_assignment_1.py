
def flatten(test_list):
    if isinstance(test_list, list):
        if len(test_list) == 0:
        first = test_list[0]
		rest = test_list[1:]
        return flatten(first) + flatten(rest)
    else:
        return [test_list]
		
	
def powerset(tlist):
    result = [[]]
    for elem in tlist:
        result.extend([x + [elem] for x in result])
    return result
	
def all_perms(t):
	  iflen(t) == 1: 
	  result = [[]]
    for i,t in enumerate(t):
        result += [t+p for p in perms(t[:i]+t[i+1:])]
    return result
