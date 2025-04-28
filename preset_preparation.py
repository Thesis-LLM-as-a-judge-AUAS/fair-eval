import json
import os
import random


def get_json_list(file_path):
    file_path = os.path.expanduser(file_path)
    with open(file_path, "r") as f:
        json_list = []
        for line in f:
            json_list.append(json.loads(line))
        return json_list

_AMOUNT_OF_PRESETS = 8

if __name__ == "__main__":
    question_list = get_json_list('./question.jsonl')

    categories = set(map(lambda x: x['category'], question_list))

    for i in range(_AMOUNT_OF_PRESETS):
        sampled_list = []

        for category in categories:
            topic_questions = list(filter(lambda x: x['category'] == category, question_list))

            sampled_list.extend(random.sample(topic_questions, 1))

        with open(f'./presets/{i}.jsonl', 'w') as f:
            for item in sampled_list:
                json.dump(item, f)
                f.write('\n')