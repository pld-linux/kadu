Summary:	An Gadu-Gadu client for online messaging
Summary(pl):	Klient Gadu-Gadu do przesy�ania wiadomo�ci po sieci
Name:		kadu
Version:	0.3.3
Release:	0.pre3.1
License:	GPL
Group:		Applications/Communications
#Source0:	http://kadu.net/%{name}-%{version}.tar.gz
Source0:	http://kadu.net/%{name}-%{version}-pre3.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-make.patch
URL:		http://kadu.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 3.0
BuildRequires:	libtool
BuildRequires:	qt-devel >= 3.0.5
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


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

%build
:> ./k_install; chmod 755 k_install
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure
cd libgadu
%configure
cd lib
%{__make} all CC=%{__cc} CXX=%{__cxx}
cd ../..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d {$RPM_BUILD_ROOT%{_bindir},$RPM_BUILD_ROOT%{_applnkdir}/Network/Communications}
install -d $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/{16x16/apps,32x32/apps,48x48/apps}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications
install kadu/hi16-app-kadu.png $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/16x16/apps/kadu.png
install kadu/hi32-app-kadu.png $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/32x32/apps/kadu.png
install kadu/hi48-app-kadu.png $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/48x48/apps/kadu.png


%clean
%{!?_without_clean:rm -rf $RPM_BUILD_ROOT}

%post
echo "Additional image files can be downloaded from http://www.kadu.net/download.php
and should be placed in .gg/images folder inside user's home directory."

%files
%defattr(644,root,root,755)
%doc ChangeLog INSTALL README TODO
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/Communications/*.desktop
%{_pixmapsdir}/*/*/apps/*.png
%{_datadir}/apps/%{name}/msg.wav
%{_datadir}/apps/%{name}/themes
%{_datadir}/apps/%{name}/doc
