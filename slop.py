#
# def remove_duplicates(values):
#     output = []
#     seen = set()
#     for value in values:
#         # If value has not been encountered yet,
#         # ... add it to both list and set.
#         if value not in seen:
#             output.append(value)
#             seen.add(value)
#     return output
#
# def sorted_dupless(lineas):
#     words = []
#     for line in lineas:  # Cleanups
#         # word = text.split('\n')  # Use first line to test parsing
#         line = line.strip()
#         if len(line) > 1:
#             words.append(line.lower())
#     words = remove_duplicates(words)
#     words.sort()
#     return words
#
# def file2list(file):
#     f = open(file, 'r+', encoding='utf-8', errors='ignore')
#     lines = f.readlines()
#     f.close()
#     wlist = []
#     for line in lines:  # Cleanups
#         line = line.strip()
#         if len(line) > 1:
#             wlist.append(line.lower())
#     return wlist
#
# ###################     BEGIN
# my_file = 'search_words'
# fresh_list = file2list(my_file)
# results = sorted_dupless(fresh_list)
# for x in results:
#     print(x)
# print('Comparing totals of DeDupped:' + str(len(results)) + ' and Original:' + str(len(fresh_list)))
# while len(results) != len(fresh_list):
#     go = input('Replace file ' + my_file + ' with Dedupped? (y/n):')
#     if go.lower() == 'y':
#         fw = open(my_file, 'w')
#         for x in results:
#             fw.write(x + '\n')
#         fw.close()
#         fresh_list = file2list(my_file)
#         print('Comparing totals of DeDupped:' + str(len(results)) + ' and updated file:' + str(len(fresh_list)))
#     else:
#         print('. . . guess not.')
#         break
# print('Done')
#
# print('Begin')
# x = [1,2,3,4,5,6]
# for i in x:
#     print('.', end='', flush=True)
import openpyxl
def open_sheet(filename, sheetname):
    wb = openpyxl.load_workbook(filename=filename)
    return wb.get_sheet_by_name(sheetname)

def read_table(sheet, columnnames, header_row=0):
    name_to_index = {
        n: i for i, n
        in enumerate(c.value for c in sheet.rows[header_row])
        if n is not None}
    column_indices = [name_to_index[n] for n in columnnames]

    for row in sheet.rows[header_row + 1:]:
        yield dict(zip(columnnames, (row[x].value for x in column_indices)))


if __name__ == "__main__":
    from operator import itemgetter
    import pprint

    # read data from Excel
    rows = read_table(
        open_sheet("sample.xlsx", "SampleSheet"),
        "Name Length Width Quantity".split(),
        2  # replace with actual header row
    )

    # add Area
    dict_list = []
    for row_dict in rows:
        row_dict["Area"] = row_dict["Width"] * row_dict["Length"]
        dict_list.append(row_dict)

    # sort and print data
    print("Unsorted:")
    pprint.pprint(dict_list)
    for sort_column in "Width", "Quantity":
        print("\nby {}:".format(sort_column))
        dict_list.sort(key=itemgetter(sort_column))
        pprint.pprint(dict_list)


To use xlrd instead of openpyxl you have to replace the open_sheet() and
read_table() functions with

def open_sheet(filename, sheetname):
    wb = xlrd.open_workbook(filename)
    return wb.sheet_by_name(sheetname)


def read_table(sheet, columnnames, header_row=0):
    name_to_index = {
        c.value: i for i, c
        in enumerate(sheet.row(header_row))
        if c.ctype == xlrd.XL_CELL_TEXT}
    column_indices = [name_to_index[n] for n in columnnames]
    for rowindex in range(header_row + 1, sheet.nrows):
        row = sheet.row(rowindex)
        yield dict(zip(columnnames, (row[x].value for x in column_indices)))


