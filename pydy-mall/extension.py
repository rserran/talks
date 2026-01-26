from databricks.sdk import WorkspaceClient
w = WorkspaceClient()
me = w.current_user.me()
print(me.user_name)
