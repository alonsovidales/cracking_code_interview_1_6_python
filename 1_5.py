# Write a method to replace all spaces in a string with %20.

def replace_spaces(s):
    return s.replace(' ', '%20')

assert(replace_spaces('hello this is a test') == 'hello%20this%20is%20a%20test')
