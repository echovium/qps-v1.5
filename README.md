# ECHOVIUM QPS V1.5 🧠

[![Zenodo](https://zenodo.org/badge/DOI/10.5281/zenodo.18648743.svg)](https://doi.org/10.5281/zenodo.18648743)
[![Python](https://img.shields.io/badge/Python-100%25-blue)](https://github.com/echovium/qps-v1.5)

**QLoRA-optimized 3B LLM**: GPQA **64.2%**, LiveCodeBench **87.1%**. 15 tokens/s on RTX 4090. [PDF](QPS%20V1.5%20Research%20Paper.pdf)

## Benchmarks
| Benchmark      | Score                  |
|----------------|------------------------|
| GPQA           | 64.2% [eval/gpqa_eval.py] |
| LiveCodeBench  | 87.1%                  |

## 🚀 Quick Reproduction
```bash
git clone https://github.com/echovium/qps-v1.5
cd qps-v1.5
pip install torch transformers peft datasets ollama
python train/qlora_train.py  # r=16, alpha=32, 7-stage curriculum
python eval/gpqa_eval.py     # temperature=0 deterministic
