# This is a test driver for our functions defined inbasic_functions.py

# Impore the modle and name as bs
import basic_functions as bs

#Test the ad_2 function defined as bs.
#print(bs.add_2(3, 5))
#print(bs.add_2(4, 6))
#print(bs.add_2(5, 7))

# Test the my_range function.
#print (bs.my_range(1,50))
#print (bs.my_range(1, 50, 3))
#print (bs.my_range(1, 50, by=4)) #Note we can specify the optional arg. inputs

#bs.print_triangle(3)
#print("\n\n")
#bs.print_triangle(5)
#print("\n\n")
#bs.print_triangle(5, full=True)


#Test histogram

#print(bs.histogram(['a', 'x', 2, 'x', 3, 2]))


#Test word count
#print(bs.word_count('./data/sample_text.txt')


#print(bs.my_max([2,3,4,5,6]))

#print(bs.variable_number_of_inputs(2, 3))


#Test the fzip function
#print(bs.fzip(lambda x, y: x _ y, [1,2,3], [4,5,6]))
#print(bs.fzip(max, [1,3,4], [4,5,6], [7,8,9]))


#print(bs.sum_range(1, 100))


#print(bs.rrev(["Reverse this stuff"]))


print(bs.fib(1,15,20)) 

print(bs.mfib(1,1,20))

#Test the cartesian_product function
print(bs.cartesian_product([1,2], [3,4]))

print(bs.flatten([1], [[3]], [44]))