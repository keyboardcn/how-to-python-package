def print_args(*args):
    '''
    Description
    '''
    for i in range(len(args)):
        print(args[i])

print_args(*[1, [3, 5]])
print(print_args.__doc__)