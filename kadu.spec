#
# TODO:
# - spy module - won't work with gg7 clients
#	downloads stuff while building: Downloading crystal16 icon theme
#--02:05:17--  http://kadu.net/autodownload/icons/kadu-0.5.0-crystal16.href
#           => `kadu-0.5.0-crystal16.href'
#
# Conditional build:
%bcond_without	advanced_userlist	# without Advanced Userlist support
%bcond_without	amarok			# without amarok player support module
%bcond_without	autoresponder		# without autoresponder module support
%bcond_without	dcopexport		# without dcopexport module support
%bcond_without	docking_desktop		# without desktop_docking module support
%bcond_without	filedesc		# without filedesc module support
%bcond_without	filtering		# without filtering module support
%bcond_without	firewall		# without firewall module support
%bcond_without	iwait4u			# without iwait4u module support
%bcond_without	notify_exec		# without exec_notify module support
%bcond_without	notify_led		# without led_notify module support
%bcond_without	notify_osdhints		# without osdhints_notify module
%bcond_without	notify_pcspeaker	# without pcspeaker_notify module support
%bcond_without	notify_speech		# without Speech synthesis support
%bcond_without	powerkadu		# without PowerKadu extensions
%bcond_without	profiles		# without profiles module support
%bcond_without	screenshot		# without screenshot module support
%bcond_without	sms_miastoplusa		# without miastoplusa_sms module support
%bcond_without	sound_alsa		# without ALSA support
%bcond_without	sound_arts		# without arts sound server support
%bcond_without	sound_dsp		# without DSP sound module support
%bcond_without	sound_esd		# without ESD sound server support
%bcond_without	sound_nas		# without Network Audio System support
%bcond_without	spellchecker		# without spellchecker (Aspell support)
%bcond_with	spy			# with Spying module that shows who's invisible
%bcond_without	tabs			# without tabs support module
%bcond_without	weather			# without weather check module support
%bcond_without	xmms			# without xmms player support module

%define		_advanced_userlist_ver	20070101
%define		_amarok_mod_ver		1.21
%define		_dcopexport_ver		0.11.3-20070321
%define		_filedesc_ver		1.12
%define		_filtering_ver		20070123
%define		_firewall_ver		0.6.4
%define		_iwait4u_ver		1.3
%define		_libgadu_ver		4:1.7
%define		_notify_exec_ver	20070101
%define		_notify_led_ver		0.9
%define		_notify_osdhints_ver	0.3.2.2
%define		_notify_pcspeaker_ver	0.5.0.3
%define		_powerkadu_ver		20070129
%define		_profiles_ver		0.1.2
%define		_screenshot_ver		0.4.4
%define		_sms_miastoplusa_ver	1.3.5
%define		_spellchecker_mod_ver	0.20
%define		_spy_mod_ver		0.0.8-3
%define		_tabs_ver		1.0.0
%define		_weather_ver		3.01
%define		_xmms_mod_ver		1.34

Summary:	A Gadu-Gadu client for online messaging
Summary(pl.UTF-8):	Klient Gadu-Gadu do przesyłania wiadomości po sieci
Name:		kadu
Version:	0.5.0
Release:	4
License:	GPL v2
Group:		Applications/Communications

Source0:	http://kadu.net/download/stable/%{name}-%{version}.tar.bz2
# Source0-md5:	895f7c88d36dbb188e8bc26664fbf430
Source1:	%{name}.desktop
Source2:	http://www.kadu.net/~joi/advanced_userlist/packages/advanced_userlist-%{_advanced_userlist_ver}.tar.bz2
# Source2-md5:	fb60ce3c6fc3bf64909550bd758560c7
Source3:	http://scripts.one.pl/amarok/stable/%{version}/amarok-%{_amarok_mod_ver}.tar.gz
# Source3-md5:	6eb387be3d3d9a275dc9642f172035b1
Source4:	http://alan.umcs.lublin.pl/~pinkworm/dcopexport/dcopexport-%{_dcopexport_ver}-0.5.0.tar.bz2
# Source4-md5:	b5fd429c42d847b14dcac51d646f96ae
Source5:	http://scripts.one.pl/filedesc/stable/%{version}/filedesc-%{_filedesc_ver}.tar.gz
# Source5-md5:	d5e5718f3a64f33874a869b235bbdff7
Source6:	http://alan.umcs.lublin.pl/~pinkworm/filtering/filtering-0.5.1-%{_filtering_ver}-0.5.0.tar.bz2
# Source6-md5:	3ecb26736c2490c18d5d534f8b0e31c2
Source7:	http://www.kadu.net/~pan_wojtas/iwait4u/download/%{name}-iwait4u-%{_iwait4u_ver}.tar.gz
# Source7-md5:	6233a8ef21d901fc5fb91c0db40d0e32
Source8:	http://www.kadu.net/~joi/exec_notify/packages/exec_notify-%{_notify_exec_ver}.tar.bz2
# Source8-md5:	ca4d620b707abf7483887f67a9c97c4f
Source9:	http://kadu.net/~blysk/led_notify-%{_notify_led_ver}.tar.bz2
# Source9-md5:	3f9e347fd775324f4077f2f6849a0de7
Source10:	http://www.kadu.net/~pan_wojtas/osdhints_notify/download/%{name}-osdhints_notify-%{_notify_osdhints_ver}-kadu-0.5.tar.gz
# Source10-md5:	d3023aba93f8085612b8c532c0e06889
Source11:	http://www.kadu.net/~dorr/%{name}-pcspeaker-%{_notify_pcspeaker_ver}.tar.gz
# Source11-md5:	ba78bb43ec27309a29922d6f8bab1a35
Source12:	http://kadu.net/~patryk/powerkadu/powerkadu-%{_powerkadu_ver}.tar.gz
# Source12-md5:	c6046e8b49dd9994fbf573faaafddab8
Source13:	http://www.kadu.net/~dorr/%{name}-profiles-%{_profiles_ver}.tar.gz
# Source13-md5:	723a58ec25a5bf6746e0ad0eb17e2f81
Source14:	http://scripts.one.pl/screenshot/devel/0.5.0/screenshot-%{_screenshot_ver}.tar.gz
# Source14-md5:	c6da85999cfebef413d228dca9c7d91f
Source15:	http://kadu.net/~patryk/miastoplusa_sms/miastoplusa_sms-0.5-%{_sms_miastoplusa_ver}.tar.gz
# Source15-md5:	fae1f6bd3d4aca845ef5a57403b5b58c
Source16:	http://scripts.one.pl/spellchecker/stable/%{version}/spellchecker-%{_spellchecker_mod_ver}.tar.gz
# Source16-md5:	384e3e039e3c1022b36780f9067caf4d
Source17:	http://student.agh.edu.pl/neeo/%{name}-spy-%{_spy_mod_ver}.tar.bz2
# Source17-md5:	b04fb7a4a98abe5d32e321da3058bbf0
Source18:	http://kadu.net/~arvenil/tabs/download/%{version}/%{name}-module-tabs-%{_tabs_ver}.tar.bz2
# Source18-md5:	7e16cd725d5ab273525130e85f16a28c
Source19:	http://kadu.net/~blysk/weather-%{_weather_ver}.tar.bz2
# Source19-md5:	c21727575d4bab551adeb9b5b1787f0c
Source20:	http://scripts.one.pl/xmms/stable/%{version}/xmms-%{_xmms_mod_ver}.tar.gz
# Source20-md5:	578191974e7dd60536373255e74bb38c
Source21:	http://www.kadu.net/download/additions/%{name}-theme-crystal-16.tar.bz2
# Source21-md5:	023085edabaf6a1b844fe6b5fc9315f9
Source22:	http://www.kadu.net/download/additions/%{name}-theme-crystal-22.tar.bz2
# Source22-md5:	57852ff3d3fd0063a642fcc173f7fa29
Source23:	http://www.kadu.net/download/additions/%{name}-theme-glass_16.tar.gz
# Source23-md5:	c3beb753222b96dad46f3adf230eb3e1
Source24:	http://www.kadu.net/download/additions/%{name}-theme-glass_22.tar.gz
# Source24-md5:	9ee70ca873fd0f22b2b83be133964d89
Source25:	http://www.kadu.net/download/additions/%{name}-theme-nuvola-16.tar.gz
# Source25-md5:	586cc6ff9ba62f0fdd7c7c1adf229efb
Source26:	http://www.kadu.net/download/additions/%{name}-theme-nuvola-22.tar.gz
# Source26-md5:	7a17b4881141b346c6268ef25c284613
Source27:	http://www.kadu.net/~pan_wojtas/firewall/download/%{name}-firewall-%{_firewall_ver}.tar.gz
# Source27-md5:	0ec61d3db8befa99032029a8a05310c5

Patch0:		%{name}-ac_am.patch
URL:		http://kadu.net/
%{?with_sound_alsa:BuildRequires:	alsa-lib-devel}
%{?with_sound_arts:BuildRequires:	arts-devel}
%{?with_spellchecker:BuildRequires:	aspell-devel}
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_sms_miastoplusa:BuildRequires:	curl-devel}
%{?with_sound_esd:BuildRequires:	esound-devel}
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libgadu-devel >= %{_libgadu_ver}
BuildRequires:	libgsm-devel
BuildRequires:	libsndfile-devel >= 1.0
BuildRequires:	libtool
%{?with_sound_nas:BuildRequires:	nas-devel}
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	qt-linguist
BuildRequires:	sed >= 4.0
%{?with_xmms:BuildRequires:	xmms-devel}
Obsoletes:	kadu-module-imiface <= 0.4.3
Obsoletes:	kadu-module-speech <= 0.4.3
Obsoletes:	kadu-module-tcl_scripting <= 0.4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_modules_dir	%{_libdir}/%{name}/modules
%define		_bin_dir	%{_libdir}/%{name}/bin

%description
Kadu is client of Gadu-Gadu protocol. It's an IM for Linux and UN*X.
It's written with use of QT libraries.

%description -l pl.UTF-8
Kadu jest klientem protokołu Gadu-Gadu. Inaczej mówiąc, jest
komunikatorem dla Linuksa (oraz, przy niewielkim wysiłku, innych
systemów UN*Xowych). Napisano go w oparciu o bibliotekę QT i KDE,
przeznaczony jest więc dla tego środowiska.

%package module-advanced_userlist
Summary:	Advanced Userlist module
Summary(pl.UTF-8):	Moduł zaawansowanej konfiguracji sortowania listy kontaktów
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-advanced_userlist
Advanced Userlist module.

%description module-advanced_userlist -l pl.UTF-8
Moduł zaawansowanej konfiguracji sortowania listy kontaktów.

%package module-amarok
Summary:	Support amarok status
Summary(pl.UTF-8):	Moduł statusu dla amarok
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	amarok

%description module-amarok
Module which allows showing in status description information about
the song currently played in amarok.

%description module-amarok -l pl.UTF-8
Moduł umożliwiający w opisie statusu pokazywanie informacji o
odgrywanym utworze z odtwarzacza amarok.

%package module-autoresponder
Summary:	Autoresponder module
Summary(pl.UTF-8):	Moduł autoodpowiedzi
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-autoresponder
Autoresponder module.

%description module-autoresponder -l pl.UTF-8
Moduł autoodpowiedzi.

%package module-dcopexport
Summary:	Kadu DCOP interface
Summary(pl.UTF-8):	Interfejs niektórych funkcji Kadu do DCOP
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-dcopexport
Kadu DCOP interface.

%description module-dcopexport -l pl.UTF-8
Interfejs niektórych funkcji Kadu do DCOP.

%package module-docking-desktop
Summary:	Desktop docking module
Summary(pl.UTF-8):	Moduł dokowania w dowolnym punkcie ekranu
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-docking-desktop
Desktop docking module.

%description module-docking-desktop -l pl.UTF-8
Moduł dokowania w dowolnym punkcie ekranu.

%package module-filtering
Summary:	User list filtering
Summary(pl.UTF-8):	Filtrowanie listy kontaktów
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-filtering
User list filtering.

%description module-filtering -l pl.UTF-8
Filtrowanie listy kontaktów.

%package module-filedesc
Summary:	Descriptions from file module
Summary(pl.UTF-8):	Moduł obsługi opisów z pliku
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-filedesc
Descriptions from file module.

%description module-filedesc -l pl.UTF-8
Moduł obsługi opisów z pliku.

%package module-firewall
Summary:	Mudule blocks unknown persons, who wants to start chat
Summary(pl.UTF-8):	Moduł blokuje nieznane osoby, chcące zacząć rozmowę
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-firewall
Mudule blocks unknown persons, who wants to start chat.

%description module-firewall -l pl.UTF-8
Moduł blokuje nieznane osoby, chcące zacząć rozmowę.

%package module-iwait4u
Summary:	iwait4u module inform you, that someone from userlist is active
Summary(pl.UTF-8):	Modul iwait4u do informowania o dostępności osób z listy
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-iwait4u
iwait4u module inform you, that someone from userlist is active.

%description module-iwait4u -l pl.UTF-8
Modul iwait4u informuje, że osoba z listy użytkowników jest dostępna.

%package module-notify-exec
Summary:	Notification by external commands module
Summary(pl.UTF-8):	Moduł powiadamiania użytkownika o zdarzeniach za pomocą zewnętrznych poleceń
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-notify-exec
Notification by external commands module.

%description module-notify-exec -l pl.UTF-8
Moduł powiadamiania użytkownika o zdarzeniach za pomocą zewnętrznych
poleceń.

%package module-notify-led
Summary:	Notification by Scroll Lock LED
Summary(pl.UTF-8):	Moduł powiadamiania diodą Scroll Lock
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-notify-led
Notification by Scroll Lock LED.

%description module-notify-led -l pl.UTF-8
Moduł powiadamiania diodą Scroll Lock.

%package module-notify-osdhints
Summary:	Notification by OSD-like hints
Summary(pl.UTF-8):	Powiadamianie o zdarzeniach przy pomocy dymków typu OSD
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-notify-osdhints
Notification by OSD-like hints.

%description module-notify-osdhints -l pl.UTF-8
Powiadamianie o zdarzeniach przy pomocy dymków typu OSD.

%package module-notify-pcspeaker
Summary:	PC Speaker module
Summary(pl.UTF-8):	Moduł do obsługi PC Speakera
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-notify-pcspeaker
PC Speaker module.

%description module-notify-pcspeaker -l pl.UTF-8
Moduł do obsługi PC Speakera.

%package module-notify-speech
Summary:	Speech synthesis support
Summary(pl.UTF-8):	Moduł obsługi "Głośnego czytania"
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	powiedz

%description module-notify-speech
Kadu module which supports reading aloud using speech synthesis
provided by external program "powiedz".

%description module-notify-speech -l pl.UTF-8
Moduł obsługi "Głośnego czytania" przez zewnętrzny program "powiedz".

%package module-powerkadu
Summary:	PowerKadu extensions
Summary(pl.UTF-8):	Rozszerzenia PowerKadu
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-powerkadu
PowerKadu is an add-on to Kadu. It extends Kadu functionality by
useful functions, like : autostatus, antistring, cenzor, TeX formula,
words fix, ...

%description module-powerkadu -l pl.UTF-8
PowerKadu jest dodatkiem do Kadu. Poszerza on możliwości Kadu o
przydatne funkcje, takie jak: autostatus, antyłańcuszek, cenzor,
formuły TeX-a, korekta słów...

%package module-profiles
Summary:	Kadu Profiles
Summary(pl.UTF-8):	Profile w Kadu
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-profiles
Kadu Profiles.

%description module-profiles -l pl.UTF-8
Profile w Kadu.

%package module-screenshot
Summary:	Simple ScreenShots module
Summary(pl.UTF-8):	Moduł prostych zrzutów ekranu
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-screenshot
Simple ScreenShots module.

%description module-screenshot -l pl.UTF-8
Moduł prostych zrzutów ekranu.

%package module-sms-miastoplusa
Summary:	SMS Gateway on Miasto Plusa module
Summary(pl.UTF-8):	Moduł obsługi bramki SMS w Mieście Plusa
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-sms-miastoplusa
SMS Gateway on Miasto Plusa module.

%description module-sms-miastoplusa -l pl.UTF-8
Moduł obsługi bramki SMS w Mieście Plusa.

%package module-sound-alsa
Summary:	Support ALSA sound
Summary(pl.UTF-8):	Wsparcie dla dźwięku ALSA
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	alsa-lib

%description module-sound-alsa
ALSA sound support module.

%description module-sound-alsa -l pl.UTF-8
Moduł obsługi dźwięku przez ALSA.

%package module-sound-arts
Summary:	Support aRts sound server
Summary(pl.UTF-8):	Wsparcie dla serwera dźwięku aRts
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	arts

%description module-sound-arts
aRts sound server support module.

%description module-sound-arts -l pl.UTF-8
Moduł do obsługi serwera dźwięku aRts.

%package module-sound-dsp
Summary:	DSP sound module
Summary(pl.UTF-8):	Moduł obsługi dźwięku przez DSP
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-sound-dsp
DSP sound module.

%description module-sound-dsp -l pl.UTF-8
Moduł obsługi dźwięku przez DSP.

%package module-sound-esd
Summary:	Support ESD sound server
Summary(pl.UTF-8):	Wsparcie dla serwera dźwięku ESD
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	esound

%description module-sound-esd
ESD sound module.

%description module-sound-esd -l pl.UTF-8
Moduł obsługi dźwięku przez ESD.

%package module-sound-nas
Summary:	Support Network Audio System
Summary(pl.UTF-8):	Wsparcie dla sieciowego systemu dźwięku NAS
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	nas

%description module-sound-nas
Network Audio System sound module.

%description module-sound-nas -l pl.UTF-8
Moduł obsługi dźwięku przez NAS.

%package module-spellchecker
Summary:	Checker of spelling mistakes
Summary(pl.UTF-8):	Moduł sprawdzający pisownię
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	aspell

%description module-spellchecker
Checker of spelling mistakes.

%description module-spellchecker -l pl.UTF-8
Moduł sprawdzający pisownię.

%package module-spy
Summary:	Spying module that shows who's invisible
Summary(pl.UTF-8):	Moduł szpiegowski pokazujący ukryte osoby
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-spy
Spying module that shows who's invisible.

%description module-spy -l pl.UTF-8
Moduł szpiegowski pokazujący ukryte osoby.

%package module-tabs
Summary:	Tabbed chat dialog module
Summary(pl.UTF-8):	Moduł okna rozmowy z zakładkami
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-tabs
Tabbed chat dialog module.

%description module-tabs -l pl.UTF-8
Moduł okna rozmowy z zakładkami.

%package module-weather
Summary:	Weather module
Summary(pl.UTF-8):	Moduł pogodowy
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-weather
Informations of weather in locality of contact.

%description module-weather -l pl.UTF-8
Informacje o pogodzie w miejscowości danego kontaktu.

%package module-xmms
Summary:	Support XMMS status
Summary(pl.UTF-8):	Moduł statusu dla XMMS-a
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	xmms

%description module-xmms
Module which allows showing in status description information about
the song currently played in XMMS.

%description module-xmms -l pl.UTF-8
Moduł umożliwiający pokazywanie w opisie statusu informacji o
odgrywanym utworze z odtwarzacza XMMS.

%package theme-icons-crystal16
Summary:	Crystal16 icon theme
Summary(pl.UTF-8):	Zestaw ikon crystal16
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description theme-icons-crystal16
Crystal16 icon theme.

%description theme-icons-crystal16 -l pl.UTF-8
Zestaw ikon crystal16.

%package theme-icons-crystal22
Summary:	Crystal22 icon theme
Summary(pl.UTF-8):	Zestaw ikon crystal22
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description theme-icons-crystal22
Crystal22 icon theme.

%description theme-icons-crystal22 -l pl.UTF-8
Zestaw ikon crystal22.

%package theme-icons-glass16
Summary:	Glass16 icon theme
Summary(pl.UTF-8):	Zestaw ikon glass16
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description theme-icons-glass16
Glass16 icon theme.

%description theme-icons-glass16 -l pl.UTF-8
Zestaw ikon glass16.

%package theme-icons-glass22
Summary:	Glass22 icon theme
Summary(pl.UTF-8):	Zestaw ikon glass22
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description theme-icons-glass22
Glass22 icon theme.

%description theme-icons-glass22 -l pl.UTF-8
Zestaw ikon glass22.

%package theme-icons-nuvola16
Summary:	Nuvola16 icon theme
Summary(pl.UTF-8):	Zestaw ikon nuvola16
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description theme-icons-nuvola16
Nuvola16 icon theme.

%description theme-icons-nuvola16 -l pl.UTF-8
Zestaw ikon nuvola16.

%package theme-icons-nuvola22
Summary:	Nuvola22 icon theme
Summary(pl.UTF-8):	Zestaw ikon nuvola22
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description theme-icons-nuvola22
Nuvola22 icon theme.

%description theme-icons-nuvola22 -l pl.UTF-8
Zestaw ikon nuvola22.

%prep
%setup -q -T -b 0 -n %{name}
%patch0 -p1

%if %{with advanced_userlist}
tar xjf %{SOURCE2} -C modules
%endif
%if %{with amarok}
tar xzf %{SOURCE3} -C modules
%endif
%if %{with dcopexport}
tar xjf %{SOURCE4} -C modules
%endif
%if %{with filedesc}
tar xzf %{SOURCE5} -C modules
%endif
%if %{with filtering}
tar xjf %{SOURCE6} -C modules
%endif
%if %{with iwait4u}
tar xzf %{SOURCE7} -C modules
%endif
%if %{with notify_exec}
tar xjf %{SOURCE8} -C modules
%endif
%if %{with notify_led}
tar xjf %{SOURCE9} -C modules
%endif
%if %{with notify_osdhints}
tar xzf %{SOURCE10} -C modules
%endif
%if %{with notify_pcspeaker}
tar xzf %{SOURCE11} -C modules
%endif
%if %{with powerkadu}
tar xzf %{SOURCE12} -C modules
%endif
%if %{with profiles}
tar xzf %{SOURCE13} -C modules
%endif
%if %{with screenshot}
tar xzf %{SOURCE14} -C modules
%endif
%if %{with sms_miastoplusa}
tar xzf %{SOURCE15} -C modules
%endif
%if %{with spellchecker}
tar xzf %{SOURCE16} -C modules
%endif
%if %{with spy}
tar xjf %{SOURCE17} -C modules
%endif
%if %{with tabs}
tar xjf %{SOURCE18} -C modules
%endif
%if %{with weather}
tar xjf %{SOURCE19} -C modules
%endif
%if %{with xmms}
tar xzf %{SOURCE20} -C modules
%endif
%if %{with firewall}
tar xzf %{SOURCE27} -C modules
%endif
# themes-icons
tar xjf %{SOURCE21} -C varia/themes/icons
tar xjf %{SOURCE22} -C varia/themes/icons
tar xzf %{SOURCE23} -C varia/themes/icons
tar xzf %{SOURCE24} -C varia/themes/icons
tar xzf %{SOURCE25} -C varia/themes/icons
tar xzf %{SOURCE26} -C varia/themes/icons

# rename theme directories to be sure that they
# will not be re-downloaded by configure
for dir in varia/themes/icons/kadu-theme-*; do
	theme=`echo $dir | %{__sed} -e 's/kadu-theme-//; s/[_-]//;'`;
	mv $dir $theme
done

%{__sed} -i 's,dataPath("kadu/modules/*,("%{_libdir}/kadu/modules/,g' kadu/modules.cpp

%build
%if %{with advanced_userlist}
%{__sed} -i 's/module_advanced_userlist=n/module_advanced_userlist=m/' .config
%endif
%if %{with amarok}
%{__sed} -i 's/module_amarok=n/module_amarok=m/' .config
echo 'MODULE_INCLUDES_PATH="%{_includedir}"'>> modules/amarok/spec
echo 'MODULE_LIBS_PATH="%{_prefix}/lib"' >> modules/amarok/spec
%endif
%if !%{with autoresponder}
%{__sed} -i 's/module_autoresponder=m/module_autoresponder=n/' .config
%endif
%if %{with dcopexport}
%{__sed} -i 's/module_dcopexport=n/module_dcopexport=m/' .config
%endif
%if %{with docking_desktop}
%{__sed} -i 's/module_desktop_docking=n/module_desktop_docking=m/' .config
%endif
%if %{with filedesc}
%{__sed} -i 's/module_filedesc=n/module_filedesc=m/' .config
%endif
%if %{with filtering}
%{__sed} -i 's/module_filtering=n/module_filtering=m/' .config
%endif
%if %{with firewall}
%{__sed} -i 's/module_firewall=n/module_firewall=m/' .config
%endif
%if %{with iwait4u}
%{__sed} -i 's/module_iwait4u=n/module_iwait4u=m/' .config
%endif
%if %{with notify_exec}
%{__sed} -i 's/module_exec_notify=n/module_exec_notify=m/' .config
%endif
%if %{with notify_led}
%{__sed} -i 's/module_led_notify=n/module_led_notify=m/' .config
%endif
%if %{with notify_osdhints}
%{__sed} -i 's/module_osdhints_notify=n/module_osdhints_notify=m/' .config
%endif
%if %{with notify_pcspeaker}
%{__sed} -i 's/module_pcspeaker=n/module_pcspeaker=m/' .config
%endif
%if %{with notify_speech}
%{__sed} -i 's/module_speech=n/module_speech=m/' .config
%endif
%if %{with powerkadu}
%{__sed} -i 's/module_powerkadu=n/module_powerkadu=m/' .config
# fix for 20070107 version
rm -f modules/powerkadu/bin/mimetex
%endif
%if %{with profiles}
%{__sed} -i 's/module_profiles=n/module_profiles=m/' .config
%endif
%if %{with screenshot}
%{__sed} -i 's/module_screenshot=n/module_screenshot=m/' .config
%endif
%if %{with sms_miastoplusa}
%{__sed} -i 's/module_miastoplusa_sms=n/module_miastoplusa_sms=m/' .config
%endif
%if %{with sound_alsa}
%{__sed} -i 's/module_alsa_sound=n/module_alsa_sound=m/' .config
%endif
%if %{with sound_arts}
%{__sed} -i 's/module_arts_sound=n/module_arts_sound=m/' .config
%endif
%if !%{with sound_dsp}
%{__sed} -i 's/module_dsp_sound=m/module_dsp_sound=n/' .config
%endif
%if %{with sound_esd}
%{__sed} -i 's/module_esd_sound=n/module_esd_sound=m/' .config
%endif
%if %{with sound_nas}
%{__sed} -i 's/module_nas_sound=n/module_nas_sound=m/' .config
echo 'MODULE_LIBS_PATH="%{_prefix}/lib"' >> modules/nas_sound/spec
%endif
%if %{with spellchecker}
%{__sed} -i 's/module_spellchecker=n/module_spellchecker=m/' .config
%endif
%if %{with tabs}
%{__sed} -i 's/module_tabs=n/module_tabs=m/' .config
%endif
%if %{with weather}
%{__sed} -i 's/module_weather=n/module_weather=m/' .config
%endif
%if %{with xmms}
%{__sed} -i 's/module_xmms=n/module_xmms=m/' .config
rm -f modules/xmms/.autodownloaded
%endif
%{__sed} -i 's/icons_crystal16=n/icons_crystal16=y/' .config
%{__sed} -i 's/icons_crystal22=n/icons_crystal22=y/' .config
%{__sed} -i 's/icons_glass16=n/icons_glass16=y/' .config
%{__sed} -i 's/icons_glass22=n/icons_glass22=y/' .config
%{__sed} -i 's/icons_nuvola16=n/icons_nuvola16=y/' .config
%{__sed} -i 's/icons_nuvola22=n/icons_nuvola22=y/' .config


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

%if %{with amarok}
mv -f $RPM_BUILD_ROOT%{_modules_dir}/data/amarok $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
%endif

%if %{with dcopexport}
cp -fa $RPM_BUILD_ROOT%{_modules_dir}/data/dcopexport $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
rm -fr $RPM_BUILD_ROOT%{_modules_dir}/data/dcopexport
%endif

%if %{with filedesc}
cp -fa $RPM_BUILD_ROOT%{_modules_dir}/data/filedesc $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
rm -fr $RPM_BUILD_ROOT%{_modules_dir}/data/filedesc
%endif

%if %{with filtering}
cp -fa $RPM_BUILD_ROOT%{_modules_dir}/data/filtering $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
rm -fr $RPM_BUILD_ROOT%{_modules_dir}/data/filtering
%endif

%if %{with firewall}
cp -fa $RPM_BUILD_ROOT%{_modules_dir}/data/firewall $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
rm -fr $RPM_BUILD_ROOT%{_modules_dir}/data/firewall
%endif

%if %{with notify_osdhints}
cp -fa $RPM_BUILD_ROOT%{_modules_dir}/data/osdhints_notify $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
rm -fr $RPM_BUILD_ROOT%{_modules_dir}/data/osdhints_notify
%endif

%if %{with powerkadu}
cp -fa $RPM_BUILD_ROOT%{_modules_dir}/data/powerkadu $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
rm -fr $RPM_BUILD_ROOT%{_modules_dir}/data/powerkadu
%endif

%if %{with screenshot}
cp -fa $RPM_BUILD_ROOT%{_modules_dir}/data/screenshot $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
rm -fr $RPM_BUILD_ROOT%{_modules_dir}/data/screenshot
%endif

%if %{with sms_miastoplusa}
cp -fa $RPM_BUILD_ROOT%{_modules_dir}/data/miastoplusa_sms $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
rm -fr $RPM_BUILD_ROOT%{_modules_dir}/data/miastoplusa_sms
%endif

%if %{with spellchecker}
cp -fa $RPM_BUILD_ROOT%{_modules_dir}/data/spellchecker $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
rm -fr $RPM_BUILD_ROOT%{_modules_dir}/data/spellchecker
%endif

%if %{with spy}
mv -f $RPM_BUILD_ROOT%{_modules_dir}/data/spy $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
%endif

%if %{with tabs}
cp -Rfa $RPM_BUILD_ROOT%{_modules_dir}/data/tabs $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
rm -fr $RPM_BUILD_ROOT%{_modules_dir}/data/tabs
%endif

%if %{with weather}
mv -f $RPM_BUILD_ROOT%{_modules_dir}/data/weather $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
%endif

%if %{with xmms}
cp -fa $RPM_BUILD_ROOT%{_modules_dir}/data/xmms $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/data
rm -fr $RPM_BUILD_ROOT%{_modules_dir}/data/xmms
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
%dir %{_datadir}/%{name}/modules
%dir %{_datadir}/%{name}/modules/data
%dir %{_datadir}/%{name}/themes
%dir %{_datadir}/%{name}/themes/emoticons
%{_datadir}/%{name}/themes/emoticons/penguins
%dir %{_datadir}/%{name}/themes/icons
%{_datadir}/%{name}/themes/icons/default
%dir %{_datadir}/%{name}/themes/sounds
%{_datadir}/%{name}/themes/sounds/default
#About... files
%{_datadir}/%{name}/AUTHORS
%{_datadir}/%{name}/ChangeLog
%{_datadir}/%{name}/COPYING
%{_datadir}/%{name}/THANKS
#default modules:
%dir %{_libdir}/%{name}
%dir %{_modules_dir}
%dir %{_modules_dir}/bin
%{_modules_dir}/account_management.desc
%attr(755,root,root) %{_modules_dir}/account_management.so
%{_modules_dir}/autoaway.desc
%attr(755,root,root) %{_modules_dir}/autoaway.so
%{_modules_dir}/config_wizard.desc
%attr(755,root,root) %{_modules_dir}/config_wizard.so
%{_modules_dir}/dcc.desc
%attr(755,root,root) %{_modules_dir}/dcc.so
%{_modules_dir}/default_sms.desc
%attr(755,root,root) %{_modules_dir}/default_sms.so
%{_modules_dir}/docking.desc
%{_modules_dir}/encryption.desc
%attr(755,root,root) %{_modules_dir}/encryption.so
%{_modules_dir}/ext_sound.desc
%attr(755,root,root) %{_modules_dir}/ext_sound.so
%{_modules_dir}/hints.desc
%attr(755,root,root) %{_modules_dir}/hints.so
%{_modules_dir}/migration.desc
%attr(755,root,root) %{_modules_dir}/migration.so
%{_modules_dir}/notify.desc
%{_modules_dir}/sms.desc
%attr(755,root,root) %{_modules_dir}/sms.so
%{_modules_dir}/sound.desc
%{_modules_dir}/voice.desc
%attr(755,root,root) %{_modules_dir}/voice.so
%{_modules_dir}/window_notify.desc
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

%if %{with advanced_userlist}
%files module-advanced_userlist
%defattr(644,root,root,755)
%{_modules_dir}/advanced_userlist.desc
%attr(755,root,root) %{_modules_dir}/advanced_userlist.so
%lang(pl) %{_modules_dir}/translations/advanced_userlist_pl.qm
%endif

%if %{with amarok}
%files module-amarok
%defattr(644,root,root,755)
%{_modules_dir}/amarok.desc
%attr(755,root,root) %{_modules_dir}/amarok.so
%lang(de) %{_modules_dir}/translations/amarok_de.qm
%lang(pl) %{_modules_dir}/translations/amarok_pl.qm
%dir %{_datadir}/%{name}/modules/data/amarok
%{_datadir}/%{name}/modules/data/amarok/amarok.png
%endif

%if %{with autoresponder}
%files module-autoresponder
%defattr(644,root,root,755)
%{_modules_dir}/autoresponder.desc
%attr(755,root,root) %{_modules_dir}/autoresponder.so
%lang(de) %{_modules_dir}/translations/autoresponder_de.qm
%lang(fr) %{_modules_dir}/translations/autoresponder_fr.qm
%lang(it) %{_modules_dir}/translations/autoresponder_it.qm
%lang(pl) %{_modules_dir}/translations/autoresponder_pl.qm
%endif

%if %{with dcopexport}
%files module-dcopexport
%defattr(644,root,root,755)
%{_modules_dir}/dcopexport.desc
%attr(755,root,root) %{_modules_dir}/dcopexport.so
%lang(pl) %{_modules_dir}/translations/dcopexport_pl.qm
%dir %{_modules_dir}/bin/dcopexport
%attr(755,root,root) %{_modules_dir}/bin/dcopexport/*.sh
%dir %{_datadir}/%{name}/modules/data/dcopexport
%{_datadir}/%{name}/modules/data/dcopexport/dcopexport.png
%endif

%if %{with docking_desktop}
%files module-docking-desktop
%defattr(644,root,root,755)
%{_modules_dir}/desktop_docking.desc
%attr(755,root,root) %{_modules_dir}/desktop_docking.so
%lang(de) %{_modules_dir}/translations/desktop_docking_de.qm
%lang(fr) %{_modules_dir}/translations/desktop_docking_fr.qm
%lang(it) %{_modules_dir}/translations/desktop_docking_it.qm
%lang(pl) %{_modules_dir}/translations/desktop_docking_pl.qm
%endif

%if %{with filedesc}
%files module-filedesc
%defattr(644,root,root,755)
%{_modules_dir}/filedesc.desc
%attr(755,root,root) %{_modules_dir}/filedesc.so
%lang(pl) %{_modules_dir}/translations/filedesc_pl.qm
%dir %{_datadir}/%{name}/modules/data/filedesc
%{_datadir}/%{name}/modules/data/filedesc/*.png
%endif

%if %{with filtering}
%files module-filtering
%defattr(644,root,root,755)
%{_modules_dir}/filtering.desc
%attr(755,root,root) %{_modules_dir}/filtering.so
%lang(pl) %{_modules_dir}/translations/filtering_pl.qm
%dir %{_datadir}/%{name}/modules/data/filtering
%{_datadir}/%{name}/modules/data/filtering/*.png
%endif

%if %{with firewall}
%files module-firewall
%defattr(644,root,root,755)
%{_modules_dir}/filtering.desc
%attr(755,root,root) %{_modules_dir}/firewall.so
%lang(pl) %{_modules_dir}/translations/firewall_pl.qm
%{_modules_dir}/firewall.desc
%dir %{_datadir}/%{name}/modules/data/firewall
%{_datadir}/%{name}/modules/data/firewall/firewall.png
%endif

%if %{with iwait4u}
%files module-iwait4u
%defattr(644,root,root,755)
%{_modules_dir}/iwait4u.desc
%attr(755,root,root) %{_modules_dir}/iwait4u.so
%lang(pl) %{_modules_dir}/translations/iwait4u_pl.qm
%endif

%if %{with notify_exec}
%files module-notify-exec
%defattr(644,root,root,755)
%{_modules_dir}/exec_notify.desc
%attr(755,root,root) %{_modules_dir}/exec_notify.so
%lang(pl) %{_modules_dir}/translations/exec_notify_pl.qm
%endif

%if %{with notify_led}
%files module-notify-led
%defattr(644,root,root,755)
%{_modules_dir}/led_notify.desc
%attr(755,root,root) %{_modules_dir}/led_notify.so
%lang(pl) %{_modules_dir}/translations/led_notify_pl.qm
%endif

%if %{with notify_osdhints}
%files module-notify-osdhints
%defattr(644,root,root,755)
%{_modules_dir}/osdhints_notify.desc
%attr(755,root,root) %{_modules_dir}/osdhints_notify.so
%lang(pl) %{_modules_dir}/translations/osdhints_notify_pl.qm
%dir %{_datadir}/%{name}/modules/data/osdhints_notify
%{_datadir}/%{name}/modules/data/osdhints_notify/*.png
%endif

%if %{with notify_pcspeaker}
%files module-notify-pcspeaker
%defattr(644,root,root,755)
%{_modules_dir}/pcspeaker.desc
%attr(755,root,root) %{_modules_dir}/pcspeaker.so
%lang(de) %{_modules_dir}/translations/pcspeaker_de.qm
%lang(it) %{_modules_dir}/translations/pcspeaker_it.qm
%lang(pl) %{_modules_dir}/translations/pcspeaker_pl.qm
%endif

%if %{with notify_speech}
%files module-notify-speech
%defattr(644,root,root,755)
%{_modules_dir}/speech.desc
%attr(755,root,root) %{_modules_dir}/speech.so
%lang(de) %{_modules_dir}/translations/speech_de.qm
%lang(fr) %{_modules_dir}/translations/speech_fr.qm
%lang(it) %{_modules_dir}/translations/speech_it.qm
%lang(pl) %{_modules_dir}/translations/speech_pl.qm
%endif

%if %{with powerkadu}
%files module-powerkadu
%defattr(644,root,root,755)
%{_modules_dir}/powerkadu.desc
%attr(755,root,root) %{_modules_dir}/powerkadu.so
%lang(pl) %{_modules_dir}/translations/powerkadu_pl.qm
%dir %{_modules_dir}/bin/powerkadu
%attr(755,root,root) %{_modules_dir}/bin/powerkadu/mimetex
%{_datadir}/%{name}/modules/data/powerkadu
%endif

%if %{with profiles}
%files module-profiles
%defattr(644,root,root,755)
%{_modules_dir}/profiles.desc
%attr(755,root,root) %{_modules_dir}/profiles.so
%lang(de) %{_modules_dir}/translations/profiles_de.qm
%lang(it) %{_modules_dir}/translations/profiles_it.qm
%lang(pl) %{_modules_dir}/translations/profiles_pl.qm
%endif

%if %{with screenshot}
%files module-screenshot
%defattr(644,root,root,755)
%{_modules_dir}/screenshot.desc
%attr(755,root,root) %{_modules_dir}/screenshot.so
%lang(pl) %{_modules_dir}/translations/screenshot_pl.qm
%dir %{_datadir}/%{name}/modules/data/screenshot
%{_datadir}/%{name}/modules/data/screenshot/*.png
%endif

%if %{with sms_miastoplusa}
%files module-sms-miastoplusa
%defattr(644,root,root,755)
%{_modules_dir}/miastoplusa_sms.desc
%attr(755,root,root) %{_modules_dir}/miastoplusa_sms.so
%lang(pl) %{_modules_dir}/translations/miastoplusa_sms_pl.qm
%dir %{_datadir}/%{name}/modules/data/miastoplusa_sms
%{_datadir}/%{name}/modules/data/miastoplusa_sms/curl-ca-bundle.crt
%endif

%if %{with sound_alsa}
%files module-sound-alsa
%defattr(644,root,root,755)
%{_libdir}/%{name}/modules/alsa_sound.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/alsa_sound.so
%lang(de) %{_libdir}/%{name}/modules/translations/alsa_sound_de.qm
%lang(fr) %{_libdir}/%{name}/modules/translations/alsa_sound_fr.qm
%lang(it) %{_libdir}/%{name}/modules/translations/alsa_sound_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/alsa_sound_pl.qm
%endif

%if %{with sound_arts}
%files module-sound-arts
%defattr(644,root,root,755)
%{_modules_dir}/arts_sound.desc
%attr(755,root,root) %{_modules_dir}/arts_sound.so
%dir %{_modules_dir}/bin/arts_sound
%attr(755,root,root) %{_modules_dir}/bin/arts_sound/arts_connector
%endif

%if %{with sound_dsp}
%files module-sound-dsp
%defattr(644,root,root,755)
%{_libdir}/%{name}/modules/dsp_sound.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/dsp_sound.so
%lang(de) %{_libdir}/%{name}/modules/translations/dsp_sound_de.qm
%lang(fr) %{_libdir}/%{name}/modules/translations/dsp_sound_fr.qm
%lang(it) %{_libdir}/%{name}/modules/translations/dsp_sound_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/dsp_sound_pl.qm
%endif

%if %{with sound_esd}
%files module-sound-esd
%defattr(644,root,root,755)
%{_modules_dir}/esd_sound.desc
%attr(755,root,root) %{_modules_dir}/esd_sound.so
%endif

%if %{with sound_nas}
%files module-sound-nas
%defattr(644,root,root,755)
%{_modules_dir}/nas_sound.desc
%attr(755,root,root) %{_modules_dir}/nas_sound.so
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

%if %{with spy}
%files module-spy
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/modules/data/spy
%{_datadir}/%{name}/modules/data/spy/spy32.png
%{_modules_dir}/spy.desc
%attr(755,root,root) %{_modules_dir}/spy.so
%lang(pl) %{_modules_dir}/translations/spy_pl.qm
%endif

%if %{with tabs}
%files module-tabs
%defattr(644,root,root,755)
%{_modules_dir}/tabs.desc
%attr(755,root,root) %{_modules_dir}/tabs.so
%lang(pl) %{_modules_dir}/translations/tabs_pl.qm
%dir %{_datadir}/%{name}/modules/data/tabs
%{_datadir}/%{name}/modules/data/tabs/attach.png
%endif

%if %{with weather}
%files module-weather
%defattr(644,root,root,755)
%{_modules_dir}/weather.desc
%attr(755,root,root) %{_modules_dir}/weather.so
%lang(pl) %{_modules_dir}/translations/weather_pl.qm
%dir %{_datadir}/%{name}/modules/data/weather
%{_datadir}/%{name}/modules/data/weather/*.ini
%dir %{_datadir}/%{name}/modules/data/weather/icons
%{_datadir}/%{name}/modules/data/weather/icons/*.gif
%endif

%if %{with xmms}
%files module-xmms
%defattr(644,root,root,755)
%{_modules_dir}/xmms.desc
%attr(755,root,root) %{_modules_dir}/xmms.so
%lang(pl) %{_modules_dir}/translations/xmms_pl.qm
%dir %{_datadir}/%{name}/modules/data/xmms
%{_datadir}/%{name}/modules/data/xmms/xmms.png
%endif

%files theme-icons-crystal16
%defattr(644,root,root,755)
%{_datadir}/%{name}/themes/icons/crystal16

%files theme-icons-crystal22
%defattr(644,root,root,755)
%{_datadir}/%{name}/themes/icons/crystal22

%files theme-icons-glass16
%defattr(644,root,root,755)
%{_datadir}/%{name}/themes/icons/glass16

%files theme-icons-glass22
%defattr(644,root,root,755)
%{_datadir}/%{name}/themes/icons/glass22

%files theme-icons-nuvola16
%defattr(644,root,root,755)
%{_datadir}/%{name}/themes/icons/nuvola16

%files theme-icons-nuvola22
%defattr(644,root,root,755)
%{_datadir}/%{name}/themes/icons/nuvola22
