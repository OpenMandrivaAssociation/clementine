%define name	clementine
%define version	0.2
#define	svn	370
%define release	%mkrel 1

%define Summary	A cross-platform music player based on Amarok 1.4  


Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://clementine-player.googlecode.com/files/%{name}-%{version}.tar.gz
#Source0:	%{name}-svn.tar.lzma
# svn checkout http://clementine-player.googlecode.com/svn/trunk/ clementine-svn
# tar -caf clementine-svn.tar.lzma clementine-svn

License:	GPLv3
Group:		Sound 
URL:		http://code.google.com/p/clementine-player/
BuildRequires:	qt4-devel 
BuildRequires:	taglib-devel
BuildRequires:	libxine-devel
BuildRequires:	libnotify-devel
BuildRequires:	liblastfm-devel
BuildRequires:	libboost-devel
BuildRequires:	cmake
Suggests:	xine-pulse

%description
Clementine is a modern music player and library organiser. Clementine is
a port of Amarok 1.4, with some features rewritten to take advantage of
Qt4. 
Features:
    * Search and play your local music library
    * Listen to internet radio from Last.fm and SomaFM
    * Edit tags on MP3 and OGG files, organise your music 

%files 
%defattr(-,root,root)
%_bindir/clementine
%_datadir/applications/clementine.desktop
%_iconsdir/hicolor/64x64/apps/application-x-clementine.png


#---------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_qt4
%make

%install
%__rm -rf %buildroot
%makeinstall_std -C build

%clean
%__rm -rf %buildroot
