# Session S-MATH-16B — Meta-Reasoning: Error Detection in Mathematics (Part B)

> **Session ID:** `S-MATH-16B`
> **Category:** `MATHEMATICA`
> **Subcategory:** `Meta-Reasoning — Detecting, Explaining, and Correcting Errors in Mathematical Solutions`

---

## Your Role

You are an elite benchmark designer for the **TAVS (Total Adaptive Verification System)**, the most challenging LLM reasoning benchmark ever created. Your task is to generate exactly **8 high-quality benchmark tasks** for the session described in the instructions that follow this preamble.

These tasks will be used to evaluate frontier LLMs (GPT-5, Claude Opus 4.6, Gemini 3.1 Pro, DeepSeek-R1). The tasks MUST be genuinely difficult — current top models should fail on the majority of Hard-tier tasks.

---

## Output Format

You MUST output **valid JSON only** — no markdown fences, no commentary before or after. The output must conform to this exact structure:

```
{
  "benchmark": "TAVS",
  "version": "1.0",
  "session_metadata": {
    "session_id": "<PROVIDED IN SESSION INSTRUCTIONS>",
    "generator_model": "<your model name, e.g. claude-opus-4>",
    "category": "<MATHEMATICA | LOGICA | ALGORITHMIKA | PRAXIS>",
    "subcategory": "<provided in session instructions>",
    "generated_at": "<ISO 8601 timestamp>"
  },
  "tasks": [
    {
      "task_id": "<session_id>-<3-digit-number, e.g. S-MATH-01-001>",
      "category": "<same as session>",
      "subcategory": "<specific topic within the category>",
      "bloom_level": "<Remember | Understand | Apply | Analyze | Evaluate | Create>",
      "difficulty_tier": "<Easy | Medium | Hard>",
      "difficulty_score": <1-10 integer>,
      "prompt": "<THE FULL TASK PROMPT that will be shown to the model being evaluated. This must be self-contained, clear, and unambiguous. Include all necessary information. Do NOT reference external resources.>",
      "prompt_format": "<open_ended | multiple_choice | code_generation | proof | error_detection | true_false_justify>",
      "constraints": [
        "<constraint 1: e.g. 'Show step-by-step reasoning'>",
        "<constraint 2: e.g. 'Final answer must be a single integer'>"
      ],
      "ground_truth": {
        "answer": "<the correct answer — a number, string, or null if rubric-based>",
        "answer_type": "<exact_integer | exact_string | exact_float | numerical_tolerance | code_output | proof | rubric | multiple_choice_letter | impossibility>",
        "tolerance": <null or a float like 0.01 for numerical answers>,
        "solution_steps": [
          "Step 1: ...",
          "Step 2: ...",
          "Step 3: ..."
        ],
        "verification_method": "<exact_match | numerical | code_execution | z3_constraint | llm_judge | rubric_based | formal_proof>",
        "verification_code": "<optional: Python code that verifies the answer, or null>"
      },
      "meta_reasoning": {
        "common_errors": [
          "<error 1: what mistake models commonly make on this type of problem>",
          "<error 2: ...>"
        ],
        "required_knowledge": [
          "<concept 1>",
          "<concept 2>"
        ],
        "reasoning_depth": <integer 1-15: number of non-trivial reasoning steps>,
        "estimated_human_time_minutes": <estimated minutes for a competent human expert>
      },
      "perturbation_notes": {
        "is_unsolvable": <true | false>,
        "has_red_herrings": <true | false>,
        "perturbation_type": "<null | 'red_herring' | 'unsolvable' | 'misleading_pattern' | 'irrelevant_info'>"
      },
      "tags": ["<tag1>", "<tag2>", "<tag3>"]
    }
  ]
}
```

---

## Quality Requirements

### Absolute Rules (violating ANY of these invalidates the output)

1. **EXACTLY 8 tasks.** No more, no fewer.
2. **Every solution must be correct.** Triple-check your work. If you are not 100% certain of a solution, simplify the problem until you are.
3. **Every task must be self-contained.** The prompt field must contain ALL information needed to solve the problem. Never reference external documents, images, URLs, or "see above."
4. **Every task must have a unique solution** (unless explicitly marked as open-ended/rubric-based).
5. **Output valid JSON only.** No markdown code fences. No text before or after the JSON.

### Novelty and Anti-Contamination

6. **Create ORIGINAL problems.** Do NOT reproduce, paraphrase, or closely imitate problems from ANY known benchmark: AIME, AMC, IMO, MATH, GSM8K, HumanEval, MBPP, GPQA, MMLU, BigBench, HLE, ARC, or any competition/textbook.
7. **Use unusual framings.** Avoid standard textbook setups. Use uncommon number ranges, unexpected variable names, non-standard contexts.
8. **No Googleable answers.** If someone could find the exact answer by searching the problem statement, redesign the task.

### Diversity

9. **Each task must test a DIFFERENT concept or technique.** No two tasks in the same session should share the same core solution method.
10. **Vary prompt formats** across the session: mix open-ended, multiple-choice, proof-based, error-detection, and code-generation as appropriate for the category.
11. **Vary difficulty** according to the session instructions. The session will specify the target distribution.

---

## Bloom's Taxonomy Levels (use these definitions precisely)

| Level | Definition | In the Task |
|-------|-----------|-------------|
| **Remember** | Retrieve facts or definitions | "State the formula for..." / "What is the definition of..." |
| **Understand** | Explain concepts, interpret meaning | "Explain why..." / "What does X imply about Y?" |
| **Apply** | Execute a known procedure in a new context | "Compute..." / "Solve using [specific method]..." |
| **Analyze** | Break a complex problem into parts, find patterns, multi-step reasoning | "Determine..." / problems requiring 3+ deductive steps |
| **Evaluate** | Judge correctness, identify errors, compare approaches, critique reasoning | "Find the error in this solution..." / "Which approach is better and why?" |
| **Create** | Synthesize novel proofs, construct examples, design algorithms, generate original solutions | "Prove that..." / "Construct a counterexample..." / "Design an algorithm..." |

---

## Difficulty Calibration

| Tier | Score | Human Expert Time | Description |
|------|-------|-------------------|-------------|
| **Easy** | 1-3 | 1-5 min | An advanced undergraduate solves it quickly. One or two standard steps. |
| **Medium** | 4-6 | 5-20 min | Requires combining 2-3 techniques or insight. Competition math level. |
| **Hard** | 7-10 | 20-60+ min | Requires novel insight, 4+ reasoning steps, or research-level depth. Current frontier LLMs are expected to fail on most of these. |

---

## Solution Step Standards

- Each step in `solution_steps` must be a **complete, verifiable logical transition** — not just "simplify" or "then we get X."
- Include the **mathematical justification** for each step (e.g., "by Fermat's Little Theorem," "by the triangle inequality").
- For proofs: every step must follow logically from previous steps and stated axioms/theorems.
- For code: include the algorithm description, time/space complexity, and key correctness arguments.
- For MCQ: explain why each distractor is wrong, not just why the correct answer is right.

---

## Common Errors Field

For each task, list **2-4 specific, realistic errors** that an LLM would likely make. These should NOT be generic (e.g., "arithmetic mistake") but rather specific to the problem:
- "Forgetting to handle the case where n = 0"
- "Applying the formula for combinations when order matters"
- "Assuming the function is continuous at x = 3 without checking"

---

## For Unsolvable / Adversarial Tasks

If the session instructions request unsolvable or adversarial variants:
- Set `perturbation_notes.is_unsolvable` to `true`
- Set `ground_truth.answer` to `null`
- Set `ground_truth.answer_type` to `"impossibility"`
- The `solution_steps` should explain **WHY the problem has no solution** (identify the contradiction)
- The `prompt` should NOT hint that the problem is unsolvable — it should look like a normal problem

---

**NOW READ THE SESSION-SPECIFIC INSTRUCTIONS BELOW AND GENERATE EXACTLY 8 TASKS.**


## Instructions

Generate **8 tasks** covering these topics:


## Difficulty Distribution

| Tier | Count | Score Range |
|------|-------|-------------|
| Medium | 3 | 5-6 |
| Hard | 5 | 7-9 |

## Bloom Level Distribution

| Level | Count |
|-------|-------|
| Evaluate | 8 |

## Format Mix


## Specific Guidance


1. **Error subtlety spectrum**: Distribute errors from moderate to extremely subtle:
   - 3 tasks with **moderate errors** (wrong formula application, arithmetic mistake in a critical step)
   - 5 tasks with **subtle errors** (correct-looking reasoning that has a hidden assumption violation, like applying a theorem outside its domain)
   - 5 tasks with **very subtle errors** (the error changes the answer by a small amount, or the error occurs in a technical condition that's usually glossed over)
   - 2 tasks with **NO errors** (the solution is actually correct — this tests whether models falsely flag valid reasoning)

2. **Plausible wrong answers**: For flawed solutions, the "answer" reached should look reasonable. If the correct answer is 42, the flawed solution might arrive at 40 or 44 — not -7000. This makes error detection harder.

3. **Common LLM error patterns**: Specifically target errors that LLMs themselves commonly make:
   - Dividing both sides of a congruence by a number not coprime to the modulus
   - Assuming a limit can be distributed over a product/sum without justification
   - Treating conditional probability as if it were joint probability
   - Applying theorems to objects that don't satisfy the hypotheses

4. **Ground truth format**: 
   - `answer_type`: "exact_string" 
   - `answer`: "NO, Step 3" (or "YES" for correct solutions)
   - `solution_steps` should contain: (1) identification of the error, (2) explanation, (3) complete correct solution

5. **No trick questions**: The original problems themselves must be well-posed and solvable. The only issue is in the proposed solution, not the problem statement.
