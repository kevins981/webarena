import json

in_file = "test.raw.json"
out_file = "test.raw.json.out"
out_list = []

#task_list = [4, 12, 13, 62, 63, 77, 78, 94, 95, 107, 108, 112, 114, 187, 193, 194, 199, 200, 212, 245]
task_list = [11, 12, 13, 14, 15, 41, 42, 43, 94, 95, 112, 113, 114, 119, 120, 121, 130, 131, 186, 187]

with open(in_file, 'r') as file:
    data = json.load(file)
    for item in data:
        if int(item["task_id"]) in task_list:
        #if "shopping_admin" == item["sites"][0]:
            #print(item)
            out_list.append(item)


with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(out_list, f, ensure_ascii=False, indent=4)
