import json
import os
import random

import pandas as pd


def save_items(df, id_field, id_list, save_path):
    df[df[id_field].isin(id_list)].to_json(save_path, orient="records", lines=True)


if __name__ == "__main__":
    with open('./review/review_gpt35_vicuna-13b_human.txt', 'r', encoding='utf-8') as f:
        text_lines = f.read().splitlines()

    question_df = pd.read_json('./question.jsonl', lines=True)
    question_df['ground_truth'] = text_lines
    question_df = question_df[question_df['ground_truth'] != 'TIE']

    answer_alpaca_df = pd.read_json('./answer/answer_alpaca-13b.jsonl', lines=True)
    answer_gpt_35_df = pd.read_json('./answer/answer_gpt35.jsonl', lines=True)
    answer_gpt_4_df = pd.read_json('./answer/answer_gpt-4.jsonl', lines=True)
    answer_vicuna_df = pd.read_json('./answer/answer_vicuna-13b.jsonl', lines=True)
    categories = question_df['category'].unique()

    sampled_list_ids = []

    for category in categories:
        topic_questions = question_df[question_df['category'] == category]

        question_id = random.sample(topic_questions['question_id'].to_list(), 1)
        sampled_list_ids.extend(question_id)

    save_items(question_df, id_field='question_id', id_list=sampled_list_ids,
               save_path=f'./repeated_sampled/questions.jsonl')

    save_items(answer_alpaca_df, id_field='question_id', id_list=sampled_list_ids,
               save_path=f'./repeated_sampled/alpaca.jsonl')
    save_items(answer_gpt_35_df, id_field='question_id', id_list=sampled_list_ids,
               save_path=f'./repeated_sampled/gpt35.jsonl')
    save_items(answer_gpt_4_df, id_field='question_id', id_list=sampled_list_ids,
               save_path=f'./repeated_sampled/gpt4.jsonl')
    save_items(answer_vicuna_df, id_field='question_id', id_list=sampled_list_ids,
               save_path=f'./repeated_sampled/vicuna.jsonl')
