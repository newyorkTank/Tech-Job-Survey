def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

def sorted_dupless(lineas):
    words = []
    for line in lineas:  # Cleanups
        # word = text.split('\n')  # Use first line to test parsing
        line = line.strip()
        if len(line) > 1:
            words.append(line.lower())
    words = remove_duplicates(words)
    words.sort()
    return words

def file2list(file):
    f = open(file, 'r+', encoding='utf-8', errors='ignore')
    lines = f.readlines()
    f.close()
    wlist = []
    for line in lines:  # Cleanups
        line = line.strip()
        if len(line) > 1:
            wlist.append(line.lower())
    return wlist

###################     BEGIN
f = 'cities.txt'
#f = 'search_words'
my_file = f
fresh_list = file2list(my_file)
results = sorted_dupless(fresh_list)
for x in results:
    print(x)
print('Comparing totals of DeDupped:' + str(len(results)) + ' and Original:' + str(len(fresh_list)))
#while len(results) != len(fresh_list):
go = input('Replace file ' + my_file + ' with Dedupped? (y/n):')
if go.lower() == 'y':
    fw = open(my_file, 'w')
    for x in results:
        fw.write(x + '\n')
    fw.close()
    fresh_list = file2list(my_file)
    print('Comparing totals of DeDupped:' + str(len(results)) + ' and updated file:' + str(len(fresh_list)))
else:
    print('. . . guess not.')
    #break
print('Done')