"""
Terraform Bootstrap Generator

This script provides a CLI application for generating Terraform bootstrap files using Jinja2 templates.

The application supports the following commands:
- Default: Displays a welcome message
- author: Shows information about the script's author
- generate: Creates Terraform bootstrap files based on configuration settings

The script reads configuration from 'genbase.config' and uses Jinja2 templates to generate:
- locals.tf
- data.tf
- output.tf
- providers.tf
- main.tf

Generated files are output to a 'bootstrap_output' directory.
"""
import cyclopts
from configparser import ConfigParser
import os
from jinja2 import Environment, FileSystemLoader

# Lendo Arquivo de Configuração
def load_config():
    config = ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), 'genbase.config')
    config.read(config_path)
    return config

# Carregando Configuração
config = load_config()

app = cyclopts.App(version=config['metadata']['version'])
appName = config['metadata']['application_name']


# Para desabilitar a versão
# app = App(version_flags=[])

@app.default()
def main():
    print("Bem-vindo ao "+str(appName)+" Use --help para ver opções.")

@app.command
def author():
    print(f"Autor: {config['metadata']['author']}")
    print(f"Github: {config['metadata']['githubprofile']}")

@app.command()
def generate():
    print("Gera arquivos de bootstrap do Terraform")

    output_dir = os.path.join(os.path.dirname(__file__), 'bootstrap_output')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    #print(template_dir)
    env = Environment(loader=FileSystemLoader(template_dir))
    context = {
        'tags': config['generate']['tags'],
        'provider': config['generate']['provider'],
        'profile': config['generate']['profile'],
        'region' :  config['generate']['region'],
        'allowed_account_ids': config['generate']['allowed_account_ids'],
        'terraform_version': config['generate']['terraform_version'],
        'bucket_name': config['generate']['bucket_name'],
        'project_name': config['generate']['project_name'],
        'aws_provider_version': config['generate']['aws_provider_version']

    }
    templates = {
        'locals.tf': 'locals.tf.j2',
        'data.tf': 'data.tf.j2',
        'output.tf': 'output.tf.j2',
        'providers.tf': 'providers.tf.j2',
        'main.tf': 'main.tf.j2'
    }

    # Gerar cada arquivo
    for output_file, template_file in templates.items():
        template = env.get_template(template_file)
        content = template.render(**context)
        
        with open(os.path.join(output_dir, output_file), 'w') as f:
            f.write(content)
    
    print(f"Arquivos Terraform gerados em {output_dir}")

if __name__ == '__main__':
    app()