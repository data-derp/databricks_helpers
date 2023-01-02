class DataDerpDatabricksHelpers:
    def __init__(self, dbutils):
        self.dbutils = dbutils

    def current_user(self) -> str:
        return self.dbutils.notebook.entry_point.getDbutils().notebook().getContext().userName().get().split("@")[0]

    def working_directory(self, current_user: str, exercise_name: str) -> str:
        return f"/FileStore/{current_user}/{exercise_name}"

    def clean_notebook(self, working_dir: str) -> bool:
        self.dbutils.fs.rm(working_dir, True)
        return True
