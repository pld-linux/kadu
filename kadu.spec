#
# TODO:
# - make miasto_plusa/tcl_scripting compile again
# - consider dropping spy module: doesn't work anymore as expected 
#   (also website is down, download is down)
#
# Conditional build:
%bcond_without	amarok		# without amarok player support module
%bcond_without	alsa		# without ALSA support
%bcond_without	arts		# without arts sound server support
%bcond_without	esd		# without ESD sound server support
%bcond_with	miasto_plusa	# without miasto_plusa module support
%bcond_without	nas		# without Network Audio System support
%bcond_without	speech		# without Speech synthesis support
%bcond_without	spellchecker	# without spellchecker (Aspell support)
%bcond_with	spy		# without Spying module that shows who's invisible
%bcond_with	tcl_scripting	# without TCL scripting support and KaduPro extensions
%bcond_without	weather		# without weather check module support
%bcond_without	xmms		# without xmms player support module

%define		_amarok_mod_ver		1.18
%define		_libgadu_ver		4:1.6
%define		_spellchecker_mod_ver	0.19
%define		_spy_mod_ver		0.0.8-2
%define		_tcl_mod_ver		0.6.2-Josephine
%define		_weather_ver		3.01
%define		_xmms_mod_ver		1.30
%define		_led_ver		0.9
%define		_miasto_plusa_ver	1.3.2
%define		_tabs_ver		rev46
%define		snapshot		20061025
%define		year	%(echo %{snapshot} |cut -b -4)
#
Summary:	A Gadu-Gadu client for online messaging
Summary(pl):	Klient Gadu-Gadu do przesy³ania wiadomo¶ci po sieci
Name:		kadu
Version:	0.5.0
Release:	0.%{snapshot}.3
License:	GPL v2
Group:		Applications/Communications
Source0:	http://kadu.net/download/snapshots/%{year}/%{name}-%{snapshot}.tar.bz2
# Source0-md5:	21a55d099699d967028e49f4d8307a99
Source1:	%{name}.desktop
Source2:	http://scripts.one.pl/xmms/devel/%{version}/xmms-%{_xmms_mod_ver}.tar.gz
# Source2-md5:	422b0bfe2fe1d67620896576e3092ac8
Source3:	http://scripts.one.pl/amarok/devel/%{version}/amarok-%{_amarok_mod_ver}.tar.gz
# Source3-md5:	0ec8466884d98d63a6d2e4eeac814612
Source4:	http://scripts.one.pl/spellchecker/devel/%{version}/spellchecker-%{_spellchecker_mod_ver}.tar.gz
# Source4-md5:	f1e1c572f9fd92dfb420e62818bc826c
Source5:	http://www.kadu.net/~blysk/weather-%{_weather_ver}.tar.bz2
# Source5-md5:	c21727575d4bab551adeb9b5b1787f0c
Source6:	http://scripts.one.pl/tcl4kadu/files/stable/0.4.3/tcl_scripting-%{_tcl_mod_ver}.tar.gz
# Source6-md5:	97406c1f3f34b8a073e0a1a18e842c9e
Source7:	http://scripts.one.pl/~przemos/download/kadu-spy-%{_spy_mod_ver}.tar.gz
# Source7-md5:	2ffba6058d5d463ade20ff697e200f7c
Source8:	http://www.kadu.net/~blysk/led_notify-%{_led_ver}.tar.bz2
# Source8-md5:	3f9e347fd775324f4077f2f6849a0de7
Source9:	http://www.kadu.net/~patryk/miastoplusa_sms/miastoplusa_sms-%{_miasto_plusa_ver}.tar.gz
# Source9-md5:	76233b35fa769c56d7ff1343b1bf810f
Source10:	http://gov.one.pl/svnsnap/tabs-svn-%{_tabs_ver}.tar.gz
# Source10-md5:	0d313a489bad8bf8b324e347e74f00e6
Patch0:		%{name}-ac_am.patch
URL:		http://kadu.net/
%{?with_alsa:BuildRequires:	alsa-lib-devel}
%{?with_arts:BuildRequires:	arts-devel}
%{?with_spellchecker:BuildRequires:	aspell-devel}
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_miasto_plusa:BuildRequires:	curl-devel}
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
%define		_modules_dir	%{_libdir}/%{name}/modules

%description
Kadu is client of Gadu-Gadu protocol. It's an IM for Linux and UN*X.
It's written with use of QT libraries.

%description -l pl
Kadu jest klientem protoko³u Gadu-Gadu. Inaczej mówi±c, jest
komunikatorem dla Linuksa (oraz, przy niewielkim wysi³ku, innych
systemów UN*Xowych). Napisano go w oparciu o bibliotekê QT i KDE,
przeznaczony jest wiêc dla tego ¶rodowiska.

%package module-xmms
Summary:	Support XMMS status
Summary(pl):	Modu³ statusu dla XMMS-a
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	xmms

%description module-xmms
Module which allows showing in status description information about
the song currently played in XMMS.

%description module-xmms -l pl
Modu³ umo¿liwiaj±cy pokazywanie w opisie statusu informacji o
odgrywanym utworze z odtwarzacza XMMS.

%package module-sound-alsa
Summary:	Support ALSA sound
Summary(pl):	Wsparcie dla d¼wiêku ALSA
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	alsa-lib

%description module-sound-alsa
ALSA sound support module.

%description module-sound-alsa -l pl
Modu³ obs³ugi d¼wiêku przez ALSA.


%package module-sound-arts
Summary:	Support aRts sound server
Summary(pl):	Wsparcie dla serwera dzwiêku arts
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	arts

%description module-sound-arts
aRts sound server support module.

%description module-sound-arts -l pl
Modu³ do obs³ugi serwera d¼wiêku aRts.

%package module-sound-esd
Summary:	Support ESD sound server
Summary(pl):	Wsparcie dla serwera d¼wiêku ESD
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	esound

%description module-sound-esd
ESD sound module.

%description module-sound-esd -l pl
Modu³ obs³ugi d¼wiêku przez ESD.

%package module-sound-nas
Summary:	Support Network Audio System
Summary(pl):	Wsparcie dla sieciowego systemu dzwiêku NAS
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	nas

%description module-sound-nas
Network Audio System sound module.

%description module-sound-nas -l pl
Modu³ obs³ugi d¼wiêku przez NAS.

%package module-speech
Summary:	Speech synthesis support
Summary(pl):	Modu³ obs³ugi "G³o¶nego czytania"
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	powiedz

%description module-speech
Kadu module which supports reading aloud using speech synthesis
provided by external program "powiedz".

%description module-speech -l pl
Modu³ obs³ugi "G³o¶nego czytania" przez zewnêtrzny program "powiedz".

%package module-amarok
Summary:	Support amarok status
Summary(pl):	Modu³ statusu dla amarok
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	amarok

%description module-amarok
Module which allows showing in status description information about
the song currently played in amarok.

%description module-amarok -l pl
Modu³ umo¿liwiaj±cy w opisie statusu pokazywanie informacji o
odgrywanym utworze z odtwarzacza amarok.

%package module-spellchecker
Summary:	Checker of spelling mistakes
Summary(pl):	Modu³ sprawdzaj±cy pisowniê
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	aspell
%description module-spellchecker
Checker of spelling mistakes.

%description module-spellchecker -l pl
Modu³ sprawdzaj±cy pisowniê.

%package module-weather
Summary:	Weather module
Summary(pl):	Modu³ pogodowy
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-weather
Informations of weather in locality of contact.

%description module-weather -l pl
Informacje o pogodzie w miejscowo¶ci danego kontaktu.

%package module-tcl_scripting
Summary:	TCL scripting support and KaduPro extensions
Summary(pl):	Obs³uga skryptów TCL i rozszerzeñ KaduPro
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	tk

%description module-tcl_scripting
KaduPro is an add-on to Kadu, which uses a TCL module. If extends Kadu
functionality by useful, common daily functions, which implementation
in Kadu might be enough complicated or time-consuming.

%description module-tcl_scripting -l pl
KaduPro jest dodatkiem do Kadu wykorzystuj±cym modu³ TCL. Poszerza on
mo¿liwo¶ci Kadu o przydatne na codzieñ funkcje, których implementacja
w samym Kadu mog³a by byæ dosyæ skomplikowana, lub te¿ czasoch³onna.

%package module-spy
Summary:	Spying module that shows who's invisible
Summary(pl):	Modu³ szpiegowski pokazuj±cy ukryte osoby
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-spy
Spying module that shows who's invisible

%description module-spy -l pl
Modu³ szpiegowski pokazuj±cy ukryte osoby.

%prep
%setup -q -n %{name}
%patch0 -p1

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
tar xjf %{SOURCE8} -C modules
%if %{with miasto_plusa}
tar xzf %{SOURCE9} -C modules
%endif
tar xzf %{SOURCE10} -C modules


%{__sed} -i 's,dataPath("kadu/modules/*,("%{_libdir}/kadu/modules/,g'  kadu/modules.cpp

%build
%{__sed} -i 's/module_tabs=n/module_tabs=m/' .config
%if %{with miasto_plusa}
%{__sed} -i 's/module_miastoplusa_sms=n/module_miastoplusa_sms=m/' .config
%endif
%{__sed} -i 's/module_led_notify=n/module_led_notify=m/' .config
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
echo 'MODULE_LIBS_PATH="/usr/lib"' >> modules/nas_sound/spec
%endif
%if %{with speech}
%{__sed} -i 's/module_speech=n/module_speech=m/' .config
%endif
%if %{with amarok}
%{__sed} -i 's/module_amarok=n/module_amarok=m/' .config
echo 'MODULE_INCLUDES_PATH="/usr/include"'>> modules/amarok/spec
echo 'MODULE_LIBS_PATH="/usr/lib"' >> modules/amarok/spec
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

# force in mv stopped working
cp -fa $RPM_BUILD_ROOT%{_datadir}/%{name}/modules $RPM_BUILD_ROOT%{_libdir}/%{name}
rm -fr $RPM_BUILD_ROOT%{_datadir}/%{name}/modules
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
cp -fa $RPM_BUILD_ROOT%{_modules_dir}/data/config_wizard $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
rm -fr $RPM_BUILD_ROOT%{_modules_dir}/data/config_wizard
cp -Rfa $RPM_BUILD_ROOT%{_modules_dir}/data/tabs $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
rm -fr $RPM_BUILD_ROOT%{_modules_dir}/data/tabs

%if %{with xmms}
cp -fa $RPM_BUILD_ROOT%{_modules_dir}/data/xmms $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
rm -fr $RPM_BUILD_ROOT%{_modules_dir}/data/xmms
%endif

%if %{with weather}
mv -f $RPM_BUILD_ROOT%{_modules_dir}/data/weather $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
%endif

%if %{with amarok}
mv -f $RPM_BUILD_ROOT%{_modules_dir}/data/amarok $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
%endif

%if %{with spellchecker}
cp -fa $RPM_BUILD_ROOT%{_modules_dir}/data/spellchecker $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
rm -fr $RPM_BUILD_ROOT%{_modules_dir}/data/spellchecker
%endif

%if %{with spy}
mv -f $RPM_BUILD_ROOT%{_modules_dir}/data/spy $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
%endif

%if %{with miasto_plusa}
cp -fa $RPM_BUILD_ROOT%{_modules_dir}/data/miastoplusa_sms $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
rm -fr $RPM_BUILD_ROOT%{_modules_dir}/data/miastoplusa_sms
%endif


rm -rf `find $RPM_BUILD_ROOT -name CVS`

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kadu.desktop
%{_pixmapsdir}/kadu.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/themes
%{_datadir}/%{name}/AUTHORS
%{_datadir}/%{name}/ChangeLog
%{_datadir}/%{name}/COPYING
%{_datadir}/%{name}/THANKS
%if %{with miasto_plusa}
%{_datadir}/%{name}/modules/data/miastoplusa_sms/curl-ca-bundle.crt
%endif

%dir %{_datadir}/%{name}/modules
%dir %{_datadir}/%{name}/modules/data
%dir %{_datadir}/%{name}/modules/data/tabs
%{_datadir}/%{name}/modules/data/tabs/attach.png

#default modules:
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules
%dir %{_modules_dir}
%{_modules_dir}/account_management.desc
%attr(755,root,root) %{_modules_dir}/account_management.so
%{_modules_dir}/autoaway.desc
%attr(755,root,root) %{_modules_dir}/autoaway.so
%{_modules_dir}/autoresponder.desc
%attr(755,root,root) %{_modules_dir}/autoresponder.so
%{_modules_dir}/config_wizard.desc
%attr(755,root,root) %{_modules_dir}/config_wizard.so
%{_modules_dir}/dcc.desc
%attr(755,root,root) %{_modules_dir}/dcc.so
%{_modules_dir}/default_sms.desc
%attr(755,root,root) %{_modules_dir}/default_sms.so
%{_modules_dir}/docking.desc
%{_modules_dir}/dsp_sound.desc
%attr(755,root,root) %{_modules_dir}/dsp_sound.so
%{_modules_dir}/encryption.desc
%attr(755,root,root) %{_modules_dir}/encryption.so
%{_modules_dir}/ext_sound.desc
%attr(755,root,root) %{_modules_dir}/ext_sound.so
%{_modules_dir}/hints.desc
%attr(755,root,root) %{_modules_dir}/hints.so
%if %{with miasto_plusa}
%{_modules_dir}/miastoplusa_sms.desc
%attr(755,root,root) %{_modules_dir}/miastoplusa_sms.so
%endif
%{_modules_dir}/migration.desc
%attr(755,root,root) %{_modules_dir}/migration.so
%{_modules_dir}/*notify.desc
%attr(755,root,root) %{_modules_dir}/led_notify.so
%{_modules_dir}/sms.desc
%attr(755,root,root) %{_modules_dir}/sms.so
%{_modules_dir}/sound.desc
%{_modules_dir}/tabs.desc
%attr(755,root,root) %{_modules_dir}/tabs.so
%{_modules_dir}/voice.desc
%attr(755,root,root) %{_modules_dir}/voice.so
%attr(755,root,root) %{_modules_dir}/window_notify.so
%{_modules_dir}/x11_docking.desc
%attr(755,root,root) %{_modules_dir}/x11_docking.so
#default modules translation:
%dir %{_modules_dir}/translations
%lang(de) %{_modules_dir}/translations/account_management_de.qm
%lang(fr) %{_modules_dir}/translations/account_management_fr.qm
%lang(it) %{_modules_dir}/translations/account_management_it.qm
%lang(pl) %{_modules_dir}/translations/account_management_pl.qm
%lang(de) %{_modules_dir}/translations/autoaway_de.qm
%lang(fr) %{_modules_dir}/translations/autoaway_fr.qm
%lang(it) %{_modules_dir}/translations/autoaway_it.qm
%lang(pl) %{_modules_dir}/translations/autoaway_pl.qm
%lang(de) %{_modules_dir}/translations/autoresponder_de.qm
%lang(fr) %{_modules_dir}/translations/autoresponder_fr.qm
%lang(it) %{_modules_dir}/translations/autoresponder_it.qm
%lang(pl) %{_modules_dir}/translations/autoresponder_pl.qm
%lang(de) %{_modules_dir}/translations/config_wizard_de.qm
%lang(fr) %{_modules_dir}/translations/config_wizard_fr.qm
%lang(it) %{_modules_dir}/translations/config_wizard_it.qm
%lang(pl) %{_modules_dir}/translations/config_wizard_pl.qm
%lang(de) %{_modules_dir}/translations/dcc_de.qm
%lang(fr) %{_modules_dir}/translations/dcc_fr.qm
%lang(it) %{_modules_dir}/translations/dcc_it.qm
%lang(pl) %{_modules_dir}/translations/dcc_pl.qm
%lang(de) %{_modules_dir}/translations/default_sms_de.qm
%lang(fr) %{_modules_dir}/translations/default_sms_fr.qm
%lang(it) %{_modules_dir}/translations/default_sms_it.qm
%lang(pl) %{_modules_dir}/translations/default_sms_pl.qm
%lang(de) %{_modules_dir}/translations/docking_de.qm
%lang(fr) %{_modules_dir}/translations/docking_fr.qm
%lang(it) %{_modules_dir}/translations/docking_it.qm
%lang(pl) %{_modules_dir}/translations/docking_pl.qm
%lang(de) %{_modules_dir}/translations/dsp_sound_de.qm
%lang(fr) %{_modules_dir}/translations/dsp_sound_fr.qm
%lang(it) %{_modules_dir}/translations/dsp_sound_it.qm
%lang(pl) %{_modules_dir}/translations/dsp_sound_pl.qm
%lang(de) %{_modules_dir}/translations/encryption_de.qm
%lang(fr) %{_modules_dir}/translations/encryption_fr.qm
%lang(it) %{_modules_dir}/translations/encryption_it.qm
%lang(pl) %{_modules_dir}/translations/encryption_pl.qm
%lang(de) %{_modules_dir}/translations/ext_sound_de.qm
%lang(fr) %{_modules_dir}/translations/ext_sound_fr.qm
%lang(it) %{_modules_dir}/translations/ext_sound_it.qm
%lang(pl) %{_modules_dir}/translations/ext_sound_pl.qm
%lang(de) %{_modules_dir}/translations/hints_de.qm
%lang(fr) %{_modules_dir}/translations/hints_fr.qm
%lang(it) %{_modules_dir}/translations/hints_it.qm
%lang(pl) %{_modules_dir}/translations/hints_pl.qm
%if %{with miasto_plusa}
%lang(pl) %{_modules_dir}/translations/miastoplusa_sms_pl.qm
%endif
%lang(de) %{_modules_dir}/translations/migration_de.qm
%lang(fr) %{_modules_dir}/translations/migration_fr.qm
%lang(it) %{_modules_dir}/translations/migration_it.qm
%lang(pl) %{_modules_dir}/translations/migration_pl.qm
%lang(de) %{_modules_dir}/translations/*notify_de.qm
%lang(fr) %{_modules_dir}/translations/*notify_fr.qm
%lang(it) %{_modules_dir}/translations/*notify_it.qm
%lang(pl) %{_modules_dir}/translations/*notify_pl.qm
%lang(de) %{_modules_dir}/translations/sms_de.qm
%lang(fr) %{_modules_dir}/translations/sms_fr.qm
%lang(it) %{_modules_dir}/translations/sms_it.qm
%lang(pl) %{_modules_dir}/translations/sms_pl.qm
%lang(de) %{_modules_dir}/translations/sound_de.qm
%lang(fr) %{_modules_dir}/translations/sound_fr.qm
%lang(it) %{_modules_dir}/translations/sound_it.qm
%lang(pl) %{_modules_dir}/translations/sound_pl.qm
%lang(pl) %{_modules_dir}/translations/tabs_pl.qm
%lang(de) %{_modules_dir}/translations/voice_de.qm
%lang(fr) %{_modules_dir}/translations/voice_fr.qm
%lang(it) %{_modules_dir}/translations/voice_it.qm
%lang(pl) %{_modules_dir}/translations/voice_pl.qm
%lang(de) %{_modules_dir}/translations/x11_docking_de.qm
%lang(fr) %{_modules_dir}/translations/x11_docking_fr.qm
%lang(it) %{_modules_dir}/translations/x11_docking_it.qm
%lang(pl) %{_modules_dir}/translations/x11_docking_pl.qm
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
%{_datadir}/%{name}/modules/data/config_wizard

%if %{with xmms}
%files module-xmms
%defattr(644,root,root,755)
%{_modules_dir}/xmms.desc
%attr(755,root,root) %{_modules_dir}/xmms.so
%lang(pl) %{_modules_dir}/translations/xmms_pl.qm
%{_datadir}/%{name}/modules/data/xmms/xmms.png
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
%{_modules_dir}/arts_sound.desc
%attr(755,root,root) %{_modules_dir}/arts_sound.so
%dir %{_modules_dir}/bin/
%dir %{_modules_dir}/bin/arts_sound
%attr(755,root,root) %{_modules_dir}/bin/arts_sound/arts_connector
%endif

%if %{with esd}
%files module-sound-esd
%defattr(644,root,root,755)
%{_modules_dir}/esd_sound.desc
%attr(755,root,root) %{_modules_dir}/esd_sound.so
%endif

%if %{with nas}
%files module-sound-nas
%defattr(644,root,root,755)
%{_modules_dir}/nas_sound.desc
%attr(755,root,root) %{_modules_dir}/nas_sound.so
%endif

%if %{with speech}
%files module-speech
%defattr(644,root,root,755)
%{_modules_dir}/speech.desc
%attr(755,root,root) %{_modules_dir}/speech.so
%lang(de) %{_modules_dir}/translations/speech_de.qm
%lang(fr) %{_modules_dir}/translations/speech_fr.qm
%lang(it) %{_modules_dir}/translations/speech_it.qm
%lang(pl) %{_modules_dir}/translations/speech_pl.qm
%endif

%if %{with amarok}
%files module-amarok
%defattr(644,root,root,755)
%{_modules_dir}/amarok.desc
%attr(755,root,root) %{_modules_dir}/amarok.so
%lang(pl) %{_modules_dir}/translations/amarok_pl.qm
%lang(de) %{_modules_dir}/translations/amarok_de.qm
%dir %{_datadir}/%{name}/modules/data/amarok
%{_datadir}/%{name}/modules/data/amarok/amarok.png
%endif

%if %{with spellchecker}
%files module-spellchecker
%defattr(644,root,root,755)
%{_modules_dir}/spellchecker.desc
%attr(755,root,root) %{_modules_dir}/spellchecker.so
%lang(pl) %{_modules_dir}/translations/spellchecker_pl.qm
%dir %{_datadir}/%{name}/modules/data/spellchecker
%{_datadir}/%{name}/modules/data/spellchecker/config.png
%endif

%if %{with weather}
%files module-weather
%defattr(644,root,root,755)
%{_modules_dir}/weather.desc
%attr(755,root,root) %{_modules_dir}/weather.so
%dir %{_datadir}/%{name}/modules/data/weather
%{_datadir}/%{name}/modules/data/weather
%lang(pl) %{_modules_dir}/translations/weather_pl.qm
%endif

%if %{with tcl_scripting}
%files module-tcl_scripting
%defattr(644,root,root,755)
%{_modules_dir}/tcl_scripting.desc
%attr(755,root,root) %{_modules_dir}/tcl_scripting.so
%{_modules_dir}/data/tcl_scripting
%lang(de) %{_modules_dir}/translations/tcl_scripting_de.qm
%lang(pl) %{_modules_dir}/translations/tcl_scripting_pl.qm
%endif

%if %{with spy}
%files module-spy
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/modules/data/spy
%{_datadir}/%{name}/modules/data/spy/spy32.png
%{_modules_dir}/spy.desc
%attr(755,root,root) %{_modules_dir}/spy.so
%lang(pl) %{_modules_dir}/translations/spy_pl.qm
%endif
