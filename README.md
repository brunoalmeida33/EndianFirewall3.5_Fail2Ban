# EndianFirewall3.5_Fail2Ban
Addon Fail2ban for Endian Firewall Community 3.2.x.

<br>

Descrição:
------

O Fail2Ban é uma estrutura de software de prevenção de intrusões que protege os servidores de computadores contra ataques de força bruta.

<br>

Inicialmente configurei este pacote para proteger os serviços SSH (Porta padrão 22), OPENVPN (Porta padrão 1194) e Painel de Controle do Endian (Portas Padrões 80, 443 e 10443), logo apos a quantidade estipulada de erros de login ser atingida, automaticamente o IP atacante sera bloqueado pelo tempo configurado.

<br>

Versão:
--------

v.2.0 ( Testado no Endian Firewall Community na versão 3.2.5).

<br>

Requerimentos/opcional:
--------
- Requer: Acesso SSH ao Servidor e configuração de "Proxy SMTP" para o envio de alertas por e-mail.

<br>

<br>

Realizando download do pacote:
--------

Para realizar a compra/download do pacote acesse o site http://www.4nsecurity.com.br/loja/EndianFirewall_Fail2ban. 

Obs: O Arquivo pode ser enviado para o firewall atraves das ferramentas (winscp - para windows) ou atraves do scp no terminal linux.

<br>

<br>

Executando a instalação do pacote:
-------

No Terminal SSH do Servidor (com o usuario root) execute o comando abaixo:
    
    rpm -Uvh fail2ban-endian3-2.0-1.x86_64.rpm
    
<br>

Habilitando o Serviço:
-------

1 - Acesso o painel de controle do Endian Firewall com o usuario Admin, selecione o menu "Firewall" e em seguida o sub-menu "Fail2ban Protecao".
<br>
<br>
2 - Seleciona a caixa checkbox "Habilitar" e pressione o botão "Salvar" para que o serviço inicialize.
<br>
<br>
Obs: No menu estado voce podera vizualizar se o Serviço Fail2ban esta "em execução". 

<br>

Configuraçoẽs do Serviço:
--------

Tempo de BAN:
------
<br>

O Tempo de BAN é a difinição de quanto tempo (em Segundos) o IP atacante ficara banido no acesso aos serviços que esta sendo protegidos.

<br>

O valor padrão é de 3600 ( 1 hora ), os valores aceitos sao de -1 (para ban permanente) a 99999 (segundos).

<br>
<br>

Contador de BAN:
------
<br>

O Contador de BAN é a quantidade de falhas de login para e execução do BAN do IP atacante, seu valor padrão é de 5 tentativas e os valores aceitos sao de 1 a 99.

<br>

Ferramentas do Fail2ban:
-------
<br>

1 - Mostrar IP Banidos 
<br>
Ao clicar em "Executar" nesta opção é exibido uma janela console informando todas as Jails, Actions e IP banidos de cada serviço. 
<br>
<br>
2 - Desbanir IP Serviço
<br>
Ao digitar o IP banido na caixa "Endereço de IP" e em seguida clicar em "Executar", sera removido o BAN do mesmo do serviço que voce selecionou (SSH, ENDIANCP ou OPENVPN).

<br>


Removendo o pacote:
--------
- No console ssh digite:

    rpm -e fail2ban-endian3
    
  <br>  
    
Outras informações:
------------------

<br>

# ATENÇÂO!!!
<br>
Caso voce altere as portas padrões dos servicos SSH(22), OPENVPN(1194) e ENDIANCP (10443,80,443), o bloqueio(BAN) do IP atacante não sera realizado corretamente, logo entre em contato comigo para realizar uma customização deste pacote.

<br>

Espero ter ajudado.

Atenciosamente,

Bruno Almeida.
