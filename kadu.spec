#
# --with icondir	installs icons in /usr/share/icons/hicolor
#

%define		_pre		rc2

Summary:	An Gadu-Gadu client for online messaging
Summary(pl):	Klient Gadu-Gadu do przesy³ania wiadomo¶ci po sieci
Name:		kadu
Version:	0.3.4
Release:	0.%{_pre}.1
License:	GPL
Group:		Applications/Communications
Source0:	http://kadu.net/releases/%{name}-%{version}-%{_pre}.tar.gz
# Source0-md5:	917fb939aa8782926f90dc2667bd0f53
Source1:	%{name}.desktop
Patch0:		%{name}-ac_am.patch
URL:		http://kadu.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
%if %{?_with_icondir:1}0
BuildRequires:	kdelibs-devel >= 8:3.2-0.030613.1
%else
BuildRequires:	kdelibs-devel >= 3.0
%endif
BuildRequires:	libtool
BuildRequires:	readline-devel
BuildRequires:	openssl-devel >= 0.9.7
Requires:	libgadu >= 3:1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%{?_with_icondir:%define _pixmapsdir %{_datadir}/icons}	

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

%build
chmod +w aclocal.m4 configure
%{__autoheader}
%{__aclocal}
%{__autoconf}
%{__automake}

%configure --with-existing-libgadu

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_appsdir=%{_applnkdir}
	

install -d $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

install -d $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/{16x16,32x32,48x48}/apps
install kadu/hi16-app-kadu.png $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/16x16/apps/kadu.png
install kadu/hi32-app-kadu.png $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/32x32/apps/kadu.png
install kadu/hi48-app-kadu.png $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/48x48/apps/kadu.png

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog INSTALL README TODO
%attr(755,root,root) %{_bindir}/kadu
%{_datadir}/apps/%{name}
%{_desktopdir}/kadu.desktop
%{_pixmapsdir}/*/*/apps/kadu.png
%lang(pl) %{_mandir}/pl/man1/kadu.1*
