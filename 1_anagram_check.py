s1 = 'hola'
s2 = 'aloh'


def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    print(sorted(s1) == sorted(s2))


anagram(s1, s2)
