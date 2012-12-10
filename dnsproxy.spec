Summary:	Proxy for DNS queries
Name:		dnsproxy
Version:	1.16
Release:	%mkrel 3
License:	BSD-style
Group:		System/Servers
URL:		http://www.wolfermann.org/dnsproxy.html
Source0:	http://www.wolfermann.org/%{name}-%{version}.tar.bz2
Source1:	dnsproxy.init
Requires(post): rpm-helper
Requires(preun): rpm-helper
BuildRequires:	libevent-devel
BuildRequires:	groff-for-man
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The dnsproxy daemon is a proxy for DNS queries. It forwards these
queries to two previously configured nameservers: one for
authoritative queries and another for recursive queries. The
received answers are sent back to the client unchanged. No local
caching is done. 

Primary motivation for this project was the need to replace Bind
servers with djbdns in an ISP environment. These servers get
recursive queries from customers and authoritative queries from
outside at the same IP address. Now it is possible to run dnscache
and tinydns on the same machine with queries dispatched by
dnsproxy.

Other scenarios are firewalls where you want to proxy queries to
the real servers in your DMZ. Or internal nameservers behind
firewalls, or...

%prep

%setup -q

cp %{SOURCE1} dnsproxy.init

%build

%configure2_5x \
    --with-native-libevent

%make

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_initrddir}
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man1

install -m0755 dnsproxy %{buildroot}%{_sbindir}/
install -m0644 dnsproxy.1 %{buildroot}%{_mandir}/man1
install -m0644 dnsproxy.conf %{buildroot}%{_sysconfdir}/dnsproxy.conf
install -m0755 dnsproxy.init %{buildroot}%{_initrddir}/dnsproxy

%post
%_post_service dnsproxy

%preun
%_preun_service dnsproxy

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%attr(0755,root,root) %{_initrddir}/dnsproxy
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/dnsproxy.conf
%attr(0755,root,root) %{_sbindir}/dnsproxy
%{_mandir}/man1/*


%changelog
* Wed Dec 22 2010 Oden Eriksson <oeriksson@mandriva.com> 1.16-3mdv2011.0
+ Revision: 623871
- rebuilt against libevent 2.x

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.16-2mdv2011.0
+ Revision: 610257
- rebuild

* Wed Jan 13 2010 Frederik Himpe <fhimpe@mandriva.org> 1.16-1mdv2010.1
+ Revision: 491031
- update to new version 1.16

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.15-7mdv2010.0
+ Revision: 428287
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.15-6mdv2009.0
+ Revision: 266570
- rebuild early 2009.0 package (before pixel changes)

* Wed May 14 2008 Oden Eriksson <oeriksson@mandriva.com> 1.15-5mdv2009.0
+ Revision: 207042
- rebuilt against libevent-1.4.4

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.15-4mdv2008.1
+ Revision: 170797
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Jul 07 2007 Oden Eriksson <oeriksson@mandriva.com> 1.15-3mdv2008.0
+ Revision: 49471
- fix deps


* Mon Jun 26 2006 Oden Eriksson <oeriksson@mandriva.com> 1.15-2mdv2007.0
- rebuild

* Tue May 17 2005 Oden Eriksson <oeriksson@mandriva.com> 1.15-1mdk
- initial Mandriva package

