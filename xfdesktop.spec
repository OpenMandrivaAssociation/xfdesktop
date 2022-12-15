%define url_ver %(echo %{version} | cut -c 1-4)
%define _disable_rebuild_configure 1

Summary:	Desktop manager for the Xfce Desktop Environment
Name:		xfdesktop
Version:	4.18.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
Patch5:		%{name}-4.6.0-default-mdv-color.patch

BuildRequires:	intltool
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	pkgconfig(exo-2)
BuildRequires:	pkgconfig(thunarx-3)
BuildRequires:	pkgconfig(libwnck-3.0)
BuildRequires:	pkgconfig(libxfconf-0)
BuildRequires:	pkgconfig(garcon-1)
BuildRequires:	pkgconfig(garcon-gtk3-1)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	pkgconfig(libnotify)
Conflicts:      xfce-utils <= 4.8.3-1
Requires:	distro-theme
Requires:	desktop-common-data
Requires:	xfce4-session >= 4.9.0
#Requires:	mandriva-xfce-config

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
%configure \
	--disable-static \
	--enable-desktop-icons \
	--enable-file-icons \
	--enable-thunarx \
	--enable-gio-unix \
	--enable-notifications \
	--enable-desktop-menu \
	--with-file-manager-fallback=Thunar

%make_build

%install
%make_install

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc README* TODO AUTHORS NEWS
%{_bindir}/*
%{_datadir}/applications/*
%{_iconsdir}/hicolor/*
%{_datadir}/pixmaps/*
%{_datadir}/backgrounds/xfce/xfce-*.jpg
%{_datadir}/backgrounds/xfce/xfce-stripes.png
%{_datadir}/backgrounds/xfce/xfce-verticals.png
%{_mandir}/man1/*
