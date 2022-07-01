def occurrences(string, substring):
    return string.count(substring)

def occurrences2(string, substring):
    count = 0
    while substring in string:
        if substring in string:
            count += 1
            string = string.replace(substring, "", 1)
    return count

print(occurrences("fleeeep floop", "e"))
print(occurrences("fleep floop", "p"))
print(occurrences("fleep floop", "ee"))
print(occurrences("fleep floop", "fe"))
print(occurrences("fleep floop", "fl"))

print("_________________________________________________\n")

print(occurrences2("fleeeep floop", "e"))
print(occurrences2("fleep floop", "p"))
print(occurrences2("fleep floop", "ee"))
print(occurrences2("fleep floop", "fe"))
print(occurrences2("fleep floop", "fl"))