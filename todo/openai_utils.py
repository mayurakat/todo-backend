


import re
from openai import OpenAI
import json

# Connect to LM Studio
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def get_ai_task_suggestions(email_list):
    results = []
    for i, email_content in enumerate(email_list, start=1):
        prompt = f"""
        You are a project assistant.
        Read the email content and suggest only **one** most important actionable task.
        Email Content: {email_content}
        return only this Format json: {{Task: <description>,deadline: yyyy-mm-dd,priority: <high/medium/low>}}
        """

        response = client.chat.completions.create(
            model="Meta-Llama-3-8B-Instruct",  # Must match your loaded model in LM Studio
            messages=[
                {"role": "system", "content": "You are a helpful assistant that finds the single most important task in each email."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,  # Lower temperature for more focused output
            max_tokens=100
        )

        task = response.choices[0].message.content.strip()
        try:
            match = re.search(r'\{.*?\}', task, re.DOTALL)

            if match:
                json_str = match.group(0)
                data = json.loads(json_str)
                tasks = data
                tasks['email_number'] = i  # Add email number to the task
        except json.JSONDecodeError:
            print("Could not parse JSON. Raw output:")
            tasks = None
        results.append(tasks)

    return results

