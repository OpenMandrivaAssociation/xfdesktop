Summary:	Desktop manager for the Xfce Desktop Environment
Name:		xfdesktop
Version:	4.4.2
Release:	%mkrel 14
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
Patch7:		%{name}-4.4.2-xdg-user-dirs.patch
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

%build
%configure2_5x \
	--sysconfdir=%{_sysconfdir}/X11 \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%post
%{update_menus}
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root)
%doc README TODO AUTHORS NEWS
%dir %{_sysconfdir}/X11/xdg/xfce4/desktop
%exclude %{_sysconfdir}/X11/xdg/xfce4/desktop/*
%{_bindir}/*
%{_libdir}/xfce4/*
%{_datadir}/applications/*
%{_iconsdir}/hicolor/*
%{_datadir}/pixmaps/*
%{_datadir}/xfce4/*
%{_datadir}/xfce4-menueditor/xfce4-menueditor.ui
%{_mandir}/man1/*
