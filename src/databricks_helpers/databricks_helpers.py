# def get_dbutils(spark):
#   from pyspark.dbutils import DBUtils
#   return DBUtils(spark)
#
# def current_user() -> str:
#     return
#
#
def working_dir(current_user: str, exercise_name: str) -> str:
    return f"/FileStore/{current_user}/last_connection_time_of_chargepoint"


def setup_notebook(exercise_name, dbutils_session):
    current_user = dbutils_session.notebook.entry_point.getDbutils().notebook().getContext().userName().get().split("@")[0]
    working_directory = working_dir(current_user, exercise_name)
    dbutils_session.fs.rm(working_directory, True)
    return current_user, working_directory
