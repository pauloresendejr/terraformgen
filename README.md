TerraformGen

🌟 Introdução
Este é um modelo para uma aplicação Python simples, demonstrando o uso do uv como gerenciador de pacotes e executor de tarefas, otimizado para ambientes Mac, Linux e Windows. O objetivo é fornecer uma estrutura inicial robusta e fácil de usar para seus projetos Python.

🤔 Motivação
No desenvolvimento Python, gerenciar dependências e garantir ambientes consistentes pode ser um desafio. Este modelo visa simplificar esse processo, utilizando o uv para instalações de pacotes ultrarrápidas e um pyproject.toml para uma configuração de projeto moderna e padronizada. Ele serve como um ponto de partida ideal para qualquer novo projeto Python, desde scripts simples até aplicações mais complexas.

✨ Recursos
Gerenciamento de Dependências com uv: Aproveite a velocidade e eficiência do uv para gerenciar as dependências do seu projeto, garantindo instalações rápidas e consistentes.

pyproject.toml para Configuração Moderna: Utiliza o padrão pyproject.toml (PEP 621) para definir metadados do projeto, dependências e scripts, centralizando a configuração.

Geração Padronizada de HCL: Ferramenta para a geração padronizada de arquivos HCL (HashiCorp Configuration Language), ideal para projetos Terraform.

```pre
📁 Estrutura do Projeto
/
├── templates/
│   └── data.tf.j2       # Template Jinja2 para data blocks
│   └── locals.tf.j2     # Template Jinja2 para locals blocks
│   └── main.tf.j2       # Template Jinja2 para main configuration
│   └── output.tf.j2     # Template Jinja2 para output variables
│   └── providers.tf.j2  # Template Jinja2 para provider configuration
├── pyproject.toml       # Metadados do projeto e gerenciamento de dependências
├── genbase.config       # Arquivo de Configuração da Aplicação
├── LICENSE              # Arquivo de Licença do Projeto
├── main.py              # Arquivo principal da Aplicação
├── uv.lock              # Arquivo de Lock para Dependências (gerado pelo uv)
└── README.md            # Este arquivo
```

🛠️ Pré-requisitos
Para executar este projeto, você precisará ter o Python 3.9 ou superior instalado no seu sistema Mac, Linux ou Windows.

Recomendamos instalar o uv globalmente ou usando pipx para facilitar o uso em todos os seus projetos:

# No macOS e Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

# ou
```bash
pip install uv # ou pipx install uv
```

# No Windows:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

⚙️ Instalação e Execução
Siga os passos abaixo para configurar o ambiente e rodar a aplicação:

Clone o repositório:

```bash
git clone https://github.com/pauloresendejr/terraformgen.git
cd terraformgen
````

Para rodar a aplicação, execute o seguinte comando:

```bash
uv run main.py
````

Nota: O uv gerenciará automaticamente o ambiente virtual e as dependências definidas no pyproject.toml ao usar uv run.

📄 Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

🤝 Contribuição
Contribuições são sempre bem-vindas! Se você tiver sugestões, encontrou um bug ou quer adicionar um novo recurso, sinta-se à vontade para abrir uma issue ou enviar um pull request.

📞 Contato
Paulo Resende - pauloresendejr@gmail.com <br>
Repositório do Projeto: https://github.com/pauloresendejr/terraformgen

📚 Mais Recursos
- Documentação Oficial do uv - https://docs.astral.sh/uv/guides/install-python/