import boto3

class DynamoCacheService:
    def __init__(self, table_name):
        self.table_name = table_name
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(table_name)

    def get_summary_data(self, repo):
        try:
            response = self.table.get_item(Key={'repo': repo})
            item = response.get('Item')
            if item:

                summary_data = {
                    'repository': {
                        'name': item.get('name'),
                        'description': item.get('description'),
                        'technology_stack': {
                            'languages': item.get('languages'),
                            'frameworks': item.get('frameworks'),
                            'databases': item.get('databases'),
                            'tools': item.get('tools')
                        },
                    },
                'suggestedQuestions': item.get('suggestedQuestions')
                }

                return summary_data
            return None
        
        except Exception as e:
            print(e)
            return None

def put_summary_data(self, repo, name, description, languages, frameworks, databases, tools, suggested_questions):
        item = {
            'repo': repo,
            'name': name,
            'description': description,
            'languages': languages,
            'frameworks': frameworks,
            'databases': databases,
            'tools': tools,
            'suggestedQuestions': suggested_questions   
        }
        self.table.put_item(Item=item)