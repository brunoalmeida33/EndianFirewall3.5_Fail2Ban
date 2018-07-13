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

Instalando o Pacote:


<br>

Realizando Download:
--------

Para realizar a compra/download do pacote acesse o site http://www.4nsecurity.com.br/loja/EndianFirewall_Fail2ban. 

Obs: O Arquivo pode ser enviado para o firewall atraves das ferramentas (winscp - para windows) ou atraves do scp no terminal linux.

<br>

<br>

Executando a instalação:
-------

No Terminal SSH do Servidor (com o usuario root) execute ocomando abaixo:
    
    rpm -Uvh fail2ban-endian3-2.0-1.x86_64.rpm
    
<br>

Configuração Adicional (Recomendado para backups dos logs do squid):
--------
<br>

Edite o arquivo /etc/logrotate.d/squid.tmpl ( com qualquer editor de texto ) na linha 31, substitua o parametro "rotate 1" para "rotate 94", salve o arquivo e reinicie o servidor firewall.

Exemplo:

nano +31 /etc/logrotate.d/squid.tmpl 

Substitua "rotate 1" para "rotate 94" nesta linha. (obs: sem as aspas " " ).

Segure CTRL + O e pressione ENTER para salvar o arquivo e CTRL + X para sair do editor nano.

para reinicia o firewall utilize o comando "reboot".

<br>

Removendo o pacote:
--------
- No console ssh digite:

    rpm -e squidanalyzer-endian3
    
  <br>  
    
Outras informações:
------------------

- Para acessar o SquidAnalyzer é necessario acessar o Servidor firewall com login padrão "admin" e sua senha atual.

Link Para acesso: HTTPS://IPDOFIREWALL:10443/squidanalyzer/

Observações: Os relatorios são atualizados a cada 55 minutos automaticamente, inicialmente nenhum relatorio é gerado, caso queira executa-lo manualmente, é necessario logar no SSH como root e executar o comando "squid-analyzer". 

Espero ter ajudado.

Atenciosamente,

Bruno Almeida.
