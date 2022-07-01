import json

with open('data/coco/word_dict.json') as json_file:
    data = json.load(json_file)

print('目前模型存取的單字量: ', len(data)-4)

def check(word):
    if word in data:
        return 'match', data[word]
    return 'not match'
