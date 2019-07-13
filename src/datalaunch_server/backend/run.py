import uuid
from datetime import datetime


class RunBackend(object):
    def __init__(self, workspace):
        self.workspace = workspace
        self.db = workspace.db

    def create_run(self, specification):
        run_id = str(uuid.uuid4())

        run = {"run_id": run_id, "status": "created", "created": datetime.utcnow(),
               "specification": specification}

        self.db.create_run(run)

        return run

    def terminate_run(self, run_id):
        run = self.db.get_run(run_id)

        run["status"] = "terminated"
        run["terminated"] = datetime.now()
        self.db.update_run(run)

    def delete_run(self, run_id):
        run = self.get_run(run_id)
        if run["status"] != "terminated":
            self.terminate_run(run_id)
        self.db.delete_run(run_id)

    def get_run(self, run_id):
        return self.db.get_run(run_id)

    def get_run_ids(self):
        return self.db.get_run_ids()

    def get_all_runs(self):
        return self.db.get_all_runs()