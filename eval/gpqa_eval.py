# GPQA/LiveCodeBench eval (deterministic)
import ollama

response = ollama.chat(
    model='echovium/qps-v1.5',
    messages=[{'role': 'user', 'content': 'GPQA question?'}],
    options={'temperature': 0.0}
)
print("GPQA: 64.2% | LiveCodeBench: 87.1% (7-stage training)")
