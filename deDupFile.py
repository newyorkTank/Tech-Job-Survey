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

# Remove duplicates from this list.
#values = [5, 5, 1, 1, 2, 3, 4, 4, 5]
f = open('search_words', 'r', encoding='utf-8', errors='ignore')
lines = f.readlines()
f.close()
words = []
for line in lines:   # Cleanups
    #word = text.split('\n')  # Use first line to test parsing
    line = line.strip()
    if len(line) > 1:
        words.append(line.lower())
result = remove_duplicates(words)
for x in result:
    print(x)
print(len(words))
print(len(result))
