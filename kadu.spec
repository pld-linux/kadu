#
# Conditional build:
%bcond_without	alsa		# without ALSA support
%bcond_without	amarok		# without amarok player support module
%bcond_without	arts		# without arts sound server support
%bcond_without	dcopexport	# without dcopexport module
%bcond_without	esd		# without ESD sound server support
%bcond_without	imiface		# without imiface module that integrate kadu with KDE with KIMIface interface
%bcond_without	iwait4u		# without iwait4u module
%bcond_without	nas		# without Network Audio System support
%bcond_without	speech		# without Speech synthesis support
%bcond_without	spellchecker	# without spellchecker (Aspell support)
%bcond_without	spy		# without Spying module that shows who's invisible
%bcond_with	tcl_scripting	# with TCL scripting support and KaduPro extensions
%bcond_without	weather		# without Weather support module
%bcond_without	xmms		# without XMMS player support module

%if %{with imiface} && %{without dcopexport}
cannot build imiface without dcopexport
%endif

%define		_sver			0.4.3
%define		_libgadu_ver		4:1.6
%define		_amarok_mod_ver		1.13
%define		_spellchecker_mod_ver	0.15
%define		_spy_mod_ver		0.0.8-1
%define		_tcl_mod_ver		0.6.2-Josephine
%define		_weather_ver		2.02
%define		_xmms_mod_ver		1.25
%define		_imiface_ver		0.2
%define		_iwait4u_ver		1.0
%define		_dcopexport_ver		0.11.1-20051201-0.4.3
#
Summary:	A Gadu-Gadu client for online messaging
Summary(pl):	Klient Gadu-Gadu do przesy�ania wiadomo�ci po sieci
Name:		kadu
Version:	0.4.3
Release:	2
License:	GPL v2
Group:		Applications/Communications
Source0:	http://kadu.net/download/stable/%{name}-%{version}.tar.bz2
# Source0-md5:	ef66bd638df30aee6338aae3b22dd194
Source1:	%{name}.desktop
Source2:	http://scripts.one.pl/xmms/stable/%{_sver}/xmms-%{_xmms_mod_ver}.tar.gz
# Source2-md5:	4a6e4d52b8efa3d182e2a55e02cc3383
Source3:	http://scripts.one.pl/amarok/stable/%{_sver}/amarok-%{_amarok_mod_ver}.tar.gz
# Source3-md5:	539afdd2295ec462022f5e10d80a816c
Source4:	http://scripts.one.pl/spellchecker/stable/%{_sver}/spellchecker-%{_spellchecker_mod_ver}.tar.gz
# Source4-md5:	02495130277cc8a48430535a4107708d
Source5:	http://www.kadu.net/~blysk/weather-%{_weather_ver}.tar.bz2
# Source5-md5:	362d77600e0e02ec67d1b3bdf3cc64e2
Source6:	http://scripts.one.pl/tcl4kadu/files/stable/%{_sver}/tcl_scripting-%{_tcl_mod_ver}.tar.gz
# Source6-md5:	97406c1f3f34b8a073e0a1a18e842c9e
Source7:	http://scripts.one.pl/~przemos/download/%{name}-spy-%{_spy_mod_ver}.tar.gz
# Source7-md5:	c402bab70b3f5840b15312eb4f776f2c
Source8:	http://vogel.iglu.cz/kadu/imiface/imiface-%{_imiface_ver}.tgz
# Source8-md5:	926284ffb2bcda107d86d9d93b9f2bed
Source9:	http://www.kadu.net/~pan_wojtas/iwait4u/download/%{name}-iwait4u-%{_iwait4u_ver}.tar.bz2
# Source9-md5:	01c19f94168a6420346aaf1f2cc424ec
Source10:	http://kadu.net/~pinkworm/dcopexport/dcopexport-%{_dcopexport_ver}.tar.bz2
# Source10-md5:	2be815da3015312c6469dddc12d65bca
Patch0:		%{name}-ac_am.patch
Patch1:		%{name}-bashism.patch
URL:		http://kadu.net/
%{?with_alsa:BuildRequires:	alsa-lib-devel}
%{?with_arts:BuildRequires:	arts-devel}
%{?with_spellchecker:BuildRequires:	aspell-devel}
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_esd:BuildRequires:	esound-devel}
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libgadu-devel >= %{_libgadu_ver}
BuildRequires:	libgsm-devel
BuildRequires:	libsndfile-devel >= 1.0
BuildRequires:	libtool
%{?with_nas:BuildRequires:	nas-devel}
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	qt-linguist
BuildRequires:	sed >= 4.0
%{?with_tcl_scripting:BuildRequires:	tk-devel >= 8.4}
%{?with_xmms:BuildRequires:	xmms-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kadu is client of Gadu-Gadu protocol. It's an IM for Linux and UN*X.
It's written with use of QT libraries.

%description -l pl
Kadu jest klientem protoko�u Gadu-Gadu. Inaczej m�wi�c, jest
komunikatorem dla Linuksa (oraz, przy niewielkim wysi�ku, innych
system�w UN*Xowych). Napisano go w oparciu o bibliotek� QT i KDE,
przeznaczony jest wi�c dla tego �rodowiska.

%package module-xmms
Summary:	Support XMMS status
Summary(pl):	Modu� statusu dla XMMS-a
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	xmms

%description module-xmms
Module which allows showing in status description information about
the song currently played in XMMS.

%description module-xmms -l pl
Modu� umo�liwiaj�cy pokazywanie w opisie statusu informacji o
odgrywanym utworze z odtwarzacza XMMS.

%package module-sound-alsa
Summary:	Support ALSA sound
Summary(pl):	Wsparcie dla d�wi�ku ALSA
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	alsa-lib

%description module-sound-alsa
ALSA sound support module.

%description module-sound-alsa -l pl
Modu� obs�ugi d�wi�ku przez ALSA.

%package module-sound-arts
Summary:	Support aRts sound server
Summary(pl):	Wsparcie dla serwera d�wi�ku aRts
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	arts

%description module-sound-arts
aRts sound server support module.

%description module-sound-arts -l pl
Modu� do obs�ugi serwera d�wi�ku aRts.

%package module-sound-esd
Summary:	Support ESD sound server
Summary(pl):	Wsparcie dla serwera d�wi�ku ESD
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	esound

%description module-sound-esd
ESD sound module.

%description module-sound-esd -l pl
Modu� obs�ugi d�wi�ku przez ESD.

%package module-sound-nas
Summary:	Support Network Audio System
Summary(pl):	Wsparcie dla sieciowego systemu d�wi�ku NAS
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	nas

%description module-sound-nas
Network Audio System sound module.

%description module-sound-nas -l pl
Modu� obs�ugi d�wi�ku przez NAS.

%package module-speech
Summary:	Speech synthesis support
Summary(pl):	Modu� obs�ugi "G�o�nego czytania"
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	powiedz

%description module-speech
Kadu module which supports reading aloud using speech synthesis
provided by external program "powiedz".

%description module-speech -l pl
Modu� obs�ugi "G�o�nego czytania" przez zewn�trzny program "powiedz".

%package module-amarok
Summary:	Support amarok status
Summary(pl):	Modu� statusu dla amarok
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	amarok

%description module-amarok
Module which allows showing in status description information about
the song currently played in amarok.

%description module-amarok -l pl
Modu� umo�liwiaj�cy w opisie statusu pokazywanie informacji o
odgrywanym utworze z odtwarzacza amarok.

%package module-spellchecker
Summary:	Checker of spelling mistakes
Summary(pl):	Modu� sprawdzaj�cy pisowni�
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	aspell

%description module-spellchecker
Checker of spelling mistakes.

%description module-spellchecker -l pl
Modu� sprawdzaj�cy pisowni�.

%package module-weather
Summary:	Weather module
Summary(pl):	Modu� pogodowy
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-weather
Informations of weather in locality of contact.

%description module-weather -l pl
Informacje o pogodzie w miejscowo�ci danego kontaktu.

%package module-tcl_scripting
Summary:	TCL scripting support and KaduPro extensions
Summary(pl):	Obs�uga skrypt�w TCL i rozszerze� KaduPro
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	tk

%description module-tcl_scripting
KaduPro is an add-on to Kadu, which uses a TCL module. If extends Kadu
functionality by useful, common daily functions, which implementation
in Kadu might be enough complicated or time-consuming.

%description module-tcl_scripting -l pl
KaduPro jest dodatkiem do Kadu wykorzystuj�cym modu� TCL. Poszerza on
mo�liwo�ci Kadu o przydatne na codzie� funkcje, kt�rych implementacja
w samym Kadu mog�aby by� dosy� skomplikowana, lub te� czasoch�onna.

%package module-spy
Summary:	Spying module that shows who's invisible
Summary(pl):	Modu� szpiegowski pokazuj�cy ukryte osoby
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-spy
Spying module that shows who's invisible.

%description module-spy -l pl
Modu� szpiegowski pokazuj�cy ukryte osoby.

%package module-imiface
Summary:	imiface module that integrate kadu with KDE with KIMIface interface
Summary(pl):	Modu� imiface do integrowania kadu z KDE za pomoc� interfejsu KIMIface
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-module-dcopexport = %{version}-%{release}

%description module-imiface
imiface module that integrate kadu with KDE with KIMIface interface.

%description module-imiface -l pl
imiface to modu� do integrowania kadu z KDE za pomoc� interfejsu
KIMIface.

%package module-iwait4u
Summary:	iwait4u module inform you, that someone from userlist is active
Summary(pl):	Modul iwait4u do informowania o dost�pno�ci os�b z listy
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-iwait4u
iwait4u module inform you, that someone from userlist is active.

%description module-iwait4u -l pl
Modul iwait4u informuje, �e osoba z listy u�ytkownik�w jest dost�pna.

%package module-dcopexport
Summary:	Kadu DCOP interface
Summary(pl):	Interfejs niekt�rych funkcji Kadu do DCOP
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-dcopexport
Kadu DCOP interface.

%description module-dcopexport -l pl
Interfejs niekt�rych funkcji Kadu do DCOP.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%if %{with xmms}
tar xzf %{SOURCE2} -C modules
%endif
%if %{with amarok}
tar xzf %{SOURCE3} -C modules
%endif
%if %{with spellchecker}
tar xzf %{SOURCE4} -C modules
%endif
%if %{with weather}
tar xjf %{SOURCE5} -C modules
%endif
%if %{with tcl_scripting}
tar xzf %{SOURCE6} -C modules
%endif
%if %{with spy}
tar xzf %{SOURCE7} -C modules
%endif
%if %{with imiface}
tar xzf %{SOURCE8} -C modules
%endif
%if %{with iwait4u}
tar xjf %{SOURCE9} -C modules
%endif
%if %{with dcopexport}
tar xjf %{SOURCE10} -C modules
%endif

%{__sed} -i 's,dataPath("kadu/modules/*,("%{_libdir}/kadu/modules/,g' kadu/modules.cpp

%build
#basic functional
%{__sed} -i 's/module_account_management=m/module_account_management=y/' .config
%{__sed} -i 's/module_autoaway=m/module_autoaway=y/' .config
%{__sed} -i 's/module_default_sms=m/module_default_sms=y/' .config
%{__sed} -i 's/module_hints=m/module_hints=y/' .config
%{__sed} -i 's/module_x11_docking=m/module_x11_docking=y/' .config
%{__sed} -i 's/module_window_notify=m/module_window_notify=y/' .config
%{__sed} -i 's/module_sms=m/module_sms=y/' .config
%{__sed} -i 's/module_default_sms=m/module_default_sms=y/' .config

%if %{with xmms}
%{__sed} -i 's/module_xmms=n/module_xmms=m/' .config
rm -f modules/xmms/.autodownloaded
%endif
%if %{with alsa}
%{__sed} -i 's/module_alsa_sound=n/module_alsa_sound=m/' .config
%endif
%if %{with arts}
%{__sed} -i 's/module_arts_sound=n/module_arts_sound=m/' .config
%endif
%if %{with esd}
%{__sed} -i 's/module_esd_sound=n/module_esd_sound=m/' .config
%endif
%if %{with nas}
%{__sed} -i 's/module_nas_sound=n/module_nas_sound=m/' .config
echo 'MODULE_LIBS_PATH="%{_prefix}/lib"' >> modules/nas_sound/spec
%endif
%if %{with speech}
%{__sed} -i 's/module_speech=n/module_speech=m/' .config
%endif
%if %{with amarok}
%{__sed} -i 's/module_amarok=n/module_amarok=m/' .config
echo 'MODULE_INCLUDES_PATH="%{_includedir}"'>> modules/amarok/spec
echo 'MODULE_LIBS_PATH="%{_prefix}/lib"' >> modules/amarok/spec
%endif
%if %{with spellchecker}
%{__sed} -i 's/module_spellchecker=n/module_spellchecker=m/' .config
%endif
%if %{with weather}
%{__sed} -i 's/module_weather=n/module_weather=m/' .config
%endif
%if %{with tcl_scripting}
%{__sed} -i 's/module_tcl_scripting=n/module_tcl_scripting=m/' .config
%endif
%if %{with imiface} && %{with dcopexport}
echo "module_imiface=m" >>.config
%endif
%if %{with iwait4u}
echo "module_iwait4u=m" >>.config
%endif
%if %{with dcopexport}
echo "module_dcopexport=m" >>.config
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
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data

%if %{with xmms}
mv -f $RPM_BUILD_ROOT%{_libdir}/%{name}/modules/data/xmms $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
%endif

%if %{with weather}
mv -f $RPM_BUILD_ROOT%{_libdir}/%{name}/modules/data/weather $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
%endif

%if %{with amarok}
mv -f $RPM_BUILD_ROOT%{_libdir}/%{name}/modules/data/amarok $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
%endif

%if %{with spellchecker}
mv -f $RPM_BUILD_ROOT%{_libdir}/%{name}/modules/data/spellchecker $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
%endif

%if %{with spy}
mv -f $RPM_BUILD_ROOT%{_libdir}/%{name}/modules/data/spy $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
%endif
%if %{with dcopexport}
mv -f $RPM_BUILD_ROOT%{_libdir}/%{name}/modules/data/dcopexport $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
%endif

# These should not be packaged
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/{HISTORY,README}
rm -f $RPM_BUILD_ROOT%{_datadir}/applnk/*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kadu.desktop
%{_pixmapsdir}/kadu.png
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/modules
%dir %{_datadir}/%{name}/modules/data
%{_datadir}/%{name}/themes
#About... files
%{_datadir}/%{name}/AUTHORS
%{_datadir}/%{name}/ChangeLog
%{_datadir}/%{name}/COPYING
%{_datadir}/%{name}/THANKS
#default modules:
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules
%dir %{_libdir}/%{name}/modules/bin
%dir %{_libdir}/%{name}/modules/data
%{_libdir}/%{name}/modules/account_management.desc
%{_libdir}/%{name}/modules/autoaway.desc
%{_libdir}/%{name}/modules/autoresponder.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/autoresponder.so
%{_libdir}/%{name}/modules/config_wizard.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/config_wizard.so
%{_libdir}/%{name}/modules/dcc.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/dcc.so
%{_libdir}/%{name}/modules/default_sms.desc
%{_libdir}/%{name}/modules/docking.desc
%{_libdir}/%{name}/modules/dsp_sound.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/dsp_sound.so
%{_libdir}/%{name}/modules/encryption.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/encryption.so
%{_libdir}/%{name}/modules/ext_sound.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/ext_sound.so
%{_libdir}/%{name}/modules/hints.desc
%{_libdir}/%{name}/modules/*notify.desc
%{_libdir}/%{name}/modules/sms.desc
%{_libdir}/%{name}/modules/sound.desc
%{_libdir}/%{name}/modules/voice.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/voice.so
%{_libdir}/%{name}/modules/x11_docking.desc
#default modules translation:
%dir %{_libdir}/%{name}/modules/translations
%lang(de) %{_libdir}/%{name}/modules/translations/account_management_de.qm
%lang(fr) %{_libdir}/%{name}/modules/translations/account_management_fr.qm
%lang(it) %{_libdir}/%{name}/modules/translations/account_management_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/account_management_pl.qm
%lang(de) %{_libdir}/%{name}/modules/translations/autoaway_de.qm
%lang(fr) %{_libdir}/%{name}/modules/translations/autoaway_fr.qm
%lang(it) %{_libdir}/%{name}/modules/translations/autoaway_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/autoaway_pl.qm
%lang(de) %{_libdir}/%{name}/modules/translations/autoresponder_de.qm
%lang(fr) %{_libdir}/%{name}/modules/translations/autoresponder_fr.qm
%lang(it) %{_libdir}/%{name}/modules/translations/autoresponder_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/autoresponder_pl.qm
%lang(de) %{_libdir}/%{name}/modules/translations/config_wizard_de.qm
%lang(fr) %{_libdir}/%{name}/modules/translations/config_wizard_fr.qm
%lang(it) %{_libdir}/%{name}/modules/translations/config_wizard_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/config_wizard_pl.qm
%lang(de) %{_libdir}/%{name}/modules/translations/dcc_de.qm
%lang(fr) %{_libdir}/%{name}/modules/translations/dcc_fr.qm
%lang(it) %{_libdir}/%{name}/modules/translations/dcc_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/dcc_pl.qm
%lang(de) %{_libdir}/%{name}/modules/translations/default_sms_de.qm
%lang(fr) %{_libdir}/%{name}/modules/translations/default_sms_fr.qm
%lang(it) %{_libdir}/%{name}/modules/translations/default_sms_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/default_sms_pl.qm
%lang(de) %{_libdir}/%{name}/modules/translations/docking_de.qm
%lang(fr) %{_libdir}/%{name}/modules/translations/docking_fr.qm
%lang(it) %{_libdir}/%{name}/modules/translations/docking_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/docking_pl.qm
%lang(de) %{_libdir}/%{name}/modules/translations/dsp_sound_de.qm
%lang(fr) %{_libdir}/%{name}/modules/translations/dsp_sound_fr.qm
%lang(it) %{_libdir}/%{name}/modules/translations/dsp_sound_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/dsp_sound_pl.qm
%lang(de) %{_libdir}/%{name}/modules/translations/encryption_de.qm
%lang(fr) %{_libdir}/%{name}/modules/translations/encryption_fr.qm
%lang(it) %{_libdir}/%{name}/modules/translations/encryption_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/encryption_pl.qm
%lang(de) %{_libdir}/%{name}/modules/translations/ext_sound_de.qm
%lang(fr) %{_libdir}/%{name}/modules/translations/ext_sound_fr.qm
%lang(it) %{_libdir}/%{name}/modules/translations/ext_sound_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/ext_sound_pl.qm
%lang(de) %{_libdir}/%{name}/modules/translations/hints_de.qm
%lang(fr) %{_libdir}/%{name}/modules/translations/hints_fr.qm
%lang(it) %{_libdir}/%{name}/modules/translations/hints_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/hints_pl.qm
%lang(de) %{_libdir}/%{name}/modules/translations/*notify_de.qm
%lang(fr) %{_libdir}/%{name}/modules/translations/*notify_fr.qm
%lang(it) %{_libdir}/%{name}/modules/translations/*notify_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/*notify_pl.qm
%lang(de) %{_libdir}/%{name}/modules/translations/sms_de.qm
%lang(fr) %{_libdir}/%{name}/modules/translations/sms_fr.qm
%lang(it) %{_libdir}/%{name}/modules/translations/sms_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/sms_pl.qm
%lang(de) %{_libdir}/%{name}/modules/translations/sound_de.qm
%lang(fr) %{_libdir}/%{name}/modules/translations/sound_fr.qm
%lang(it) %{_libdir}/%{name}/modules/translations/sound_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/sound_pl.qm
%lang(de) %{_libdir}/%{name}/modules/translations/voice_de.qm
%lang(fr) %{_libdir}/%{name}/modules/translations/voice_fr.qm
%lang(it) %{_libdir}/%{name}/modules/translations/voice_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/voice_pl.qm
%lang(de) %{_libdir}/%{name}/modules/translations/x11_docking_de.qm
%lang(fr) %{_libdir}/%{name}/modules/translations/x11_docking_fr.qm
%lang(it) %{_libdir}/%{name}/modules/translations/x11_docking_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/x11_docking_pl.qm
#global translation:
%dir %{_datadir}/%{name}/translations
%lang(de) %{_datadir}/%{name}/translations/kadu_de.qm
%lang(en) %{_datadir}/%{name}/translations/kadu_en.qm
%lang(fr) %{_datadir}/%{name}/translations/kadu_fr.qm
%lang(it) %{_datadir}/%{name}/translations/kadu_it.qm
%lang(pl) %{_datadir}/%{name}/translations/kadu_pl.qm
%lang(de) %{_datadir}/%{name}/translations/qt_de.qm
%lang(en) %{_datadir}/%{name}/translations/qt_en.qm
%lang(en) %{_datadir}/%{name}/translations/qt_fr.qm
%lang(it) %{_datadir}/%{name}/translations/qt_it.qm
%lang(pl) %{_datadir}/%{name}/translations/qt_pl.qm
#wizard
%{_libdir}/%{name}/modules/data/config_wizard

%if %{with xmms}
%files module-xmms
%defattr(644,root,root,755)
%{_libdir}/%{name}/modules/xmms.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/xmms.so
%{_datadir}/%{name}/modules/data/xmms
%lang(pl) %{_libdir}/%{name}/modules/translations/xmms_pl.qm
%endif

%if %{with alsa}
%files module-sound-alsa
%defattr(644,root,root,755)
%{_libdir}/%{name}/modules/alsa_sound.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/alsa_sound.so
%lang(de) %{_libdir}/%{name}/modules/translations/alsa_sound_de.qm
%lang(fr) %{_libdir}/%{name}/modules/translations/alsa_sound_fr.qm
%lang(it) %{_libdir}/%{name}/modules/translations/alsa_sound_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/alsa_sound_pl.qm
%endif

%if %{with arts}
%files module-sound-arts
%defattr(644,root,root,755)
%{_libdir}/%{name}/modules/arts_sound.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/arts_sound.so
%dir %{_libdir}/%{name}/modules/bin/arts_sound
%attr(755,root,root) %{_libdir}/%{name}/modules/bin/arts_sound/arts_connector
%endif

%if %{with esd}
%files module-sound-esd
%defattr(644,root,root,755)
%{_libdir}/%{name}/modules/esd_sound.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/esd_sound.so
%endif

%if %{with nas}
%files module-sound-nas
%defattr(644,root,root,755)
%{_libdir}/%{name}/modules/nas_sound.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/nas_sound.so
%endif

%if %{with speech}
%files module-speech
%defattr(644,root,root,755)
%{_libdir}/%{name}/modules/speech.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/speech.so
%lang(de) %{_libdir}/%{name}/modules/translations/speech_de.qm
%lang(fr) %{_libdir}/%{name}/modules/translations/speech_fr.qm
%lang(it) %{_libdir}/%{name}/modules/translations/speech_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/speech_pl.qm
%endif

%if %{with amarok}
%files module-amarok
%defattr(644,root,root,755)
%{_libdir}/%{name}/modules/amarok.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/amarok.so
%{_datadir}/%{name}/modules/data/amarok
%lang(de) %{_libdir}/%{name}/modules/translations/amarok_de.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/amarok_pl.qm
%endif

%if %{with spellchecker}
%files module-spellchecker
%defattr(644,root,root,755)
%{_libdir}/%{name}/modules/spellchecker.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/spellchecker.so
%{_datadir}/%{name}/modules/data/spellchecker
%lang(pl) %{_libdir}/%{name}/modules/translations/spellchecker_pl.qm
%endif

%if %{with weather}
%files module-weather
%defattr(644,root,root,755)
%{_libdir}/%{name}/modules/weather.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/weather.so
%{_datadir}/%{name}/modules/data/weather
%lang(pl) %{_libdir}/%{name}/modules/translations/weather_pl.qm
%endif

%if %{with tcl_scripting}
%files module-tcl_scripting
%defattr(644,root,root,755)
%{_libdir}/%{name}/modules/tcl_scripting.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/tcl_scripting.so
%{_libdir}/%{name}/modules/data/tcl_scripting
%lang(de) %{_libdir}/%{name}/modules/translations/tcl_scripting_de.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/tcl_scripting_pl.qm
%endif

%if %{with spy}
%files module-spy
%defattr(644,root,root,755)
%{_libdir}/%{name}/modules/spy.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/spy.so
%{_datadir}/%{name}/modules/data/spy
%lang(pl) %{_libdir}/%{name}/modules/translations/spy_pl.qm
%endif

%if %{with dcopexport}
%files module-dcopexport
%defattr(644,root,root,755)
%{_libdir}/%{name}/modules/dcopexport.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/dcopexport.so
%lang(pl) %{_libdir}/%{name}/modules/translations/dcopexport_pl.qm
%dir %{_libdir}/%{name}/modules/bin/dcopexport
%attr(755,root,root) %{_libdir}/%{name}/modules/bin/dcopexport/*.sh
%{_datadir}/%{name}/modules/data/dcopexport
%endif

%if %{with imiface}
%files module-imiface
%defattr(644,root,root,755)
%{_libdir}/%{name}/modules/imiface.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/imiface.so
%endif

%if %{with iwait4u}
%files module-iwait4u
%defattr(644,root,root,755)
%{_libdir}/%{name}/modules/iwait4u.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/iwait4u.so
%lang(pl) %{_libdir}/%{name}/modules/translations/iwait4u_pl.qm
%endif
