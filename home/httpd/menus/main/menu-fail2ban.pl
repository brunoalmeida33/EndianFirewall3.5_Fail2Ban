#!/usr/bin/perl

my $item = {
    'caption' => _('Fail2ban Protecao'),
    'enabled' => 1,
    'uri' => '/cgi-bin/fail2ban.cgi',
    'title' => _('Fail2ban'),
    'helpuri' => 'firewall.html#fail2ban',
};

register_menuitem('05.firewall', '10.fail2ban', $item);

1; 
