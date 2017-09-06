
def stars(arr):
    for value in range(0,len(arr)):
        if isinstance(arr[value], basestring):
            letter = arr[value][0].lower()
            print str(letter) * len(arr[value])
        else:
            print "*" * arr[value]
arr = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
stars(arr)
