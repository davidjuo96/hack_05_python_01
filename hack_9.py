"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    new_result = []
    x = 0
    while x < len(result):
        new_result.append(x+1)
        new_result.append("@")
        x = x + 1
    return new_result