import json
import os

def generate_json(data):
    res = json.dumps(data, indent=4, ensure_ascii=False)
    return res


def create_json_file(data):
    
    if os.path.isdir('result') is False:
        os.mkdir('result')
        
    with open('./result/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f,  ensure_ascii=False, indent=4)