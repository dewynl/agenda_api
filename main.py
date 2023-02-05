import os
from fastapi import FastAPI
from connectors.airtable import AirtableTable
from models.task import Task, format_input_to_airtable

app = FastAPI()
tasks_table = AirtableTable(os.environ.get('AGENDA_BASE_ID'), os.environ.get('TASK_TABLE_NAME'))

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/tasks")
def read_task(skip: int = 0, limit: int = 10):
    records = tasks_table.get_tasks_list()
    return records

@app.get("/task/{task_id}")
def read_task(task_id: str):
    record = tasks_table.get_record(task_id)
    return record
    
@app.post("/task/create")
def create_task(task: Task):
    formatted_input = format_input_to_airtable(task=task)
    new_record = tasks_table.create_task(formatted_input)
    return new_record

@app.post("/task/update/{task_id}")
def update_task(task_id: str, task: Task):
    formatted_input = format_input_to_airtable(task=task)
    updated_record = tasks_table.update_task(record_id=task_id, fields=formatted_input)
    return updated_record    


