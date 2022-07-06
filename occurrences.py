#############
## FUNCTIONS
#############
def occurrences(string, substring):
    return string.count(substring)

def occurrences2(string, substring):
    count = 0
    while substring in string:
        if substring in string:
            count += 1
            string = string.replace(substring, "", 1)
    return count

def occurrences3(string, substring):
    count = 0
    next_letter = substring
    numerator = 0
    
    if len(substring) > 1:  
        len_substring = len(substring)
        for i in range(len(string)):
            for j in range(len(substring)):
                if string[i] == next_letter[0]:
                    count += 1
                    next_letter = next_letter[1:]
                    if count == len(substring): #an occurrence was found
                        numerator += len_substring
                        next_letter = substring
                        count = 0
                    break
                else:
                    next_letter = substring
                    count = 0                    
        return int(numerator / len_substring)
    else:
        for i in range(len(string)):
            if string[i] == substring:
                count += 1
        return count
    
#################
## TEST FUNCTIONS
#################

print(occurrences("fleep floop", "e"))
print(occurrences("fleep floop", "p"))
print(occurrences("fleep floop", "ee"))
print(occurrences("fleep floop", "fe"))
print(occurrences("fleep floop", "fl"))

print("_________________________________________________\n")

print(occurrences2("fleep floop", "e"))
print(occurrences2("fleep floop", "p"))
print(occurrences2("fleep floop", "ee"))
print(occurrences2("fleep floop", "fe"))
print(occurrences2("fleep floop", "fl"))

print("_________________________________________________\n")

print(occurrences3("fleep floop", "e"))
print(occurrences3("fleep floop", "p"))
print(occurrences3("fleep floop", "ee"))
print(occurrences3("fleep floop", "fe"))
print(occurrences3("fleep floop", "fl"))  