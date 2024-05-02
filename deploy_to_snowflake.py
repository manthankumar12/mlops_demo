import snowflake.connector
import requests
import os

# Snowflake connection parameters
snowflake_account = os.environ.get('ls31517.ap-southeast-1')
snowflake_user = os.environ.get('manthan')
snowflake_password = os.environ.get('Manthanrana123')
snowflake_role = os.environ.get('ACCOUNTADMIN')
snowflake_database = os.environ.get('SNOWLENS')
snowflake_schema = os.environ.get('DEMO')
snowflake_warehouse = os.environ.get('COMPUTE_WH')

# GitHub repository URL
github_repo_url = os.environ.get('https://github.com/manthankumar12/mlops_demo/blob/main/output.py')

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

    # Fetch the Python script from the GitHub repository
    response = requests.get(github_repo_url)
    python_script = response.text

    # Execute the Python script in Snowflake
    cursor.execute(python_script)

    # Commit the transaction
    conn.commit()

    # Print success message
    print("Python script deployed to Snowflake successfully.")

    # Close the Snowflake cursor and connection
    cursor.close()
    conn.close()

except Exception as e:
    print("Error:", e)
