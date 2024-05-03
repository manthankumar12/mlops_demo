import snowflake.connector
import argparse
import os

def deploy_to_snowpark(file_path, snowflake_account, snowflake_user, snowflake_password, snowflake_database, snowflake_schema, snowflake_warehouse):
    # Connect to Snowflake
    ctx = snowflake.connector.connect(
        user=snowflake_user,
        password=snowflake_password,
        account=snowflake_account,
        warehouse=snowflake_warehouse,
        database=snowflake_database,
        schema=snowflake_schema
    )
    
    # Read the content of the Python file
    with open(file_path, 'r') as file:
        code = file.read()
    
    # Create a Snowpark script object
    script = ctx.create_snowpark_script()
    
    # Set the script content
    script.set_sql_text(code)
    
    # Execute the script
    result = script.execute()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Deploy Python file to Snowpark Snowflake')
    parser.add_argument('file_path', type=str, help='Path to the Python file to deploy')
    parser.add_argument('--account', type=str, default=os.getenv('SNOWFLAKE_ACCOUNT'), help='Snowflake account')
    parser.add_argument('--user', type=str, default=os.getenv('SNOWFLAKE_USER'), help='Snowflake user')
    parser.add_argument('--password', type=str, default=os.getenv('SNOWFLAKE_PASSWORD'), help='Snowflake password')
    parser.add_argument('--database', type=str, default=os.getenv('SNOWFLAKE_DATABASE'), help='Snowflake database')
    parser.add_argument('--schema', type=str, default=os.getenv('SNOWFLAKE_SCHEMA'), help='Snowflake schema')
    parser.add_argument('--warehouse', type=str, default=os.getenv('SNOWFLAKE_WAREHOUSE'), help='Snowflake warehouse')
    
    args = parser.parse_args()
    
    deploy_to_snowpark(args.file_path, args.account, args.user, args.password, args.database, args.schema, args.warehouse)
