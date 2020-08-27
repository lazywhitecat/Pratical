word_list = input('Enter your string:')
data = word_list.split(' ')
word_dict = {word:0 for word in data}
for keys in data:
    word_dict[keys]+=1
for list1,list2 in word_dict.items():
    print('{} - {}'.format(list1,list2))
