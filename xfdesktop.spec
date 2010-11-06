%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Desktop manager for the Xfce Desktop Environment
Name:		xfdesktop
Version:	4.7.2
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
Patch5:		%{name}-4.6.0-default-mdv-color.patch
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	xfce4-panel-devel >= 4.7.0
BuildRequires:	exo-devel >= 0.5.4
BuildRequires:	thunar-devel >= 1.1.2
BuildRequires:	libwnck-devel
BuildRequires:	xfconf-devel >= 4.7.0
BuildRequires:	libglade2-devel
BuildRequires:	garcon-devel >= 0.1.1
BuildRequires:	libxfce4ui-devel >= 4.7.0
Requires:	mandriva-theme
Requires:	desktop-common-data
Requires:	xfce-utils >= 4.6.0
Requires:	mandriva-xfce-config
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The desktop manager sets the background image, provides a right-click
menu to launch applications and can optionally show files
(including application launchers) or iconified windows. It includes
gradient support for background color, saturation support for background image,
real multiscreen and xinerama support, and it provides a desktop menu editor.

%prep
%setup -q
%patch5 -p1

%build
%configure2_5x \
%if %mdkversion < 200900
	--sysconfdir=%{_sysconfdir}/X11 \
%endif
	--disable-static \
	--enable-desktop-icons \
	--disable-file-icons \
	--enable-thunarx \
	--enable-exo \
	--enable-desktop-menu \
	--disable-desktop-menu-dir-monitor

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc README TODO AUTHORS NEWS
%if %mdkversion < 200900
%dir %{_sysconfdir}/X11/xdg/xfce4/desktop
%exclude %{_sysconfdir}/X11/xdg/xfce4/desktop/*
%endif
%{_bindir}/*
%{_datadir}/applications/*
%{_iconsdir}/hicolor/*
%{_datadir}/pixmaps/*
%{_datadir}/xfce4/*
%{_mandir}/man1/*
