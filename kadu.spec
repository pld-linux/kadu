#
%bcond_without	xmms	# without xmms player support module
%bcond_without	arts	# without arts sound server support
%bcond_without  esd	# without ESD sound server support
%bcond_without	nas	# without Network Audio System support
%bcond_without	echo	# without Echo sample module
#%%bcond_without	speech	# without Speech synthesis support
#%%bcond_without WM	# without WindowMaker docking module

%define		_libgadu_ver	4:1.4-2
%define		_xmms_mod_ver	1.9
#
Summary:	A Gadu-Gadu client for online messaging
Summary(pl):	Klient Gadu-Gadu do przesy³ania wiadomo¶ci po sieci
Name:		kadu
Version:	0.3.9
Release:	1.2
License:	GPL
Group:		Applications/Communications
Source0:	http://kadu.net/download/stable/%{name}-%{version}.tar.bz2
# Source0-md5:	d461c4b19670920e2ba1425d12e23f6b
Source1:	%{name}.desktop
Source2:	http://scripts.one.pl/xmms/stable/%{version}/xmms-%{_xmms_mod_ver}.tar.gz
# Source2-md5	c5a35a5d206dd5024304fc891f3e7723
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
%{?with_arts:BuildRequires:	arts-devel}
%{?with_esd:BuildRequires:	esound-devel}
%{?with_nas:BuildRequires:	nas-devel}
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

%package module-xmms
Summary:	Support xmms status
Summary(pl):	Modu³ statusu dla xmms
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	xmms

%description module-xmms
TODO
Module to enlabe (to make possible ?)... 

%description module-xmms -l pl
Modu³ umo¿liwiajacy w opisie statusu pokazywanie informacji o
odgrywanym utowrze z odtwarzacza xmms.

%prep
%setup -q -n %{name}
%patch0 -p1
%if %{with xmms}
tar xzf %{SOURCE2} -C modules
%endif

%build
%if %{with xmms}
sed -i -e 's/module_xmms=n/module_xmms=m/' .config
%endif
%if %{with arts}
sed -i -e 's/module_arts_sound=n/module_arts_sound=m/' .config
%endif
%if %{with esd}
sed -i -e 's/module_esd_sound=n/module_esd_sound=m/' .config
%endif
%if %{with nas}
sed -i -e 's/module_nas_sound=n/module_nas_sound=m/' .config
%endif
%if %{with echo}
sed -i -e 's/module_echo=n/module_echo=m/' .config
%endif
#%%if %{with speech}
#sed -i -e 's/module_speech=n/module_speech=m/' .config
#%%endif
#%%if %{with speech}
#sed -i -e 's/module_wmaker_docking=n/module_wmaker_docking=m/' .config
#%%endif


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

rm -rf $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog INSTALL README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kadu.desktop
%{_pixmapsdir}/kadu.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/themes
#default modules:
%dir %{_datadir}/%{name}/modules
%{_datadir}/%{name}/modules/autoaway.desc
%{_datadir}/%{name}/modules/autoresponder.desc
%{_datadir}/%{name}/modules/autoresponder.so
%{_datadir}/%{name}/modules/default_sms.desc
%{_datadir}/%{name}/modules/docking.desc
%{_datadir}/%{name}/modules/dsp_sound.desc
%{_datadir}/%{name}/modules/dsp_sound.so
%{_datadir}/%{name}/modules/encryption.desc
%{_datadir}/%{name}/modules/ext_sound.desc
%{_datadir}/%{name}/modules/sms.desc
%{_datadir}/%{name}/modules/sound.desc
%{_datadir}/%{name}/modules/voice.desc
%{_datadir}/%{name}/modules/x11_docking.desc
#default modules translation:
%dir %{_datadir}/%{name}/modules/translations
%lang(de) %{_datadir}/%{name}/modules/translations/autoaway_de.qm
%lang(it) %{_datadir}/%{name}/modules/translations/autoaway_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/autoaway_pl.qm
%lang(de) %{_datadir}/%{name}/modules/translations/autoresponder_de.qm
%lang(it) %{_datadir}/%{name}/modules/translations/autoresponder_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/autoresponder_pl.qm
%lang(de) %{_datadir}/%{name}/modules/translations/default_sms_de.qm
%lang(it) %{_datadir}/%{name}/modules/translations/default_sms_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/default_sms_pl.qm
%lang(de) %{_datadir}/%{name}/modules/translations/docking_de.qm
%lang(it) %{_datadir}/%{name}/modules/translations/docking_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/docking_pl.qm
%lang(de) %{_datadir}/%{name}/modules/translations/dsp_sound_de.qm
%lang(it) %{_datadir}/%{name}/modules/translations/dsp_sound_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/dsp_sound_pl.qm
%lang(de) %{_datadir}/%{name}/modules/translations/encryption_de.qm
%lang(it) %{_datadir}/%{name}/modules/translations/encryption_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/encryption_pl.qm
%lang(de) %{_datadir}/%{name}/modules/translations/ext_sound_de.qm
%lang(it) %{_datadir}/%{name}/modules/translations/ext_sound_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/ext_sound_pl.qm
%lang(de) %{_datadir}/%{name}/modules/translations/sms_de.qm
%lang(it) %{_datadir}/%{name}/modules/translations/sms_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/sms_pl.qm
%lang(de) %{_datadir}/%{name}/modules/translations/sound_de.qm
%lang(it) %{_datadir}/%{name}/modules/translations/sound_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/sound_pl.qm
%lang(de) %{_datadir}/%{name}/modules/translations/voice_de.qm
%lang(it) %{_datadir}/%{name}/modules/translations/voice_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/voice_pl.qm
%lang(de) %{_datadir}/%{name}/modules/translations/x11_docking_de.qm
%lang(it) %{_datadir}/%{name}/modules/translations/x11_docking_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/x11_docking_pl.qm
#global translation:
%dir %{_datadir}/%{name}/translations
%lang(de) %{_datadir}/%{name}/translations/kadu_de.qm
%lang(en) %{_datadir}/%{name}/translations/kadu_en.qm
%lang(it) %{_datadir}/%{name}/translations/kadu_it.qm
%lang(pl) %{_datadir}/%{name}/translations/kadu_pl.qm
%lang(de) %{_datadir}/%{name}/translations/qt_de.qm
%lang(en) %{_datadir}/%{name}/translations/qt_en.qm
%lang(it) %{_datadir}/%{name}/translations/qt_it.qm
%lang(pl) %{_datadir}/%{name}/translations/qt_pl.qm

#temporarily, move to subpackages
%{_datadir}/%{name}/modules/arts*
%{_datadir}/%{name}/modules/esd*
%{_datadir}/%{name}/modules/nas*
%{_datadir}/%{name}/modules/echo*

%if %{with xmms}
%files module-xmms
%defattr(644,root,root,755)
%lang(pl) %{_datadir}/%{name}/modules/translations/xmms_pl.qm
%{_datadir}/%{name}/modules/xmms.desc
%{_datadir}/%{name}/modules/xmms.so
%endif
