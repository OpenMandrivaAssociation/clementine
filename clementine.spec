Name:		clementine
Summary:	A cross-platform music player based on Amarok 1.4
Group:		Sound
Version:	1.1.1
Release:	1
License:	GPLv3
URL:		http://www.clementine-player.org/
Source0:	http://clementine-player.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:	Clementine.conf
Source2:	clementine-1.0.1-ru.po
Patch0:		clementine-0.6-use-default-language.patch
# Search albums at metal-archives.com (Encyclopaedia Metallum) from:
# - Now Playing widget (album art context menu) - current album
# - Playlist (selected songs context menu) - unique selected albums
Patch1:		clementine-1.1.0-metalarchives.patch
# Covers should always fit the screen resolution so we scale them if needed
Patch2:		clementine-1.0.0-coversize.patch
# Fix desktop file
Patch3:		clementine-1.1.0-fix-desktop.patch

BuildRequires:	qt4-devel >= 4.5.0
BuildRequires:	pkgconfig(taglib) >= 1.6
BuildRequires:	liblastfm-devel
BuildRequires:	boost-devel
BuildRequires:	qt4-linguist
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	cmake
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libmtp)
BuildRequires:	pkgconfig(libusbmuxd)
BuildRequires:	pkgconfig(libplist)
BuildRequires:	pkgconfig(libimobiledevice-1.0)
# Disable for now as indicate-qt seems to be broken and we don't really need it anyway
#BuildRequires:	pkgconfig(indicate-qt)
BuildRequires:	pkgconfig(libechonest)
BuildRequires:	pkgconfig(libgpod-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(protobuf)
Requires:	libprojectm-data
Requires:	qt4-database-plugin-sqlite
Requires:	gstreamer0.10-flac
Requires:	gstreamer0.10-plugins-ugly

Suggests:	gstreamer0.10-decoders-audio
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
    * Edit tags on MP3 and OGG files, organise your music
    * Download missing album cover art from Last.fm
    * Remote control using a Wii Remote, MPRIS or the command-line
    * Copy music to your iPod, iPhone, MTP or mass-storage USB player
    * Queue manage

%files
%{_bindir}/clementine
%{_bindir}/clementine-tagreader
%{_datadir}/kde4/services/clementine-*.protocol
%{_datadir}/applications/clementine.desktop
%{_iconsdir}/hicolor/64x64/apps/application-x-clementine.png
%{_iconsdir}/hicolor/scalable/apps/application-x-clementine.svg
%config %{_sysconfdir}/Clementine/Clementine.conf


#---------------------------------------------------------------------

%prep
%setup -q
# Update russian translation
# Needed only until next after 1.1.0 version is released
cp -f %{SOURCE2} src/translations/ru.po
%patch0 -p1
%patch1 -p1 -b .ma~
%patch2 -p1 -b .coversize~
%patch3 -p1

%build
%cmake_qt4 -DBUNDLE_PROJECTM_PRESETS=OFF -DBUILD_WERROR=OFF
%make

%install
%makeinstall_std -C build

install -m 644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/Clementine/Clementine.conf
