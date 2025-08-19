source .env

python -m swebench.inference.run_api \
    --dataset_name_or_path princeton-nlp/SWE-bench_oracle \
    --model_name_or_path gpt-5-nano-2025-08-07 \
    --output_dir ./outputs