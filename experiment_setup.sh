#!/bin/bash

experiment_matrix=(
  "gpt35 vicuna gpt-3.5-turbo 0 1"
  "gpt35 vicuna gpt-4 0 1"
#  "gpt35 vicuna-13b gpt-3.5-turbo 0 3"
#  "gpt35 vicuna-13b gpt-4 0 3"
#  "gpt35 vicuna-13b gpt-3.5-turbo 0 6"
#  "gpt35 vicuna-13b gpt-4 0 6"
#  "gpt35 vicuna gpt-3.5-turbo 1 3"
#  "gpt35 vicuna gpt-4 1 3"
)
for i in $(seq 1 40); do
  mkdir -p repeated_experiment_results/"${i}"

  for j in "${!experiment_matrix[@]}"; do
      row="${experiment_matrix[$j]}"
      read -r m1 m2 eval_model bpc k <<< "$row"

      python FairEval.py \
          -q repeated_sampled/questions.jsonl \
          -a repeated_sampled/answer_"$m1".jsonl repeated_sampled/answer_"$m2".jsonl \
          -o repeated_experiment_results/"${i}"/"review_${m1}_${m2}_${eval_model}_mec${k}_bpc${bpc}.jsonl" \
          -m "$eval_model" \
          --bpc "$bpc" \
          -k "$k"
  done
done
