#!/usr/bin/python3

def find_integer(integers):

    odd_int = 0
    even_int = 0
    for x in integers[0:3]:
        if x % 2 == 0:
            even_int += 1
        else:
            odd_int += 1
    is_even = False
    if even_int >= 2:
        is_even = True
    # da questo punto sò se l'array ha maggioranza pari o dispari
    for x in integers:
        if is_even:
            if x % 2 == 1:
                return x
        else:
            if x % 2 == 0:
                return x

# variazione


def find_outlier(inte):
    odds = [x for x in inte if x % 2 != 0]
    evens = [x for x in inte if x % 2 == 0]
    return odds[0] if len(odds) < len(evens) else evens[0]


def high_and_low(number):
    num = [int(x) for x in number.split()]
    x = str(max(num))
    y = str(min(num))
    return x + ' ' + y


def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return


def count_bits(n):
    x = bin(n)
    return x.count('1')


def solution(string, ending):  # oppure uso il metodo predefinito .endswith
    return ending in string[-len(ending):]


def get_sum(a, b):
    #good luck!
    sum = 0
    i = b
    x = a
    if a > b:
        while i <= a:
            sum = sum + i
            i = i + 1
        return sum
    elif a < b:
        while x <= b:
            sum = sum + x
            x = x + 1
        return sum
    else:
        return a or b


def repeat_str(repeat, string):
    x = string
    for i in range(repeat):
        x += string
    return x

def ripeti_stringa(rep, stri):
    for i in range(rep):
        stri = stri + stri
    return stri

def to_jaden_case(string):
    i = string.split()
    y = [x[0].upper() for x in i]
    z = [x[1:].lower() for x in i]
    q = [y[index]+z[index] for index in range(len(y))]
    one_hour_later = ' '.join(q)
    return one_hour_later

def friend(x):
    #Code
    y = [i for i in x if len(i) == 4]

def find_needle(haystack):
    # your code here
    for index in range(len(haystack)):
        if haystack[index] == 'needle':
            return 'found the needle at position ' + str(index)


def find_short(s):
    # your code here
    x = s.split()
    i = 0
    z = len(x[0])
    while i < len(x):
        y = len(x[i])
        if y < z:
            z = y
        i += 1
    return z

def find_average(numbers):
    # your code here
    x = 0
    n = 0
    for i in numbers:
        x += i
        n += 1
    return x / n

def abbrev_name(name):
    x = name.split()
    y = [z[0].upper() for z in x]
    return y[0] + '.' + y[1]



def disemvowel(string_):
    y = [x for x in string_ if x != 'a' and x != 'e' and x != 'i' and x != 'o' and x != 'u']
    return ''.join(y)


def is_square(n):
    if n < 0:
        return False
    elif n // pow(n, 1/2) == pow(n, 1/2):
        return True
    elif n == 0:
        return True
    else:
        return False


def DNA_strand(dna):
    # code here
    dnacs = []
    for x in dna:
        if x == 'A':
            dnacs.append('T')
        elif x == 'T':
            dnacs.append('A')
        elif x == 'C':
            dnacs.append('G')
        else:
            dnacs.append('C')
    return ''.join(dnacs)


def sum_two_smallest_numbers(numbers):
    #your code here
    numbers.sort()
    return numbers[0] + numbers[1]


def is_isogram(string):
    # your code here
    x = 0
    for i in string.lower():
        if string.lower().count(i) > 1:
            x += 1
        else:
            x += 0
    return True if x == 0 else False


def add_binary(a,b):
    #your code here
    x = bin(a + b)
    return x[2:]


# Given a string of words, you need to find the highest scoring word.
#
# Each letter of a word scores points according to its position in the alphabet et: a = 1, b = 2, c = 3c.
#
# You need to return the highest scoring word as a string.
#
# If two words score the same, return the word that appears earliest in the original string.
#
# All letters will be lowercase and all inputs will be valid.


# def high(x):
#     # Code here
#     alfabet = 'abcdefghijklmnopqrstuvwxyz'
#     valori = {letter: ord(letter) for letter in alfabet}
#     x = x.split()
#     y = []
#     z = 0
#     while z < len(x):
#         y.append(0)
#         i = 0
#         while i < len(x[z]):
#             y[z] += [x[z][i]]
#             i += 1
#         z += 1
#     # trova l'indice di max(y)
#     indice = y.index(max(y))
#     return x[indice]


def reverse_seq(n):
    return list(range(n, 0, -1))


def likes(names):
    # make a dictionary d of all the possible answers. Keys are the respective number
    # of people who liked it.

    # {} indicate placeholders. They do not need any numbers but are simply replaced/formatted
    # in the order the arguments in names are given to format
    # {others} can be replaced by its name; below the argument "others = length - 2"
    # is passed to str.format()
    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
    }
    length = len(names)
    # d[min(4, length)] insures that the appropriate string is called from the dictionary
    # and subsequently returned. Min is necessary as len(names) may be > 4

    # The * in *names ensures that the list names is blown up and that format is called
    # as if each item in names was passed to format individually, i. e.
    # format(names[0], names[1], .... , names[n], others = length - 2
    return d[min(4, length)].format(*names, others=length - 2)


def unique_in_order(iterable):
    iterable = str(iterable) + ' '
    lista = []
    i = 0
    while i < len(iterable) - 1:
        if iterable[i] != iterable[i + 1]:
            lista.append((iterable[i]))
        i += 1
    return lista


def delete_nth(order, max_e):
    # code here
    i = 0
    lista = []
    while i < len(order) - 2:
        for number in order:
            lista.append(number)
            if order[0:2 + i].count(number) >= max_e:
                lista.append(number)
        i += 1
    return lista
# prendo il primo elemento e conto quante volte si è presentato fino a questo momento nell'array x[0:2].count(n1), x[:2+i].count[n2] dove i cresce di 1 ogni ciclo ecc
# if x[0:2+i].count(elemento1) <= max_e allora .append(elemento1) if


def square_sum(numbers):
    #your code here
    sum = 0
    for i in numbers:
        sum += i**2
    return sum


def get_middle(s):
    #your code here
    x = len(s)
    if x % 2 == 0:
        i = int((x/2) - 1)
        return s[i:i + 2]
    else:
        i = x // 2
        return str(s[i])


def maps(a):
    mapsx = [i + i for i in a]
    return mapsx


def nb_year(p0, percent, aug, p):
    # your code
    years = 0
    population = p0
    while population < p:
        population += population * percent + aug
        years += 1
    return years


def longest(a1, a2):
    # your code
    x = sorted(set(a1 + a2))
    y = ''
    for letter in x:
        y += letter
    return y


def longest_consec(strarr, k):
    # your code
    list = []
    lenlist = []
    i = 0
    valmax = 0
    imax = 0
    while i < len(strarr) - (k - 1):
        list.append([])
        x = 0
        while x < k:
            list[i].append(strarr[i + x])
            x += 1
        lenlist.append(len(''.join(list[i])))
        if lenlist[i] > valmax:
            valmax = lenlist[i]
            imax = i
        i += 1
    return ''.join(list[imax])


def check(seq, elem):
    i = 0
    x = False
    while i < len(seq):
        if seq[i] != elem:
            i += 1
        elif seq[i] == elem:
            x = True
            i += 1
    return x


def fake_bin(x):
    pass
    i = 0
    result = ''
    while i < len(x):
        if int(x[i]) < 5:
            result += '0'
        else:
            result += '1'
        i += 1
    return result


def array_diff(a, b):
    # your code here
    i = 0
    bro_i_hate_you = []
    while i < len(a):
        ii = 0
        y = True
        while ii < len(b):
            if a[i] == b[ii]:
                y = False
            ii += 1
        if y:
            bro_i_hate_you.append(a[i])
        i += 1
    return bro_i_hate_you


def row_sum_odd_numbers(n):
    #your code here
    triangle = []
    ne = sum(range(n, -1, -1))
    i = 0
    while i < ne*2:
        if i % 2 == 1:
            triangle.append(i)
        i += 1
    return triangle[-1:-n:-1]


def sum_array(arr):
    #your code here
    x = sorted(arr)
    return sum(x[1:-1])


def sort_array(source_array):
    # Return a sorted array.
    odd = [i for i in source_array if i % 2 == 1]
    odd = sorted(odd)
    i = 0
    ii = 0
    while i < len(source_array):
        if source_array[i] % 2 == 1:
            source_array[i] = odd[ii]
            ii += 1
        i += 1
    return source_array


def reverse_words(text):
  #go for it
    text = text.split(' ')
    i = 0
    reverse = ''
    while i < len(text):
        reverse += (text[i][::-1])
        reverse += ' '
        i += 1
    return reverse[0:-1]


def duplicate_encode(word):
    # your code here
    i = 0
    newstring = ''
    while i < len(word):
        if word.count(word[i]) > 1:
            newstring += '('
        else:
            newstring += ')'
        i += 1
    return newstring


def persistence(n):
    # your code
    ns = str(n)
    persistence = 0
    while len(ns) > 1:
        i = 0
        moltiplicazione = 1
        while i < len(ns):
            moltiplicazione *= int(ns[i])
            i += 1
        persistence += 1
        ns = str(moltiplicazione)
    return persistence


def generate_hashtag(s):
    #your code here
    if s == '':
        return False
    hastag = [word[0].upper() + word[1:] for word in s.split()]
    if len(hastag) > 140:
        return False
    return '#' + ''.join(hastag)


def zeros(n):
    # Initialize result
    count = 0

    # Keep dividing n by
    # powers of 5 and
    # update Count
    i = 5
    while (n / i >= 1):
        count += int(n / i)
        i *= 5

    return int(count)


