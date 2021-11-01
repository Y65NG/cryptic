import pandas as pd
import random as rd

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', ',', '.', '!', '+', '-', '*', '/', '=', '?', '<', '>', ';', ':', '"', '\'', '\\', '|', '_', '@', '#', '$', '%', '^', '&', '~', '`', '{', '}', '[', ']', '(', ')', '\n']

def generate_table(n):
    matchs = []
    for i in range(n):
        visited = set()
        match = [-1] * len(ALPHABET)
        
        for j in range(len(ALPHABET)):
            if match[j] == -1:
                visited.add(j)
                # print(list(set(range(len(ALPHABET))) - visited))
                other = rd.choice(list(set(range(len(ALPHABET))) - visited))
                visited.add(other)
                match[j] = other
                match[other] = j
            
        matchs.append(match)
    pd.DataFrame(matchs).to_csv('matchs.csv')
    return pd.DataFrame(matchs)

def read_table(table_name):
    return pd.read_csv(table_name)

def encrypt(text, tables, start, n):
    result = ''
    te = 0
    ta = start
    while te < len(text):
        # print(te)
        # print(ta)
        # print(list(tables.loc[ta]))
        table = list(tables.loc[ta])[1:]
        result += ALPHABET[table[ALPHABET.index(text[te])]]
        te += 1
        ta += 1
        if ta >= n:
            ta = 0
    return result

if __name__ == '__main__':
    # generate_table(100)
    tables = read_table('matchs.csv')
    choice = input('Encrypt(1) or decrypt(2)?\n')
    start = int(input('key?\n'))
    if choice == '1':
        text = input('Text to encrypt:\n')
        result = encrypt(text, tables, start, 100)
        print('Encrypted text:', result)
    elif choice == '2':
        text = input('Text to decrypt:\n')
        result = encrypt(text, tables, start, 100)
        print('Decrypted text:', result)
    else:
        print('Invalid choice')
    