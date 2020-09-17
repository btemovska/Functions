def func(p1, p2, *args, k, **kwargs):
    print("positional-or-keyword:...{}, {}".format(p1, p2)) #positional-or-keyword:...1, 2
    print("var-positional (*args):..{}".format(args)) #var-positional (*args):..(3, 4, 5)
    print("keyword:.................{}".format(k)) #keyword:.................6
    print("var-keyword:.............{}".format(kwargs)) #var-keyword:.............{'key1': 7, 'key2': 8}


func(1, 2, 3, 4, 5, k=6, key1=7, key2=8)

