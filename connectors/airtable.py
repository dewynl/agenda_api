import os
from dotenv import load_dotenv
from pyairtable import Table
load_dotenv()

class AirtableTable:
    def __init__(self, base_id: str, table_name: str) -> None:
        self.base_id = base_id
        self.table_name = table_name
        self.connection = Table(os.environ.get('AIRTABLE_AUTH_TOKEN'),  base_id=self.base_id, table_name=self.table_name)

    def get_record(self, record_id: str):
        return self.connection.get(record_id)

    def get_tasks_list(self, skip:int =0, limit:int = 100):
        return self.connection.iterate(max_records=limit)

    def create_task(self, payload: dict):
        return self.connection.create(payload, typecast=True)

    def update_task(self, record_id: str, fields: dict):
        return self.connection.update(record_id=record_id, fields=fields, typecast=True)