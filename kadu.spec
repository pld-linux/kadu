Summary:	An Gadu-Gadu client for online messaging
Summary(pl):	Klient Gadu-Gadu do przesy�ania wiadomo�ci po sieci
Name:		kadu
Version:	0.3.0
Release:	1
License:	GPL
Group:		Applications/Communications
URL:		http://cpi.pl/Kadu/
#Source0:	http://cpi.pl/Kadu/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.pld.org.pl/people/tomee/kadu/unstable/%{name}-%{version}.tar.gz
#Patch0:		%{name}-edit_clear.patch
Patch1:		%{name}-am.patch
#Patch2:		%{name}-gcc31.patch
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 2.2.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	qt-devel >= 2.1.1
BuildRequires:	zlib-devel
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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
#%patch0
%patch1
#%patch2 -p1

%build
#gettextize --copy --force
#libtoolize --copy --force
#aclocal
#autoconf
#automake -a -c
:> ./k_install; chmod 755 k_install
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install kadu/kadu.desktop $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications

gzip -9nf ChangeLog INSTALL README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "Additional image files can be downloaded from http://cpi.pl/Kadu/images.tgz
and should be placed in .gg/images folder inside user's home directory."

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/Communications/*.desktop
%{_datadir}/pixmaps/hicolor/*/*/*.png
%{_datadir}/apps/%{name}/*
