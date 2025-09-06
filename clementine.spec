######################
# Hardcode PLF build
%bcond_with plf
######################

%if %{with plf}
# make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define extrarelsuffix plf
%endif

%define	gstapi 1.0
%define	oname Clementine
%define	buildnum	50-ge281c4508

%define candidate %{nil}
%define git %{nil}
%define pre %{nil}

%global optflags %{optflags} -DPROTOBUF_USE_DLLS
%global ldflags %{ldflags} -lprotobuf -labsl_log_internal_check_op -labsl_log_internal_message

Summary:	A cross-platform music player based on Amarok 1.4
Name:		clementine
Version:	1.4.1
License:	GPLv3+
Group:	Sound
Url:		https://www.clementine-player.org/
%if "%git"
# Packaged from qt5 branch
Source0:	%{name}-%{git}.tar.xz
Release:	0.%{git}.1
%endif
%if "%candidate"
Source0:	https://github.com/clementine-player/Clementine/archive/%{version}%{candidate}/%{oname}-%{version}%{candidate}.tar.gz
Release:	0.%{candidate}.10
%else
Source0:	https://github.com/clementine-player/Clementine/archive/%{version}-%{buildnum}/%{oname}-%{version}-%{buildnum}.tar.gz
#Source0:	https://github.com/clementine-player/%%{oname}/archive/%%(echo %%{version} |sed -e 's,.0$,,').tar.gz
Release:	%{?{pre}:0.%{pre}.}1%{?extrarelsuffix}
%endif

Source1:	Clementine.conf

Patch0:		clementine-1.4.1-50-cmake-4.0.0.patch
Patch1:		clementine-sqlite-no-deprecated.patch

# Upstream merged or not yet
#Patch2:		https://patch-diff.githubusercontent.com/raw/clementine-player/Clementine/pull/7342.patch
#Patch3:		https://patch-diff.githubusercontent.com/raw/clementine-player/Clementine/pull/7356.patch
#Patch3:		https://github.com/clementine-player/Clementine/pull/7314.patch

# from OpenMamba
Patch4:		https://src.openmamba.org/rpms/clementine/src/commit/19407827d87265adc35a3d2c565fc83c4e836cf6/clementine-1.4.1-cmake-fix-version.patch

BuildRequires:	gettext
#BuildRequires:	git
BuildRequires:	cmake
BuildRequires:	qmake5
BuildRequires:	cmake(absl)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5OpenGL)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	cmake(Qt5WebKitWidgets)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	boost-devel
BuildRequires:	liblastfm-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(cryptopp)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gstreamer-%{gstapi})
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{gstapi})
BuildRequires:	pkgconfig(gstreamer-tag-%{gstapi})
# Disable for now as indicate-qt seems to be broken and we don't really need it anyway
#BuildRequires:	pkgconfig(indicate-qt)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(libchromaprint)
#BuildRequires:	pkgconfig(libechonest)
BuildRequires:	pkgconfig(libgpod-1.0)
BuildRequires:	pkgconfig(libmtp)
#BuildRequires:	pkgconfig(libmygpo-qt)
BuildRequires:	pkgconfig(libplist-2.0)
BuildRequires:	pkgconfig(libpulse)
# For Google Drive integration
BuildRequires:	pkgconfig(libsparsehash)
%if %{with plf}
BuildRequires:	pkgconfig(libspotify)
%endif
BuildRequires:	pkgconfig(libusbmuxd-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(protobuf) >= 3.3.2
BuildRequires:	pkgconfig(QJson)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(taglib) >= 2.0
BuildRequires:	pkgconfig(udisks2)
#BuildRequires:	pkgconfig(vreen)
#BuildRequires:	pkgconfig(vreenoauth)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(zlib)

# Needed for listen music from some online sources like Google Drive or SoundCloud (bug 2133)
Recommends:	glib-networking
Requires:	gstreamer-tools
Requires:	gstreamer%{gstapi}-flac
Requires:	gstreamer%{gstapi}-plugins-ugly
Requires:	gstreamer%{gstapi}-plugins-bad
Suggests:	gstreamer%{gstapi}-decoders-audio
# Needed to be able to mount ipod/iphone/ipad (not tested locally) but it's also pulling gvfs
# which is need at least to mount mtp devices (tested locally)
Suggests:	gvfs-iphone
Requires:	libprojectm-data
Requires:	%{_lib}qt5sql5-sqlite

%description
Clementine is a modern music player and library organiser. Clementine is
a port of Amarok 1.4, with some features rewritten to take advantage of
Qt5.
Features:
 * Search and play your local music library.
* Listen to internet radio from Last.fm, SomaFM and Magnatune.
* Tabbed playlists, import and export M3U, XSPF, PLS and ASX.
* Visualisations from projectM.
* Transcode music into MP3, Ogg Vorbis, Ogg Speex, FLAC or AAC.
* Edit tags on MP3 and OGG files, organize your music.
* Download missing album cover art from Last.fm.
* Remote control using a Wii Remote, MPRIS or the command-line.
* Copy music to your iPod, iPhone, MTP or mass-storage USB player.
* Queue manage.

%files
%config %{_sysconfdir}/%{oname}/%{oname}.conf
%{_bindir}/%{name}
%if %{with plf}
%{_bindir}/%{name}-spotifyblob
%endif
%{_bindir}/%{name}-tagreader
%{_datadir}/kservices5/%{name}-*.protocol
%{_datadir}/applications/org.%{name}_player.%{oname}.desktop
%{_datadir}/metainfo/org.%{name}_player.%{oname}.appdata.xml
%{_iconsdir}/hicolor/*/apps/org.%{name}_player.%{oname}.*

#----------------------------------------------------------------------------

%prep
%if "%{git}"
%autosetup -p1 -n %{name}-%{git}
%endif
%if "%{candidate}"
%autosetup -p1 -n %{oname}-%{version}%{candidate}
%else
%autosetup -p1 -n %{oname}-%{version}-%{buildnum}
#autosetup -p1 -n %%{oname}-%%(echo %%{version} |sed -e 's,.0$,,')%%{pre}
%endif

sed -i 's|local_server_name_ = qApp->applicationName().toLower();|local_server_name_ = QString(qApp->applicationName()).toLower();|' ext/libclementine-common/core/workerpool.h


%build
%cmake_qt5 \
	-DBUNDLE_PROJECTM_PRESETS=OFF \
 	-DFORCE_GIT_REVISION=%{version} \
  	-DCMAKE_CXX_STANDARD=20 \
   	-DCMAKE_EXE_LINKER_FLAGS="`pkgconf --libs protobuf`" \
	-DBUILD_WERROR=OFF   
    
%make_build VERBOSE=1


%install
%make_install -C build

install -m 644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/%{oname}/%{oname}.conf

%if %{with plf}
# Ugly hack, not sure why that file appears
rm -rf %{buildroot}/builddir
rm -rf %{buildroot}/home
%endif
