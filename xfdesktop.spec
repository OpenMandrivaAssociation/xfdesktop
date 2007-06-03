Summary:	Desktop manager for the Xfce Desktop Environment
Name:		xfdesktop
Version: 	4.4.1
Release:	%mkrel 4
License:	GPL
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	%{name}-%{version}.tar.bz2
# Xfce menu-method script
Source1:	xfce-menu-method.bz2
# Remove "Mandriva Linux" submenu from menu2.xml
Source2:	xfce-4.2.2-menu_method_postrun.sh.bz2
# (fc) 4.0.6-2mdk fix background dithering
Patch0:		xfdesktop-4.3.0-dither.patch
# (mpol) 4.1.99.1-4mdk use mdkmenu
Patch2:		xfdesktop-4.3.0-mdkmenu.patch
# (mpol) 4.2.0-4mdk define default backdrop
# trem : rejected
# Patch3:		xfdesktop-4.3.0-backdrop.patch.bz2
# (saispo) add Xubuntu patches
Patch4:		02_show_context_menu.patch  
Patch5:		03_special_icons_config.patch  
Patch6:		10_backdrop_zoom.patch
# (tpg) use  wallpaper from mandriva-theme
Patch7:		%{name}-4.4.1-mdv-wallpaper.patch
# (tpg) show wallpaper by default
Patch8:		%{name}-4.4.1-show-wallpaper.patch
Requires:	mandriva-theme
Requires:	ia_ora-gnome
Requires:	desktop-common-data
BuildRequires:	xfce-mcs-manager-devel >= %{version}
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	libxml2-devel >= 2.4.0
BuildRequires:	xfce-panel-devel >= 4.3.0
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
#%patch0 -p1 -b .dither
#%patch2 -p1 -b .mdkmenu
# trem : rejected
# %patch3 -p1 -b .backdrop
%patch4 -p1 -b .show-context
%patch5 -p1 -b .special-icons
%patch6 -p1 -b .backdrop
%patch7 -p0 -b .wallpaper
%patch8 -p0 -b .show

# use www-browser
#perl -pi -e 's#mozilla#www-browser#' menu.*
# use thunar as default fm
perl -pi -e 's#xffm#thunar#g' menu.*

%build
%configure2_5x \
	--sysconfdir=%{_sysconfdir}/X11 \
	--disable-static \

%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}%{_sysconfdir}/menu-methods
bzcat %SOURCE1 > %{buildroot}%{_sysconfdir}/menu-methods/xfce4
bzcat %SOURCE2 > %{buildroot}%{_sysconfdir}/X11/xdg/xfce4/desktop/menu_method_postrun.sh

# fix permissions
chmod 0755 %{buildroot}%{_sysconfdir}/X11/xdg/xfce4/desktop/menu_method_postrun.sh

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
%config(noreplace) %{_sysconfdir}/X11/xdg/*
%attr(755,root,root) %config(noreplace) %{_sysconfdir}/menu-methods/xfce4
%{_bindir}/*
%{_libdir}/xfce4/*
%{_datadir}/applications/*
%{_iconsdir}/hicolor/*
%{_datadir}/pixmaps/*
%{_datadir}/xfce4/*
%{_datadir}/xfce4-menueditor/xfce4-menueditor.ui
%{_mandir}/man1/*
