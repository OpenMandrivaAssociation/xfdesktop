%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Desktop manager for the Xfce Desktop Environment
Name:		xfdesktop
Version:	4.10.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
Patch5:		%{name}-4.6.0-default-mdv-color.patch
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	xfce4-panel-devel >= 4.9.0
BuildRequires:	exo-devel >= 0.7.2
BuildRequires:	thunar-devel >= 1.3.1
BuildRequires:	libwnck-devel
BuildRequires:	xfconf-devel >= 4.9.0
BuildRequires:	garcon-devel >= 0.1.11
BuildRequires:	libxfce4ui-devel >= 4.9.1
BuildRequires:	libnotify-devel
Conflicts:      xfce-utils <= 4.8.3-1
Requires:	mandriva-theme
Requires:	desktop-common-data
Requires:	xfce4-session >= 4.9.0
Requires:	mandriva-xfce-config

%description
The desktop manager sets the background image, provides a right-click
menu to launch applications and can optionally show files
(including application launchers) or iconified windows. It includes
gradient support for background color, saturation support for background image,
real multiscreen and xinerama support, and it provides a desktop menu editor.

%prep
%setup -q
#%patch5 -p1

%build
%configure2_5x \
	--disable-static \
	--enable-desktop-icons \
	--enable-file-icons \
	--disable-thunarx \
	--enable-gio-unix \
	--enable-notifications \
	--enable-desktop-menu \
	--with-file-manager-fallback=Thunar

%make

%install
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc README TODO AUTHORS NEWS
%{_bindir}/*
%{_datadir}/applications/*
%{_iconsdir}/hicolor/*
%{_datadir}/pixmaps/*
%{_datadir}/backgrounds/xfce/xfce-blue.jpg
%{_mandir}/man1/*
