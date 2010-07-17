%define name	clementine
%define version	0.4.2
%define release	%mkrel 1

%define Summary	A cross-platform music player based on Amarok 1.4  


Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://clementine-player.googlecode.com/files/%{name}-%{version}.tar.gz
#Source0:	%{name}-0.2.99.tar.gz
# svn checkout http://clementine-player.googlecode.com/svn/trunk/ clementine-svn
# tar -caf clementine-svn.tar.lzma clementine-svn

License:	GPLv3
Group:		Sound 
URL:		http://code.google.com/p/clementine-player/
BuildRequires:	qt4-devel 
BuildRequires:	taglib-devel
BuildRequires:	liblastfm-devel
BuildRequires:	libboost-devel
BuildRequires:	qt4-linguist
BuildRequires:	vlc-devel
BuildRequires:	libxine-devel
BuildRequires:	gstreamer0.10-devel
BuildRequires:	cmake
BuildRequires:	glew-devel
Requires:	qt4-database-plugin-sqlite
Suggests:	gstreamer0.10-decoders-audio

%description
Clementine is a modern music player and library organiser. Clementine is
a port of Amarok 1.4, with some features rewritten to take advantage of
Qt4. 
Features:
      * Album cover art is now automatically loaded from disk for your library
      * Cover manager downloads missing covers from Last.fm
      * Covers for Last.fm radio tracks are shown in notifications
      * Much better "Various Artists" detection
      * Menu items to force albums to be shown under "Various Artists"
      * Support for M3U and XSPF playlists
      * Menu items to add files and streams by URL
      * Shuffle and Repeat modes for the playlist
      * Option to hide the system tray icon
      * Option to show notifications when changing volume (disabled by default)
      * Playlist columns for albumartist, composer, file type, date
      * Menu item to automatically number tracks in the playlist
      * More 2D analyzers from Amarok 1.4
      * (Linux) Media keys (play, stop, etc.) should work under Gnome 

%files 
%defattr(-,root,root)
%_bindir/clementine
%_datadir/clementine
%_datadir/applications/clementine.desktop
%_iconsdir/hicolor/64x64/apps/application-x-clementine.png

#---------------------------------------------------------------------

%prep
%setup -q  

%build
%cmake_qt4 -DQT_PHONON_INCLUDE_DIR=%_includedir 
%make

%install
%__rm -rf %buildroot
%makeinstall_std -C build

%clean
%__rm -rf %buildroot
