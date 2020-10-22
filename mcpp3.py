import operator
def most_frequent():
    most_frequent =str(input("enter a string : "))
    string_dict = dict()
    for letter in most_frequent:
        if letter not in string_dict:
            string_dict[letter] = most_frequent.count(letter)
    order = sorted(string_dict.items(), key=operator.itemgetter(1), reverse=True)
    for i in order:
        print(i[0],i[1])
most_frequent()
