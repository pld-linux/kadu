#
# TODO:
# - modules update/remove: desc_history, geoip, mail, mediaplayer_amarok2, notify_kde, notify_mx610,
#   notify_water, pajacyk, plus_pl_sms
# - make voice module link with system libgsm
#
# Conditional build:
%bcond_without	anonymous_check		# without anonymous_check module support
%bcond_without	antistring		# without antistring module support
%bcond_without	auto_hide		# without auto_hide module support
%bcond_without	autoaway		# without autoaway module support
%bcond_without	autoresponder		# without autoresponder module support
%bcond_without	autostatus		# without autostatus module support
%bcond_without	cenzor			# without cenzor module support
%bcond_with	desc_history		# without description history module support
%bcond_without	docking_desktop		# without desktop_docking module support
%bcond_without	encryption		# without encryption module support
%bcond_without	filedesc		# without filedesc module support
%bcond_without	firewall		# without firewall module support
%bcond_with	geoip			# without geoip module support
%bcond_without	globalhotkeys		# without globalhotkeys module support
%bcond_without	last_seen		# without last_seen module support
%bcond_with	mail			# without mail module support
%bcond_without	mediaplayer		# without media player modules support
%bcond_with	mediaplayer_amarok	# without amarok player support module
%bcond_with	mediaplayer_amarok2	# without amarok2 player support module
%bcond_without	mediaplayer_falf	# without falf player support module
%bcond_with	mediaplayer_mpd		# without mpd player support module
%bcond_without	mediaplayer_mpris	# without generic mpris interface support module
%bcond_without	messagessplitter	# without messagessplitter module support
%bcond_without	mime_tex		# without mime_tex module support
%bcond_without	nextinfo		# without nextinfo module support
%bcond_without	notify_exec		# without exec_notify module support
%bcond_without	notify_freedesktop	# without freedesktop_notify module support
%bcond_with	notify_kde		# without kde_notify module support
%bcond_without	notify_led		# without led_notify module support
%bcond_with	notify_mx610		# without mc610_notify module support
%bcond_without	notify_chat	        # without chat_notify module support
%bcond_without	notify_pcspeaker	# without pcspeaker_notify module support
%bcond_without	notify_qt4_docking	# without qt4_docking_notify module support
%bcond_without	notify_speech		# without Speech synthesis support
%bcond_with	notify_water		# without water_notify module support
%bcond_with	pajacyk			# without pajacyk module support
%bcond_without	panelkadu		# without panelkadu module support
%bcond_with	powerkadu		# without PowerKadu extensions
%bcond_without	screenshot		# without screenshot module support
%bcond_without	senthistory		# without senthistory module support
%bcond_without	single_window		# without single_window module support
%bcond_with	sms_plus_pl		# without plus_pl_sms module support
%bcond_without	sound_ext		# without external application sound module support
%bcond_without	sound_phonon		# without phonon sound module support
%bcond_without	sound_qt4		# without qt4 sound module support
%bcond_without	spellchecker		# without spellchecker (enchant support) invisible
%bcond_without	tabs			# without tabs support module
%bcond_with	voice			# without voice support module
%bcond_with	weather			# without weather check module support
%bcond_without	word_fix		# without word_fix module support

%define		libgadu_ver		4:1.11.0
%define		qt_ver			4.7.0

%define		anonymous_check_ver	0.10.1
%define		dcopexport_ver		0.11.3-20071129
%define		desc_history_ver	1.1
%define		geoip_ver		0.2
%define		globalhotkeys_ver	0.10-25
%define		mail_ver		0.3.6
%define		messagessplitter_ver	0.10-2
%define		mime_tex_ver		0.10.1
%define		nextinfo_ver		0.10-6
%define		notify_kde_ver		0.3.4
%define		notify_led_ver		0.10-29
%define		notify_mx610_ver	0.4.1
%define		notify_water_ver	0.2.1
%define		pajacyk_ver		0.2.1
%define		panelkadu_ver		0.10-8
%define		senthistory_ver		0.10-9
%define		sms_plus_pl_ver		0.6.5.4-1

Summary:	A Gadu-Gadu client for online messaging
Summary(pl.UTF-8):	Klient Gadu-Gadu do przesyłania wiadomości po sieci
Name:		kadu
Version:	0.10.0
Release:	0.1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://download.kadu.im/stable/%{name}-%{version}.tar.bz2
# Source0-md5:	6d3e9889f53cf10c2cd9499aabbff67a
Source1:	%{name}.desktop
Source2:	http://kadu.net/~weagle/anonymous_check-%{anonymous_check_ver}.tar.bz2
# Source2-md5:	2dc4f69cf71d5ed9c7a94e5ff1719c5b
Source3:	dcopexport-%{dcopexport_ver}-0.6.0.tar.bz2
# Source3-md5:	b36fcfcf4756285f30cbb6c2b6c2a2da
Source4:	http://www.ultr.pl/kadu/globalhotkeys-%{globalhotkeys_ver}.tar.gz
# Source4-md5:	b7eecb5a889cbb59b0c146357f689630
Source5:	http://kadu.net/~michal/mail/mail-%{mail_ver}.tar.bz2
# Source5-md5:	85fdf695c7fbc58e607dc15278391ab3
Source6:	http://kadu.net/~weagle/mime_tex-%{mime_tex_ver}.tar.bz2
# Source6-md5:	aa5a34784f4044c425fcc1b11f0ede3f
Source7:	http://www.ultr.pl/kadu/nextinfo-%{nextinfo_ver}.tar.gz
# Source7-md5:	b7645a7ce571dc3549249863bf783020
Source8:	http://www.ultr.pl/kadu/lednotify-%{notify_led_ver}.tar.gz
# Source8-md5:	e6f54571976c422d07154a66482fd343
Source9:	http://www.kadu.net/~dorr/moduly/%{name}-mx610_notify-%{notify_mx610_ver}.tar.bz2
# Source9-md5:	4b2a47068928b9687c61816abeed86fe
Source10:	http://www.kadu.net/~dorr/moduly/%{name}-water_notify-%{notify_water_ver}.tar.bz2
# Source10-md5:	4196e85fc4be93bd662f5148ebc18235
Source11:	http://www.ultr.pl/kadu/panelkadu-%{panelkadu_ver}.tar.gz
# Source11-md5:	26772365e6aa794bc6e8155a60c9d01d
Source12:	http://www.ultr.pl/kadu/senthistory-%{senthistory_ver}.tar.gz
# Source12-md5:	0ec2a68a636f2428be1f20967fa23baf
Source13:	http://kadu.net/~patryk/plus_pl_sms/plus_pl_sms-plus_pl_sms-%{sms_plus_pl_ver}.tar.bz2
# Source13-md5:	59f7ba01a63464818acaa5ff6fd176d5
Source14:	http://kadu.net/~neeo/kadu/geoip/geoip_lookup-%{geoip_ver}.tar.bz2
# Source14-md5:	83d9672c7f88b803510e7757dd36ea92
Source15:	http://www.kadu.net/download/additions/%{name}-0.6.5.4-theme-glass-16.tar.gz
# Source15-md5:	25374d4b876037de6d00eedca76eae0f
Source16:	http://www.kadu.net/download/additions/%{name}-0.6.5.4-theme-glass-22.tar.gz
# Source16-md5:	d9df73a452cf190abd5605112c53c21f
Source17:	http://www.kadu.net/download/additions/%{name}-0.6.5.4-theme-oxygen-16.tar.gz
# Source17-md5:	1dd08c856ec86f55dccf88ab19be6f5a
Source18:	http://www.kadu.net/download/additions/%{name}-0.6.5.4-theme-tango-16.tar.gz
# Source18-md5:	9710fd37c6fd8c24e2bae8fa377ee465
Source19:	http://www.kadu.net/download/additions/%{name}-0.6.5-theme-kadu05.tar.gz
# Source19-md5:	9174f621138b6fc28127cc4396cb59ed
Source20:	desc_history-%{desc_history_ver}.tar.bz2
# Source20-md5:	cf7d7c8f86d9cfe4b5a0ab52b5deff34
Source21:	http://www.kadu.net/~dorr/moduly/kde_notify-%{notify_kde_ver}.tar.gz
# Source21-md5:	2da919d6359049a6e4827e795ba46b1a
Source22:	http://www.kadu.net/download/additions/%{name}-0.6.5.4-emots-tango.tar.gz
# Source22-md5:	436f12011f209c4427a9e411091ecb0a
Source23:	http://www.kadu.net/~dorr/moduly/%{name}-pajacyk-%{pajacyk_ver}.tar.bz2
# Source23-md5:	c87d4b68d65c923118b6ac3e9396ff13
Source24:	http://www.kadu.net/download/additions/%{name}-sound-bns.tar.bz2
# Source24-md5:	fcf829d687df27d2ac296a077dc2814e
Source25:	http://www.kadu.net/download/additions/%{name}-sound-drums.tar.bz2
# Source25-md5:	0f29ac64019d841b38eefadad2a49e4f
Source26:	http://www.kadu.net/download/additions/%{name}-sound-florkus.tar.bz2
# Source26-md5:	d90070390134c2809a2b53df07563712
Source27:	http://www.kadu.net/download/additions/%{name}-sound-michalsrodek.tar.bz2
# Source27-md5:	5951d828833ea0e452654dbc80c02787
Source28:	http://www.kadu.net/download/additions/%{name}-sound-percussion.tar.bz2
# Source28-md5:	124175025038cd1fedb3d0caa3a0d478
Source29:	http://www.kadu.net/download/additions/%{name}-sound-ultr.tar.bz2
# Source29-md5:	1caec2ba480a2f47430d12ec681aa871
Source30:	http://www.ultr.pl/kadu/messagessplitter-%{messagessplitter_ver}.tar.gz
# Source30-md5:	14de43361e3bc149478a076874e024f2
Patch0:		%{name}-sounds.patch
Patch1:		%{name}-mail.patch
Patch2:		%{name}-link.patch
URL:		http://kadu.im/
%{?with_geoip:BuildRequires:	GeoIP-devel}
BuildRequires:	Qt3Support-devel >= %{qt_ver}
BuildRequires:	QtScript-devel >= %{qt_ver}
BuildRequires:	QtScriptTools-devel >= %{qt_ver}
BuildRequires:	QtSvg-devel >= %{qt_ver}
BuildRequires:	QtWebKit-devel >= %{qt_ver}
BuildRequires:	QtXmlPatterns-devel >= %{qt_ver}
BuildRequires:	cmake >= 2.8.0
%{?with_sms_plus_pl:BuildRequires:	curl-devel}
%{?with_notify_water:BuildRequires:	dbus-devel}
%{?with_spellchecker:BuildRequires:	enchant-devel}
%{?with_sound_ao:BuildRequires:	libao-devel}
BuildRequires:	libgadu-devel >= %{libgadu_ver}
%{?with_voice:BuildRequires:	libgsm-devel}
BuildRequires:	libsndfile-devel >= 1.0
BuildRequires:	libstdc++-devel
%{?with_encryption:BuildRequires:	openssl-devel >= 0.9.7d}
BuildRequires:	pkgconfig
%{?with_encryption:BuildRequires:	qca-devel}
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-linguist >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	sed >= 4.0
%{?with_desc_history:BuildRequires:     sqlite3-devel}
BuildRequires:	xorg-lib-libXScrnSaver-devel
%{?with_panelkadu:BuildRequires:	xorg-lib-libXtst-devel}
Requires:	QtSql-sqlite3 >= %{qt_ver}
Requires:	libgadu >= %{libgadu_ver}
Obsoletes:	kadu-module-advanced_userlist
Obsoletes:	kadu-module-agent
Obsoletes:	kadu-module-dbus
Obsoletes:	kadu-module-docking-wmaker <= 0.6.5
Obsoletes:	kadu-module-filtering
Obsoletes:	kadu-module-gg_avatars
Obsoletes:	kadu-module-imiface <= 0.4.3
Obsoletes:	kadu-module-iwait4u <= 0.5.0
Obsoletes:	kadu-module-mediaplayer-audacious
Obsoletes:	kadu-module-mediaplayer-bmpx
Obsoletes:	kadu-module-mediaplayer-dragon
Obsoletes:	kadu-module-mediaplayer-vlc
Obsoletes:	kadu-module-mediaplayer-xmms
Obsoletes:	kadu-module-mediaplayer-xmms2
%{!?with_mediaplayer:Obsoletes:	kadu-module-mediaplayer}
Obsoletes:	kadu-module-notify-osdhints
Obsoletes:	kadu-module-notify-window
Obsoletes:	kadu-module-notify-xosd <= 0.6.5
Obsoletes:	kadu-module-parser_extender
Obsoletes:	kadu-module-profiles
Obsoletes:	kadu-module-sound-alsa
Obsoletes:	kadu-module-sound-ao
Obsoletes:	kadu-module-sound-arts <= 0.6.5
Obsoletes:	kadu-module-sound-dsp
Obsoletes:	kadu-module-sound-esd <= 0.6.5
%{!?with_speech:Obsoletes:	kadu-module-speech <= 0.4.3}
Obsoletes:	kadu-module-tcl_scripting <= 0.4.3
Obsoletes:	kadu-theme-icons-crystal16
Obsoletes:	kadu-theme-icons-crystal22
Obsoletes:	kadu-theme-icons-nuvola16
Obsoletes:	kadu-theme-icons-nuvola22
# for encryption module and TLS in jabber module
Suggests:	qt4-plugin-qca-ossl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		modules_lib_dir		%{_libdir}/%{name}/plugins
%define		modules_data_dir	%{_datadir}/%{name}/plugins
%define		modules_bin_dir		%{modules_lib_dir}/bin

%description
Kadu is client of Gadu-Gadu protocol. It's an IM for Linux and UN*X.
It's written with use of Qt.

%description -l pl.UTF-8
Kadu jest klientem protokołu Gadu-Gadu. Inaczej mówiąc, jest
komunikatorem dla Linuksa (oraz, przy niewielkim wysiłku, innych
systemów uniksowych). Napisano go w oparciu o bibliotekę Qt.

%package module-autoresponder
Summary:	Autoresponder module
Summary(pl.UTF-8):	Moduł autoodpowiedzi
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-autoresponder
Autoresponder module.

%description module-autoresponder -l pl.UTF-8
Moduł autoodpowiedzi.

%package module-autostatus
Summary:	Automatic status change module
Summary(pl.UTF-8):	Moduł automatycznych zmian statusu
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-autostatus
Automatic status change module.

%description module-autostatus -l pl.UTF-8
Moduł automatycznych zmian statusu.

%package module-anonymous_check
Summary:	Automatic lookup of an interlocutor in public directory
Summary(pl.UTF-8):	Automatyczne wyszukiwanie nieznajomych rozmówców w katalogu publicznym
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-anonymous_check
Automatic lookup of an interlocutor in public directory.

%description module-anonymous_check -l pl.UTF-8
Automatyczne wyszukiwanie nieznajomych rozmówców w katalogu
publicznym.

%package module-antistring
Summary:	Antistring module
Summary(pl.UTF-8):	Moduł chroniący przed łańcuszkami
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-antistring
Antistring module.

%description module-antistring -l pl.UTF-8
Moduł chroniący przed łańcuszkami.

%package module-autoaway
Summary:	Auto away module
Summary(pl.UTF-8):	Moduł automatycznej zajętości
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-autoaway
Auto away module.

%description module-autoaway -l pl.UTF-8
Moduł automatycznej zajętości.

%package module-auto_hide
Summary:	Auto hide Kadu window
Summary(pl.UTF-8):	Automatyczne ukrywanie okna Kadu
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-auto_hide
Auto hide Kadu window.

%description module-auto_hide -l pl.UTF-8
Automatyczne ukrywanie okna Kadu.

%package module-cenzor
Summary:	Censor module
Summary(pl.UTF-8):	Moduł cenzora
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-cenzor
Censor module.

%description module-cenzor -l pl.UTF-8
Moduł cenzora.

%package module-desc_history
Summary:	Status descriptions history
Summary(pl.UTF-8):	Historia opisów statusów
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-desc_history
Status descriptions history.

%description module-desc_history -l pl.UTF-8
Historia opisów statusów.

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

%package module-firewall
Summary:	Module to block unknown persons, who wants to start chat
Summary(pl.UTF-8):	Moduł blokuje nieznane osoby, chcące zacząć rozmowę
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-firewall
Module to block unknown persons, who wants to start chat.

%description module-firewall -l pl.UTF-8
Moduł blokuje nieznane osoby, chcące zacząć rozmowę.

%package module-geoip
Summary:	Geoip module
Summary(pl.UTF-8):	Moduł geoip
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-geoip
Geoip module.

%description module-geoip -l pl.UTF-8
Moduł geoip.

%package module-globalhotkeys
Summary:	Adds global hotkeys support to Kadu
Summary(pl.UTF-8):	Moduł dodający do Kadu obsługę skrótów globalnych
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-globalhotkeys
Adds global hotkeys support to Kadu.

%description module-globalhotkeys -l pl.UTF-8
Moduł dodający do Kadu obsługę skrótów globalnych.

%package module-last_seen
Summary:	Last seen
Summary(pl.UTF-8):	Ostatnio widziani
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-last_seen
Last seen.

%description module-last_seen -l pl.UTF-8
Ostatnio widziani.

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
Moduł umożliwiający pokazywanie w opisie statusu informacji o
odgrywanym utworze.

%package module-mediaplayer-amarok
Summary:	Support amarok status
Summary(pl.UTF-8):	Moduł statusu dla odtwarzacza amarok
Group:		Applications/Communications
Requires:	%{name}-module-mediaplayer = %{version}-%{release}
Requires:	amarok < 2.0.0
Provides:	kadu-module-amarok = %{version}
Obsoletes:	kadu-module-amarok <= 0.5.0

%description module-mediaplayer-amarok
Module which allows showing in status description information about
the song currently played in amarok.

%description module-mediaplayer-amarok -l pl.UTF-8
Moduł umożliwiający w opisie statusu pokazywanie informacji o
odgrywanym utworze z odtwarzacza amarok.

%package module-mediaplayer-amarok2
Summary:	Support amarok 2 status
Summary(pl.UTF-8):	Moduł statusu dla odtwarzacza amarok 2
Group:		Applications/Communications
Requires:	%{name}-module-mediaplayer-mpris = %{version}-%{release}
Requires:	amarok > 2.0.0
Provides:	kadu-module-amarok2 = %{version}

%description module-mediaplayer-amarok2
Module which allows showing in status description information about
the song currently played in amarok 2.

%description module-mediaplayer-amarok2 -l pl.UTF-8
Moduł umożliwiający w opisie statusu pokazywanie informacji o
odgrywanym utworze z odtwarzacza amarok 2.

%package module-mediaplayer-falf
Summary:	Support falf status
Summary(pl.UTF-8):	Moduł statusu dla falf
Group:		Applications/Communications
Requires:	%{name}-module-mediaplayer = %{version}-%{release}
Requires:	falf

%description module-mediaplayer-falf
Module which allows showing in status description information about
the song currently played in falf.

%description module-mediaplayer-falf -l pl.UTF-8
Moduł umożliwiający w opisie statusu pokazywanie informacji o
odgrywanym utworze z odtwarzacza falf.

%package module-mediaplayer-mpris
Summary:	Generic mpris interface support
Summary(pl.UTF-8):	Moduł ogólnego interfejsu do mpris
Group:		Applications/Communications
Requires:	%{name}-module-mediaplayer = %{version}-%{release}

%description module-mediaplayer-mpris
Module which allows showing in status description information about
the song currently played in mpris compatible player. It is used by
other modules.

%description module-mediaplayer-mpris -l pl.UTF-8
Moduł umożliwiający w opisie statusu pokazywanie informacji o
odgrywanym utworze z odtwarzacza zgodnego z mpris. Jest wykorzystywany
przez inne moduły.

%package module-messagessplitter
Summary:	Automaticaly split too long messages in Kadu
Summary(pl.UTF-8):	Automatyczne dzielenie zbyt długich wiadomości w Kadu
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Provides:	kadu-module-split_messages
Obsoletes:	kadu-module-split_messages

%description module-messagessplitter
Automaticaly split too long messages in Kadu.

%description module-messagessplitter -l pl.UTF-8
Automatyczne dzielenie zbyt długich wiadomości w Kadu.

%package module-mime_tex
Summary:	Mathematical TeX formulas in chat windows
Summary(pl.UTF-8):	Matematyczne formuły TeX w oknach czat
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-mime_tex
Mathematical TeX formulas for chat windows.

%description module-mime_tex -l pl.UTF-8
Matematyczne formuły TeX w oknach czat.

%package module-nextinfo
Summary:	Extended contact informations
Summary(pl.UTF-8):	Rozszerzone informacje o kontakcie
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-nextinfo
Extended contact information.

%description module-nextinfo -l pl.UTF-8
Rozszerzone informacje o kontakcie.

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

%package module-notify-freedesktop
Summary:	Freedesktop notification support
Summary(pl.UTF-8):	Wsparcie dla powiadamiania freedesktop
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-notify-freedesktop
Freedesktop notification support

%description module-notify-freedesktop -l pl.UTF-8
Wsparcie dla powiadamiania freedesktop

%package module-notify-kde4
Summary:	Notification for KDE4
Summary(pl.UTF-8):	Moduł powiadamiania dla KDE4
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-notify-kde4
Notification for KDE4.

%description module-notify-kde4 -l pl.UTF-8
Moduł powiadamiania dla KDE4.

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

%package module-notify-chat
Summary:	Notifications in chat windows
Summary(pl.UTF-8):	Powiadomienia w oknach rozmowy
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-notify-chat
Notifications about buddies presence and other in chat windows.

%description module-notify-chat -l pl.UTF-8
Powiadomienia o aktywności znajomych i innych zdarzeniach w oknach
rozmowy.

%package module-notify-pcspeaker
Summary:	Notification by PC Speaker
Summary(pl.UTF-8):	Powiadamianie o zdarzeniach przy pomocy PC Speakera
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-notify-pcspeaker
Notification by PC Speaker.

%description module-notify-pcspeaker -l pl.UTF-8
Powiadamianie o zdarzeniach przy pomocy PC Speakera.

%package module-notify-qt4_docking
Summary:	Notification by qt4_docking
Summary(pl.UTF-8):	Powiadamianie o zdarzeniach przy pomocy qt4_docking
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-notify-qt4_docking
Notification by qt4_docking.

%description module-notify-qt4_docking -l pl.UTF-8
Powiadamianie o zdarzeniach przy pomocy modulu qt4_docking.

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
Summary(pl.UTF-8):	Moduł powiadamiania wtyczką Water w Compizie
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-notify-water
Notification by Water Plugin in Compiz.

%description module-notify-water -l pl.UTF-8
Moduł powiadamiania wtyczką Water w Compizie.

%package module-pajacyk
Summary:	Pajacyk - feed polish childrens
Summary(pl.UTF-8):	Pajacyk - nakarm polskie dzieci
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-pajacyk
Click on Puppet and feed polish children.

%description module-pajacyk -l pl.UTF-8
Kliknij w Pajacyka i nakarm polskie dzieci.

%package module-panelkadu
Summary:	Module which makes Kadu look and behave like a panel
Summary(pl.UTF-8):	Moduł sprawiający, że Kadu wygląda i zachowuje się jak panel
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-panelkadu
Module which makes Kadu look and behave like a panel.

%description module-panelkadu -l pl.UTF-8
Moduł sprawiający, że Kadu wygląda i zachowuje się jak panel.

%package module-powerkadu
Summary:	PowerKadu extensions
Summary(pl.UTF-8):	Rozszerzenia PowerKadu
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-module-anonymous_check = %{version}-%{release}
Requires:	%{name}-module-antistring = %{version}-%{release}
Requires:	%{name}-module-auto_hide = %{version}-%{release}
Requires:	%{name}-module-autostatus = %{version}-%{release}
Requires:	%{name}-module-cenzor = %{version}-%{release}
Requires:	%{name}-module-messagessplitter = %{version}-%{release}
Requires:	%{name}-module-word_fix = %{version}-%{release}

%description module-powerkadu
PowerKadu is an add-on to Kadu. It extends Kadu functionality by
useful functions, like: autostatus, antistring, cenzor, words fix...

%description module-powerkadu -l pl.UTF-8
PowerKadu jest dodatkiem do Kadu. Poszerza on możliwości Kadu o
przydatne funkcje, takie jak: autostatus, antyłańcuszek, cenzor,
korekta słów...

%package module-senthistory
Summary:	Kadu module which adds history of sent messages to chat windows
Summary(pl.UTF-8):	Moduł kadu który dodaje historię wysłanych wiadomości do okien rozmowy
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-senthistory
Kadu module which adds history of sent messages to chat windows.

%description module-senthistory -l pl.UTF-8
Moduł kadu który dodaje historię wysłanych wiadomości do okien
rozmowy.

%package module-screenshot
Summary:	Simple ScreenShots module
Summary(pl.UTF-8):	Moduł prostych zrzutów ekranu
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-screenshot
Simple ScreenShots module.

%description module-screenshot -l pl.UTF-8
Moduł prostych zrzutów ekranu.

%package module-sms-plus_pl
Summary:	SMS Plus.pl module
Summary(pl.UTF-8):	Moduł obsługi bramki SMS w Plus.pl
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Provides:	kadu-module-sms-miastoplusa = %{name}
Obsoletes:	kadu-module-sms-miastoplusa <= 0.6.5

%description module-sms-plus_pl
SMS Gateway on Plus.pl module.

%description module-sms-plus_pl -l pl.UTF-8
Moduł obsługi bramki SMS Plus.pl.

%package module-sound-ext
Summary:	External application sound module
Summary(pl.UTF-8):	Moduł obsługi dźwięku przez zewnętrzną aplikację
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-sound-ext
External application sound module.

%description module-sound-ext -l pl.UTF-8
Moduł obsługi dźwięku przez zewnętrzną aplikację.

%package module-sound-phonon
Summary:	Phonon sound module
Summary(pl.UTF-8):	Moduł obsługi dźwięku przez phonon
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-sound-phonon
Phonon sound module.

%description module-sound-phonon -l pl.UTF-8
Moduł obsługi dźwięku przez phonon.

%package module-sound-qt4
Summary:	Qt4 sound module
Summary(pl.UTF-8):	Moduł obsługi dźwięku przez qt4
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-sound-qt4
Qt4 sound module.

%description module-sound-qt4 -l pl.UTF-8
Moduł obsługi dźwięku przez qt4.

%package module-spellchecker
Summary:	Checker of spelling mistakes
Summary(pl.UTF-8):	Moduł sprawdzający pisownię
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	enchant
Suggests:	enchant-aspell

%description module-spellchecker
Checker of spelling mistakes.

%description module-spellchecker -l pl.UTF-8
Moduł sprawdzający pisownię.

%package module-single_window
Summary:	Joins contacts and chats in one window
Summary(pl.UTF-8):	Łączy listę kontaktów i rozmowy w jednym oknie
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-single_window
Joins contacts and chats in one window. This module is especialy for
small devices in mind.

%description module-single_window -l pl.UTF-8
Łączy listę kontaktów i rozmowy w jednym oknie. Moduł przygotowany z
myślą o małych urządzeniach.

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

%package module-word_fix
Summary:	Automatic word replacement module for Kadu
Summary(pl.UTF-8):	Moduł automatycznej zamiany słów dla Kadu
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description module-word_fix
Automatic word replacement module for Kadu.

%description module-word_fix -l pl.UTF-8
Moduł automatycznej zamiany słów dla Kadu.

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

%package theme-icons-kadu05
Summary:	Kadu05 icon theme
Summary(pl.UTF-8):	Zestaw ikon Kadu05
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description theme-icons-kadu05
Kadu05 icon theme.

%description theme-icons-kadu05 -l pl.UTF-8
Zestaw ikon Kadu05.

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

%package theme-emoticons-tango
Summary:	Tango emoticons theme
Summary(pl.UTF-8):	Zestaw emotikon Tango
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description theme-emoticons-tango
Tango emoticons theme.

%description theme-emoticons-tango -l pl.UTF-8
Zestaw emotikon Tango.

%package theme-sounds
Summary:	Sounds themes
Summary(pl.UTF-8):	Zestaw dźwięków
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description theme-sounds
Additional sounds theme.

%description theme-sounds -l pl.UTF-8
Zestaw dodatkowych dźwięków.

%prep
%setup -q -T -b 0

#% patch0 -p1
%if %{with anonymous_check}
tar xjf %{SOURCE2} -C plugins
%endif
%if %{with dcopexport}
tar xjf %{SOURCE3} -C plugins
%endif
%if %{with globalhotkeys}
tar xzf %{SOURCE4} -C plugins
%endif
%if %{with mail}
tar xjf %{SOURCE5} -C plugins
%undos plugins/mail/translations/mail_pl.ts
%patch1 -p0
%endif
%if %{with mime_tex}
tar xjf %{SOURCE6} -C plugins
%endif
%if %{with nextinfo}
tar xzf %{SOURCE7} -C plugins
%endif
%if %{with notify_led}
tar xzf %{SOURCE8} -C plugins
%endif
%if %{with notify_mx610}
tar xjf %{SOURCE9} -C plugins
%endif
%if %{with notify_water}
tar xjf %{SOURCE10} -C plugins
%endif
%if %{with panelkadu}
tar xzf %{SOURCE11} -C plugins
%endif
%if %{with senthistory}
tar xzf %{SOURCE12} -C plugins
%endif
%if %{with sms_plus_pl}
tar xjf %{SOURCE13} -C plugins
%endif
%if %{with geoip}
tar xjf %{SOURCE14} -C plugins
%endif
%if %{with desc_history}
tar xjf %{SOURCE20} -C plugins
%endif
%if %{with notify_kde}
#tar xzf %{SOURCE21} -C plugins
%endif
%if %{with pajacyk}
tar xjf %{SOURCE23} -C plugins
%endif
%if %{with messagessplitter}
tar xzf %{SOURCE30} -C plugins
%endif

# themes-icons
tar xzf %{SOURCE15} -C varia/themes/icons
tar xzf %{SOURCE16} -C varia/themes/icons
tar xzf %{SOURCE17} -C varia/themes/icons
tar xzf %{SOURCE18} -C varia/themes/icons
tar xzf %{SOURCE19} -C varia/themes/icons

# themes-emoticons
tar xzf %{SOURCE22} -C varia/themes/emoticons

# themes-sounds
tar xjf %{SOURCE24} -C varia/themes/sounds
tar xjf %{SOURCE25} -C varia/themes/sounds
tar xjf %{SOURCE26} -C varia/themes/sounds
tar xjf %{SOURCE27} -C varia/themes/sounds
tar xjf %{SOURCE28} -C varia/themes/sounds
tar xjf %{SOURCE29} -C varia/themes/sounds

# Change hard coded path to modules data files
%{__sed} -i 's,dataPath("kadu/plugins/*,("%{modules_data_dir}/,g' kadu-core/plugins/plugin.cpp

echo "module_desc_history=n" >>.config
%{__sed} -i 's/module_qt4_docking=y/module_qt4_docking=m/' .config

#% patch2 -p1

%build
mkdir -p build

%{?with_anonymous_check:%{__sed} -i '/^set (COMPILE_PLUGINS$/a\\tanonymous_check' Plugins.cmake}
%{!?with_antistring:%{__sed} -i 's/\tantistring$/\t#antistring/' Plugins.cmake}
%{!?with_autoaway:%{__sed} -i 's/\tautoaway$/\t#autoaway/' Plugins.cmake}
%{!?with_auto_hide:%{__sed} -i 's/\tauto_hide$/\t#auto_hide/' Plugins.cmake}
%{!?with_autoresponder:%{__sed} -i 's/\tautoresponder$/\t#autoresponder/' Plugins.cmake}
%{!?with_autostatus:%{__sed} -i 's/\tautostatus$/\t#autostatus/' Plugins.cmake}
%{!?with_cenzor:%{__sed} -i 's/\tcenzor$/\t#cenzor/' Plugins.cmake}
%if %{with desc_history}
%{__sed} -i 's/module_desc_history=n/module_desc_history=m/' .config
%else
%{__sed} -i 's/module_desc_history=m/module_desc_history=n/' .config
%endif
%{!?with_docking_desktop:%{__sed} -i 's/\tdesktop_docking$/\t#desktop_docking/' Plugins.cmake}
%if %{without encryption}
%{__sed} -i 's/\tencryption_ng$/\t#encryption_ng/' Plugins.cmake
%{__sed} -i 's/\tencryption_ng_simlite$/\t#encryption_ng_simlite/' Plugins.cmake
%endif
%{!?with_filedesc:%{__sed} -i 's/\tfiledesc$/\t#filedesc/' Plugins.cmake}
%{!?with_firewall:%{__sed} -i 's/\tfirewall$/\t#firewall/' Plugins.cmake}
%if %{with geoip}
%{__sed} -i 's/module_geoip_lookup=n/module_geoip_lookup=m/' .config
%else
%{__sed} -i 's/module_geoip_lookup=m/module_geoip_lookup=n/' .config
%endif
%{?with_globalhotkeys:%{__sed} -i '/^set (COMPILE_PLUGINS$/a\\tglobalhotkeys' Plugins.cmake}
%{!?with_last_seen:%{__sed} -i 's/\tlast_seen$/\t#last_seen/' Plugins.cmake}
%if %{with mail}
%{__sed} -i 's/module_mail=n/module_mail=m/' .config
%else
%{__sed} -i 's/module_mail=m/module_mail=n/' .config
%endif
%{!?with_mediaplayer:%{__sed} -i 's/\tmediaplayer$/\t#mediaplayer/' Plugins.cmake}
%{!?with_mediaplayer_amarok:%{__sed} -i 's/\tamarok1_mediaplayer$/\t#amarok1_mediaplayer/' Plugins.cmake}
%if %{with mediaplayer_amarok2}
%{__sed} -i 's/module_amarok2_mediaplayer=n/module_amarok2_mediaplayer=m/' .config
echo 'MODULE_INCLUDES_PATH="%{_includedir}"' >> plugins/amarok2_mediaplayer/spec
echo 'MODULE_LIBS_PATH="%{_libdir}"' >> plugins/amarok2_mediaplayer/spec
%else
%{__sed} -i 's/module_amarok2_mediaplayer=m/module_amarok2_mediaplayer=n/' .config
%endif
%{!?with_mediaplayer_falf:%{__sed} -i 's/\tfalf_mediaplayer$/\t#falf_mediaplayer/' Plugins.cmake}
%{!?with_mediaplayer_mpris:%{__sed} -i 's/\tmprisplayer_mediaplayer$/\t#mprisplayer_mediaplayer/' Plugins.cmake}
%{?with_mime_tex:%{__sed} -i '/^set (COMPILE_PLUGINS$/a\\tmime_tex' Plugins.cmake}
%{?with_nextinfo:%{__sed} -i '/^set (COMPILE_PLUGINS$/a\\tnextinfo' Plugins.cmake}
%{!?with_notify_exec:%{__sed} -i 's/\texec_notify$/\t#exec_notify/' Plugins.cmake}
%{!?with_notify_freedesktop:%{__sed} -i 's/\tfreedesktop_notify$/\t#freedesktop_notify/' Plugins.cmake}
%if %{with notify_kde}
%{__sed} -i 's/module_kde_notify=n/module_kde_notify=m/' .config
%else
%{__sed} -i 's/module_kde_notify=m/module_kde_notify=n/' .config
%endif
%{?with_notify_led:%{__sed} -i '/^set (COMPILE_PLUGINS$/a\\tlednotify' Plugins.cmake}
%if %{with notify_mx610}
%{__sed} -i 's/module_mx610_notify=n/module_mx610_notify=m/' .config
%else
%{__sed} -i 's/module_mx610_notify=m/module_mx610_notify=n/' .config
%endif
%{!?with_notify_chat:%{__sed} -i 's/\tchat_notify$/\t#chat_notify/' Plugins.cmake}
%{!?with_notify_pcspeaker:%{__sed} -i 's/\tpcspeaker$/\t#pcspeaker/' Plugins.cmake}
%{!?with_notify_qt4_docking:%{__sed} -i 's/\tqt4_docking_notify$/\t#qt4_docking_notify/' Plugins.cmake}
%{!?with_notify_speech:%{__sed} -i 's/\tspeech$/\t#speech/' Plugins.cmake}
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
%if %{with pajacyk}
%{__sed} -i 's/module_pajacyk=n/module_pajacyk=m/' .config
%else
%{__sed} -i 's/module_pajacyk=m/module_pajacyk=n/' .config
%endif
%{?with_panelkadu:%{__sed} -i '/^set (COMPILE_PLUGINS$/a\\tpanelkadu' Plugins.cmake}
%if %{with powerkadu}
%{__sed} -i 's/module_powerkadu=n/module_powerkadu=m/' .config
%else
%{__sed} -i 's/module_powerkadu=m/module_powerkadu=n/' .config
%endif
%{!?with_screenshot:%{__sed} -i 's/\tscreenshot$/\t#screenshot/' Plugins.cmake}
%{?with_senthistory:%{__sed} -i '/^set (COMPILE_PLUGINS$/a\\tsenthistory' Plugins.cmake}
%{!?with_single_window:%{__sed} -i 's/\tsingle_window$/\t#single_window/' Plugins.cmake}
%if %{with sms_plus_pl}
%{__sed} -i 's/module_plus_pl_sms=n/module_plus_pl_sms=m/' .config
%else
%{__sed} -i 's/module_plus_pl_sms=m/module_plus_pl_sms=n/' .config
%endif
%{!?with_sound_ext:%{__sed} -i 's/\text_sound$/\t#ext_sound/' Plugins.cmake}
%{!?with_sound_phonon:%{__sed} -i 's/\tphonon_sound$/\t#phonon_sound/' Plugins.cmake}
%{!?with_sound_qt4:%{__sed} -i 's/\tqt4_sound$/\t#qt4_sound/' Plugins.cmake}
%{!?with_spellchecker:%{__sed} -i 's/\tspellchecker$/\t#spellchecker/' Plugins.cmake}
%{?with_messagessplitter:%{__sed} -i '/^set (COMPILE_PLUGINS$/a\\tmessagessplitter' Plugins.cmake}
%{!?with_tabs:%{__sed} -i 's/\ttabs$/\t#tabs/' Plugins.cmake}
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
%{!?with_word_fix:%{__sed} -i 's/\tword_fix$/\t#word_fix/' Plugins.cmake}

%{__sed} -i 's/icons_glass16=n/icons_glass16=y/' .config
%{__sed} -i 's/icons_glass22=n/icons_glass22=y/' .config
%{__sed} -i 's/icons_kadu05=n/icons_kadu05=y/' .config
%{__sed} -i 's/icons_oxygen16=n/icons_oxygen16=y/' .config
%{__sed} -i 's/icons_tango16=n/icons_tango16=y/' .config

%{__sed} -i 's/emoticons_tango=n/emoticons_tango=y/' .config

%{__sed} -i 's/sound_bns=n/sound_bns=y/' .config
%{__sed} -i 's/sound_drums=n/sound_drums=y/' .config
%{__sed} -i 's/sound_florkus=n/sound_florkus=y/' .config
%{__sed} -i 's/sound_michalsrodek=n/sound_michalsrodek=y/' .config
%{__sed} -i 's/sound_percussion=n/sound_percussion=y/' .config
%{__sed} -i 's/sound_ultr=n/sound_ultr=y/' .config

cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

# we don't need headers
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/%{name}

# docs are packaged in %%docs
%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/{AUTHORS,COPYING,ChangeLog*,HISTORY,README,THANKS}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog ChangeLog.OLD-PL HISTORY README THANKS
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%if 0
%{_pixmapsdir}/%{name}.png
%endif
%{_iconsdir}/*/*x*/apps/%{name}.png
%dir %{_datadir}/%{name}
%dir %{modules_data_dir}
%dir %{modules_data_dir}/data
%dir %{_datadir}/%{name}/themes
%dir %{_datadir}/%{name}/themes/emoticons
%{_datadir}/%{name}/themes/emoticons/penguins
%{_datadir}/%{name}/themes/emoticons/tango
%dir %{_datadir}/%{name}/themes/icons
%{_datadir}/%{name}/themes/icons/default
%{_datadir}/%{name}/themes/icons/glass
%{_datadir}/%{name}/themes/icons/oxygen
%dir %{_datadir}/%{name}/themes/sounds
%{_datadir}/%{name}/themes/sounds/default

# default modules:
%dir %{_libdir}/%{name}
%dir %{modules_lib_dir}
#%%dir %{modules_bin_dir}
%{modules_data_dir}/config_wizard.desc
%attr(755,root,root) %{modules_lib_dir}/libconfig_wizard.so
%{modules_data_dir}/docking.desc
%attr(755,root,root) %{modules_lib_dir}/libdocking.so
%{modules_data_dir}/gadu_protocol.desc
%attr(755,root,root) %{modules_lib_dir}/libgadu_protocol.so
%{modules_data_dir}/hints.desc
%attr(755,root,root) %{modules_lib_dir}/libhints.so
%{modules_data_dir}/history.desc
%attr(755,root,root) %{modules_lib_dir}/libhistory.so
%{modules_data_dir}/history_migration.desc
%attr(755,root,root) %{modules_lib_dir}/libhistory_migration.so
%{modules_data_dir}/idle.desc
%attr(755,root,root) %{modules_lib_dir}/libidle.so
%{modules_data_dir}/imagelink.desc
%attr(755,root,root) %{modules_lib_dir}/libimagelink.so
%{modules_data_dir}/jabber_protocol.desc
%attr(755,root,root) %{modules_lib_dir}/libjabber_protocol.so
%{modules_data_dir}/profiles_import.desc
%attr(755,root,root) %{modules_lib_dir}/libprofiles_import.so
%{modules_data_dir}/simpleview.desc
%attr(755,root,root) %{modules_lib_dir}/libsimpleview.so
%{modules_data_dir}/sms.desc
%attr(755,root,root) %{modules_lib_dir}/libsms.so
%{modules_data_dir}/sound.desc
%attr(755,root,root) %{modules_lib_dir}/libsound.so
%{modules_data_dir}/sql_history.desc
%attr(755,root,root) %{modules_lib_dir}/libsql_history.so
%{modules_data_dir}/qt4_docking.desc
%attr(755,root,root) %{modules_lib_dir}/libqt4_docking.so

# default modules translation:
%dir %{modules_data_dir}/translations
%lang(cs) %{modules_data_dir}/translations/config_wizard_cs.qm
%lang(en) %{modules_data_dir}/translations/config_wizard_en.qm
%lang(it) %{modules_data_dir}/translations/config_wizard_it.qm
%lang(pl) %{modules_data_dir}/translations/config_wizard_pl.qm
%lang(de) %{modules_data_dir}/translations/docking_de.qm
%lang(en) %{modules_data_dir}/translations/docking_en.qm
%lang(it) %{modules_data_dir}/translations/docking_it.qm
%lang(pl) %{modules_data_dir}/translations/docking_pl.qm
%lang(cs) %{modules_data_dir}/translations/gadu_protocol_cs.qm
%lang(en) %{modules_data_dir}/translations/gadu_protocol_en.qm
%lang(pl) %{modules_data_dir}/translations/gadu_protocol_pl.qm
%lang(cs) %{modules_data_dir}/translations/hints_cs.qm
%lang(de) %{modules_data_dir}/translations/hints_de.qm
%lang(en) %{modules_data_dir}/translations/hints_en.qm
%lang(it) %{modules_data_dir}/translations/hints_it.qm
%lang(pl) %{modules_data_dir}/translations/hints_pl.qm
%lang(cs) %{modules_data_dir}/translations/history_cs.qm
%lang(de) %{modules_data_dir}/translations/history_de.qm
%lang(en) %{modules_data_dir}/translations/history_en.qm
%lang(pl) %{modules_data_dir}/translations/history_pl.qm
%lang(cs) %{modules_data_dir}/translations/history_migration_cs.qm
%lang(en) %{modules_data_dir}/translations/history_migration_en.qm
%lang(pl) %{modules_data_dir}/translations/history_migration_pl.qm
%lang(cs) %{modules_data_dir}/translations/imagelink_cs.qm
%lang(en) %{modules_data_dir}/translations/imagelink_en.qm
%lang(it) %{modules_data_dir}/translations/imagelink_it.qm
%lang(pl) %{modules_data_dir}/translations/imagelink_pl.qm
%lang(cs) %{modules_data_dir}/translations/jabber_protocol_cs.qm
%lang(de) %{modules_data_dir}/translations/jabber_protocol_de.qm
%lang(en) %{modules_data_dir}/translations/jabber_protocol_en.qm
%lang(pl) %{modules_data_dir}/translations/jabber_protocol_pl.qm
%lang(cs) %{modules_data_dir}/translations/profiles_import_cs.qm
%lang(en) %{modules_data_dir}/translations/profiles_import_en.qm
%lang(pl) %{modules_data_dir}/translations/profiles_import_pl.qm
%lang(cs) %{modules_data_dir}/translations/simpleview_cs.qm
%lang(en) %{modules_data_dir}/translations/simpleview_en.qm
%lang(pl) %{modules_data_dir}/translations/simpleview_pl.qm
%lang(cs) %{modules_data_dir}/translations/sms_cs.qm
%lang(de) %{modules_data_dir}/translations/sms_de.qm
%lang(en) %{modules_data_dir}/translations/sms_en.qm
%lang(it) %{modules_data_dir}/translations/sms_it.qm
%lang(pl) %{modules_data_dir}/translations/sms_pl.qm
%lang(cs) %{modules_data_dir}/translations/sound_cs.qm
%lang(de) %{modules_data_dir}/translations/sound_de.qm
%lang(en) %{modules_data_dir}/translations/sound_en.qm
%lang(it) %{modules_data_dir}/translations/sound_it.qm
%lang(pl) %{modules_data_dir}/translations/sound_pl.qm
%lang(cs) %{modules_data_dir}/translations/sql_history_cs.qm
%lang(de) %{modules_data_dir}/translations/sql_history_de.qm
%lang(en) %{modules_data_dir}/translations/sql_history_en.qm
%lang(pl) %{modules_data_dir}/translations/sql_history_pl.qm

# global translation:
%dir %{_datadir}/%{name}/translations
%lang(cs) %{_datadir}/%{name}/translations/kadu_cs.qm
%lang(cs) %{_datadir}/%{name}/translations/cs.language
%lang(de) %{_datadir}/%{name}/translations/kadu_de.qm
%lang(de) %{_datadir}/%{name}/translations/de.language
%lang(de) %{_datadir}/%{name}/translations/kadu_en.qm
%lang(en) %{_datadir}/%{name}/translations/en.language
%lang(fr) %{_datadir}/%{name}/translations/kadu_fr.qm
%lang(it) %{_datadir}/%{name}/translations/kadu_it.qm
%lang(pl) %{_datadir}/%{name}/translations/kadu_pl.qm
%lang(pl) %{_datadir}/%{name}/translations/pl.language
%lang(ru) %{_datadir}/%{name}/translations/kadu_ru.qm
%lang(sk) %{_datadir}/%{name}/translations/kadu_sk.qm

# wizard
%{_datadir}/%{name}/configuration
%{_datadir}/%{name}/syntax
%{_datadir}/%{name}/scripts

# default modules configurations
%dir %{modules_data_dir}/configuration
%{modules_data_dir}/configuration/docking.ui
%{modules_data_dir}/configuration/hints.ui
%{modules_data_dir}/configuration/hint-over-user.ui
%{modules_data_dir}/configuration/hints-advanced.ui
%{modules_data_dir}/configuration/hints-notifier.ui
%{modules_data_dir}/configuration/history.ui
%{modules_data_dir}/configuration/image-link.ui
%{modules_data_dir}/configuration/jabber_protocol.ui
%{modules_data_dir}/configuration/qt4-docking-notify.ui
%{modules_data_dir}/configuration/simpleview.ui
%{modules_data_dir}/configuration/sms.ui
%{modules_data_dir}/configuration/sound.ui

# default modules datas
%dir %{modules_data_dir}/data
%dir %{modules_data_dir}/data/gadu_protocol
%{modules_data_dir}/data/gadu_protocol/servers.txt
%dir %{modules_data_dir}/data/sms
%dir %{modules_data_dir}/data/sms/scripts
%{modules_data_dir}/data/sms/scripts/*.js

%if %{with antistring}
%files module-antistring
%defattr(644,root,root,755)
%{modules_data_dir}/antistring.desc
%{modules_data_dir}/configuration/antistring.ui
%attr(755,root,root) %{modules_lib_dir}/libantistring.so
%lang(cs) %{modules_data_dir}/translations/antistring_cs.qm
%lang(de) %{modules_data_dir}/translations/antistring_de.qm
%lang(en) %{modules_data_dir}/translations/antistring_en.qm
%lang(pl) %{modules_data_dir}/translations/antistring_pl.qm
%dir %{modules_data_dir}/data/antistring
%{modules_data_dir}/data/antistring/ant_conditions.conf
%endif

%if %{with auto_hide}
%files module-auto_hide
%defattr(644,root,root,755)
%{modules_data_dir}/auto_hide.desc
%{modules_data_dir}/configuration/auto_hide.ui
%attr(755,root,root) %{modules_lib_dir}/libauto_hide.so
%lang(cs) %{modules_data_dir}/translations/auto_hide_cs.qm
%lang(de) %{modules_data_dir}/translations/auto_hide_de.qm
%lang(en) %{modules_data_dir}/translations/auto_hide_en.qm
%lang(it) %{modules_data_dir}/translations/auto_hide_it.qm
%lang(pl) %{modules_data_dir}/translations/auto_hide_pl.qm
%endif

%if %{with autoaway}
%files module-autoaway
%defattr(644,root,root,755)
%{modules_data_dir}/autoaway.desc
%{modules_data_dir}/configuration/autoaway.ui
%attr(755,root,root) %{modules_lib_dir}/libautoaway.so
%lang(cs) %{modules_data_dir}/translations/autoaway_cs.qm
%lang(de) %{modules_data_dir}/translations/autoaway_de.qm
%lang(en) %{modules_data_dir}/translations/autoaway_en.qm
%lang(it) %{modules_data_dir}/translations/autoaway_it.qm
%lang(pl) %{modules_data_dir}/translations/autoaway_pl.qm
%endif

%if %{with anonymous_check}
%files module-anonymous_check
%defattr(644,root,root,755)
%{modules_data_dir}/anonymous_check.desc
%attr(755,root,root) %{modules_lib_dir}/libanonymous_check.so
%lang(pl) %{modules_data_dir}/translations/anonymous_check_pl.qm
%endif

%if %{with autoresponder}
%files module-autoresponder
%defattr(644,root,root,755)
%{modules_data_dir}/autoresponder.desc
%{modules_data_dir}/configuration/autoresponder.ui
%attr(755,root,root) %{modules_lib_dir}/libautoresponder.so
%lang(cs) %{modules_data_dir}/translations/autoresponder_cs.qm
%lang(de) %{modules_data_dir}/translations/autoresponder_de.qm
%lang(en) %{modules_data_dir}/translations/autoresponder_en.qm
%lang(it) %{modules_data_dir}/translations/autoresponder_it.qm
%lang(pl) %{modules_data_dir}/translations/autoresponder_pl.qm
%endif

%if %{with autostatus}
%files module-autostatus
%defattr(644,root,root,755)
%{modules_data_dir}/autostatus.desc
%{modules_data_dir}/configuration/autostatus.ui
%attr(755,root,root) %{modules_lib_dir}/libautostatus.so
%lang(cs) %{modules_data_dir}/translations/autostatus_cs.qm
%lang(en) %{modules_data_dir}/translations/autostatus_en.qm
%lang(it) %{modules_data_dir}/translations/autostatus_it.qm
%lang(pl) %{modules_data_dir}/translations/autostatus_pl.qm
%endif

%if %{with cenzor}
%files module-cenzor
%defattr(644,root,root,755)
%{modules_data_dir}/cenzor.desc
%{modules_data_dir}/configuration/cenzor.ui
%attr(755,root,root) %{modules_lib_dir}/libcenzor.so
%lang(cs) %{modules_data_dir}/translations/cenzor_cs.qm
%lang(de) %{modules_data_dir}/translations/cenzor_de.qm
%lang(en) %{modules_data_dir}/translations/cenzor_en.qm
%lang(pl) %{modules_data_dir}/translations/cenzor_pl.qm
%lang(tr) %{modules_data_dir}/translations/cenzor_tr.qm
%dir %{modules_data_dir}/data/cenzor
%{modules_data_dir}/data/cenzor/cenzor_words.conf
%{modules_data_dir}/data/cenzor/cenzor_words_ok.conf
%endif

%if 0
%if %{with desc_history}
%files module-desc_history
%defattr(644,root,root,755)
%{modules_data_dir}/desc_history.desc
%{modules_data_dir}/configuration/desc_history.ui
%attr(755,root,root) %{modules_lib_dir}/desc_history.so
%lang(pl) %{modules_data_dir}/translations/desc_history_pl.qm
%endif
%endif

%if %{with encryption}
%files module-encryption
%defattr(644,root,root,755)
%{modules_data_dir}/encryption_ng.desc
%{modules_data_dir}/encryption_ng_simlite.desc
%{modules_data_dir}/configuration/encryption-ng.ui
%attr(755,root,root) %{modules_lib_dir}/libencryption_ng.so
%attr(755,root,root) %{modules_lib_dir}/libencryption_ng_simlite.so
%lang(cs) %{modules_data_dir}/translations/encryption_ng_cs.qm
%lang(en) %{modules_data_dir}/translations/encryption_ng_en.qm
%lang(it) %{modules_data_dir}/translations/encryption_ng_it.qm
%lang(pl) %{modules_data_dir}/translations/encryption_ng_pl.qm
%lang(cs) %{modules_data_dir}/translations/encryption_ng_simlite_cs.qm
%lang(de) %{modules_data_dir}/translations/encryption_ng_simlite_de.qm
%lang(en) %{modules_data_dir}/translations/encryption_ng_simlite_en.qm
%lang(it) %{modules_data_dir}/translations/encryption_ng_simlite_it.qm
%lang(pl) %{modules_data_dir}/translations/encryption_ng_simlite_pl.qm
%endif

%if %{with docking_desktop}
%files module-docking-desktop
%defattr(644,root,root,755)
%{modules_data_dir}/desktop_docking.desc
%{modules_data_dir}/configuration/desktop_docking.ui
%attr(755,root,root) %{modules_lib_dir}/libdesktop_docking.so
%lang(cs) %{modules_data_dir}/translations/desktop_docking_cs.qm
%lang(de) %{modules_data_dir}/translations/desktop_docking_de.qm
%lang(en) %{modules_data_dir}/translations/desktop_docking_en.qm
%lang(it) %{modules_data_dir}/translations/desktop_docking_it.qm
%lang(pl) %{modules_data_dir}/translations/desktop_docking_pl.qm
%endif

%if %{with filedesc}
%files module-filedesc
%defattr(644,root,root,755)
%{modules_data_dir}/filedesc.desc
%{modules_data_dir}/configuration/filedesc.ui
%attr(755,root,root) %{modules_lib_dir}/libfiledesc.so
%lang(cs) %{modules_data_dir}/translations/filedesc_cs.qm
%lang(de) %{modules_data_dir}/translations/filedesc_de.qm
%lang(en) %{modules_data_dir}/translations/filedesc_en.qm
%lang(pl) %{modules_data_dir}/translations/filedesc_pl.qm
%endif

%if %{with firewall}
%files module-firewall
%defattr(644,root,root,755)
%{modules_data_dir}/firewall.desc
%{modules_data_dir}/configuration/firewall.ui
%attr(755,root,root) %{modules_lib_dir}/libfirewall.so
%lang(cs) %{modules_data_dir}/translations/firewall_cs.qm
%lang(de) %{modules_data_dir}/translations/firewall_de.qm
%lang(en) %{modules_data_dir}/translations/firewall_en.qm
%lang(pl) %{modules_data_dir}/translations/firewall_pl.qm
%endif

%if 0
%if %{with geoip}
%files module-geoip
%defattr(644,root,root,755)
%{modules_data_dir}/geoip_lookup.desc
%attr(755,root,root) %{modules_lib_dir}/libgeoip_lookup.so
%endif
%endif

%if %{with globalhotkeys}
%files module-globalhotkeys
%defattr(644,root,root,755)
%{modules_data_dir}/globalhotkeys.desc
%{modules_data_dir}/configuration/globalhotkeys.ui
%attr(755,root,root) %{modules_lib_dir}/libglobalhotkeys.so
%lang(cs) %{modules_data_dir}/translations/globalhotkeys_cs.qm
%lang(en) %{modules_data_dir}/translations/globalhotkeys_en.qm
%lang(it) %{modules_data_dir}/translations/globalhotkeys_it.qm
%lang(pl) %{modules_data_dir}/translations/globalhotkeys_pl.qm
%endif

%if %{with last_seen}
%files module-last_seen
%defattr(644,root,root,755)
%{modules_data_dir}/last_seen.desc
%attr(755,root,root) %{modules_lib_dir}/liblast_seen.so
%lang(cs) %{modules_data_dir}/translations/last_seen_cs.qm
%lang(de) %{modules_data_dir}/translations/last_seen_de.qm
%lang(en) %{modules_data_dir}/translations/last_seen_en.qm
%lang(pl) %{modules_data_dir}/translations/last_seen_pl.qm
%lang(tr) %{modules_data_dir}/translations/last_seen_tr.qm
%endif

%if 0
%if %{with mail}
%files module-mail
%defattr(644,root,root,755)
%{modules_data_dir}/mail.desc
%{modules_data_dir}/configuration/mail.ui
%attr(755,root,root) %{modules_lib_dir}/libmail.so
%lang(pl) %{modules_data_dir}/translations/mail_pl.qm
%endif
%endif

%if %{with mediaplayer}
%files module-mediaplayer
%defattr(644,root,root,755)
%{modules_data_dir}/mediaplayer.desc
%{modules_data_dir}/configuration/mediaplayer.ui
%attr(755,root,root) %{modules_lib_dir}/libmediaplayer.so
%{modules_data_dir}/data/mediaplayer
%lang(cs) %{modules_data_dir}/translations/mediaplayer_cs.qm
%lang(de) %{modules_data_dir}/translations/mediaplayer_de.qm
%lang(en) %{modules_data_dir}/translations/mediaplayer_en.qm
%lang(pl) %{modules_data_dir}/translations/mediaplayer_pl.qm
%endif

%if %{with mediaplayer_amarok}
%files module-mediaplayer-amarok
%defattr(644,root,root,755)
%{modules_data_dir}/amarok1_mediaplayer.desc
%attr(755,root,root) %{modules_lib_dir}/libamarok1_mediaplayer.so
%endif

%if 0
%if %{with mediaplayer_amarok2}
%files module-mediaplayer-amarok2
%defattr(644,root,root,755)
%{modules_data_dir}/amarok2_mediaplayer.desc
%attr(755,root,root) %{modules_lib_dir}/libamarok2_mediaplayer.so
%endif
%endif

%if %{with mediaplayer_falf}
%files module-mediaplayer-falf
%defattr(644,root,root,755)
%{modules_data_dir}/falf_mediaplayer.desc
%attr(755,root,root) %{modules_lib_dir}/libfalf_mediaplayer.so
%endif

%if %{with mediaplayer_mpris}
%files module-mediaplayer-mpris
%defattr(644,root,root,755)
%{modules_data_dir}/mprisplayer_mediaplayer.desc
%{modules_data_dir}/configuration/mprisplayer_mediaplayer.ui
%attr(755,root,root) %{modules_lib_dir}/libmprisplayer_mediaplayer.so
%lang(en) %{modules_data_dir}/translations/mprisplayer_mediaplayer_en.qm
%lang(pl) %{modules_data_dir}/translations/mprisplayer_mediaplayer_pl.qm
%{modules_data_dir}/data/mprisplayer_mediaplayer/mprisplayer-players.data
%endif

%if %{with mime_tex}
%files module-mime_tex
%defattr(644,root,root,755)
%dir %{modules_bin_dir}/mime_tex
%attr(755,root,root) %{modules_bin_dir}/mime_tex/mimetex
%{modules_data_dir}/mime_tex.desc
%{modules_data_dir}/configuration/mime_tex.ui
%attr(755,root,root) %{modules_lib_dir}/libmime_tex.so
%dir %{modules_data_dir}/data/mime_tex
%dir %{modules_data_dir}/data/mime_tex/editor_icons
%dir %{modules_data_dir}/data/mime_tex/mime_tex_icons
%{modules_data_dir}/data/mime_tex/mime_tex_32x32.png
%{modules_data_dir}/data/mime_tex/editor_icons/*.png
%{modules_data_dir}/data/mime_tex/mime_tex_icons/*.png
%lang(pl) %{modules_data_dir}/translations/mime_tex_pl.qm
%endif

%if %{with nextinfo}
%files module-nextinfo
%defattr(644,root,root,755)
%{modules_data_dir}/nextinfo.desc
%{modules_data_dir}/configuration/nextinfo.ui
%attr(755,root,root) %{modules_lib_dir}/libnextinfo.so
%lang(cs) %{modules_data_dir}/translations/nextinfo_cs.qm
%lang(en) %{modules_data_dir}/translations/nextinfo_en.qm
%lang(pl) %{modules_data_dir}/translations/nextinfo_pl.qm
%endif

%if %{with notify_exec}
%files module-notify-exec
%defattr(644,root,root,755)
%{modules_data_dir}/exec_notify.desc
%attr(755,root,root) %{modules_lib_dir}/libexec_notify.so
%lang(en) %{modules_data_dir}/translations/exec_notify_en.qm
%lang(pl) %{modules_data_dir}/translations/exec_notify_pl.qm
%endif

%if %{with notify_freedesktop}
%files module-notify-freedesktop
%defattr(644,root,root,755)
%{modules_data_dir}/freedesktop_notify.desc
%{modules_data_dir}/configuration/freedesktop_notify.ui
%attr(755,root,root) %{modules_lib_dir}/libfreedesktop_notify.so
%lang(cs) %{modules_data_dir}/translations/freedesktop_notify_cs.qm
%lang(de) %{modules_data_dir}/translations/freedesktop_notify_de.qm
%lang(en) %{modules_data_dir}/translations/freedesktop_notify_en.qm
%lang(pl) %{modules_data_dir}/translations/freedesktop_notify_pl.qm
%endif

%if 0
%if %{with notify_kde}
%files module-notify-kde4
%defattr(644,root,root,755)
%{modules_data_dir}/kde_notify.desc
%{modules_data_dir}/configuration/kde_notify.ui
%attr(755,root,root) %{modules_lib_dir}/libkde_notify.so
%lang(de) %{modules_data_dir}/translations/kde_notify_de.qm
%lang(fr) %{modules_data_dir}/translations/kde_notify_fr.qm
%lang(it) %{modules_data_dir}/translations/kde_notify_it.qm
%lang(pl) %{modules_data_dir}/translations/kde_notify_pl.qm
%endif
%endif

%if %{with notify_led}
%files module-notify-led
%defattr(644,root,root,755)
%{modules_data_dir}/lednotify.desc
%{modules_data_dir}/configuration/lednotify.ui
%attr(755,root,root) %{modules_lib_dir}/liblednotify.so
%lang(cs) %{modules_data_dir}/translations/lednotify_cs.qm
%lang(en) %{modules_data_dir}/translations/lednotify_en.qm
%lang(pl) %{modules_data_dir}/translations/lednotify_pl.qm
%endif

%if 0
%if %{with notify_mx610}
%files module-notify-mx610
%defattr(644,root,root,755)
%{modules_data_dir}/mx610_notify.desc
%{modules_data_dir}/configuration/mx610_notify.ui
%attr(755,root,root) %{modules_lib_dir}/libmx610_notify.so
%lang(pl) %{modules_data_dir}/translations/mx610_notify_pl.qm
%endif
%endif

%if %{with notify_chat}
%files module-notify-chat
%defattr(644,root,root,755)
%{modules_data_dir}/chat_notify.desc
%attr(755,root,root) %{modules_lib_dir}/libchat_notify.so
%lang(de) %{modules_data_dir}/translations/chat_notify_de.qm
%lang(en) %{modules_data_dir}/translations/chat_notify_en.qm
%lang(pl) %{modules_data_dir}/translations/chat_notify_pl.qm
%endif

%if %{with notify_pcspeaker}
%files module-notify-pcspeaker
%defattr(644,root,root,755)
%{modules_data_dir}/pcspeaker.desc
%attr(755,root,root) %{modules_lib_dir}/libpcspeaker.so
%lang(cs) %{modules_data_dir}/translations/pcspeaker_cs.qm
%lang(de) %{modules_data_dir}/translations/pcspeaker_de.qm
%lang(en) %{modules_data_dir}/translations/pcspeaker_en.qm
%lang(it) %{modules_data_dir}/translations/pcspeaker_it.qm
%lang(pl) %{modules_data_dir}/translations/pcspeaker_pl.qm
%endif

%if %{with notify_qt4_docking}
%files module-notify-qt4_docking
%defattr(644,root,root,755)
%{modules_data_dir}/qt4_docking_notify.desc
%attr(755,root,root) %{modules_lib_dir}/libqt4_docking_notify.so
%lang(cs) %{modules_data_dir}/translations/qt4_docking_notify_cs.qm
%lang(de) %{modules_data_dir}/translations/qt4_docking_notify_de.qm
%lang(en) %{modules_data_dir}/translations/qt4_docking_notify_en.qm
%lang(pl) %{modules_data_dir}/translations/qt4_docking_notify_pl.qm
%endif

%if %{with notify_speech}
%files module-notify-speech
%defattr(644,root,root,755)
%{modules_data_dir}/speech.desc
%{modules_data_dir}/configuration/speech.ui
%attr(755,root,root) %{modules_lib_dir}/libspeech.so
%lang(cs) %{modules_data_dir}/translations/speech_cs.qm
%lang(de) %{modules_data_dir}/translations/speech_de.qm
%lang(en) %{modules_data_dir}/translations/speech_en.qm
%lang(it) %{modules_data_dir}/translations/speech_it.qm
%lang(pl) %{modules_data_dir}/translations/speech_pl.qm
%endif

%if 0
%if %{with notify_water}
%files module-notify-water
%defattr(644,root,root,755)
%{modules_data_dir}/water_notify.desc
%{modules_data_dir}/configuration/water_notify.ui
%attr(755,root,root) %{modules_lib_dir}/libwater_notify.so
%lang(pl) %{modules_data_dir}/translations/water_notify_pl.qm
%endif

%if %{with pajacyk}
%files module-pajacyk
%defattr(644,root,root,755)
%{modules_data_dir}/pajacyk.desc
%{modules_data_dir}/configuration/pajacyk.ui
%attr(755,root,root) %{modules_lib_dir}/libpajacyk.so
%lang(pl) %{modules_data_dir}/translations/pajacyk_pl.qm
%endif
%endif

%if %{with panelkadu}
%files module-panelkadu
%defattr(644,root,root,755)
%{modules_data_dir}/panelkadu.desc
%{modules_data_dir}/configuration/panelkadu.ui
%attr(755,root,root) %{modules_lib_dir}/libpanelkadu.so
%lang(cs) %{modules_data_dir}/translations/panelkadu_cs.qm
%lang(en) %{modules_data_dir}/translations/panelkadu_en.qm
%lang(pl) %{modules_data_dir}/translations/panelkadu_pl.qm
%endif

%if 0
%if %{with powerkadu}
%files module-powerkadu
%defattr(644,root,root,755)
%{modules_data_dir}/powerkadu.desc
%attr(755,root,root) %{modules_lib_dir}/libpowerkadu.so
%lang(pl) %{modules_data_dir}/translations/powerkadu_pl.qm
%{modules_data_dir}/configuration/powerkadu.ui
%dir %{modules_data_dir}/data/powerkadu
%{modules_data_dir}/data/powerkadu/ChangeLog
%{modules_data_dir}/data/powerkadu/powerkadu_32x32.png
%{modules_data_dir}/data/powerkadu/powerkadu_big.png
%lang(en) %{modules_data_dir}/data/powerkadu/AUTHORS
%lang(pl) %{modules_data_dir}/data/powerkadu/AUTHORS.pl
%endif
%endif

%if %{with single_window}
%files module-single_window
%defattr(644,root,root,755)
%{modules_data_dir}/single_window.desc
%{modules_data_dir}/configuration/single_window.ui
%attr(755,root,root) %{modules_lib_dir}/libsingle_window.so
%lang(cs) %{modules_data_dir}/translations/single_window_cs.qm
%lang(en) %{modules_data_dir}/translations/single_window_en.qm
%lang(pl) %{modules_data_dir}/translations/single_window_pl.qm
%endif

%if %{with senthistory}
%files module-senthistory
%defattr(644,root,root,755)
%{modules_data_dir}/senthistory.desc
%{modules_data_dir}/configuration/senthistory.ui
%attr(755,root,root) %{modules_lib_dir}/libsenthistory.so
%lang(cs) %{modules_data_dir}/translations/senthistory_cs.qm
%lang(en) %{modules_data_dir}/translations/senthistory_en.qm
%lang(pl) %{modules_data_dir}/translations/senthistory_pl.qm
%lang(tr) %{modules_data_dir}/translations/senthistory_tr.qm
%endif

%if %{with screenshot}
%files module-screenshot
%defattr(644,root,root,755)
%{modules_data_dir}/screenshot.desc
%{modules_data_dir}/configuration/screenshot.ui
%attr(755,root,root) %{modules_lib_dir}/libscreenshot.so
%lang(cs) %{modules_data_dir}/translations/screenshot_cs.qm
%lang(en) %{modules_data_dir}/translations/screenshot_en.qm
%lang(pl) %{modules_data_dir}/translations/screenshot_pl.qm
%endif

%if 0
%if %{with sms_plus_pl}
%files module-sms-plus_pl
%defattr(644,root,root,755)
%{modules_data_dir}/plus_pl_sms.desc
%{modules_data_dir}/configuration/plus_pl_sms.ui
%attr(755,root,root) %{modules_lib_dir}/libplus_pl_sms.so
%lang(pl) %{modules_data_dir}/translations/plus_pl_sms_pl.qm
%dir %{modules_data_dir}/data/plus_pl_sms
%{modules_data_dir}/data/plus_pl_sms/curl-ca-bundle.crt
%endif
%endif

%if %{with sound_ext}
%files module-sound-ext
%defattr(644,root,root,755)
%{modules_data_dir}/ext_sound.desc
%{modules_data_dir}/configuration/ext_sound.ui
%attr(755,root,root) %{modules_lib_dir}/libext_sound.so
%lang(cs) %{modules_data_dir}/translations/ext_sound_cs.qm
%lang(de) %{modules_data_dir}/translations/ext_sound_de.qm
%lang(en) %{modules_data_dir}/translations/ext_sound_en.qm
%lang(it) %{modules_data_dir}/translations/ext_sound_it.qm
%lang(pl) %{modules_data_dir}/translations/ext_sound_pl.qm
%endif

%if %{with sound_phonon}
%files module-sound-phonon
%defattr(644,root,root,755)
%{modules_data_dir}/phonon_sound.desc
%attr(755,root,root) %{modules_lib_dir}/libphonon_sound.so
%endif

%if %{with sound_qt4}
%files module-sound-qt4
%defattr(644,root,root,755)
%{modules_data_dir}/qt4_sound.desc
%attr(755,root,root) %{modules_lib_dir}/libqt4_sound.so
%lang(cs) %{modules_data_dir}/translations/qt4_sound_cs.qm
%lang(en) %{modules_data_dir}/translations/qt4_sound_en.qm
%lang(pl) %{modules_data_dir}/translations/qt4_sound_pl.qm
%endif

%if %{with spellchecker}
%files module-spellchecker
%defattr(644,root,root,755)
%{modules_data_dir}/spellchecker.desc
%{modules_data_dir}/configuration/spellchecker.ui
%attr(755,root,root) %{modules_lib_dir}/libspellchecker.so
%lang(cs) %{modules_data_dir}/translations/spellchecker_cs.qm
%lang(de) %{modules_data_dir}/translations/spellchecker_de.qm
%lang(en) %{modules_data_dir}/translations/spellchecker_en.qm
%lang(pl) %{modules_data_dir}/translations/spellchecker_pl.qm
%endif

%if 0
%if %{with split_messages}
%files module-split_messages
%defattr(644,root,root,755)
%{modules_data_dir}/split_messages.desc
%{modules_data_dir}/configuration/split_messages.ui
%attr(755,root,root) %{modules_lib_dir}/libsplit_messages.so
%lang(pl) %{modules_data_dir}/translations/split_messages_pl.qm
%endif
%endif

%if %{with tabs}
%files module-tabs
%defattr(644,root,root,755)
%{modules_data_dir}/tabs.desc
%{modules_data_dir}/configuration/tabs.ui
%attr(755,root,root) %{modules_lib_dir}/libtabs.so
%lang(cs) %{modules_data_dir}/translations/tabs_cs.qm
%lang(de) %{modules_data_dir}/translations/tabs_de.qm
%lang(en) %{modules_data_dir}/translations/tabs_en.qm
%lang(pl) %{modules_data_dir}/translations/tabs_pl.qm
%endif

%if 0
%if %{with voice}
%files module-voice
%defattr(644,root,root,755)
%{modules_data_dir}/voice.desc
%{modules_data_dir}/configuration/voice.ui
%attr(755,root,root) %{modules_lib_dir}/libvoice.so
%lang(de) %{modules_data_dir}/translations/voice_de.qm
%lang(fr) %{modules_data_dir}/translations/voice_fr.qm
%lang(it) %{modules_data_dir}/translations/voice_it.qm
%lang(pl) %{modules_data_dir}/translations/voice_pl.qm
%endif

%if %{with weather}
%files module-weather
%defattr(644,root,root,755)
%{modules_data_dir}/weather.desc
%{modules_data_dir}/configuration/weather.ui
%attr(755,root,root) %{modules_lib_dir}/libweather.so
%lang(pl) %{modules_data_dir}/translations/weather_pl.qm
%dir %{modules_data_dir}/data/weather
%{modules_data_dir}/data/weather/*.ini
%dir %{modules_data_dir}/data/weather/icons
%{modules_data_dir}/data/weather/icons/*.gif
%endif
%endif

%if %{with word_fix}
%files module-word_fix
%defattr(644,root,root,755)
%{modules_data_dir}/word_fix.desc
%{modules_data_dir}/configuration/word_fix.ui
%attr(755,root,root) %{modules_lib_dir}/libword_fix.so
%lang(cs) %{modules_data_dir}/translations/word_fix_cs.qm
%lang(de) %{modules_data_dir}/translations/word_fix_de.qm
%lang(en) %{modules_data_dir}/translations/word_fix_en.qm
%lang(pl) %{modules_data_dir}/translations/word_fix_pl.qm
%lang(ru) %{modules_data_dir}/translations/word_fix_ru.qm
%dir %{modules_data_dir}/data/word_fix
%{modules_data_dir}/data/word_fix/wf_default_list.data
%endif

%if 0
#%files theme-icons-glass16
#%defattr(644,root,root,755)
#%{_datadir}/%{name}/themes/icons/glass16

#%files theme-icons-glass22
#%defattr(644,root,root,755)
#%{_datadir}/%{name}/themes/icons/glass22

#%files theme-icons-kadu05
#%defattr(644,root,root,755)
#%{_datadir}/%{name}/themes/icons/kadu05

#%files theme-icons-oxygen16
#%defattr(644,root,root,755)
#%{_datadir}/%{name}/themes/icons/oxygen16

#%files theme-icons-tango16
#%defattr(644,root,root,755)
#%{_datadir}/%{name}/themes/icons/tango16

#%files theme-emoticons-tango
#%defattr(644,root,root,755)
#%{_datadir}/%{name}/themes/emoticons/tango

%files theme-sounds
%defattr(644,root,root,755)
%{_datadir}/%{name}/themes/sounds/bns
%{_datadir}/%{name}/themes/sounds/drums
%{_datadir}/%{name}/themes/sounds/florkus
%{_datadir}/%{name}/themes/sounds/michalsrodek
%{_datadir}/%{name}/themes/sounds/percussion
%{_datadir}/%{name}/themes/sounds/ultr
%endif
