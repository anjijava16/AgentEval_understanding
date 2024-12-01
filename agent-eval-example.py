import autogen
from autogen import Task, generate_criteria, quantify_criteria

# Configuration for OpenAI API
config_list = autogen.config_list_from_json("OAI_CONFIG_LIST")

# Define the task for math problem solving
math_task = Task(
    name="Math Problem Solving",
    description="Solve mathematical problems accurately and concisely",
    successful_response="""
    Problem: Find $24^{-1} \\pmod{11^2}$
    Solution: 
    1. Use Extended Euclidean Algorithm
    2. Compute modular inverse step by step
    3. Verify the result
    Answer: 239 (correct modular inverse)
    """,
    failed_response="""
    Problem: Find $24^{-1} \\pmod{11^2}$
    Solution: 
    - Incomplete steps
    - Incorrect calculation
    - No verification
    Answer: Incorrect or incomplete
    """
)

# Generate evaluation criteria
criteria = generate_criteria(
    task=math_task, 
    llm_config={"config_list": config_list},
    max_round=2,
    use_subcritic=True
)

# Example test case for quantification
test_case = """[
    {
        "content": "Find $24^{-1} \\pmod{11^2}$. That is, find the residue $b$ for which $24b \\equiv 1\\pmod{11^2}$.",
        "role": "user"
    },
    {
        "content": "To solve this, I'll use the Extended Euclidean Algorithm:\n1. gcd(24, 11^2) = 1\n2. Apply Extended Euclidean Algorithm\n3. The modular inverse is 239",
        "role": "assistant"
    }
]"""

# Quantify performance against criteria
quantifier_output = quantify_criteria(
    llm_config={"config_list": config_list},
    criteria=criteria,
    task=math_task,
    test_case=test_case,
    ground_truth="true"
)

# Print results
print("Generated Criteria:", criteria)
print("\nQuantification Results:", quantifier_output)
