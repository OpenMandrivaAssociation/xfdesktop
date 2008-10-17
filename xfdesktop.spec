Summary:	Desktop manager for the Xfce Desktop Environment
Name:		xfdesktop
Version:	4.5.91
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	%{name}-%{version}.tar.bz2
Patch0:		01_show-backdrop-by-default.patch
Patch5:		%{name}-4.4.2-default-mdv-color.patch
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	xfce4-panel-devel >= %{version}
BuildRequires:	exo-devel
BuildRequires:	thunar-devel >= 0.9.91
BuildRequires:	libwnck-devel
BuildRequires:	xfconf-devel
BuildRequires:	libglade2-devel
BuildRequires:	libxfce4menu-devel
Requires:	mandriva-theme
Requires:	desktop-common-data
Requires:	xfce-utils >= %{version}
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
#patch0 -p1
#patch5 -p1

%build
%configure2_5x \
%if %mdkversion < 200900
	--sysconfdir=%{_sysconfdir}/X11 \
%endif
	--disable-static \
	--enable-menu-editor

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
%{_sysconfdir}/xdg/menus/xfce-applications.menu
%{_bindir}/*
%{_libdir}/xfce4/*
%{_datadir}/applications/*
%{_iconsdir}/hicolor/*
%{_datadir}/pixmaps/*
%{_datadir}/xfce4/*
%{_datadir}/xfce4-menueditor
%{_datadir}/desktop-directories/*.directory
%{_mandir}/man1/*
