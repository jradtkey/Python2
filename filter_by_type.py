def func(val):
    if isinstance(val, int):
        if val >= 100:
            print("that's a big number")
        else:
            print("that's a small number")

    if isinstance(val, basestring):
        if len(val) > 50:
            print("long sentnece")
        else:
            print("short sentence")

    if isinstance(val, list):
        if len(val) >= 10:
            print("big list")
        else:
            print("short list")

val = []

func(val)
