##bajar archivo http
curl -O https://caelum-online-public.s3.amazonaws.com/2928-transformacao-manipulacao-dados/dados_vendas_clientes.json

#run program
python3 [program_name].py

source .venv/bin/activate

#Crear ambiente python: python3 -m venv venv
Ativar ambiente: source venv/bin/activate
Desactivar: deactivate 

Verificar los pacotes instalados:  pip freeze
pip freeze > requirements.txt