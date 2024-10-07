import json
import os
from jinja2 import Environment, FileSystemLoader

def load_config():
    with open('config.json') as config_file:
        return json.load(config_file)

def generate_template(resource_type, resource_name):
    env = Environment(loader=FileSystemLoader('src/templates'))
    template = env.get_template('template.jinja2')

    # Generate the template with user-defined resource
    output = template.render(resource_type=resource_type, resource_name=resource_name)
    
    return output

def main():
    config = load_config()
    
    # User input
    resource_type = input("Enter resource type (e.g., EC2, S3): ")
    resource_name = input("Enter resource name: ")
    
    # Generate CloudFormation template
    template_output = generate_template(resource_type, resource_name)
    
    # Output the generated template to a file
    output_file = os.path.join('output', f'{resource_name}-template.yaml')
    with open(output_file, 'w') as f:
        f.write(template_output)
    
    print(f"CloudFormation template generated: {output_file}")

if __name__ == "__main__":
    main()

