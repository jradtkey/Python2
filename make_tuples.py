def make_tuples(my_dict):
    new_arr = []
    for key in my_dict:
        new_arr.append((key, my_dict[key]))
    print new_arr
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

make_tuples(my_dict)
