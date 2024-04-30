import os

from openai import OpenAI


def call_chatgpt(prompt):
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)

    # Call the OpenAI ChatGPT API
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": '''You are a master engineer, analyze the provided software repository data and generate a comprehensive report covering the following aspects:
'''}, 
                  {"role": "system", "content": '''{
 "repository": {
   "name": "string",
   "description": "string",
   "technology_stack": {
     "languages": ["string"],
     "frameworks": ["string"],
     "databases": ["string"],
     "tools": ["string"]
   },
 },
 "suggestedQuestions": ["string","string"] (Give three potential questions a user might ask about the repository.),
}'''},
                  {"role": "user", "content": str(prompt)}],
    )

 
    # Extract the generated response from the API response
    generated_response = response.choices[0].message.content

    return generated_response

