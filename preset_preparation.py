import json
import os
import random

import pandas as pd



_AMOUNT_OF_PRESETS = 4

def save_items(df, id_field, id_list, save_path):
    df[df[id_field].isin(id_list)].to_json(save_path, orient="records", lines=True)

if __name__ == "__main__":
    question_df = pd.read_json('./question.jsonl', lines=True)

    answer_alpaca_df = pd.read_json('./answer/answer_alpaca-13b.jsonl', lines=True)
    answer_gpt_35_df = pd.read_json('./answer/answer_gpt35.jsonl', lines=True)
    answer_gpt_4_df = pd.read_json('./answer/answer_gpt-4.jsonl', lines=True)
    answer_vicuna_df = pd.read_json('./answer/answer_vicuna-13b.jsonl', lines=True)
    categories = question_df['category'].unique()

    for i in range(_AMOUNT_OF_PRESETS):
        sampled_list_ids = []

        for category in categories:
            topic_questions = question_df[question_df['category'] == category]

            question_id = random.sample(topic_questions['question_id'].to_list(), 1)
            sampled_list_ids.extend(question_id)

        save_items(question_df, id_field='question_id', id_list=sampled_list_ids, save_path=f'./sampled/questions/{i}.jsonl')

        save_items(answer_alpaca_df, id_field='question_id', id_list=sampled_list_ids, save_path=f'./sampled/answer_alpaca/{i}.jsonl')
        save_items(answer_gpt_35_df, id_field='question_id', id_list=sampled_list_ids, save_path=f'./sampled/answer_gpt35/{i}.jsonl')
        save_items(answer_gpt_4_df, id_field='question_id', id_list=sampled_list_ids, save_path=f'./sampled/answer_gpt4/{i}.jsonl')
        save_items(answer_vicuna_df, id_field='question_id', id_list=sampled_list_ids, save_path=f'./sampled/answer_vicuna/{i}.jsonl')