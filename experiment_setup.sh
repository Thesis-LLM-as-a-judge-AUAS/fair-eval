#!/bin/bash

experiment_matrix=(
  "gpt35 vicuna-13b gpt-4 0 1 1"
  "gpt35 vicuna-13b gpt-3.5-turbo 0 1 1"
  "gpt35 vicuna-13b gpt-4 0 3 1"
  "gpt35 vicuna-13b gpt-3.5-turbo 0 3 1"
  "gpt35 vicuna-13b gpt-4 0 6 1"
  "gpt35 vicuna-13b gpt-3.5-turbo 0 6 1"
  "gpt35 vicuna-13b gpt-4 1 3 1"
  "gpt35 vicuna-13b gpt-3.5-turbo 1 3 1"
  "gpt35 vicuna-13b gpt-3.5-turbo 1 1 1"
  "gpt35 vicuna-13b gpt-3.5-turbo 1 5 1"
  "gpt35 vicuna-13b gpt-3.5-turbo 1 7 1"
  "gpt35 vicuna-13b gpt-3.5-turbo 1 3 0.2"
  "gpt35 vicuna-13b gpt-3.5-turbo 1 3 0.6"
  "gpt35 vicuna-13b gpt-3.5-turbo 1 3 1.4"
)

for row in "${experiment_matrix[@]}"; do
    read -r m1 m2 eval_model bpc k t <<< "$row"

    python3 FairEval.py \
        -q question.jsonl \
        -a answer/answer_"$m1".jsonl answer/answer_"$m2".jsonl \
        -o review/review_"${m1}_${m2}_${eval_model}_mec${k}_bpc${bpc}.json" \
        -m "$eval_model" \
        --bpc "$bpc" \
        -k "$k" -t "$t"
done
