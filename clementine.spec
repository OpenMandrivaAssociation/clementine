%define name	clementine
%define version	0.6
%define release	%mkrel 1

%define Summary	A cross-platform music player based on Amarok 1.4  


Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://clementine-player.googlecode.com/files/%{name}-%{version}.tar.gz
License:	GPLv3
Group:		Sound 
URL:		http://www.clementine-player.org/
BuildRequires:	qt4-devel >= 4.5.0
BuildRequires:	taglib-devel >= 1.6
BuildRequires:	liblastfm-devel
BuildRequires:	libboost-devel
BuildRequires:	qt4-linguist
BuildRequires:	gstreamer0.10-devel
BuildRequires:	cmake
BuildRequires:	glew-devel
BuildRequires:	libmtp-devel
BuildRequires:	usbmuxd-devel
BuildRequires:	libplist-devel
BuildRequires:	libimobiledevice-devel
BuildRequires:	libgpod-devel >= 0.7.92

Requires:	libprojectm-data
Requires:	qt4-database-plugin-sqlite
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
%defattr(-,root,root)
%_bindir/clementine
%_datadir/applications/clementine.desktop
%_iconsdir/hicolor/64x64/apps/application-x-clementine.png
%_iconsdir/hicolor/scalable/apps/application-x-clementine.svg
#---------------------------------------------------------------------

%prep
%setup -q  

%build
%cmake_qt4 -DBUNDLE_PROJECTM_PRESETS=OFF -DENABLE_LIBGPOD=ON -DENABLE_LIBMTP=ON -DENABLE_IMOBILEDEVICE=ON -DENABLE_WIIMOTEDEV=ON
# use of make -j 4 because %make seems to failed on BS here 
make -j 4 

%install
%__rm -rf %buildroot
%makeinstall_std -C build
# Remove unused files (aka ubuntu theme...) for the momemnt

%__rm -rf  %{buildroot}/%{_datadir}/icons/ubuntu-mono-dark/ %{buildroot}/%{_datadir}/icons/ubuntu-mono-light

%clean
%__rm -rf %buildroot
