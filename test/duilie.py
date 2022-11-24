def search_word_num(string):
    end = 0
    first = 0
    string_list = []
    for i in string:
        if i == ' ' or end == len(string)-1:
            if end == len(string)-1:
                string_list.append(string[first:])
                first = end + 1
            else:
                string_list.append(string[first:end])
                first = end + 1
        end = end + 1

    # print(string_list)
    # string_list = string.strip(" ")
    string_dic = {}
    for i in string_list:
        if i in string_dic.keys():
            string_dic[i] = string_dic[i] + 1
        else:
            string_dic[i] = 1
    print(string_dic)

search_word_num("hello world hello")
    