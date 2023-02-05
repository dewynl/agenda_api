from typing import Optional
from pydantic import BaseModel
from connectors.airtable import AirtableTable

tasks_table = AirtableTable('appO3CJwAp5PlynMJ', 'Tasks')


AIRTABLE_FIELDS_NAME = {
    'name': 'Name',
    'description': 'Description',
    'status': "Status",
    'url': 'URL',
    'project': "Project"
}


class Task(BaseModel):
    name: str
    description: str
    status: str
    url: str
    project: str



def format_input_to_airtable(task: Task):
    result = {}
    for entry in task.dict().items():
        result[AIRTABLE_FIELDS_NAME[entry[0]]] = entry[1]
    return result
