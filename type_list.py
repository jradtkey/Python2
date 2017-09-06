def types(arr):
    total = 0;
    string = []
    for value in range(0, len(arr)):
        if isinstance(arr[value], int) or isinstance(arr[value], float):
            total = total + arr[value]
        if isinstance(arr[value], basestring):
            string.append(arr[value])
            sent = ' '.join(string)

    if (total > 0) & (len(string) > 0):
        print("This is a mixed list")
        print('Sum: ' + str(total))
        print('String: ' + sent)
    if (total > 0) & (len(string) < 1):
        print("This is a list of integers")
        print('Sum: ' + str(total))
    if (total < 1) & (len(string) > 0):
        print("This is a list of strings")
        print('String: ' + sent)


arr = ['magical unicorns',19,'hello',98.98,'world']

types(arr)
