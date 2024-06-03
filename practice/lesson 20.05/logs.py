logs = [
    '192.168.0.1 /home',
    '192.168.0.1 /about',
    '192.168.0.2 /home',
    '192.168.0.1 /home',
    '192.168.0.2 /contact',
    '192.168.0.1 /about',
]
uniq_words = []
new_dict = {}
for i in logs:
    new_str = i.split()
    uniq_words.append(new_str[1])
for word in uniq_words:
    if word in uniq_words:
        new_dict[0] +=1
    else:
        new_dict[0] = 1
    #new_dict[new_str[0]] = new_str[1]
    # if new_str[1] in uniq_words:
    #     new_dict[new_str[0]] +=1
    # else:
    #     new_dict[new_str[0]] = 1
    #     uniq_words.append(new_str[1])
print(new_dict)
   