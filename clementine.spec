%define name	clementine
%define version	0.4.2
%define release	%mkrel 4

%define Summary	A cross-platform music player based on Amarok 1.4  


Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://clementine-player.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		clementine-0.4.2-upstream-fix-lastfmcrash.patch
Patch1:		clementine-0.4.2-upstream-fix-debug.patch
Patch2:		clementine-0.4.2-upstream-fix-numeric-locale.patch
License:	GPLv3
Group:		Sound 
URL:		http://code.google.com/p/clementine-player/
BuildRequires:	qt4-devel 
BuildRequires:	taglib-devel
BuildRequires:	liblastfm-devel
BuildRequires:	libboost-devel
BuildRequires:	qt4-linguist
BuildRequires:	gstreamer0.10-devel
BuildRequires:	cmake
BuildRequires:	glew-devel
Requires:	libprojectm-data
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
%_datadir/applications/clementine.desktop
%_iconsdir/hicolor/64x64/apps/application-x-clementine.png

#---------------------------------------------------------------------

%prep
%setup -q  
%patch0 -p 0
%patch1 -p 0
%patch2 -p 0

%build
%cmake_qt4 -DBUNDLE_PROJECTM_PRESETS=OFF 
# use of make -j 4 because %make seems to failed on BS here 
make -j 4 

%install
%__rm -rf %buildroot
%makeinstall_std -C build

%clean
%__rm -rf %buildroot
