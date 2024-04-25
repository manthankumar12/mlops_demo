import yaml

def extract_source_code(yaml_file_path):
    try:
        # Load the YAML file
        with open(yaml_file_path, 'r') as file:
            data = yaml.safe_load(file)

        # Extract the source code from the YAML
        source_code = data['cells'][0]['config']['source']

        return source_code
    except Exception as e:
        print(f"Error occurred while extracting source code: {str(e)}")
        return None

def save_source_code(source_code, output_file_path):
    try:
        # Save the source code to output.py
        with open(output_file_path, 'w') as file:
            file.write(source_code)
        print(f"Source code extracted and saved as {output_file_path}")
    except Exception as e:
        print(f"Error occurred while saving source code: {str(e)}")

def main():
    yaml_file_path = 'hex/mlops.yaml'  # Replace with the path to your YAML file
    output_file_path = 'hex/output.py'  # Output file path

    # Extract source code from YAML
    source_code = extract_source_code(yaml_file_path)
    if source_code:
        # Save source code to output.py
        save_source_code(source_code, output_file_path)

if __name__ == "__main__":
    main()
