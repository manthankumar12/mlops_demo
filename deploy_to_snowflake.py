import snowflake.connector
import requests

# Snowflake connection parameters
snowflake_account = 'ls31517.ap-southeast-1'
snowflake_user = 'manthan'
snowflake_password = 'Manthanrana123'
snowflake_role = 'ACCOUNTADMIN'
snowflake_database = 'SNOWLENS'
snowflake_schema = 'DEMO'
snowflake_warehouse = 'COMPUTE_WH'

# GitHub repository URL
github_repo_url = 'https://github.com/manthankumar12/mlops_demo/blob/main/output.py'

# Snowflake SQL to execute the Python script
snowflake_sql = """
CREATE OR REPLACE PROCEDURE EXECUTE_PYTHON_SCRIPT()
  RETURNS STRING
  LANGUAGE JAVASCRIPT
  EXECUTE AS CALLER
  AS
  $$
    var pythonScriptURL = '{github_repo_url}';
    var response = httpClient.get(pythonScriptURL);
    var pythonScript = response.body;
    var stmt = snowflake.createStatement({sqlText: pythonScript});
    var result = stmt.execute();
    return 'Script executed successfully.';
  $$;
""".format(github_repo_url=github_repo_url)

try:
    # Connect to Snowflake
    conn = snowflake.connector.connect(
        user=snowflake_user,
        password=snowflake_password,
        account=snowflake_account,
        role=snowflake_role,
        warehouse=snowflake_warehouse,
        database=snowflake_database,
        schema=snowflake_schema
    )

    # Create a Snowflake cursor
    cursor = conn.cursor()

    # Execute the Snowflake SQL to create the procedure
    cursor.execute(snowflake_sql.format(github_repo_url=github_repo_url))

    # Call the procedure to execute the Python script
    cursor.execute("CALL EXECUTE_PYTHON_SCRIPT()")

    # Fetch and print the result
    result = cursor.fetchone()[0]
    print(result)

    # Close the Snowflake cursor and connection
    cursor.close()
    conn.close()

except snowflake.connector.errors.ProgrammingError as e:
    print("Error:", e)
