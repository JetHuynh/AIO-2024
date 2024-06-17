# 2.dictionary - Character Count
def count_chars(string):
    result = {}
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    result = dict(sorted(result.items(), key=lambda x: x[0]))
    return result


print(count_chars('Happiness'))
print(count_chars('smiles'))
