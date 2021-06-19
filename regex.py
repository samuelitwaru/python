import re


my_string1 = "The Quick Blue Bird1234 Flew Over the Fast River"
my_string2 = "The Quick Blue Bird76521212 Flew Over the Fast River"

pattern1 = 'Blue'
pattern2 = 'Bird[012345678]+'
pattern3 = 'Fast'
pattern4 = 'Flew'
pattern5 = 'River'


def convert_string(my_string):
    # find 'Blue', replace with 'Brown' (pattern1)
    match = re.search(pattern, my_string)
    my_string = my_string.replace(my_string[match.start():match.end()], 'Brown')

    # find 'Bird followed by 1 or more numbers', replace with 'Cow' (pattern2)
    match = re.search(pattern2, my_string)
    my_string = my_string.replace(my_string[match.start():match.end()], 'Cow')

    # find 'Fast' replace with 'Lazy' (pattern3)
    match = re.search(pattern3, my_string)
    my_string = my_string.replace(my_string[match.start():match.end()], 'Lazy')

    # find 'Flew' replace with 'Jumped' (pattern4)
    match = re.search(pattern4, my_string)
    my_string = my_string.replace(my_string[match.start():match.end()], 'Jumped')

    # find 'River', replace with 'Moon' (pattern5)
    match = re.search(pattern5, my_string)
    my_string = my_string.replace(my_string[match.start():match.end()], 'Moon')
    
    return my_string



patterns = {
    'Blue': 'Brown',
    'Bird[0123456789]+': 'Cow',
    'Fast': 'Lazy',
    'Flew': 'Jumped',
    'River': 'Moon'    
}

def convert_string(my_string):
    for pattern, replacement in patterns.items():
        match = re.search(pattern, my_string)
        my_string = my_string.replace(my_string[match.start():match.end()], replacement)
    return my_string


print(convert_string(my_string1))
print(convert_string(my_string2))
