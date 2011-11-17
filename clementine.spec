%define git 1

Name:       clementine
Summary:    A cross-platform music player based on Amarok 1.4
Group:      Sound
Version:    0.7.1
Release:    10
License:    GPLv3
URL:        http://www.clementine-player.org/
Source0:    http://clementine-player.googlecode.com/files/%{name}%{?git:-20111117}%{?!git:-%{version}}.tar.bz2
Source1:    Clementine.conf
Patch0:     clementine-0.6-use-default-language.patch

BuildRequires:  qt4-devel >= 4.5.0
BuildRequires:  taglib-devel >= 1.6
BuildRequires:  liblastfm-devel
BuildRequires:  libboost-devel
BuildRequires:  qt4-linguist
BuildRequires:  gstreamer0.10-devel
BuildRequires:  cmake
BuildRequires:  glew-devel
BuildRequires:  libmtp-devel
BuildRequires:  usbmuxd-devel
BuildRequires:  libplist-devel
BuildRequires:  libimobiledevice-devel
BuildRequires:  libindicate-qt-devel
BuildRequires:  echonest-devel
BuildRequires:  libgpod-devel >= 0.7.92
BuildRequires:  libgstreamer-plugins-base-devel
BuildRequires:  libcdio-devel
Requires:   libprojectm-data
Requires:   qt4-database-plugin-sqlite
Requires:   gstreamer0.10-flac
Requires:   gstreamer0.10-plugins-ugly

Suggests:   gstreamer0.10-decoders-audio
# Needed to be able to mount ipod/iphone/ipad (not tested locally) but it's also pulling gvfs
# which is need at least to mount mtp devices (tested locally)
Suggests:   gvfs-iphone

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
%_bindir/clementine
%_datadir/applications/clementine.desktop
%_iconsdir/hicolor/64x64/apps/application-x-clementine.png
%_iconsdir/hicolor/scalable/apps/application-x-clementine.svg
%config %{_sysconfdir}/Clementine/Clementine.conf
%doc %_defaultdocdir/HTML/*/%name 

#---------------------------------------------------------------------

%prep
%setup -q%{?git:n %{name}}
%patch0 -p1

%build
%cmake_qt4 -DBUNDLE_PROJECTM_PRESETS=OFF
%make

%install
%__rm -rf %buildroot
%makeinstall_std -C build

install -m 644 -D %{_sourcedir}/Clementine.conf \
%{buildroot}%{_sysconfdir}/Clementine/Clementine.conf

