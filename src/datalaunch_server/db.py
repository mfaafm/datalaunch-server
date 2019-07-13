from pymongo import MongoClient


class DBApi(object):
    def __init__(self, client=MongoClient("mongodb://localhost:27017/")):
        self.client = client
        self.db = client.workspace

    def create_run(self, run):
        run_id = run["run_id"]

        if self.get_run(run_id) is not None:
            raise ValueError(f"Run with run_id {run_id}")
        else:
            self.db["run"].insert_one(run)
            del run["_id"]

    def get_run(self, run_id):
        return self.db["run"].find_one({"run_id": run_id}, projection={"_id": False})

    def update_run(self, run):
        self.db["run"].update_one(
            {"run_id": run["run_id"]}, {"$set": run}, upsert=False
        )

    def delete_run(self, run_id):
        self.db["run"].delete_one({"run_id": run_id})

    def get_run_ids(self):
        results = self.db["run"].find({}, projection={"_id": False, "run_id": True})
        return [r["run_id"] for r in results]

    def get_all_runs(self):
        results = self.db["run"].find({}, projection={"_id": False})
        return list(results)
