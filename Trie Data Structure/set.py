# words = set()
# with open('techwords.txt', 'r') as fh:
#     for line in fh:
#         words.add(fh)
# print(words.len)
# import re
# # input
# to_search = input("enter letters in words to search for")
# for i in words:
#     x = re.search(to_search, i)
# print(x)

test_list = []
with open('techwords.txt', 'r') as fh:
    for line in fh:
        test_list.append(line)
start_letter = 'go'
with_s = [x for x in test_list if x.startswith(start_letter)]
print("The list with prefix s : " + str(with_s))