%define		_snapshot	20020830
Summary:	An Gadu-Gadu client for online messaging
Summary(pl):	Klient Gadu-Gadu do przesy�ania wiadomo�ci po sieci
Name:		kadu
Version:	0.3.1
Release:	3
License:	GPL
Group:		Applications/Communications
#Source0:	http://kadu.net/%{name}-%{version}.tar.gz
Source0:	http://kadu.net/%{name}-%{_snapshot}.tar.gz
Source1:	kadu.desktop
URL:		http://kadu.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 3.0
BuildRequires:	libtool
BuildRequires:	qt-devel >= 3.0.5
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Kadu is client of Gadu-Gadu protocol. It's an IM for Linux and UN*X.
It's written for KDE.

%description -l pl
Kadu jest klientem protko�u Gadu-Gadu. Inaczej m�wi�c, jest
komunikatorem dla Linuksa (oraz, przy niewielkim wysi�ku, innych
system�w UN*Xowych). Napisano go w oparciu o bibliotek� Qt i KDE,
przeznaczony jest wi�c dla tego �rodowiska.

%prep
%setup -q -n %{name}-%{_snapshot}

%build
:> ./k_install; chmod 755 k_install
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure
#%{__make}
make || make 

%install
rm -rf $RPM_BUILD_ROOT
install -d {$RPM_BUILD_ROOT%{_bindir},$RPM_BUILD_ROOT%{_applnkdir}/Network/Communications}

#%{__make} install DESTDIR=$RPM_BUILD_ROOT
install kadu/kadu $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "Additional image files can be downloaded from http://cpi.pl/Kadu/images.tgz
and should be placed in .gg/images folder inside user's home directory."

%files
%defattr(644,root,root,755)
%doc ChangeLog INSTALL README TODO
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/Communications/*.desktop
#%{_pixmapsdir}/*/*/apps/*.png
#%{_datadir}/apps/%{name}
