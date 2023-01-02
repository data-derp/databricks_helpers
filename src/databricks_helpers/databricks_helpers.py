class DataDerpDatabricksHelpers:
    def __init__(self, dbutils, exercise_name):
        self.dbutils = dbutils
        self.exercise_name = exercise_name

    def current_user(self) -> str:
        return self.dbutils.notebook.entry_point.getDbutils().notebook().getContext().userName().get().split("@")[0]

    def working_directory(self) -> str:
        return f"/FileStore/{self.current_user()}/{self.exercise_name}"

    def clean_working_directory(self) -> bool:
        self.dbutils.fs.rm(self.working_directory(), True)
        return True
