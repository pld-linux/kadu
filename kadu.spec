Summary:	An Gadu-Gadu client for online messaging
Summary(pl):	Klient Gadu-Gadu do przesy³ania wiadomo¶ci po sieci
Name:		kadu
Version:	0.3.3
%define		_pre	rc3
Release:	0.%{_pre}.1
License:	GPL
Group:		Applications/Communications
Source0:	http://kadu.net/releases/%{name}-%{version}-%{_pre}.tar.gz
Source1:	%{name}.desktop
URL:		http://kadu.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 3.0
BuildRequires:	libtool
BuildRequires:	qt-devel >= 3.0.5
BuildRequires:	readline-devel
BuildRequires:	openssl-devel >= 0.9.6i
Requires:	libgadu >= 1:20030208
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure \
    --with-qt-includes=/usr/X11R6/include/qt

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications
install -d $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/{16x16/apps,32x32/apps,48x48/apps}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications
install kadu/hi16-app-kadu.png $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/16x16/apps/kadu.png
install kadu/hi32-app-kadu.png $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/32x32/apps/kadu.png
install kadu/hi48-app-kadu.png $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/48x48/apps/kadu.png

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "Additional image files can be downloaded from http://cpi.pl/Kadu/images.tgz
and should be placed in .gg/images folder inside user's home directory."

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog INSTALL README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/%{name}
%{_applnkdir}/Network/Communications/*.desktop
%{_pixmapsdir}/*/*/apps/*.png
%lang(pl) %{_mandir}/pl/man1/*.1*
