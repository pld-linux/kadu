Summary:	An Gadu-Gadu client for online messaging
Summary(pl):	Klient Gadu-Gadu do przesy�ania wiadomo�ci po sieci
Name:		kadu
Version:	0.1.6b
Release:	1
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
URL:		http://cpi.pl/Kadu/
Source0:	http://cpi.pl/Kadu/%{name}-%{version}.tar.gz
Patch0:		%{name}-am_ac.patch
Patch1:		%{name}-libgg.patch
BuildRequires:	qt-devel >= 2.1.1
BuildRequires:	libstdc++-devel
BuildRequires:	kdelibs-devel >= 2.2.0
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6
%define		_mandi	%{_prefix}/man

%description
Kadu is client of Gadu-Gadu protocol. It's an IM for Linux and UN*X.
It's written for KDE2.

%description -l pl
Kadu jest klientem protko�u Gadu-Gadu. Inaczej m�wi�c, jest
komunikatorem dla Linuxa (oraz, przy niewielkim wysi�ku, innych
system�w UN*Xowych). Napisano go w oparciu o bibliotek� Qt2 i KDE2,
przeznaczony jest wi�c dla tego �rodowiska.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
gettextize --copy --force
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications

%{__make} DESTDIR=$RPM_BUILD_ROOT install
install kadu/kadu.desktop $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications

gzip -9nf ChangeLog, INSTALL, README, TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/Communications/*.desktop
%{_datadir}/icons/*/*/*.png
