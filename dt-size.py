import sys

data_types = [
    (int, 0),
    (float, 0.0),
    (bool, True),
    (str, '')

]

for t, v in data_types:
    print(t.__name__, " size is: ", sys.getsizeof(v), 'bytes')

# Output:
# int  size is:  28 bytes
# float  size is:  24 bytes
# bool  size is:  28 bytes
# str  size is:  41 bytes
