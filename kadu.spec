
%define		_pre		rc3

Summary:	An Gadu-Gadu client for online messaging
Summary(pl):	Klient Gadu-Gadu do przesy³ania wiadomo¶ci po sieci
Name:		kadu
Version:	0.3.4
Release:	0.%{_pre}.3
License:	GPL
Group:		Applications/Communications
Source0:	http://kadu.net/releases/%{name}-%{version}-%{_pre}.tar.gz
# Source0-md5:	036224e2b72749ba5fae72520dd52bf3
Source1:	%{name}.desktop
Patch0:		%{name}-ac_am.patch
Patch1:		%{name}-config-reading-fix.patch
URL:		http://kadu.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libgadu-devel >= 3:1.1
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	qt-devel
BuildRequires:	readline-devel
Requires:	libgadu >= 3:1.1
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
%patch1 -p1

%build
chmod +w aclocal.m4 configure
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-dist-info=PLD \
	--with-existing-libgadu

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_appsdir=%{_applnkdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

install kadu/hi48-app-kadu.png $RPM_BUILD_ROOT%{_pixmapsdir}/kadu.png

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog INSTALL README TODO
%attr(755,root,root) %{_bindir}/kadu
%{_datadir}/apps/%{name}
%{_desktopdir}/kadu.desktop
%{_pixmapsdir}/kadu.png
%lang(pl) %{_mandir}/pl/man1/kadu.1*
