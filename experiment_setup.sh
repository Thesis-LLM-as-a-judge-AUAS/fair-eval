#!/bin/bash

experiment_matrix=(
  "gpt35 vicuna-13b gpt-3.5-turbo 0 1"
  "gpt35 vicuna-13b gpt-4 0 1"
#  "gpt35 vicuna-13b gpt-3.5-turbo 0 3"
#  "gpt35 vicuna-13b gpt-4 0 3"
#  "gpt35 vicuna-13b gpt-3.5-turbo 0 6"
#  "gpt35 vicuna-13b gpt-4 0 6"
  "gpt35 vicuna-13b gpt-3.5-turbo 1 3"
  "gpt35 vicuna-13b gpt-4 1 3"
)
for i in $(seq 1 100); do
  mkdir -p sampled_review/"${i}"

  for i in "${!experiment_matrix[@]}"; do
      row="${experiment_matrix[$i]}"
      read -r m1 m2 eval_model bpc k <<< "$row"

      python3 FairEval.py \
          -q presets/"$i".jsonl \
          -a answer/answer_"$m1".jsonl answer/answer_"$m2".jsonl \
          -o sampled_review/"${i}"/"review_${m1}_${m2}_${eval_model}_mec${k}_bpc${bpc}.jsonl" \
          -m "$eval_model" \
          --bpc "$bpc" \
          -k "$k"
  done
done
