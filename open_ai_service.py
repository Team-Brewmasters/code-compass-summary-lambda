import os

from openai import OpenAI


def call_chatgpt(prompt):
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)

    # Call the OpenAI ChatGPT API
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": '''Analyze the provided software repository data and generate a comprehensive report covering the following aspects:
1. Overview of the repository including a summary of technology stack and key components.
2. Detailed code analysis identifying functions, classes, and key files, including any code smells and testing coverage insights.
3. Documentation quality assessment focusing on README, inline comments, and API documentation completeness.
4. Security analysis highlighting potential vulnerabilities, with severity ratings and recommendations for mitigation.
5. Performance analysis detailing any issues, their implications, and suggested optimizations.
6. Dependency analysis with details on library versions, potential security risks, and suggestions for updates.
7. Contributor statistics, including commit frequency, major contributors, and their areas of impact.
8. Information on build and deployment processes, change frequency of components, and any CI/CD practices.
9. Review of all software licenses involved to ensure compliance with legal requirements.
Please provide the analysis in a structured JSON format as outlined in the system specification document.'''}, 
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

