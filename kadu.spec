#
# TODO: move arch-dependent modules out of /usr/share!!!
#
# Conditional build:
%bcond_without	xmms		# without xmms player support module
%bcond_without	arts		# without arts sound server support
%bcond_without	esd		# without ESD sound server support
%bcond_without	nas		# without Network Audio System support
%bcond_without	speech		# without Speech synthesis support
%bcond_without	amarok		# without amarok player support module
%bcond_without	spellchecker	# without spellchecker (Aspell support)

%define		_libgadu_ver	4:1.4-2
%define		_xmms_mod_ver	1.11
%define		_amarok_mod_ver	1.5
#
Summary:	A Gadu-Gadu client for online messaging
Summary(pl):	Klient Gadu-Gadu do przesy³ania wiadomo¶ci po sieci
Name:		kadu
Version:	0.3.9
Release:	2.2
License:	GPL
Group:		Applications/Communications
Source0:	http://kadu.net/download/stable/%{name}-%{version}.tar.bz2
# Source0-md5:	d461c4b19670920e2ba1425d12e23f6b
Source1:	%{name}.desktop
Source2:	http://scripts.one.pl/xmms/stable/%{version}/xmms-%{_xmms_mod_ver}.tar.gz
# Source2-md5:	db1de97ec33b84d406ca1d45daaae17f
Source3:	http://scripts.one.pl/amarok/stable/%{version}/amarok-%{_amarok_mod_ver}.tar.gz
# Source3-md5:	2ad7832cf02422a84bdd675a507a47d0
Source4:	http://scripts.one.pl/spellchecker/stable/%{version}/spellchecker-0.9.tar.gz
# Source4-md5:	b699879a56b679690a57e653dbc9d64d
Patch0:		%{name}-ac_am.patch
Patch1:		%{name}-FHS.patch
URL:		http://kadu.net/
#BuildRequires:	FHS-compliance-needed
%{?with_arts:BuildRequires:	arts-devel}
%{?with_spellchecker:BuildRequires:	aspell-devel}
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_esd:BuildRequires:	esound-devel}
BuildRequires:	gettext-devel
BuildRequires:	libgadu-devel >= %{_libgadu_ver}
BuildRequires:	libgsm-devel
BuildRequires:	libtool
%{?with_nas:BuildRequires:	nas-devel}
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	kdelibs-devel
BuildRequires:	qt-devel
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
Module which allows showing in status description information about
the song currently played in xmms.

%description module-xmms -l pl
Modu³ umo¿liwiajacy w opisie statusu pokazywanie informacji o
odgrywanym utworze z odtwarzacza xmms.

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
Summary(pl):	Wsparcie dla serwera dzwiêku ESD
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
Modu³ obs³ugi "G³o¶nego czytania" przez zewnêtrzny program "Powiedz".

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
Modu³ umo¿liwiajacy w opisie statusu pokazywanie informacji o
odgrywanym utworze z odtwarzacza amarok.

%package module-spellchecker
Summary:	Checker of spelling mistakes
Summary(pl):	Modu³ sprawdzaj±cy pisownie
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	aspell

%description module-spellchecker
Checker of spelling mistakes.

%description module-spellchecker -l pl
Modu³ sprawdzaj±cy pisownie.

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

%{__perl} -pi -e 's@/lib@/%{_lib}@g' kadu/modules.cpp
%{__perl} -pi -e 's@/lib@/%{_lib}@g' modules/x11_docking/spec

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
echo 'MODULE_LIBS_PATH="/usr/lib"' >> modules/nas_sound/spec
%endif
%if %{with speech}
sed -i -e 's/module_speech=n/module_speech=m/' .config
%endif
%if %{with amarok}
sed -i -e 's/module_amarok=n/module_amarok=m/' .config
echo 'MODULE_INCLUDES_PATH="/usr/include"'>> modules/amarok/spec
echo 'MODULE_LIBS_PATH="/usr/lib"' >> modules/amarok/spec
%endif
%if %{with spellchecker}
sed -i -e 's/module_spellchecker=n/module_spellchecker=m/' .config
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

#ending of FHS-patch
mv -f $RPM_BUILD_ROOT%{_datadir}/%{name}/modules $RPM_BUILD_ROOT%{_libdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kadu.desktop
%{_pixmapsdir}/kadu.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/themes
#default modules:
%dir %{_libdir}/%{name}/modules
%{_libdir}/%{name}/modules/autoaway.desc
%{_libdir}/%{name}/modules/autoresponder.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/autoresponder.so
%{_libdir}/%{name}/modules/default_sms.desc
%{_libdir}/%{name}/modules/docking.desc
%{_libdir}/%{name}/modules/dsp_sound.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/dsp_sound.so
%{_libdir}/%{name}/modules/encryption.desc
%{_libdir}/%{name}/modules/ext_sound.desc
%{_libdir}/%{name}/modules/sms.desc
%{_libdir}/%{name}/modules/sound.desc
%{_libdir}/%{name}/modules/voice.desc
%{_libdir}/%{name}/modules/x11_docking.desc
#default modules translation:
%dir %{_libdir}/%{name}/modules/translations
%lang(de) %{_libdir}/%{name}/modules/translations/autoaway_de.qm
%lang(it) %{_libdir}/%{name}/modules/translations/autoaway_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/autoaway_pl.qm
%lang(de) %{_libdir}/%{name}/modules/translations/autoresponder_de.qm
%lang(it) %{_libdir}/%{name}/modules/translations/autoresponder_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/autoresponder_pl.qm
%lang(de) %{_libdir}/%{name}/modules/translations/default_sms_de.qm
%lang(it) %{_libdir}/%{name}/modules/translations/default_sms_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/default_sms_pl.qm
%lang(de) %{_libdir}/%{name}/modules/translations/docking_de.qm
%lang(it) %{_libdir}/%{name}/modules/translations/docking_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/docking_pl.qm
%lang(de) %{_libdir}/%{name}/modules/translations/dsp_sound_de.qm
%lang(it) %{_libdir}/%{name}/modules/translations/dsp_sound_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/dsp_sound_pl.qm
%lang(de) %{_libdir}/%{name}/modules/translations/encryption_de.qm
%lang(it) %{_libdir}/%{name}/modules/translations/encryption_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/encryption_pl.qm
%lang(de) %{_libdir}/%{name}/modules/translations/ext_sound_de.qm
%lang(it) %{_libdir}/%{name}/modules/translations/ext_sound_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/ext_sound_pl.qm
%lang(de) %{_libdir}/%{name}/modules/translations/sms_de.qm
%lang(it) %{_libdir}/%{name}/modules/translations/sms_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/sms_pl.qm
%lang(de) %{_libdir}/%{name}/modules/translations/sound_de.qm
%lang(it) %{_libdir}/%{name}/modules/translations/sound_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/sound_pl.qm
%lang(de) %{_libdir}/%{name}/modules/translations/voice_de.qm
%lang(it) %{_libdir}/%{name}/modules/translations/voice_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/voice_pl.qm
%lang(de) %{_libdir}/%{name}/modules/translations/x11_docking_de.qm
%lang(it) %{_libdir}/%{name}/modules/translations/x11_docking_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/x11_docking_pl.qm
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

%if %{with xmms}
%files module-xmms
%defattr(644,root,root,755)
%{_libdir}/%{name}/modules/xmms.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/xmms.so
%lang(pl) %{_libdir}/%{name}/modules/translations/xmms_pl.qm
%endif

%if %{with arts}
%files module-sound-arts
%defattr(644,root,root,755)
%{_libdir}/%{name}/modules/arts_sound.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/arts_sound.so
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
%lang(it) %{_libdir}/%{name}/modules/translations/speech_it.qm
%lang(pl) %{_libdir}/%{name}/modules/translations/speech_pl.qm
%endif

%if %{with amarok}
%files module-amarok
%defattr(644,root,root,755)
%{_libdir}/%{name}/modules/amarok.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/amarok.so
%lang(pl) %{_libdir}/%{name}/modules/translations/amarok_pl.qm
%endif

%if %{with spellchecker}
%files module-spellchecker
%defattr(644,root,root,755)
%{_libdir}/%{name}/modules/spellchecker.desc
%attr(755,root,root) %{_libdir}/%{name}/modules/spellchecker.so
%lang(pl) %{_libdir}/%{name}/modules/translations/spellchecker_pl.qm
%endif
