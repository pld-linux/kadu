#
# TODO:
# - Some modules with bcond_with will not work for now, we need to wait for next releases
# - Add Obsoletes for modules iwait4u, powerkadu, notify_osdhints if they will not be fixed before final 0.6.0
#
# NOTE:
# - We use staticly linked libgadu because of no stable release with dcc7
#
# Conditional build:
%bcond_with	snap			# build cvs snapshot
%bcond_with	debug			# build with debug

%bcond_without	advanced_userlist	# without Advanced Userlist support
%bcond_without	agent			# without agent module support
%bcond_without	autoresponder		# without autoresponder module support
%bcond_without	dcopexport		# without dcopexport module support
%bcond_without	docking_desktop		# without desktop_docking module support
%bcond_without	encryption		# without encryption module support
%bcond_without	filedesc		# without filedesc module support
%bcond_without	filtering		# without filtering module support
%bcond_without	firewall		# without firewall module support
%bcond_with	iwait4u			# with iwait4u module support
%bcond_without	mail			# without mail module support
%bcond_without	mediaplayer		# without media player modules support
%bcond_without	mediaplayer_amarok	# without amarok player support module
%bcond_without	mediaplayer_audacious	# without audacious player support module
%bcond_without	mediaplayer_falf	# without falf player support module
%bcond_without	mediaplayer_xmms	# without xmms player support module
%bcond_without	mime_tex		# without mime_tex module support
%bcond_without	notify_exec		# without exec_notify module support
%bcond_without	notify_led		# without led_notify module support
%bcond_without	notify_mx610		# without led_notify module support
%bcond_with	notify_osdhints		# with osdhints_notify module
%bcond_without	notify_pcspeaker	# without pcspeaker_notify module support
%bcond_without	notify_speech		# without Speech synthesis support
%bcond_without	notify_water		# without water_notify module support
%bcond_without	notify_xosd		# without xosd_notify module support
%bcond_with	powerkadu		# with PowerKadu extensions
%bcond_without	profiles		# without profiles module support
%bcond_without	sound_alsa		# without ALSA support
%bcond_without	sound_ao		# without ao support
%bcond_without	sound_arts		# without arts sound server support
%bcond_without	sound_dsp		# without DSP sound module support
%bcond_without	sound_esd		# without ESD sound server support
%bcond_without	sound_ext		# without external application sound module support
%bcond_without	sound_nas		# without Network Audio System support
%bcond_without	screenshot		# without screenshot module support
%bcond_without	sms_miastoplusa		# without miastoplusa_sms module support
%bcond_without	spellchecker		# without spellchecker (Aspell support) invisible
%bcond_without	tabs			# without tabs support module
%bcond_without	voice			# without voice support module
%bcond_without	weather			# without weather check module support

%define		_snap	20080208
%define		_rel	rc3

%define		_agent_mod_ver		0.4.4
%define		_amarok_mod_ver		20071220
%define		_dcopexport_ver		0.11.3-20071129
%define		_falf_mod_ver		20071225
%define		_filedesc_ver		20080104
%define		_filtering_ver		20080204
%define		_firewall_ver		0.7.5
%define		_iwait4u_ver		1.3
%define		_mail_ver		0.3.2
%define		_mediaplayer_mod_ver	20080210
%define		_mediaplayer_audacious_ver	20071220
%define		_mime_tex_ver		1.4.1
%define		_notify_exec_ver	20070101
%define		_notify_led_ver		0.18
%define		_notify_mx610_ver	0.3.1
%define		_notify_osdhints_ver	0.4.0.3
%define		_notify_pcspeaker_ver	0.6.0.3
%define		_notify_water_ver	0.1.1-try2
%define		_powerkadu_ver		20070129
%define		_profiles_ver		0.3.1
%define		_screenshot_ver		20080104
%define		_sms_miastoplusa_ver	1.3.9
%define		_sound_ao_ver		20060424
%define		_spellchecker_mod_ver	20071230
%define		_tabs_ver		1.1.4
%define		_weather_ver		3.13
%define		_xmms_mod_ver		20080116

%if %{with snap}
%define		year	%(echo %{_snap} |cut -b -4)
%endif

Summary:	A Gadu-Gadu client for online messaging
Summary(pl.UTF-8):	Klient Gadu-Gadu do przesyłania wiadomości po sieci
Name:		kadu
Version:	0.6.0
Release:	0.%{?with_snap:%{_snap}}%{!?with_snap:%{_rel}}.1
License:	GPL v2
Group:		Applications/Communications

%if %{with snap}
Source100:	http://kadu.net/download/snapshots/2008/%{name}-%{_snap}.tar.bz2
# Source100-md5:	d158fe973922a66b36a3616b5494fd72
%else
Source0:	http://kadu.net/download/stable/%{name}-%{version}-%{_rel}.tar.bz2
# Source0-md5:	f943e42c31ca0dec3137472d37344f39
%endif
Source1:	%{name}.desktop
Source2:	http://www.kadu.net/download/modules_extra/mediaplayer/mediaplayer-%{_mediaplayer_mod_ver}.tar.bz2
# Source2-md5:	f24c85c640fa88a887cab078d8cacfc4
Source3:	http://www.kadu.net/download/modules_extra/amarok_mediaplayer/amarok_mediaplayer-%{_amarok_mod_ver}.tar.bz2
# Source3-md5:	51d304e335e814f3d8c0f1654007a7d7
Source4:	http://alan.umcs.lublin.pl/~pinkworm/dcopexport/dcopexport-%{_dcopexport_ver}-%{version}.tar.bz2
# Source4-md5:	b36fcfcf4756285f30cbb6c2b6c2a2da
Source5:	http://www.kadu.net/download/modules_extra/filedesc/filedesc-%{_filedesc_ver}.tar.bz2
# Source5-md5:	8d11979fa8a3795f7ab20fbb1fb8bdbb
Source6:	http://www.kadu.net/download/modules_extra/filtering/filtering-%{_filtering_ver}.tar.bz2
# Source6-md5:	89174f20bf9c71d23ca7d3619907737a
Source7:	http://www.kadu.net/~pan_wojtas/iwait4u/download/%{name}-iwait4u-%{_iwait4u_ver}.tar.gz
# Source7-md5:	6233a8ef21d901fc5fb91c0db40d0e32
Source8:	http://www.kadu.net/download/modules_extra/falf_mediaplayer/falf_mediaplayer-%{_falf_mod_ver}.tar.bz2
# Source8-md5:	927db40f7136ff86b3e83307b5cec2d9
Source9:	http://kadu.net/~blysk/led_notify-%{_notify_led_ver}.tar.bz2
# Source9-md5:	786a0ee40a3aef03b51e2d89a2bceda5
Source10:	http://www.kadu.net/~dorr/moduly/%{name}-osdhints_notify-%{_notify_osdhints_ver}.tar.bz2
# Source10-md5:	c1c1d2e1b0122684bb23145a71877c00
Source11:	http://www.kadu.net/~dorr/%{name}-pcspeaker-%{_notify_pcspeaker_ver}.tar.bz2
# Source11-md5:	5fef08c32809bbce6b6bf96659b39df6
Source12:	http://kadu.net/~patryk/powerkadu/powerkadu-%{_powerkadu_ver}.tar.gz
# Source12-md5:	c6046e8b49dd9994fbf573faaafddab8
Source13:	http://www.kadu.net/~dorr/%{name}-profiles-%{_profiles_ver}.tar.bz2
# Source13-md5:	2f5ba8fd20efd00c88d22a9ee014ea7b
Source14:	http://www.kadu.net/download/modules_extra/screenshot/screenshot-%{_screenshot_ver}.tar.bz2
# Source14-md5:	47d3d5564b272a186667c1507e19844f
Source15:	http://kadu.net/~patryk/miastoplusa_sms/miastoplusa_sms-0.6-%{_sms_miastoplusa_ver}.tar.gz
# Source15-md5:	e5c4d5cd94cef40730e281b9a6c9ed37
Source16:	http://www.kadu.net/download/modules_extra/spellchecker/spellchecker-%{_spellchecker_mod_ver}.tar.bz2
# Source16-md5:	a46eab2f3d9c31cee13ccf3a441bceec
Source17:	http://misiek.jah.pl/assets/2008/2/8/agent-%{_agent_mod_ver}.tar.gz
# Source17-md5:	4401e0e3c509af347cb14a89236301ea
Source18:	http://kadu.net/~arvenil/tabs/download/%{version}/%{_tabs_ver}/%{name}-tabs-%{_tabs_ver}.tar.bz2
# Source18-md5:	57e4c970f496ba81495d59d7b96bcdf1
Source19:	http://kadu.net/~blysk/weather-%{_weather_ver}.tar.bz2
# Source19-md5:	41a6edd1356a36e4606e432d0bc856f6
Source20:	http://www.kadu.net/download/modules_extra/xmms_mediaplayer/xmms_mediaplayer-%{_xmms_mod_ver}.tar.bz2
# Source20-md5:	97dd4c9cd19b69b9ab6d38a20cd37a2e
Source21:	http://kadu.jarzebski.pl/water_notify-%{_notify_water_ver}.tar.bz2
# Source21-md5:	10320f9b96366422bbcd7ec76d4e85a1
Source23:	http://www.kadu.net/download/additions/%{name}-0.6-theme-glass-16.tar.gz
# Source23-md5:	d09256b6b2ae801088c1f6e04bbac5f7
Source24:	http://www.kadu.net/download/additions/%{name}-0.6-theme-glass-22.tar.gz
# Source24-md5:	d9f33f1224315771615faaefd2397918
Source27:	http://www.kadu.net/~dorr/moduly/%{name}-firewall-%{_firewall_ver}.tar.bz2
# Source27-md5:	3f4bf46efa6345870537b865c8d84ef6
Source28:	http://kadu.net/~patryk/mime_tex/mime_tex-%{_mime_tex_ver}.tar.bz2
# Source28-md5:	d640b2ba650fb5aa0f3502ad7379b14b
Source29:	http://kadu.jarzebski.pl/mx610_notify-%{_notify_mx610_ver}.tar.bz2
# Source29-md5:	08bba105d9307bbf1a8e8482529441a4
Source30:	http://www.kadu.net/~joi/ao_sound/packages/ao_sound-%{_sound_ao_ver}.tar.bz2
# Source30-md5:	95809d330e48e61f58ec961ddbf0b529
Source31:	http://www.kadu.net/download/modules_extra/audacious_mediaplayer/audacious_mediaplayer-%{_mediaplayer_audacious_ver}.tar.bz2
# Source31-md5:	37cb762e361208c5c571771fb86968b5
Source32:	http://www.kadu.net/~weagle/mail/mail-%{_mail_ver}.tar.bz2
# Source32-md5:	0526354146a6c46b3670239f820a7caa
Source33:	http://www.kadu.net/download/additions/%{name}-0.6-theme-oxygen-16.tar.gz
# Source33-md5:	fb13f2624dec27632c42a6bc2c1a252f
Source34:	http://www.kadu.net/download/additions/%{name}-0.6-theme-tango-16.tar.gz
# Source34-md5:	52fe12765b600b9aa44cfc6489dce8eb
Patch0:		%{name}-ac_am.patch
Patch1:		%{name}-voice.patch
Patch2:		%{name}-mediaplayer-audacious.patch
URL:		http://kadu.net/
%{?with_sound_alsa:BuildRequires:	alsa-lib-devel}
%{?with_sound_arts:BuildRequires:	artsc-devel}
%{?with_spellchecker:BuildRequires:	aspell-devel}
%{?with_mediaplayer_audacious:BuildRequires:	audacious-devel >= 1.4.0}
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_sms_miastoplusa:BuildRequires:	curl-devel}
%{?with_sound_esd:BuildRequires:	esound-devel}
%if %{with mediaplayer_amarok} || %{with dcopexport}
BuildRequires:	kdelibs-devel
%endif
%{?with_sound_ao:BuildRequires:	libao-devel}
%{?with_voice:BuildRequires:	libgsm-devel}
BuildRequires:	libsndfile-devel >= 1.0
%{?with_sound_nas:BuildRequires:	nas-devel}
%{?with_encryption:BuildRequires:	openssl-devel >= 0.9.7d}
%{?with_mediaplayer_audacious:BuildRequires:	pkgconfig}
BuildRequires:	qt-linguist
BuildRequires:	sed >= 4.0
%{?with_mediaplayer_xmms:BuildRequires:	xmms-devel}
%{?with_notify_xosd:BuildRequires:	xosd-devel}
Obsoletes:	kadu-module-imiface <= 0.4.3
Obsoletes:	kadu-module-speech <= 0.4.3
Obsoletes:	kadu-module-tcl_scripting <= 0.4.3
Obsoletes:	kadu-theme-icons-crystal16 <= 0.5.0
Obsoletes:	kadu-theme-icons-crystal22 <= 0.5.0
Obsoletes:	kadu-theme-icons-nuvola16 <= 0.5.0
Obsoletes:	kadu-theme-icons-nuvola22 <= 0.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_modules_lib_dir	%{_libdir}/%{name}/modules
%define		_modules_data_dir	%{_datadir}/%{name}/modules
%define		_modules_bin_dir	%{_modules_lib_dir}/bin

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

%package module-agent
Summary:	Spying module that shows who has you on list
Summary(pl.UTF-8):	Moduł szpiegowski pokazujący osoby które mają cię na liście
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-agent
Spying module that shows who has you on list.

%description module-agent -l pl.UTF-8
Moduł szpiegowski pokazujący osoby które mają cię na liście.

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

%package module-encryption
Summary:	Chat encryption module
Summary(pl.UTF-8):	Moduł szyfrowania rozmów
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-encryption
Chat encryption module.

%description module-encryption -l pl.UTF-8
Moduł szyfrowania rozmów.

%package module-filedesc
Summary:	Descriptions from file module
Summary(pl.UTF-8):	Moduł obsługi opisów z pliku
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-filedesc
Descriptions from file module.

%description module-filedesc -l pl.UTF-8
Moduł obsługi opisów z pliku.

%package module-filtering
Summary:	User list filtering
Summary(pl.UTF-8):	Filtrowanie listy kontaktów
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-filtering
User list filtering.

%description module-filtering -l pl.UTF-8
Filtrowanie listy kontaktów.

%package module-firewall
Summary:	Module blocks unknown persons, who wants to start chat
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

%package module-mail
Summary:	Mail checker module
Summary(pl.UTF-8):	Moduł do sprawdzania poczty
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-mail
Mail checker module.

%description module-mail -l pl.UTF-8
Moduł do sprawdzania poczty.

%package module-mediaplayer
Summary:	Support for status from mediaplayer
Summary(pl.UTF-8):	Moduł statusu pobieranego z odtwarzaczy
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-mediaplayer
Module which allows showing in status description information about
the song currently played.

%description module-mediaplayer -l pl.UTF-8
Moduł umożliwiający w opisie statusu pokazywanie informacji o
odgrywanym utworze.

%package module-mediaplayer-amarok
Summary:	Support amarok status
Summary(pl.UTF-8):	Moduł statusu dla amarok
Group:		Applications/Communications
Requires:	%{name}-module-mediaplayer = %{version}-%{release}
Requires:	amarok
Provides:	kadu-module-amarok = %{version}
Obsoletes:	kadu-module-amarok <= 0.5.0

%description module-mediaplayer-amarok
Module which allows showing in status description information about
the song currently played in amarok.

%description module-mediaplayer-amarok -l pl.UTF-8
Moduł umożliwiający w opisie statusu pokazywanie informacji o
odgrywanym utworze z odtwarzacza amarok.

%package module-mediaplayer-audacious
Summary:	Support audacious status
Summary(pl.UTF-8):	Moduł statusu dla audacious
Group:		Applications/Communications
Requires:	%{name}-module-mediaplayer = %{version}-%{release}
Requires:	audacious

%description module-mediaplayer-audacious
Module which allows showing in status description information about
the song currently played in audacious.

%description module-mediaplayer-audacious -l pl.UTF-8
Moduł umożliwiający w opisie statusu pokazywanie informacji o
odgrywanym utworze z odtwarzacza audacious.

%package module-mediaplayer-falf
Summary:	Support falf status
Summary(pl.UTF-8):	Moduł statusu dla falf
Group:		Applications/Communications
Requires:	%{name}-module-mediaplayer = %{version}-%{release}

%description module-mediaplayer-falf
Module which allows showing in status description information about
the song currently played in falf.

%description module-mediaplayer-falf -l pl.UTF-8
Moduł umożliwiający w opisie statusu pokazywanie informacji o
odgrywanym utworze z odtwarzacza falf.

%package module-mediaplayer-xmms
Summary:	Support XMMS status
Summary(pl.UTF-8):	Moduł statusu dla XMMS-a
Group:		Applications/Communications
Requires:	%{name}-module-mediaplayer = %{version}-%{release}
Requires:	xmms
Provides:	kadu-module-xmms = %{version}
Obsoletes:	kadu-module-xmms <= 0.5.0

%description module-mediaplayer-xmms
Module which allows showing in status description information about
the song currently played in XMMS.

%description module-mediaplayer-xmms -l pl.UTF-8
Moduł umożliwiający pokazywanie w opisie statusu informacji o
odgrywanym utworze z odtwarzacza XMMS.

%package module-mime_tex
Summary:	Mathematical TeX formulas in chat windows
Summary(pl.UTF-8):	Matematyczne formuły TeX w oknach czat
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-mime_tex
Mathematical TeX formulas for chat windows.

%description module-mime_tex -l pl.UTF-8
Matematyczne formuły TeX w oknach czat.

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

%package module-notify-mx610
Summary:	Notification by IM-LED in Logitech MX610 mouse
Summary(pl.UTF-8):	Moduł powiadamiania diodą IM w myszcze Logitech MX610
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-notify-mx610
Notification by IM-LED in Logitech MX610 mouse.

%description module-notify-mx610 -l pl.UTF-8
Moduł powiadamiania diodą IM w myszcze Logitech MX610.

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

%package module-notify-water
Summary:	Notification by Water Plugin in Compiz
Summary(pl.UTF-8):	Moduł powiadamiania pluginem Water w Compiz
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-notify-water
Notification by Water Plugin in Compiz.

%description module-notify-water -l pl.UTF-8
Moduł powiadamiania pluginem Water w Compiz.

%package module-notify-xosd
Summary:	Notification by XOSD module
Summary(pl.UTF-8):	Moduł powiadamiania o zdarzeniach przy pomocy XOSD
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-notify-xosd
Notification by XOSD module.

%description module-notify-xosd -l pl.UTF-8
Moduł powiadamiania o zdarzeniach przy pomocy XOSD.

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

%package module-sound-ao
Summary:	Libao sound module
Summary(pl.UTF-8):	Moduł obsługi dźwięku poprzez bibliotekę libao
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-sound-ao
Libao sound module.

%description module-sound-ao -l pl.UTF-8
Moduł obsługi dźwięku poprzez bibliotekę libao.

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

%package module-sound-ext
Summary:	External application sound module
Summary(pl.UTF-8):	Moduł obsługi dźwięku przez zewnętrzną aplikację
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-sound-ext
External application sound module.

%description module-sound-ext -l pl.UTF-8
Moduł obsługi dźwięku przez zewnętrzną aplikację.

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

%package module-tabs
Summary:	Tabbed chat dialog module
Summary(pl.UTF-8):	Moduł okna rozmowy z kartami
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-tabs
Tabbed chat dialog module.

%description module-tabs -l pl.UTF-8
Moduł okna rozmowy z kartami.

%package module-voice
Summary:	Voice chat support module
Summary(pl.UTF-8):	Moduł obsługi rozmów głosowych
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-voice
Voice chat support module.

%description module-voice -l pl.UTF-8
Moduł obsługi rozmów głosowych.

%package module-weather
Summary:	Weather module
Summary(pl.UTF-8):	Moduł pogodowy
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-weather
Informations of weather in locality of contact.

%description module-weather -l pl.UTF-8
Informacje o pogodzie w miejscowości danego kontaktu.

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

%package theme-icons-oxygen16
Summary:	Oxygen16 icon theme
Summary(pl.UTF-8):	Zestaw ikon Oxygen16
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description theme-icons-oxygen16
Oxygen16 icon theme.

%description theme-icons-oxygen16 -l pl.UTF-8
Zestaw ikon Oxygen16.

%package theme-icons-tango16
Summary:	Tango16 icon theme
Summary(pl.UTF-8):	Zestaw ikon Tango16
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description theme-icons-tango16
Tango16 icon theme.

%description theme-icons-tango16 -l pl.UTF-8
Zestaw ikon Tango16.

%prep
%setup -q -T -b %{?with_snap:10}0 -n %{name}
%patch0 -p1
%patch1 -p1

%if %{with mediaplayer}
tar xjf %{SOURCE2} -C modules
%endif
%if %{with mediaplayer_amarok}
tar xjf %{SOURCE3} -C modules
%endif
%if %{with mediaplayer_audacious}
tar xjf %{SOURCE31} -C modules
%patch2 -p1
%endif
%if %{with dcopexport}
tar xjf %{SOURCE4} -C modules
%endif
%if %{with filedesc}
tar xjf %{SOURCE5} -C modules
%endif
%if %{with filtering}
tar xjf %{SOURCE6} -C modules
%endif
%if %{with firewall}
tar xjf %{SOURCE27} -C modules
%endif
%if %{with iwait4u}
tar xzf %{SOURCE7} -C modules
%endif
%if %{with mail}
tar xjf %{SOURCE32} -C modules
%endif
%if %{with mediaplayer_falf}
tar xjf %{SOURCE8} -C modules
%endif
%if %{with mime_tex}
tar xjf %{SOURCE28} -C modules
%endif
%if %{with notify_led}
tar xjf %{SOURCE9} -C modules
%endif
%if %{with notify_mx610}
tar xjf %{SOURCE29} -C modules
%endif
%if %{with notify_osdhints}
tar xjf %{SOURCE10} -C modules
%endif
%if %{with notify_pcspeaker}
tar xjf %{SOURCE11} -C modules
%endif
%if %{with notify_water}
tar xjf %{SOURCE21} -C modules
%endif
%if %{with powerkadu}
tar xzf %{SOURCE12} -C modules
%endif
%if %{with profiles}
tar xjf %{SOURCE13} -C modules
%endif
%if %{with screenshot}
tar xjf %{SOURCE14} -C modules
%endif
%if %{with sms_miastoplusa}
tar xzf %{SOURCE15} -C modules
%endif
%if %{with sound_ao}
tar xjf %{SOURCE30} -C modules
%endif
%if %{with spellchecker}
tar xjf %{SOURCE16} -C modules
%endif
%if %{with agent}
tar xzf %{SOURCE17} -C modules
%endif
%if %{with tabs}
tar xjf %{SOURCE18} -C modules
%endif
%if %{with weather}
tar xjf %{SOURCE19} -C modules
%endif
%if %{with mediaplayer_xmms}
tar xjf %{SOURCE20} -C modules
%endif
# themes-icons
tar xzf %{SOURCE23} -C varia/themes/icons
tar xzf %{SOURCE24} -C varia/themes/icons
tar xzf %{SOURCE33} -C varia/themes/icons
tar xzf %{SOURCE34} -C varia/themes/icons

# Change hard coded path to modules data files
%{__sed} -i 's,dataPath("kadu/modules/*,("%{_modules_data_dir}/,g' kadu-core/modules.cpp

%build
%if %{with advanced_userlist}
%{__sed} -i 's/module_advanced_userlist=n/module_advanced_userlist=m/' .config
%else
%{__sed} -i 's/module_advanced_userlist=m/module_advanced_userlist=n/' .config
%endif
%if %{with agent}
%{__sed} -i 's/module_agent=n/module_agent=m/' .config
%else
%{__sed} -i 's/module_agent=m/module_agent=n/' .config
%endif
%if %{with autoresponder}
%{__sed} -i 's/module_autoresponder=n/module_autoresponder=m/' .config
%else
%{__sed} -i 's/module_autoresponder=m/module_autoresponder=n/' .config
%endif
%if %{with dcopexport}
%{__sed} -i 's/module_dcopexport=n/module_dcopexport=m/' .config
%else
%{__sed} -i 's/module_dcopexport=m/module_dcopexport=n/' .config
%endif
%if %{with docking_desktop}
%{__sed} -i 's/module_desktop_docking=n/module_desktop_docking=m/' .config
%else
%{__sed} -i 's/module_desktop_docking=m/module_desktop_docking=n/' .config
%endif
%if %{with encryption}
%{__sed} -i 's/module_encryption=n/module_encryption=m/' .config
%else
%{__sed} -i 's/module_encryption=m/module_encryption=n/' .config
%endif
%if %{with filedesc}
%{__sed} -i 's/module_filedesc=n/module_filedesc=m/' .config
%else
%{__sed} -i 's/module_filedesc=m/module_filedesc=n/' .config
%endif
%if %{with filtering}
%{__sed} -i 's/module_filtering=n/module_filtering=m/' .config
%else
%{__sed} -i 's/module_filtering=m/module_filtering=n/' .config
%endif
%if %{with firewall}
%{__sed} -i 's/module_firewall=n/module_firewall=m/' .config
%else
%{__sed} -i 's/module_firewall=m/module_firewall=n/' .config
%endif
%if %{with iwait4u}
%{__sed} -i 's/module_iwait4u=n/module_iwait4u=m/' .config
%else
%{__sed} -i 's/module_iwait4u=m/module_iwait4u=n/' .config
%endif
%if %{with mail}
%{__sed} -i 's/module_mail=n/module_mail=m/' .config
%else
%{__sed} -i 's/module_mail=m/module_mail=n/' .config
%endif
%if %{with mediaplayer}
%{__sed} -i 's/module_mediaplayer=n/module_mediaplayer=m/' .config
%else
%{__sed} -i 's/module_mediaplayer=m/module_mediaplayer=n/' .config
%endif
%if %{with mediaplayer_amarok}
%{__sed} -i 's/module_amarok_mediaplayer=n/module_amarok_mediaplayer=m/' .config
echo 'MODULE_INCLUDES_PATH="%{_includedir}"' >> modules/amarok_mediaplayer/spec
echo 'MODULE_LIBS_PATH="%{_libdir}"' >> modules/amarok_mediaplayer/spec
%else
%{__sed} -i 's/module_amarok_mediaplayer=m/module_amarok_mediaplayer=n/' .config
%endif
%if %{with mediaplayer_audacious}
%{__sed} -i 's/module_audacious_mediaplayer=n/module_audacious_mediaplayer=m/' .config
%else
%{__sed} -i 's/module_audacious_mediaplayer=m/module_audacious_mediaplayer=n/' .config
%endif
%if %{with mediaplayer_falf}
%{__sed} -i 's/module_falf_mediaplayer=n/module_falf_mediaplayer=m/' .config
%else
%{__sed} -i 's/module_falf_mediaplayer=m/module_falf_mediaplayer=n/' .config
%endif
%if %{with mediaplayer_xmms}
%{__sed} -i 's/module_xmms_mediaplayer=n/module_xmms_mediaplayer=m/' .config
%else
%{__sed} -i 's/module_xmms_mediaplayer=m/module_xmms_mediaplayer=n/' .config
%endif
%if %{with mime_tex}
%{__sed} -i 's/module_mime_tex=n/module_mime_tex=m/' .config
%else
%{__sed} -i 's/module_mime_tex=m/module_mime_tex=n/' .config
%endif
%if %{with notify_exec}
%{__sed} -i 's/module_exec_notify=n/module_exec_notify=m/' .config
%else
%{__sed} -i 's/module_exec_notify=m/module_exec_notify=n/' .config
%endif
%if %{with notify_led}
%{__sed} -i 's/module_led_notify=n/module_led_notify=m/' .config
%else
%{__sed} -i 's/module_led_notify=m/module_led_notify=n/' .config
%endif
%if %{with notify_mx610}
%{__sed} -i 's/module_mx610_notify=n/module_mx610_notify=m/' .config
%else
%{__sed} -i 's/module_mx610_notify=m/module_mx610_notify=n/' .config
%endif
%if %{with notify_osdhints}
%{__sed} -i 's/module_osdhints_notify=n/module_osdhints_notify=m/' .config
%else
%{__sed} -i 's/module_osdhints_notify=m/module_osdhints_notify=n/' .config
%endif
%if %{with notify_pcspeaker}
%{__sed} -i 's/module_pcspeaker=n/module_pcspeaker=m/' .config
%else
%{__sed} -i 's/module_pcspeaker=m/module_pcspeaker=n/' .config
%endif
%if %{with notify_speech}
%{__sed} -i 's/module_speech=n/module_speech=m/' .config
%else
%{__sed} -i 's/module_speech=m/module_speech=n/' .config
%endif
%if %{with notify_water}
%{__sed} -i 's/module_water_notify=n/module_water_notify=m/' .config
%else
%{__sed} -i 's/module_water_notify=m/module_water_notify=n/' .config
%endif
%if %{with notify_xosd}
%{__sed} -i 's/module_xosd_notify=n/module_xosd_notify=m/' .config
%else
%{__sed} -i 's/module_xosd_notify=m/module_xosd_notify=n/' .config
%endif
%if %{with powerkadu}
%{__sed} -i 's/module_powerkadu=n/module_powerkadu=m/' .config
# fix for 20070107 version
rm -f modules/powerkadu/bin/mimetex
%else
%{__sed} -i 's/module_powerkadu=m/module_powerkadu=n/' .config
%endif
%if %{with profiles}
%{__sed} -i 's/module_profiles=n/module_profiles=m/' .config
%else
%{__sed} -i 's/module_profiles=m/module_profiles=n/' .config
%endif
%if %{with screenshot}
%{__sed} -i 's/module_screenshot=n/module_screenshot=m/' .config
%else
%{__sed} -i 's/module_screenshot=m/module_screenshot=n/' .config
%endif
%if %{with sms_miastoplusa}
%{__sed} -i 's/module_miastoplusa_sms=n/module_miastoplusa_sms=m/' .config
%else
%{__sed} -i 's/module_miastoplusa_sms=m/module_miastoplusa_sms=n/' .config
%endif
%if %{with sound_alsa}
%{__sed} -i 's/module_alsa_sound=n/module_alsa_sound=m/' .config
%else
%{__sed} -i 's/module_alsa_sound=m/module_alsa_sound=n/' .config
%endif
%if %{with sound_ao}
%{__sed} -i 's/module_ao_sound=n/module_ao_sound=m/' .config
%else
%{__sed} -i 's/module_ao_sound=m/module_ao_sound=n/' .config
%endif
%if %{with sound_arts}
%{__sed} -i 's/module_arts_sound=n/module_arts_sound=m/' .config
%else
%{__sed} -i 's/module_arts_sound=m/module_arts_sound=n/' .config
%endif
%if %{with sound_dsp}
%{__sed} -i 's/module_dsp_sound=n/module_dsp_sound=m/' .config
%else
%{__sed} -i 's/module_dsp_sound=m/module_dsp_sound=n/' .config
%endif
%if %{with sound_esd}
%{__sed} -i 's/module_esd_sound=n/module_esd_sound=m/' .config
%else
%{__sed} -i 's/module_esd_sound=m/module_esd_sound=n/' .config
%endif
%if %{with sound_ext}
%{__sed} -i 's/module_ext_sound=n/module_ext_sound=m/' .config
%else
%{__sed} -i 's/module_ext_sound=m/module_ext_sound=n/' .config
%endif
%if %{with sound_nas}
%{__sed} -i 's/module_nas_sound=n/module_nas_sound=m/' .config
echo 'MODULE_LIBS_PATH="%{_prefix}/lib"' >> modules/nas_sound/spec
%else
%{__sed} -i 's/module_nas_sound=m/module_nas_sound=n/' .config
%endif
%if %{with spellchecker}
%{__sed} -i 's/module_spellchecker=n/module_spellchecker=m/' .config
%else
%{__sed} -i 's/module_spellchecker=m/module_spellchecker=n/' .config
%endif
%if %{with tabs}
%{__sed} -i 's/module_tabs=n/module_tabs=m/' .config
%else
%{__sed} -i 's/module_tabs=m/module_tabs=n/' .config
%endif
%if %{with voice}
%{__sed} -i 's/module_voice=n/module_voice=m/' .config
%else
%{__sed} -i 's/module_voice=m/module_voice=n/' .config
%endif
%if %{with weather}
%{__sed} -i 's/module_weather=n/module_weather=m/' .config
%else
%{__sed} -i 's/module_weather=m/module_weather=n/' .config
%endif

%{__sed} -i 's/icons_glass16=n/icons_glass16=y/' .config
%{__sed} -i 's/icons_glass22=n/icons_glass22=y/' .config
%{__sed} -i 's/icons_oxygen16=n/icons_oxygen16=y/' .config
%{__sed} -i 's/icons_tango16=n/icons_tango16=y/' .config

chmod u+w aclocal.m4 configure
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--%{?with_debug:en}%{!?with_debug:dis}able-debug \
	--enable-dist-info="PLD Linux Distribution" \
	--disable-autodownload
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

# We dont need 8 same icons with just diffrent size - one is enough
rm -f  $RPM_BUILD_ROOT%{_pixmapsdir}/*.png
install kadu-core/hi64-app-kadu.png $RPM_BUILD_ROOT%{_pixmapsdir}/kadu.png

# Remove useless scripts
rm -f $RPM_BUILD_ROOT%{_bindir}/kadu-{mozilla,config}

rm -rf $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%dir %{_datadir}/%{name}
%dir %{_modules_data_dir}
%dir %{_modules_data_dir}/data
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
%dir %{_modules_lib_dir}
%dir %{_modules_bin_dir}
%{_modules_data_dir}/account_management.desc
%attr(755,root,root) %{_modules_lib_dir}/account_management.so
%{_modules_data_dir}/autoaway.desc
%attr(755,root,root) %{_modules_lib_dir}/autoaway.so
%{_modules_data_dir}/config_wizard.desc
%attr(755,root,root) %{_modules_lib_dir}/config_wizard.so
%{_modules_data_dir}/dcc.desc
%attr(755,root,root) %{_modules_lib_dir}/dcc.so
%{_modules_data_dir}/default_sms.desc
%attr(755,root,root) %{_modules_lib_dir}/default_sms.so
%{_modules_data_dir}/docking.desc
%{_modules_data_dir}/hints.desc
%attr(755,root,root) %{_modules_lib_dir}/hints.so
%{_modules_data_dir}/migration.desc
%attr(755,root,root) %{_modules_lib_dir}/migration.so
%{_modules_data_dir}/notify.desc
%{_modules_data_dir}/sms.desc
%attr(755,root,root) %{_modules_lib_dir}/sms.so
%{_modules_data_dir}/history.desc
%attr(755,root,root) %{_modules_lib_dir}/history.so
%{_modules_data_dir}/sound.desc
%{_modules_data_dir}/window_notify.desc
%attr(755,root,root) %{_modules_lib_dir}/window_notify.so
%{_modules_data_dir}/x11_docking.desc
%attr(755,root,root) %{_modules_lib_dir}/x11_docking.so

#default modules translation:
%dir %{_modules_data_dir}/translations
%lang(de) %{_modules_data_dir}/translations/account_management_de.qm
%lang(fr) %{_modules_data_dir}/translations/account_management_fr.qm
%lang(it) %{_modules_data_dir}/translations/account_management_it.qm
%lang(pl) %{_modules_data_dir}/translations/account_management_pl.qm
%lang(de) %{_modules_data_dir}/translations/autoaway_de.qm
%lang(fr) %{_modules_data_dir}/translations/autoaway_fr.qm
%lang(it) %{_modules_data_dir}/translations/autoaway_it.qm
%lang(pl) %{_modules_data_dir}/translations/autoaway_pl.qm
%lang(de) %{_modules_data_dir}/translations/config_wizard_de.qm
%lang(fr) %{_modules_data_dir}/translations/config_wizard_fr.qm
%lang(it) %{_modules_data_dir}/translations/config_wizard_it.qm
%lang(pl) %{_modules_data_dir}/translations/config_wizard_pl.qm
%lang(de) %{_modules_data_dir}/translations/dcc_de.qm
%lang(fr) %{_modules_data_dir}/translations/dcc_fr.qm
%lang(it) %{_modules_data_dir}/translations/dcc_it.qm
%lang(pl) %{_modules_data_dir}/translations/dcc_pl.qm
%lang(de) %{_modules_data_dir}/translations/default_sms_de.qm
%lang(fr) %{_modules_data_dir}/translations/default_sms_fr.qm
%lang(it) %{_modules_data_dir}/translations/default_sms_it.qm
%lang(pl) %{_modules_data_dir}/translations/default_sms_pl.qm
%lang(de) %{_modules_data_dir}/translations/docking_de.qm
%lang(fr) %{_modules_data_dir}/translations/docking_fr.qm
%lang(it) %{_modules_data_dir}/translations/docking_it.qm
%lang(pl) %{_modules_data_dir}/translations/docking_pl.qm
%lang(de) %{_modules_data_dir}/translations/hints_de.qm
%lang(fr) %{_modules_data_dir}/translations/hints_fr.qm
%lang(it) %{_modules_data_dir}/translations/hints_it.qm
%lang(pl) %{_modules_data_dir}/translations/hints_pl.qm
%lang(de) %{_modules_data_dir}/translations/history_de.qm
%lang(fr) %{_modules_data_dir}/translations/history_fr.qm
%lang(it) %{_modules_data_dir}/translations/history_it.qm
%lang(pl) %{_modules_data_dir}/translations/history_pl.qm
%lang(de) %{_modules_data_dir}/translations/migration_de.qm
%lang(fr) %{_modules_data_dir}/translations/migration_fr.qm
%lang(it) %{_modules_data_dir}/translations/migration_it.qm
%lang(pl) %{_modules_data_dir}/translations/migration_pl.qm
%lang(de) %{_modules_data_dir}/translations/notify_de.qm
%lang(fr) %{_modules_data_dir}/translations/notify_fr.qm
%lang(it) %{_modules_data_dir}/translations/notify_it.qm
%lang(pl) %{_modules_data_dir}/translations/notify_pl.qm
%lang(de) %{_modules_data_dir}/translations/sms_de.qm
%lang(fr) %{_modules_data_dir}/translations/sms_fr.qm
%lang(it) %{_modules_data_dir}/translations/sms_it.qm
%lang(pl) %{_modules_data_dir}/translations/sms_pl.qm
%lang(de) %{_modules_data_dir}/translations/sound_de.qm
%lang(fr) %{_modules_data_dir}/translations/sound_fr.qm
%lang(it) %{_modules_data_dir}/translations/sound_it.qm
%lang(pl) %{_modules_data_dir}/translations/sound_pl.qm
%lang(de) %{_modules_data_dir}/translations/window_notify_de.qm
%lang(fr) %{_modules_data_dir}/translations/window_notify_fr.qm
%lang(it) %{_modules_data_dir}/translations/window_notify_it.qm
%lang(pl) %{_modules_data_dir}/translations/window_notify_pl.qm
%lang(de) %{_modules_data_dir}/translations/x11_docking_de.qm
%lang(fr) %{_modules_data_dir}/translations/x11_docking_fr.qm
%lang(it) %{_modules_data_dir}/translations/x11_docking_it.qm
%lang(pl) %{_modules_data_dir}/translations/x11_docking_pl.qm
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
%{_modules_data_dir}/data/config_wizard
%{_datadir}/%{name}/configuration
%{_datadir}/%{name}/syntax

%dir %{_modules_data_dir}/configuration
%{_modules_data_dir}/configuration/autoaway.ui
%{_modules_data_dir}/configuration/dcc.ui
%{_modules_data_dir}/configuration/default_sms.ui
%{_modules_data_dir}/configuration/docking.ui
%{_modules_data_dir}/configuration/hints.ui
%{_modules_data_dir}/configuration/history.ui
%{_modules_data_dir}/configuration/notify.ui
%{_modules_data_dir}/configuration/sms.ui
%{_modules_data_dir}/configuration/sound.ui

%if %{with advanced_userlist}
%files module-advanced_userlist
%defattr(644,root,root,755)
%{_modules_data_dir}/advanced_userlist.desc
%{_modules_data_dir}/configuration/advanced_userlist.ui
%attr(755,root,root) %{_modules_lib_dir}/advanced_userlist.so
%lang(de) %{_modules_data_dir}/translations/advanced_userlist_de.qm
%lang(fr) %{_modules_data_dir}/translations/advanced_userlist_fr.qm
%lang(it) %{_modules_data_dir}/translations/advanced_userlist_it.qm
%lang(pl) %{_modules_data_dir}/translations/advanced_userlist_pl.qm
%endif

%if %{with agent}
%files module-agent
%defattr(644,root,root,755)
%{_modules_data_dir}/agent.desc
%attr(755,root,root) %{_modules_lib_dir}/agent.so
%lang(pl) %{_modules_data_dir}/translations/agent_pl.qm
%endif

%if %{with autoresponder}
%files module-autoresponder
%defattr(644,root,root,755)
%{_modules_data_dir}/autoresponder.desc
%{_modules_data_dir}/configuration/autoresponder.ui
%attr(755,root,root) %{_modules_lib_dir}/autoresponder.so
%lang(de) %{_modules_data_dir}/translations/autoresponder_de.qm
%lang(fr) %{_modules_data_dir}/translations/autoresponder_fr.qm
%lang(it) %{_modules_data_dir}/translations/autoresponder_it.qm
%lang(pl) %{_modules_data_dir}/translations/autoresponder_pl.qm
%endif

%if %{with encryption}
%files module-encryption
%defattr(644,root,root,755)
%{_modules_data_dir}/encryption.desc
%{_modules_data_dir}/configuration/encryption.ui
%attr(755,root,root) %{_modules_lib_dir}/encryption.so
%lang(de) %{_modules_data_dir}/translations/encryption_de.qm
%lang(fr) %{_modules_data_dir}/translations/encryption_fr.qm
%lang(it) %{_modules_data_dir}/translations/encryption_it.qm
%lang(pl) %{_modules_data_dir}/translations/encryption_pl.qm
%endif

%if %{with dcopexport}
%files module-dcopexport
%defattr(644,root,root,755)
%{_modules_data_dir}/dcopexport.desc
%attr(755,root,root) %{_modules_lib_dir}/dcopexport.so
%lang(pl) %{_modules_data_dir}/translations/dcopexport_pl.qm
%dir %{_modules_bin_dir}/dcopexport
%attr(755,root,root) %{_modules_bin_dir}/dcopexport/install-firefox-gg.sh
%attr(755,root,root) %{_modules_bin_dir}/dcopexport/install-konqueror-gg.sh
%attr(755,root,root) %{_modules_bin_dir}/dcopexport/install-konqueror-setAsKaduDesc.sh
%attr(755,root,root) %{_modules_bin_dir}/dcopexport/install-opera-gg.sh
%attr(755,root,root) %{_modules_bin_dir}/dcopexport/kadu-gg-handler.sh
%dir %{_modules_data_dir}/data/dcopexport
%{_modules_data_dir}/data/dcopexport/dcopexport.png
%endif

%if %{with docking_desktop}
%files module-docking-desktop
%defattr(644,root,root,755)
%{_modules_data_dir}/desktop_docking.desc
%{_modules_data_dir}/configuration/desktop_docking.ui
%attr(755,root,root) %{_modules_lib_dir}/desktop_docking.so
%lang(de) %{_modules_data_dir}/translations/desktop_docking_de.qm
%lang(fr) %{_modules_data_dir}/translations/desktop_docking_fr.qm
%lang(it) %{_modules_data_dir}/translations/desktop_docking_it.qm
%lang(pl) %{_modules_data_dir}/translations/desktop_docking_pl.qm
%endif

%if %{with filedesc}
%files module-filedesc
%defattr(644,root,root,755)
%{_modules_data_dir}/filedesc.desc
%{_modules_data_dir}/configuration/filedesc.ui
%attr(755,root,root) %{_modules_lib_dir}/filedesc.so
%lang(pl) %{_modules_data_dir}/translations/filedesc_pl.qm
%dir %{_modules_data_dir}/data/filedesc
%{_modules_data_dir}/data/filedesc/*.png
%endif

%if %{with filtering}
%files module-filtering
%defattr(644,root,root,755)
%{_modules_data_dir}/filtering.desc
%{_modules_data_dir}/configuration/filtering.ui
%attr(755,root,root) %{_modules_lib_dir}/filtering.so
%lang(pl) %{_modules_data_dir}/translations/filtering_pl.qm
%dir %{_modules_data_dir}/data/filtering
%{_modules_data_dir}/data/filtering/*.png
%endif

%if %{with firewall}
%files module-firewall
%defattr(644,root,root,755)
%{_modules_data_dir}/filtering.desc
%{_modules_data_dir}/configuration/firewall.ui
%attr(755,root,root) %{_modules_lib_dir}/firewall.so
%lang(pl) %{_modules_data_dir}/translations/firewall_pl.qm
%{_modules_data_dir}/firewall.desc
%endif

%if %{with iwait4u}
%files module-iwait4u
%defattr(644,root,root,755)
%{_modules_data_dir}/iwait4u.desc
%attr(755,root,root) %{_modules_lib_dir}/iwait4u.so
%lang(pl) %{_modules_data_dir}/translations/iwait4u_pl.qm
%endif

%if %{with mail}
%files module-mail
%defattr(644,root,root,755)
%{_modules_data_dir}/mail.desc
%{_modules_data_dir}/configuration/mail.ui
%attr(755,root,root) %{_modules_lib_dir}/mail.so
%lang(pl) %{_modules_data_dir}/translations/mail_pl.qm
%endif

%if %{with mediaplayer}
%files module-mediaplayer
%defattr(644,root,root,755)
%{_modules_data_dir}/mediaplayer.desc
%{_modules_data_dir}/configuration/mediaplayer.ui
%attr(755,root,root) %{_modules_lib_dir}/mediaplayer.so
%{_modules_data_dir}/data/mediaplayer
%lang(pl) %{_modules_data_dir}/translations/mediaplayer_pl.qm
%endif

%if %{with mediaplayer_amarok}
%files module-mediaplayer-amarok
%defattr(644,root,root,755)
%{_modules_data_dir}/amarok_mediaplayer.desc
%attr(755,root,root) %{_modules_lib_dir}/amarok_mediaplayer.so
%endif

%if %{with mediaplayer_audacious}
%files module-mediaplayer-audacious
%defattr(644,root,root,755)
%{_modules_data_dir}/audacious_mediaplayer.desc
%attr(755,root,root) %{_modules_lib_dir}/audacious_mediaplayer.so
%endif

%if %{with mediaplayer_falf}
%files module-mediaplayer-falf
%defattr(644,root,root,755)
%{_modules_data_dir}/falf_mediaplayer.desc
%attr(755,root,root) %{_modules_lib_dir}/falf_mediaplayer.so
%endif

%if %{with mediaplayer_xmms}
%files module-mediaplayer-xmms
%defattr(644,root,root,755)
%{_modules_data_dir}/xmms_mediaplayer.desc
%attr(755,root,root) %{_modules_lib_dir}/xmms_mediaplayer.so
%endif

%if %{with mime_tex}
%files module-mime_tex
%defattr(644,root,root,755)
%dir %{_modules_bin_dir}/mime_tex
%attr(755,root,root) %{_modules_bin_dir}/mime_tex/mimetex
%{_modules_data_dir}/mime_tex.desc
%{_modules_data_dir}/configuration/mime_tex.ui
%attr(755,root,root) %{_modules_lib_dir}/mime_tex.so
%dir %{_modules_data_dir}/data/mime_tex
%dir %{_modules_data_dir}/data/mime_tex/editor_icons
%dir %{_modules_data_dir}/data/mime_tex/mime_tex_icons
%{_modules_data_dir}/data/mime_tex/mime_tex_32x32.png
%{_modules_data_dir}/data/mime_tex/editor_icons/*.png
%{_modules_data_dir}/data/mime_tex/mime_tex_icons/*.png
%lang(pl) %{_modules_data_dir}/translations/mime_tex_pl.qm
%endif

%if %{with notify_exec}
%files module-notify-exec
%defattr(644,root,root,755)
%{_modules_data_dir}/exec_notify.desc
%attr(755,root,root) %{_modules_lib_dir}/exec_notify.so
%lang(de) %{_modules_data_dir}/translations/exec_notify_de.qm
%lang(fr) %{_modules_data_dir}/translations/exec_notify_fr.qm
%lang(it) %{_modules_data_dir}/translations/exec_notify_it.qm
%lang(pl) %{_modules_data_dir}/translations/exec_notify_pl.qm
%endif

%if %{with notify_led}
%files module-notify-led
%defattr(644,root,root,755)
%{_modules_data_dir}/led_notify.desc
%{_modules_data_dir}/configuration/led_notify.ui
%attr(755,root,root) %{_modules_lib_dir}/led_notify.so
%lang(pl) %{_modules_data_dir}/translations/led_notify_pl.qm
%endif

%if %{with notify_mx610}
%files module-notify-mx610
%defattr(644,root,root,755)
%{_modules_data_dir}/mx610_notify.desc
%{_modules_data_dir}/configuration/mx610_notify.ui
%attr(755,root,root) %{_modules_lib_dir}/mx610_notify.so
%lang(pl) %{_modules_data_dir}/translations/mx610_notify_pl.qm
%endif

%if %{with notify_osdhints}
%files module-notify-osdhints
%defattr(644,root,root,755)
%{_modules_data_dir}/osdhints_notify.desc
%{_modules_data_dir}/configuration/osdhints_notify.ui
%attr(755,root,root) %{_modules_lib_dir}/osdhints_notify.so
%lang(pl) %{_modules_data_dir}/translations/osdhints_notify_pl.qm
%dir %{_modules_data_dir}/data/osdhints_notify
%{_modules_data_dir}/data/osdhints_notify/License
%{_modules_data_dir}/data/osdhints_notify/*.png
%endif

%if %{with notify_pcspeaker}
%files module-notify-pcspeaker
%defattr(644,root,root,755)
%{_modules_data_dir}/pcspeaker.desc
%{_modules_data_dir}/configuration/pcspeaker.ui
%attr(755,root,root) %{_modules_lib_dir}/pcspeaker.so
%lang(de) %{_modules_data_dir}/translations/pcspeaker_de.qm
%lang(it) %{_modules_data_dir}/translations/pcspeaker_it.qm
%lang(pl) %{_modules_data_dir}/translations/pcspeaker_pl.qm
%endif

%if %{with notify_speech}
%files module-notify-speech
%defattr(644,root,root,755)
%{_modules_data_dir}/speech.desc
%{_modules_data_dir}/configuration/speech.ui
%attr(755,root,root) %{_modules_lib_dir}/speech.so
%lang(de) %{_modules_data_dir}/translations/speech_de.qm
%lang(fr) %{_modules_data_dir}/translations/speech_fr.qm
%lang(it) %{_modules_data_dir}/translations/speech_it.qm
%lang(pl) %{_modules_data_dir}/translations/speech_pl.qm
%endif

%if %{with notify_water}
%files module-notify-water
%defattr(644,root,root,755)
%{_modules_data_dir}/water_notify.desc
%{_modules_data_dir}/configuration/water_notify.ui
%attr(755,root,root) %{_modules_lib_dir}/water_notify.so
%lang(pl) %{_modules_data_dir}/translations/water_notify_pl.qm
%endif

%if %{with notify_xosd}
%files module-notify-xosd
%defattr(644,root,root,755)
%{_modules_data_dir}/xosd_notify.desc
%{_modules_data_dir}/configuration/xosd_notify.ui
%attr(755,root,root) %{_modules_lib_dir}/xosd_notify.so
%dir %{_modules_bin_dir}/xosd_notify
%attr(755,root,root) %{_modules_bin_dir}/xosd_notify/gtkfontdialog
%lang(de) %{_modules_data_dir}/translations/xosd_notify_de.qm
%lang(fr) %{_modules_data_dir}/translations/xosd_notify_fr.qm
%lang(it) %{_modules_data_dir}/translations/xosd_notify_it.qm
%lang(pl) %{_modules_data_dir}/translations/xosd_notify_pl.qm
%endif

%if %{with powerkadu}
%files module-powerkadu
%defattr(644,root,root,755)
%{_modules_data_dir}/powerkadu.desc
%attr(755,root,root) %{_modules_lib_dir}/powerkadu.so
%lang(pl) %{_modules_data_dir}/translations/powerkadu_pl.qm
%dir %{_modules_bin_dir}/powerkadu
%attr(755,root,root) %{_modules_bin_dir}/powerkadu/mimetex
%{_modules_data_dir}/data/powerkadu
%endif

%if %{with profiles}
%files module-profiles
%defattr(644,root,root,755)
%{_modules_data_dir}/profiles.desc
%attr(755,root,root) %{_modules_lib_dir}/profiles.so
%lang(it) %{_modules_data_dir}/translations/profiles_it.qm
%lang(pl) %{_modules_data_dir}/translations/profiles_pl.qm
%endif

%if %{with screenshot}
%files module-screenshot
%defattr(644,root,root,755)
%{_modules_data_dir}/screenshot.desc
%{_modules_data_dir}/configuration/screenshot.ui
%attr(755,root,root) %{_modules_lib_dir}/screenshot.so
%lang(pl) %{_modules_data_dir}/translations/screenshot_pl.qm
%dir %{_modules_data_dir}/data/screenshot
%{_modules_data_dir}/data/screenshot/*.png
%endif

%if %{with sms_miastoplusa}
%files module-sms-miastoplusa
%defattr(644,root,root,755)
%{_modules_data_dir}/miastoplusa_sms.desc
%{_modules_data_dir}/configuration/miastoplusa_sms.ui
%attr(755,root,root) %{_modules_lib_dir}/miastoplusa_sms.so
%lang(pl) %{_modules_data_dir}/translations/miastoplusa_sms_pl.qm
%dir %{_modules_data_dir}/data/miastoplusa_sms
%{_modules_data_dir}/data/miastoplusa_sms/curl-ca-bundle.crt
%endif

%if %{with sound_alsa}
%files module-sound-alsa
%defattr(644,root,root,755)
%{_modules_data_dir}/alsa_sound.desc
%{_modules_data_dir}/configuration/alsa_sound.ui
%attr(755,root,root) %{_modules_lib_dir}/alsa_sound.so
%lang(de) %{_modules_data_dir}/translations/alsa_sound_de.qm
%lang(fr) %{_modules_data_dir}/translations/alsa_sound_fr.qm
%lang(it) %{_modules_data_dir}/translations/alsa_sound_it.qm
%lang(pl) %{_modules_data_dir}/translations/alsa_sound_pl.qm
%endif

%if %{with sound_ao}
%files module-sound-ao
%defattr(644,root,root,755)
%{_modules_data_dir}/ao_sound.desc
%attr(755,root,root) %{_modules_lib_dir}/ao_sound.so
%endif

%if %{with sound_arts}
%files module-sound-arts
%defattr(644,root,root,755)
%{_modules_data_dir}/arts_sound.desc
%attr(755,root,root) %{_modules_lib_dir}/arts_sound.so
%dir %{_modules_bin_dir}/arts_sound
%attr(755,root,root) %{_modules_bin_dir}/arts_sound/arts_connector
%endif

%if %{with sound_dsp}
%files module-sound-dsp
%defattr(644,root,root,755)
%{_modules_data_dir}/dsp_sound.desc
%{_modules_data_dir}/configuration/dsp_sound.ui
%attr(755,root,root) %{_modules_lib_dir}/dsp_sound.so
%lang(de) %{_modules_data_dir}/translations/dsp_sound_de.qm
%lang(fr) %{_modules_data_dir}/translations/dsp_sound_fr.qm
%lang(it) %{_modules_data_dir}/translations/dsp_sound_it.qm
%lang(pl) %{_modules_data_dir}/translations/dsp_sound_pl.qm
%endif

%if %{with sound_esd}
%files module-sound-esd
%defattr(644,root,root,755)
%{_modules_data_dir}/esd_sound.desc
%attr(755,root,root) %{_modules_lib_dir}/esd_sound.so
%endif

%if %{with sound_ext}
%files module-sound-ext
%defattr(644,root,root,755)
%{_modules_data_dir}/ext_sound.desc
%{_modules_data_dir}/configuration/ext_sound.ui
%attr(755,root,root) %{_modules_lib_dir}/ext_sound.so
%lang(de) %{_modules_data_dir}/translations/ext_sound_de.qm
%lang(fr) %{_modules_data_dir}/translations/ext_sound_fr.qm
%lang(it) %{_modules_data_dir}/translations/ext_sound_it.qm
%lang(pl) %{_modules_data_dir}/translations/ext_sound_pl.qm
%endif

%if %{with sound_nas}
%files module-sound-nas
%defattr(644,root,root,755)
%{_modules_data_dir}/nas_sound.desc
%attr(755,root,root) %{_modules_lib_dir}/nas_sound.so
%endif

%if %{with spellchecker}
%files module-spellchecker
%defattr(644,root,root,755)
%{_modules_data_dir}/spellchecker.desc
%{_modules_data_dir}/configuration/spellchecker.ui
%attr(755,root,root) %{_modules_lib_dir}/spellchecker.so
%lang(pl) %{_modules_data_dir}/translations/spellchecker_pl.qm
%dir %{_modules_data_dir}/data/spellchecker
%{_modules_data_dir}/data/spellchecker/config.png
%endif

%if %{with tabs}
%files module-tabs
%defattr(644,root,root,755)
%{_modules_data_dir}/tabs.desc
%{_modules_data_dir}/configuration/tabs.ui
%attr(755,root,root) %{_modules_lib_dir}/tabs.so
%lang(pl) %{_modules_data_dir}/translations/tabs_pl.qm
%endif

%if %{with voice}
%files module-voice
%defattr(644,root,root,755)
%{_modules_data_dir}/voice.desc
%{_modules_data_dir}/configuration/voice.ui
%attr(755,root,root) %{_modules_lib_dir}/voice.so
%lang(de) %{_modules_data_dir}/translations/voice_de.qm
%lang(fr) %{_modules_data_dir}/translations/voice_fr.qm
%lang(it) %{_modules_data_dir}/translations/voice_it.qm
%lang(pl) %{_modules_data_dir}/translations/voice_pl.qm
%endif

%if %{with weather}
%files module-weather
%defattr(644,root,root,755)
%{_modules_data_dir}/weather.desc
%{_modules_data_dir}/configuration/weather.ui
%attr(755,root,root) %{_modules_lib_dir}/weather.so
%lang(pl) %{_modules_data_dir}/translations/weather_pl.qm
%dir %{_modules_data_dir}/data/weather
%{_modules_data_dir}/data/weather/*.ini
%dir %{_modules_data_dir}/data/weather/icons
%{_modules_data_dir}/data/weather/icons/*.gif
%endif

%files theme-icons-glass16
%defattr(644,root,root,755)
%{_datadir}/%{name}/themes/icons/glass16

%files theme-icons-glass22
%defattr(644,root,root,755)
%{_datadir}/%{name}/themes/icons/glass22

%files theme-icons-oxygen16
%defattr(644,root,root,755)
%{_datadir}/%{name}/themes/icons/oxygen16

%files theme-icons-tango16
%defattr(644,root,root,755)
%{_datadir}/%{name}/themes/icons/tango16
