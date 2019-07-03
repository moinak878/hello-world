# single line
text = "hello"

# multi line
multi_line = """line1""" \
	"""line2""" \
	"""line3"""
print multi_line,

# substrings
name = 'engineer man'
first_name = name[0:8]
# 8 is not included 

# integer
num1 = 6

# float
dec1 = 5.4
print dec1

# conversion to string        using str() fn
to_string = str(num1)

# conversion to integer/float            using int(),float() fn
num_string = '5'     #string representation of 5 
to_int = int(num_string)
to_float = float(num_string)
