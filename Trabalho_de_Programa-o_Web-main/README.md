# Trabalho_de_Programa-o_Web
trabalho de web
<h2>Instalação</h2>
<p>para fazer a instalação da aplicação você deve ter o python 3 instalado na sua maquina, além de ser recomendável a criação de um ambiente virtual de desenvolvimento 'venv'</p>
Passo 1- instale as dependencias necessarias da aplicação.<br>
 SO Windows
	
```
pip install requirements.txt       
```
 SO Linux

```
pip install -r requirements.txt
```
Após essa configurações é necessario fazer as migrações, com os comandos:

```
python manage.py makemigrations
python manage.py migrate
```
Após essa configurações já sera possivel rodar a aplicação utilizando-o

```
python manage.py runserver
```
<h2>Projeto</h2>
Comunidade de Receitas: Resgatando e Compartilhando Tradições Culinárias

No mundo atual, com o avanço das redes sociais, vemos praticamente tudo sendo postado e compartilhado. No entanto, aqueles preciosos livros de receitas antigos que nossos pais, avós e até bisavós possuíam acabam se perdendo no tempo, sujeitos a mofo, mudanças ou deterioração. O objetivo deste projeto é resgatar e manter vivas as receitas tradicionais de família, preservando também as histórias por trás de cada simples almoço, sobremesa e muito mais.

Nossa aplicação web oferece um cadastro simples para os usuários, onde eles podem criar uma conta com seu e-mail e senha. Após o registro, eles terão a possibilidade de cadastrar suas próprias receitas, fornecendo informações como nome, ingredientes, modo de preparo, foto, tempo de preparo e rendimento.

No entanto, antes de uma receita ser publicada, passará por uma análise de um moderador da comunidade. Essa avaliação tem o objetivo de garantir que todas as postagens estejam de acordo com as políticas da comunidade, evitando qualquer conteúdo inadequado ou indesejado. As receitas podem ser aprovadas ou rejeitadas, garantindo um ambiente seguro e confiável para todos os usuários.

Além disso, a aplicação também conta com uma página inicial que apresenta um feed com todas as receitas aprovadas. Assim, os usuários têm acesso rápido e fácil a uma variedade de pratos tradicionais compartilhados por outros membros da comunidade.

Junte-se a nós e faça parte dessa comunidade apaixonada por gastronomia, onde as tradições culinárias são preservadas e compartilhadas, conectando gerações e sabores de todo o mundo.

<h2>Alunos</h2>
Gabriel Corrêa Terra 21105570 <br>
Hermelan David K . N ( 19103894) <br>
Vinicius Dias de Paula Ramos 21102228 <br>
Marcelo de Oliveira (21104286)

<h2>Repositorio</h2>
https://github.com/GabrielTerra55/Trabalho_de_Programa-o_Web

<h2>Deploy</h2>
https://trabalhodeprograma-oweb-production.up.railway.app/