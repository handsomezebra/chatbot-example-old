from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

anthropic = Anthropic()
completion = anthropic.completions.create(
    model="claude-2",
    max_tokens_to_sample=300,
    prompt=f"{HUMAN_PROMPT} How are you today?{AI_PROMPT}",
)

print(completion.completion)