#
%bcond_with	xmms	# with xmms player support module

%define		_libgadu_ver	4:1.4-2
%define		_xmms_mod_ver	1.8
%define		snapshot	20040628
#
Summary:	A Gadu-Gadu client for online messaging
Summary(pl):	Klient Gadu-Gadu do przesy³ania wiadomo¶ci po sieci
Name:		kadu
Version:	0.3.9.0.%{snapshot}
Release:	1
License:	GPL
Group:		Applications/Communications
# Source0:	http://kadu.net/download/stable/%{name}-%{version}.tar.bz2
Source0:       http://kadu.net/download/snapshots/kadu-%{snapshot}.tar.bz2
# Source0-md5:	ea23bc609b056a189c1847614a13dd73
Source1:	%{name}.desktop
# Source2:	http://scripts.one.pl/xmms/stable/%{version}/xmms-%{_xmms_mod_ver}.tar.gz
Source2:	http://scripts.one.pl/xmms/stable/0.3.8/xmms-%{_xmms_mod_ver}.tar.gz
# Source2-md5	376537ff5e2a605958097e4a5f024a26
Patch0:		%{name}-ac_am.patch
URL:		http://kadu.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libgadu-devel >= %{_libgadu_ver}
BuildRequires:	libgsm-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	qt-devel
%{?with_xmms:BuildRequires:     xmms-devel}
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

%build
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
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

install kadu/hi48-app-kadu.png $RPM_BUILD_ROOT%{_pixmapsdir}/kadu.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog INSTALL README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kadu.desktop
%{_pixmapsdir}/kadu.png
%{_datadir}/%{name}
