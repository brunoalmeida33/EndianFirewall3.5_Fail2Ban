#!/usr/bin/perl

#+---------------------------------------------------------------------------+
#| Endian Hotspot                                                            |
#+---------------------------------------------------------------------------+
#| Copyright (c) 2005-2006 Endian GmbH/Srl                                   |
#|      Endian GmbH/Srl                                                      |
#|      Bergweg 41 Via Monte                                                 |
#|      39057 Eppan/Appiano                                                  |
#|      ITALIEN/ITALIA                                                       |
#|      info@endian.it                                                       |
#+---------------------------------------------------------------------------+
#| This program is proprietary software; you are not allowed to redistribute |
#| and/or modify it.                                                         |
#| This program is distributed in the hope that it will be useful,           |
#| but WITHOUT ANY WARRANTY; without even the implied warranty of            |
#| MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                      |
#+---------------------------------------------------------------------------+

require 'header.pl';
require '/home/httpd/cgi-bin/endianinc.pl';

my $fail2ban = ['fail2ban-server', '/var/run/fail2ban/fail2ban.pid', ''];
register_status(_('Fail2ban Server'), $fail2ban);

1;

