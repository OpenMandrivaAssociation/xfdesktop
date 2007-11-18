Summary:	Desktop manager for the Xfce Desktop Environment
Name:		xfdesktop
Version: 	4.4.2
Release:	%mkrel 3
License:	GPL
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	%{name}-%{version}.tar.bz2
Requires:	mandriva-theme
Requires:	ia_ora-gnome
Requires:	desktop-common-data
Requires:	xfce-utils >= %{version}
BuildRequires:	xfce-mcs-manager-devel >= %{version}
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	libxml2-devel >= 2.4.0
BuildRequires:	xfce4-panel-devel >= %{version}
BuildRequires:	exo-devel
BuildRequires:	thunar-devel >= 0.8.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The desktop manager sets the background image, provides a right-click
menu to launch applications and can optionally show files
(including application launchers) or iconified windows. It includes
gradient support for background color, saturation support for background image,
real multiscreen and xinerama support, and it provides a desktop menu editor.

%prep
%setup -q

%build
%configure2_5x \
	--sysconfdir=%{_sysconfdir}/X11 \
	--disable-static \

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
%doc README TODO COPYING AUTHORS
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
