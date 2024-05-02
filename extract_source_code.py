import yaml
import os
import datetime

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

def save_source_code(source_code, output_dir):
    try:
        # Create the output directory if it doesnt exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate a unique output file name using timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        output_file_name = f"output_{timestamp}.py"
        output_file_path = os.path.join(output_dir, output_file_name)

        # Save the source code to the output file
        with open(output_file_path, 'w') as file:
            file.write(source_code)
        print(f"Source code extracted and saved as {output_file_path}")
        return output_file_path
    except Exception as e:
        print(f"Error occurred while saving source code: {str(e)}")
        return None

def main():
    yaml_file_path = 'hex/mlops.yaml'  # Replace with the path to your YAML file
    output_dir = 'hex'  # Output directory path

    # Extract source code from YAML
    source_code = extract_source_code(yaml_file_path)
    if source_code:
        # Save source code to a unique file in the output directory
        saved_file_path = save_source_code(source_code, output_dir)
        if saved_file_path:
            print(f"Saved source code as: {saved_file_path}")

if __name__ == "__main__":
    main()
