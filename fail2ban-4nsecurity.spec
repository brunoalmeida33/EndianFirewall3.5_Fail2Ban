Requires: gethardwareid >= 1.0
Requires: mailx >= 1.0

Summary: RPM FAIL2BAN-4NSECURITY
Name: fail2ban-4nsecurity
Version: 1.0
Release: 1
License: GPL
Group: network/fail2ban
URL: N/A
Vendor: N/A
Packager: Bruno A.
BuildRoot: %{_tmppath}/%{name}-{%version}
Source0: %{name}-%version.tar.gz
AutoReqProv: yes

Provides: /var/efw/fail2ban


%define _unpackaged_files_terminate_build 0



%description
PACOTE RPM FAIL2BAN 4nsecurity, prevencao anti ataque de forca bruta.

%prep
rm -rf %{name}-%{version}
mkdir -p %{name}-%{version}
tar -zxf $RPM_SOURCE_DIR/%{name}-%{version}.tar.gz

%install
mkdir -p $RPM_BUILD_ROOT/usr/
mkdir -p $RPM_BUILD_ROOT/etc/
mkdir -p $RPM_BUILD_ROOT/var/
mkdir -p $RPM_BUILD_ROOT/home/
cd %{name}-%{version}
cp -r usr/* $RPM_BUILD_ROOT/usr/
cp -r var/* $RPM_BUILD_ROOT/var/
cp -r etc/* $RPM_BUILD_ROOT/etc/
cp -r home/* $RPM_BUILD_ROOT/home/

%files
%defattr(0755,root,root)
/etc/cron.minutely/fail2ban
/etc/fail2ban/filter.d/endiancp.conf
/etc/fail2ban/filter.d/openvpn.conf
/etc/fail2ban/filter.d/endiancp-common.conf
/etc/fail2ban/jail.d/openvpn.local
/etc/fail2ban/jail.d/endiancp.local
/etc/fail2ban/jail.d/sshd.local
/home/httpd/menus/main/menu-fail2ban.pl
/home/httpd/cgi-bin/status-fail2ban.pl
/home/httpd/cgi-bin/fail2ban.cgi
/usr/local/bin/restartfail2ban
/var/efw/fail2ban/iptables-common.conf

%defattr(0440,root,root)
/etc/sudoers.d/fail2ban


%defattr(0755,nobody,nogroup)
/var/efw/fail2ban/settings

%pre
if [ `/usr/local/bin/gethardwareid 2>/dev/null | grep -v HardwareID` = "4C4C4544-005A-3710-8048-C7C04F325631" ]; then
echo HardwareID ok > /dev/null
else
echo " "
echo HardwareID invalido, entre em contato no site www.4nsecurity.com.br.
echo " "
exit 1
fi


%post
if [ -e /var/log/openvpn/openvpn.log ]; then
        echo arquivo existe. > /dev/null
else
      echo Arquivo criado. >/dev/null
      touch /var/log/openvpn/openvpn.log
      chmod 755 /var/log/openvpn/openvpn.log
fi

if [ -e /usr/sbin/sendmail ]; then
        echo arquivo existe. > /dev/null
else
        ln -s /usr/sbin/sendmail.postfix /usr/sbin/sendmail 2> /dev/null
fi

if [ -e /etc/fail2ban/action.d/iptables-common.conf.original ]; then
        echo arquivo existe. > /dev/null
else
        mv /etc/fail2ban/action.d/iptables-common.conf /etc/fail2ban/action.d/iptables-common.conf.original
        cp /var/efw/fail2ban/iptables-common.conf /etc/fail2ban/action.d/iptables-common.conf
fi


checkinit=`cat /var/efw/inithooks/start.local 2>/dev/null | grep fail2ban`
if [ -e /var/efw/inithooks/start.local ] && [ -z "$checkinit" ]; then
echo "/etc/init.d/fail2ban start" >> /var/efw/inithooks/start.local
elif [ -e /var/efw/inithooks/start.local ] && [ "$checkinit" = "/etc/init.d/fail2ban start" ]; then
echo nothingtosay >/dev/null
else
touch /var/efw/inithooks/start.local
chmod 755 /var/efw/inithooks/start.local
echo "#!/bin/bash" > /var/efw/inithooks/start.local
echo "/etc/init.d/fail2ban start" >> /var/efw/inithooks/start.local
fi

/etc/init.d/fcron restart >/dev/null

%postun
/etc/init.d/fcron restart >/dev/null
mv /etc/fail2ban/action.d/iptables-common.conf.original /etc/fail2ban/action.d/iptables-common.conf
