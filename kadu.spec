#
%bcond_without	xmms	# without xmms player support module
%bcond_without	spellchecker	# without spellchecker (Aspell support)

%define		_libgadu_ver	4:1.4-2
%define		_xmms_mod_ver	1.11
%define		snapshot	20040828
#
Summary:	A Gadu-Gadu client for online messaging
Summary(pl):	Klient Gadu-Gadu do przesy³ania wiadomo¶ci po sieci
Name:		kadu
Version:	0.4.0
Release:	0.%{snapshot}.1
License:	GPL
Group:		Applications/Communications
# Source0:	http://kadu.net/download/stable/%{name}-%{version}.tar.bz2
Source0:	http://kadu.net/download/snapshots/kadu-%{snapshot}.tar.bz2
# Source0-md5:	60f816ba9e3cd0abe55369945195c929
Source1:	%{name}.desktop
# Source2:	http://scripts.one.pl/xmms/stable/%{version}/xmms-%{_xmms_mod_ver}.tar.gz
Source2:	http://scripts.one.pl/xmms/stable/0.3.9/xmms-%{_xmms_mod_ver}.tar.gz
# Source2-md5	c5a35a5d206dd5024304fc891f3e7723
Source3:       http://scripts.one.pl/spellchecker/stable/%{version}/spellchecker-0.9.tar.gz
# Source3-md5: b699879a56b679690a57e653dbc9d64d
Patch0:		%{name}-ac_am.patch
URL:		http://kadu.net/
%{?with_spellchecker:BuildRequires:	aspell-devel}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libgadu-devel >= %{_libgadu_ver}
BuildRequires:	libgsm-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	qt-devel
%{?with_xmms:BuildRequires:	xmms-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kadu is client of Gadu-Gadu protocol. It's an IM for Linux and UN*X.
It's written for KDE.

%description -l pl
Kadu jest klientem protko³u Gadu-Gadu. Inaczej mówi±c, jest
komunikatorem dla Linuksa (oraz, przy niewielkim wysi³ku, innych
systemów UN*Xowych). Napisano go w oparciu o bibliotekê Qt i KDE,
przeznaczony jest wiêc dla tego ¶rodowiska.

%prep
%setup -q -n %{name}
%patch0 -p1
%if %{with xmms}
tar xzf %{SOURCE2} -C modules
%endif
%if %{with spellchecker}
tar xzf %{SOURCE3333C modules
%endif

%{__perl} -pi -e 's@\(dataPath\("kadu/modules/?@\(\("%{_libdir}/kadu/modules/@g' kadu/modules.cpp
%{__perl} -pi -e 's@/lib@/%{_lib}@g' modules/x11_docking/spec

%build
%if %{with xmms}
sed -i -e 's/module_xmms=n/module_xmms=m/' .config
%endif
%if %{with spellchecker}
sed -i -e 's/module_spellchecker=n/module_spellchecker=m/' .config
%endif

chmod u+w aclocal.m4 configure
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-voice \
	--enable-dist-info=PLD \
	--with-existing-libgadu=/usr

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_libdir}/%{name}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

install kadu/hi48-app-kadu.png $RPM_BUILD_ROOT%{_pixmapsdir}/kadu.png

rm -rf $RPM_BUILD_ROOT%{_includedir}

mv -f $RPM_BUILD_ROOT%{_datadir}/%{name}/modules $RPM_BUILD_ROOT%{_libdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kadu.desktop
%{_pixmapsdir}/kadu.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/themes
%dir %{_datadir}/%{name}/modules
%{_datadir}/%{name}/modules/*.desc
# XXX: binaries cannot reside in /usr/share!!!
%attr(755,root,root) %{_datadir}/%{name}/modules/*.so
%dir %{_datadir}/%{name}/modules/translations
%lang(de) %{_datadir}/%{name}/modules/translations/*_de.qm
%lang(it) %{_datadir}/%{name}/modules/translations/*_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/*_pl.qm
%dir %{_datadir}/%{name}/translations
%lang(de) %{_datadir}/%{name}/translations/*_de.qm
%lang(en) %{_datadir}/%{name}/translations/*_en.qm
%lang(it) %{_datadir}/%{name}/translations/*_it.qm
%lang(pl) %{_datadir}/%{name}/translations/*_pl.qm
