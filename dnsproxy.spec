Summary:	Proxy for DNS queries
Name:		dnsproxy
Version:	1.16
Release:	3
License:	BSD-style
Group:		System/Servers
Url:		http://www.wolfermann.org/dnsproxy.html
Source0:	http://www.wolfermann.org/%{name}-%{version}.tar.bz2
Source1:	dnsproxy.init
BuildRequires:	groff-base
BuildRequires:	pkgconfig(libevent)
Requires(post,preun):	rpm-helper

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

%files
%doc README
%{_initrddir}/dnsproxy
%config(noreplace) %{_sysconfdir}/dnsproxy.conf
%{_sbindir}/dnsproxy
%{_mandir}/man1/*

