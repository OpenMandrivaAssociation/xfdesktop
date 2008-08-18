Summary:	Desktop manager for the Xfce Desktop Environment
Name:		xfdesktop
Version:	4.4.2
Release:	%mkrel 19
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	%{name}-%{version}.tar.bz2
Patch0:		01_show-backdrop-by-default.patch
Patch1:		%{name}-4.4.2-use-eject-where-necessary.patch
Patch2:		%{name}-4.4.2-menu-free-items-leak.patch
Patch3:		%{name}-4.4.2-fix-relocation-x86_64.patch
Patch4:		%{name}-4.4.2-hide-desktop-files-marked-as-hidden.patch
Patch5:		%{name}-4.4.2-default-mdv-color.patch
Patch6:		%{name}-4.4.2-fix-settings_register_callback-assertion.patch
# (tpg) http://bugzilla.xfce.org/show_bug.cgi?id=4062
# and https://bugzilla.redhat.com/show_bug.cgi?id=457740
Patch7:		%{name}-4.4.2-xdg-user-dirs.patch
Patch8:		%{name}-4.4.2-simplify-freeing-code.patch
Patch9:		%{name}-4.4.2-activate-menu-item.patch
Patch10:	%{name}-4.4.2-backdrop-zoom.patch
BuildRequires:	xfce-mcs-manager-devel >= %{version}
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	xfce4-panel-devel >= %{version}
BuildRequires:	exo-devel
BuildRequires:	thunar-devel >= 0.8.0
BuildRequires:	libusb-devel
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
%patch0 -p1
%patch1 -p1 -b .eject
%patch2 -p1 -b .leak
%if %mdkversion > 200800
%ifnarch ix86
%patch3 -p1 -b .reloc
%endif
%endif
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build
%configure2_5x \
%if %mdkversion < 200900
	--sysconfdir=%{_sysconfdir}/X11 \
%endif
	--disable-static

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
%else
%dir %{_sysconfdir}/xdg/xfce4/desktop
%exclude %{_sysconfdir}/xdg/xfce4/desktop/*
%endif
%{_bindir}/*
%{_libdir}/xfce4/*
%{_datadir}/applications/*
%{_iconsdir}/hicolor/*
%{_datadir}/pixmaps/*
%{_datadir}/xfce4/*
%{_datadir}/xfce4-menueditor
%{_mandir}/man1/*
