#!/usr/bin/perl

require 'header.pl';

my $conffile = "${swroot}/fail2ban/settings"; 
my $restart = 'sudo /usr/local/bin/restartfail2ban';
my $stop = 'sudo /usr/local/bin/restartfail2ban';
my $name ='Fail2ban Configuraçoes';
my %checked     = ( 0 => '', 1 => 'checked', 'on' => 'checked');

my %opt;
my @address, @addrs;
my %opt;

&getcgihash(\%opt);

$selected{'TOOL'}{'SHOWBANNEDIP'} = '';
$selected{'TOOL'}{'UNBANSSH'} = '';
$selected{'TOOL'}{'UNBANCP'} = '';
$selected{'TOOL'}{'UNBANVPN'} = '';
$selected{'TOOL'}{$opt{'TOOL'}} = 'SELECTED';


# -------------------------------------------------------------
# get settings and CGI parameters
# -------------------------------------------------------------

my %confhash = ();
my $conf = \%confhash;

readhash($conffile, $conf);

my %par;
getcgihash(\%par);

# -------------------------------------------------------------
# action to do?
# -------------------------------------------------------------

sub save() {
    return if ($par{'ACTION'} ne 'save');

    my $logid = "fail2ban.cgi";
    my $needrestart = 0;
    if ( ($conf->{'FAIL2BAN_ENABLED'} ne $par{'FAIL2BAN_ENABLED'}) ) {
        &log(_("%s - writing new configuration file", $logid));
        $needrestart = 1;
        $conf->{'FAIL2BAN_ENABLED'} = $par{'FAIL2BAN_ENABLED'};
        writehash($conffile, $conf);
        $notemessage=_('Configuration saved successfully');
    }
	if ( ($conf->{'BAN_TIME'} ne $par{'BAN_TIME'}) or
	($conf->{'BAN_COUNT'} ne $par{'BAN_COUNT'}) or
	($conf->{'SSH_PORT'} ne $par{'SSH_PORT'}) or
	($conf->{'OPENVPN_PORT'} ne $par{'OPENVPN_PORT'}) or
	($conf->{'IP_IGNORE'} ne $par{'IP_IGNORE'})
) {
	print STDERR "$logid: writing new configuration file\n";
        $needrestart = 1;
        $conf->{'BAN_TIME'} = $par{'BAN_TIME'};
        $conf->{'BAN_COUNT'} = $par{'BAN_COUNT'};
        $conf->{'SSH_PORT'} = $par{'SSH_PORT'};
	$conf->{'OPENVPN_PORT'} = $par{'OPENVPN_PORT'};
	$conf->{'IP_IGNORE'} = $par{'IP_IGNORE'};
        writehash($conffile, $conf);
	$notemessage=_('Configuration saved successfully');
    }
    if ( ($conf->{'FAIL2BAN_ENABLED'} ne 'on') ) {
	$needrestart = 0; 
        print STDERR `$stop`;
        &log(_("%s - stop done", $logid));
}
    if ($needrestart) {
        print STDERR `$restart`;
        &log(_("%s - restarting done", $logid));
    }

}


# -------------------------------------------------------------
# ouput page
# -------------------------------------------------------------

sub display() {
    openbox('100%', 'left', "$name");
    printf <<EOF
<form enctype='multipart/form-data' method='post' action='$ENV{SCRIPT_NAME}'>
<input type='hidden' name='ACTION' value='save' />
<table>
  <tr>
    <td>%s:</td>
    <td><input type='checkbox' name='FAIL2BAN_ENABLED' $checked{$conf->{'FAIL2BAN_ENABLED'}} />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>

    <td>%s</td>
    <td><input type='number' name='BAN_TIME' SIZE=5 MAXLENGTH=5 value='$conf->{'BAN_TIME'}' />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
    
    <td>%s</td>
    <td><input type='number' name='BAN_COUNT' SIZE=5 MAXLENGTH=2 value='$conf->{'BAN_COUNT'}' />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
</tr>
</table>

<table>
<tr>
<td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>   
 <td>%s</td>
   <td><input type='number' name='SSH_PORT' value='$conf->{'SSH_PORT'}' min="1" max="65535"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>

  <td>%s</td>
   <td><input type='number' name='OPENVPN_PORT' value='$conf->{'OPENVPN_PORT'}'  maxlength="1000"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
</table>

<table>
<td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp</d>
   <td>%s</td>
   <td><input type='text' name='IP_IGNORE' value='$conf->{'IP_IGNORE'}' maxlength="1000" size="56" />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>

</tr>

<tr>
    <td colspan="2">
      <input class='submitbutton' type='submit' name='submit' value='%s' />
    </td>
  </tr>
</table>
</form>

EOF

,
_('Habilitar'),
_('Tempo de BAN (segundos): '),
_('Contador de BAN: '),
_('Porta SSH: '),
_('Porta OpenVPN: '),
_('Ignore IPs: '),
_('Salvar')
;

printf <<EOF
<br>
<br>
  <div>%s</div>
  <div>%s</div>
 <div>%s</div>
EOF
, _('1- Por padrao este pacote vem configurado com o bloqueio de IP apos 5 tentativas de login incorreto.')
, _('2- O tempo para bloqueio do ip pode ser por 1 hora (padrao 3600 secs) ou definitivo (-1).')
, _('3- Inserir ips a serem ignorados seguidos de "," virgulas (Ex: 8.8.8.8,1.1.1.1 ).')
;

printf <<END
<br class="cb" />
<p align="center">Addon desenvolvido por <a href="http://www.4nsecurity.com.br" target="_blank">www.4nsecurity.com.br</a></p>

</div>
END
;

    closebox();
}

sub display_report() {
    return if ($conf->{'FAIL2BAN_ENABLED'} ne 'on');

    openbox('100%', 'left', _('Ferramentas do Fail2ban')); {
print "<FORM METHOD='POST'>\n";

printf <<END
Escolha qual teste deseja executar.<p><p>
END
;

print <<END
<TABLE WIDTH='100%'>
<TR>
<TD WIDTH='15%' CLASS='base'>Selecione: $tr{'toolc'}</TD>
<TD WIDTH='20%'>
<SELECT NAME='TOOL'>
<OPTION VALUE='SHOWBANNEDIP' $selected{'TOOL'}{'SHOWBANNEDIP'}>Mostrar IP Banidos
<OPTION VALUE='UNBANSSH' $selected{'TOOL'}{'UNBANSSH'}>Desbanir IP SSH
<OPTION VALUE='UNBANCP' $selected{'TOOL'}{'UNBANCP'}>Desbanir IP ENDIANCP
<OPTION VALUE='UNBANVPN' $selected{'TOOL'}{'UNBANVPN'}>Desbanir IP OPENVPN
</SELECT>
</TD>
<TD WIDTH='20%' CLASS='base'>Endereco de IP:  $tr{'ip addresses or hostnames'}</TD>
<TD WIDTH='30%'><INPUT TYPE='text' SIZE='20' NAME='IP' VALUE='$opt{'IP'}'></TD>
<TD WIDTH='15%' ALIGN='CENTER'><INPUT TYPE='submit' NAME='ACTION' VALUE='Executar'></TD>
</TR>
</TABLE>
END
;

printf <<END
<br class="cb" />
</div>
END
;

    }

    closebox();
}

showhttpheaders();

openpage($name, 1, '');

save();
&openbigbox($errormessage, $warnmessage, $notemessage);
display();
display_report();

#closebigbox();
#closepage();

if ($opt{'ACTION'} eq "Executar")

{

@address = split(/,/, $opt{'IP'});

&openbox('100%', 'left', _('Console'));
print "<PRE>\n";
if ($opt{'TOOL'} eq 'SHOWBANNEDIP') 
{
system('sudo /usr/bin/fail2ban-client status ssh-iptables');
system('echo " "');
system('echo " "');
system('sudo /usr/bin/fail2ban-client status endiancp-iptables');
system('echo " "');
system('echo " "');
system('sudo /usr/bin/fail2ban-client status openvpn-iptables'); 
}
if ($opt{'TOOL'} eq 'UNBANSSH') 
{
system('sudo', '/usr/bin/fail2ban-client', 'set', 'ssh-iptables', 'unbanip', $opt{'IP'});
}
if ($opt{'TOOL'} eq 'UNBANCP')
{
system('sudo', '/usr/bin/fail2ban-client', 'set', 'endiancp-iptables', 'unbanip', $opt{'IP'});
}
if ($opt{'TOOL'} eq 'UNBANVPN')
{
system('sudo', '/usr/bin/fail2ban-client', 'set', 'openvpn-iptables', 'unbanip', $opt{'IP'});
}

print "</PRE>\n";
&closebox();
}

print "</FORM>\n";

#&closebox();
&closebigbox();
&closepage();
exit;






