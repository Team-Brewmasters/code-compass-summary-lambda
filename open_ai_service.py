import os

from openai import OpenAI


def call_chatgpt(prompt):
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)

    # Call the OpenAI ChatGPT API
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": '''.'''}, 
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
   "total_files": "integer",
   "total_lines_of_code": "integer"
 },
 "overview": {
   "architecture": {
     "high_level_components": [
       {
         "name": "string",
         "description": "string"
       }
     ],
     "data_flow": "string"
   },
   "performance": {
     "issues" (If no issues are found, simply say that there are no discernable issues. Be truthful, do not create an issue. Should be based on code.): [
       {
         "description": "string",
         "suggestions": ["string"]
       }
     ]
   },
   "security": {
     "vulnerabilities": [
       {
         "description": "string",
         "severity": "string",
         "fix_recommendations": ["string"]
       }
     ]
   }
 },
 "code_analysis": {
   "functions": [
     {
       "name": "string",
       "description": "string",
       "parameters": [
         {
           "name": "string",
           "type": "string",
           "description": "string"
         }
       ],
       "returns": {
         "type": "string",
         "description": "string"
       }
     }
   ],
   "classes" (Ensure you give every single class available): [
     {
       "name": "string",
       "methods": [
         {
           "name": "string",
           "description": "string",
           "visibility": "string"
         }
       ]
     }
   ],
   "files": [
     {
       "path": "string",
       "size": "integer",
       "summary": "string"
     }
   ]
 },
 "documentation": {
   "readme": "string",
   "code_comments": "float",
   "api_docs": [
     {
       "endpoint": "string",
       "method": "string",
       "description": "string"
     }
   ]
 },
 "suggestedQuestions": ["string","string"] (Give three potential questions a user might ask about the repository.),
}'''},
                  {"role": "user", "content": str(prompt)}],
    )

 
    # Extract the generated response from the API response
    generated_response = response.choices[0].message.content

    return generated_response

