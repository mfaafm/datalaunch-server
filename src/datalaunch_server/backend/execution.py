import time
from datetime import datetime


class RunExecution(object):
    def __init__(self, workspace, run_id):
        self.workspace = workspace
        self.run_id = run_id
        self.db = workspace.db

    def _update_run(self, fields):
        run = self.db.get_run(self.run_id)
        run.update(fields)
        self.db.update_run(run)

    def run(self):
        self.build_run()
        self.start_run()

    def build_run(self):
        self._update_run({"status": "building", "build_started": datetime.utcnow()})

        time.sleep(10)

        self._update_run(
            {"status": "build finished", "build_finished": datetime.utcnow()}
        )

    def start_run(self):
        self._update_run({"status": "running", "run_started": datetime.utcnow()})

        time.sleep(10)

        self._update_run({"status": "run finished", "run_finished": datetime.utcnow()})
