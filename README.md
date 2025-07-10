TerraformGen

🌟 Introdução 

🚀 Sobre o Projeto
    A aplicação escrita em Python simples, demonstra o uso do uv como gerenciador de pacotes e executor de tarefas, otimizado para ambientes Mac / Linux e Windows

🤔 Motivação
    No desenvolvimento Python, gerenciar dependências e garantir ambientes consistentes pode ser um desafio. Este modelo visa simplificar esse processo, utilizando
o uv para instalações de pacotes ultrarrápidas e um pyproject.toml para uma configuração de projeto moderna e padronizada. Ele serve como um ponto de partida ideal para qualquer novo projeto Python, desde scripts simples até aplicações mais complexas.

✨ Recursos

- Gerenciamento de Dependências com uv: Aproveite a velocidade e eficiência do uv para gerenciar as dependências do seu projeto, garantindo instalações rápidas e consistentes.

- pyproject.toml para Configuração Moderna: Utiliza o padrão pyproject.toml (PEP 621) para definir metadados do projeto, dependências e scripts, centralizando a configuração.

📁 Estrutura do Projeto
/
├── templates/
│   └── data.tf.j2       # Template Jinja2
│   └── locals.tf.j2     # Template Jinja2
│   └── main.tf.j2       # Template Jinja2
│   └── output.tf.j2     # Template Jinja2
│   └── providers.tf.j2  # Template Jinja2
├── pyproject.toml       # Metadados do projeto e gerenciamento de dependências
├── genbase.config       # Arquivo de Configuração
├── LICENSE              # Arquivo de Licenca
├── main.py              # Arquivo da Aplicação
├── uv.lock              # Arquivo de Lock para Dependencias
└── README.md            # Este arquivo


🛠️ Pré-requisitos
    Para executar este projeto, você precisará ter o Python 3.9 ou superior instalado no seu sistema Mac/Linux.

Recomendamos instalar o uv globalmente ou usando pipx para facilitar o uso em todos os seus projetos:

# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh 

pip install uv # ou pipx install uv

# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"


⚙️ Instalação
Siga os passos abaixo para configurar o ambiente e instalar as dependências no seu sistema Linux:

Clone o repositório:

git clone https://github.com/pauloresendejr/terraformgen.git
cd terraformgen

Para rodar a aplicação, execute o seguinte comando:

uv run main.py 