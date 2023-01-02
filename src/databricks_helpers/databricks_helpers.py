def current_user() -> str:
    return dbutils.notebook.entry_point.getDbutils().notebook().getContext().userName().get().split("@")[0]


def working_dir(current_user: str, exercise_name: str) -> str:
    return f"/FileStore/{current_user}/last_connection_time_of_chargepoint"


def setup_notebook(exercise_name: str):
    working_directory = working_dir(current_user(), exercise_name)
    dbutils.fs.rm(working_directory, True)
