from decorators import dataIO

@dataIO
def test():
    print()
    return [('a', 'b', 'c')]

test()