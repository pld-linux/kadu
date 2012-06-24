#
%bcond_without	xmms	# without xmms player support module
%bcond_without	spellchecker	# without spellchecker (Aspell support)
%bcond_without	weather	# without weather check module support

%define		_libgadu_ver	4:1.4-2
%define		_xmms_mod_ver	1.19
%define		_spellchecker_mod_ver	0.11
%define		_weather_ver	1.46
%define		snapshot	20040905
#
Summary:	A Gadu-Gadu client for online messaging
Summary(pl):	Klient Gadu-Gadu do przesy�ania wiadomo�ci po sieci
Name:		kadu
Version:	0.4.0
Release:	0.%{snapshot}.1
License:	GPL
Group:		Applications/Communications
# Source0:	http://kadu.net/download/stable/%{name}-%{version}.tar.bz2
Source0:	http://kadu.net/download/snapshots/kadu-%{snapshot}.tar.bz2
# Source0-md5:	aa191261ac96bcc74c53ca2e0bb70b7e
Source1:	%{name}.desktop
Source2:	http://scripts.one.pl/xmms/devel/%{version}/xmms-%{_xmms_mod_ver}.tar.gz
# Source2-md5:	5513d94b1f2f41b1e5f0dbf785dc8a15
Source3:	http://scripts.one.pl/spellchecker/devel/%{version}/spellchecker-%{_spellchecker_mod_ver}.tar.gz
# Source3-md5:	a721c8f4b51f447ba287e918aee926bc
Source4:	http://republika.pl/buysk/weather/%{name}-weather-%{_weather_ver}.tar.bz2
# Source4-md5:	6be160f44f9f1fbe4e959c4983ee790c
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
%define		_modules_dir	%{_libdir}/%{name}/modules

%description
Kadu is client of Gadu-Gadu protocol. It's an IM for Linux and UN*X.
It's written for KDE.

%description -l pl
Kadu jest klientem protko�u Gadu-Gadu. Inaczej m�wi�c, jest
komunikatorem dla Linuksa (oraz, przy niewielkim wysi�ku, innych
system�w UN*Xowych). Napisano go w oparciu o bibliotek� Qt i KDE,
przeznaczony jest wi�c dla tego �rodowiska.

%prep
%setup -q -n %{name}
%patch0 -p1
%if %{with xmms}
tar xzf %{SOURCE2} -C modules
%endif
%if %{with spellchecker}
tar xzf %{SOURCE3} -C modules
%endif
%if %{with weather}
tar xjf %{SOURCE4} -C modules
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
%if %{with weather}
sed -i -e 's/module_weather=n/module_weather=m/' .config
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
%doc ChangeLog README TODO HISTORY
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kadu.desktop
%{_pixmapsdir}/kadu.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/AUTHORS
%{_datadir}/%{name}/ChangeLog
%{_datadir}/%{name}/COPYING
%{_datadir}/%{name}/THANKS
%{_datadir}/%{name}/themes
%dir %{_modules_dir}
%{?with_weather: %dir %{_modules_dir}/data/weather}
%{?with_weather: %{_modules_dir}/data/weather/*}
%{_modules_dir}/*.desc
# XXX: binaries cannot reside in /usr/share!!!
%attr(755,root,root) %{_modules_dir}/*.so
%dir %{_modules_dir}/translations
%{_modules_dir}/data/config_wizard/ronk2/*

%lang(de) %{_modules_dir}/translations/*_de.qm
%lang(it) %{_modules_dir}/translations/*_it.qm
%lang(pl) %{_modules_dir}/translations/*_pl.qm
%dir %{_datadir}/%{name}/translations
%lang(de) %{_datadir}/%{name}/translations/*_de.qm
%lang(en) %{_datadir}/%{name}/translations/*_en.qm
%lang(it) %{_datadir}/%{name}/translations/*_it.qm
%lang(pl) %{_datadir}/%{name}/translations/*_pl.qm
