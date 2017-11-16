# These are some examples of python-style function dfinitions.

#Simple example: Add two numbers
def add_2(x, y):
	return x + y
	
# Illustrate default arguments:
def my_range (start, end, by = 1):
	return range(start, end, by)
	#Homework: rewrite this function to use a for loop rather than resorting to Python's built in range function.
	
	
	
#def print_triangle(n, full=False):
#	counter = 1
#	for x in range(n):
#	print('*' * counter)
#	counter += 1
#	if full == True:
#	counter -+ 2
#	for x in range(n):
#	print('*' * counter)
#	counter -= 1
	
def histogram(items):
	
	d={}
	for i in items:
		if not d.has_key(i):
			d[i] = 0
		d[i] += 1
	return d
	
	#Reads in a file and gets the word counts as a histogram
	

	
	

def word_counts(file_path, case_sensitive=True, treat_punct_as_word = False, punct = ['!', '.', ',', '"', "'", '?', '~']):
	text= open(file_path, 'r').read()
	if not(case_sensitive):
		text = text.lower()
	#TODO: add code to count each pnctuation character
	#For time being, remove punctuation characters:
	for p in punct:
		text = text.replace(p, ' ')
	words= text.split(' ')
	cleaned_words = []
	for w in words:
		if len(w) > 0:
			cleaned_words.append(w.strip())
	return histogram(cleaned_words)
	
	
	
#Returns the maximum(largest) element in the list
#def my_max(elements):
#	if len(elements) > 0
##		curr_max = elements[0]
#		for e in elements:
#			if e > curr_max:
#				curr_max = e
#		return curr_max
#	return None
	
	#Illustrate variable-length inputs into a function
def variable_number_of_inputs(a, b, *rest):
	print("A is " + str(a))
	print("B is " + str(b))
	for e in rest:
		print(" Next optional input: ") + str(e)
		
		
	#Options for functions are: map, zip, reduce, filter
	#step 1: tups=zip(1,2,3) (4,5,6) = (1,4)(2,5), (3,6)]
	#Step 2: fzip = lambda x: f(*x)
	 #Step3 map =fnew , tups
		

#implrement fzip - Zip a set of lists and collapse resulting tuples
#based on an aggregating function f.
def fzip(f, *lists):
	return map(lambda tup: f(*tup), zip(*lists))
	

	
	
	
	
	
	
	#Recursive definition of usmming number over a range
	
def sum_range(a, b):
	if a == b: 
		return a
	else:
		return sum_range(a, b - 1) + b 
		
	
	
#def rrev(list):
#	list=[]
#	revword = list[::-1]
	
#	return rrev[]

	#Recursively compute the nth fibonacci number
	
def fib(first, second, n):
	if n == 1:
		return first
	if n == 2:
		return second
	else:
		return fib(first, second, n - 1) + fib(first, second, n - 2)
		
		
		#Recursively compute the nth fibonacci number - use memoization to avoid resolving sub-problems

def mfib(first, second, n, cache={}):
	if n == 1:
		return first
	if n == 2:
		return second
	elif cache.has_key(n):
		return cache[n]
	else:
		v = mfib(first, second, n - 1, cache) + mfib(first, second, n - 2, cache)
		cache[n] = v
		return v
		

def cartesian_product(*sets):
	if len(sets) == 1:
		return map(lambda x: [x], sets[0])
	else:
		rest = cartesian_product(*sets[1:])
		combine = lambda x: map(lambda y: [x] + y, rest)
		return reduce(lambda x,y: x + y, map(combine, sets[0]))
		
	#Kcomb, use recurssion and should be around 7 to 8 lines

def flatten(test_list):
    if isinstance(test_list, list):
        if len(test_list) == 0:
            return []
        first, rest = test_list[0], test_list[1:]
        return flatten(first) + flatten(rest)
    else:
        return [test_list]
		
	
def powerset(tlist):
    result = [[]]
    for elem in tlist:
        result.extend([x + [elem] for x in result])
    return result
	
def all_perms(tlist):
	  if(len(tlist) ==1 ): return [tlist]
    result=[]
    for i,t in enumerate(tlist):
        result += [t+p for p in perms(tlist[:i]+tlist[i+1:])]
    return result
