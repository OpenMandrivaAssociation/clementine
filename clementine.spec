######################
# Hardcode PLF build
%bcond_with plf
######################

%if %{with plf}
# make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define extrarelsuffix plf
%endif

%bcond_with vkontakte

%define gstapi 1.0
%define oname Clementine

%define git 2cc560ff1e939a1c5f4b08c9504e26b9e23ca242
Summary:	A cross-platform music player based on Amarok 1.4
Name:		clementine
Version:	1.2.4git
Release:	0.1%{?extrarelsuffix}
License:	GPLv3+
Group:		Sound
Url:		http://www.clementine-player.org/
%if "%git"
Source0:	http://github.com/clementine-player/Clementine/archive/%{oname}-%{git}.tar.gz
%else
Source0:	http://github.com/clementine-player/%{oname}/archive/%{oname}-%{version}.tar.gz
%endif

Source1:	Clementine.conf
%if %{with vkontakte}
Source2:	clementine-1.2.0-vk-files.tar.bz2
%endif
Patch0:		clementine-1.2.0-libmygpo-qt.patch
# Search albums at metal-archives.com (Encyclopaedia Metallum) from:
# - Now Playing widget (album art context menu) - current album
# - Playlist (selected songs context menu) - unique selected albums
Patch1:		clementine-1.2.2-metalarchives.patch
# Covers should always fit the screen resolution so we scale them if needed
Patch2:		clementine-1.0.0-coversize.patch
# VKontakte (vk.com) support from http://code.google.com/r/shedwardx-clementine-experiments/
# With some ROSA adjustments (use system vreen library etc)
Patch3:		clementine-1.2.2-vkontakte-advanced.patch
Patch4:		clementine-1.2.0-vkontakte-tags.patch
# Localization issues
Patch5:		clementine-1.2.0-l10n-ru-vkontakte.patch
Patch10:	clementine-1.2.0-l10n-ru-desktop.patch
Patch11:	clementine-1.2.0-l10n-ru-search.patch

BuildRequires:	cmake
BuildRequires:	qt4-linguist
BuildRequires:	boost-devel
BuildRequires:	liblastfm-devel
BuildRequires:	qt4-devel >= 4.5.0
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gstreamer-%{gstapi})
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{gstapi})
BuildRequires:	pkgconfig(gstreamer-tag-%{gstapi})
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(libchromaprint)
BuildRequires:	pkgconfig(libechonest)
BuildRequires:	pkgconfig(libgpod-1.0)
BuildRequires:	pkgconfig(libmtp)
BuildRequires:	pkgconfig(libmygpo-qt)
BuildRequires:	pkgconfig(libplist)
# For Google Drive integration
BuildRequires:	pkgconfig(libsparsehash)
%if %{with plf}
BuildRequires:	pkgconfig(libspotify)
%endif
BuildRequires:	pkgconfig(libusbmuxd)
# Disable for now as indicate-qt seems to be broken and we don't really need it anyway
#BuildRequires:	pkgconfig(indicate-qt)
BuildRequires:	pkgconfig(protobuf)
BuildRequires:	pkgconfig(qca2)
BuildRequires:	pkgconfig(QJson)
BuildRequires:	pkgconfig(taglib) >= 1.6
BuildRequires:	pkgconfig(vreen)
BuildRequires:	pkgconfig(vreenoauth)
Requires:	libprojectm-data
Requires:	qt4-database-plugin-sqlite
Requires:	gstreamer%{gstapi}-flac
Requires:	gstreamer%{gstapi}-plugins-ugly
Suggests:	gstreamer%{gstapi}-decoders-audio
# Needed to be able to mount ipod/iphone/ipad (not tested locally) but it's also pulling gvfs
# which is need at least to mount mtp devices (tested locally)
Suggests:	gvfs-iphone

%description
Clementine is a modern music player and library organiser. Clementine is
a port of Amarok 1.4, with some features rewritten to take advantage of
Qt4.
Features:
    * Search and play your local music library
    * Listen to internet radio from Last.fm, SomaFM and Magnatune
    * Tabbed playlists, import and export M3U, XSPF, PLS and ASX
    * Visualisations from projectM
    * Transcode music into MP3, Ogg Vorbis, Ogg Speex, FLAC or AAC
    * Edit tags on MP3 and OGG files, organize your music
    * Download missing album cover art from Last.fm
    * Remote control using a Wii Remote, MPRIS or the command-line
    * Copy music to your iPod, iPhone, MTP or mass-storage USB player
    * Queue manage

%files
%config %{_sysconfdir}/Clementine/Clementine.conf
%{_bindir}/clementine
%{_bindir}/clementine-tagreader
%{_datadir}/kde4/services/clementine-*.protocol
%{_datadir}/applications/clementine.desktop
%{_datadir}/appdata/clementine.appdata.xml
%{_iconsdir}/hicolor/64x64/apps/application-x-clementine.png
%{_iconsdir}/hicolor/scalable/apps/application-x-clementine.svg
%if %{with plf}
%{_bindir}/clementine-spotifyblob
%endif

#----------------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{git}
#patch0 -p1 -b .mygpo~
#patch1 -p1 -b .ma~
#patch2 -p1 -b .coversize~

%if %{with vkontakte}
tar -xf %{SOURCE2}
%patch3 -p1 -b .vkontakte~
%patch4 -p1 -b .vkontakte~
%patch5 -p1 -b .vkontakte~
%endif

#patch10 -p1 -b .l10n~
#patch11 -p1 -b .l10n~


%build
export CC=gcc
export CXX=g++
%patch12 -p1 -b .gcc47~

%cmake_qt4 \
	-DBUNDLE_PROJECTM_PRESETS=OFF \
	-DBUILD_WERROR=OFF   
    
%make VERBOSE=1

%install
%makeinstall_std -C build

install -m 644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/Clementine/Clementine.conf

%if %{with plf}
# Ugly hack, not sure why that file appears
rm -rf %{buildroot}/builddir
rm -rf %{buildroot}/home
%endif

