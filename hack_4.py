"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    result = ((result[::-1]).capitalize())[::-1]
    return result