# EndianFirewall3.5_Fail2Ban
Addon Fail2ban for Endian Firewall Community 3.2.x.

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

Configuraçoẽs do Serviço:
--------

Habilitando o Serviço:

1 - Acesso o painel de controle do Endian Firewall com o usuario Admin, selecione o menu "Firewall" e em seguida o sub-menu "Protecao Fail2ban".<br>
2 - 

<br>

Removendo o pacote:
--------
- No console ssh digite:

    rpm -e fail2ban-endian3
    
  <br>  
    
Outras informações:
------------------



Espero ter ajudado.

Atenciosamente,

Bruno Almeida.
