%define version 4.4.1
%define __libtoolize /bin/true

Summary: 	Desktop manager for the Xfce Desktop Environment
Name: 		xfdesktop
Version: 	%{version}
Release: 	%mkrel 2
License:	GPL
URL: 		http://www.xfce.org/
Source0: 	%{name}-%{version}.tar.bz2
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
Group: 		Graphical desktop/Xfce
BuildRoot: 	%{_tmppath}/%{name}-root
Requires:	mandriva-theme
Requires:	desktop-common-data
BuildRequires:	xfce-mcs-manager-devel >= %{version}
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	libxml2-devel >= 2.4.0
BuildRequires:	xfce-panel-devel >= 4.3.0
BuildRequires:	exo-devel
BuildRequires:  thunar-devel >= 0.8.0
%description
Xfdesktop is a desktop manager for the Xfce Desktop Environment.

%prep
%setup -q
#%patch0 -p1 -b .dither
#%patch2 -p1 -b .mdkmenu
# trem : rejected
# %patch3 -p1 -b .backdrop
%patch4 -p1 -b .show-context
%patch5 -p1 -b .special-icons
%patch6 -p1 -b .backdrop

# use www-browser
#perl -pi -e 's#mozilla#www-browser#' menu.*
# use thunar as default fm
perl -pi -e 's#xffm#thunar#g' menu.*

%build
%configure2_5x --sysconfdir=%_sysconfdir/X11
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
mkdir -p %buildroot%_sysconfdir/menu-methods
bzcat %SOURCE1 > %buildroot%_sysconfdir/menu-methods/xfce4
bzcat %SOURCE2 > %buildroot%_sysconfdir/X11/xdg/xfce4/desktop/menu_method_postrun.sh

# fix permissions
chmod 0755 %buildroot%_sysconfdir/X11/xdg/xfce4/desktop/menu_method_postrun.sh

# remove unneeded devel files
rm -f %{buildroot}/%{_libdir}/xfce4/mcs-plugins/*.*a \
	%{buildroot}/%{_libdir}/xfce4/modules/*.*a \
	%{buildroot}/%{_libdir}/xfce4/panel-plugins/*.*a

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
%clean_menus
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files -f %{name}.lang
%defattr(-,root,root)
%doc README TODO COPYING AUTHORS
%config(noreplace) %{_sysconfdir}/X11/xdg/*
%attr(755,root,root) %config(noreplace) %_sysconfdir/menu-methods/xfce4
%{_bindir}/*
%{_libdir}/xfce4/*
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/pixmaps/*
%{_datadir}/xfce4/*
%{_datadir}/xfce4-menueditor/xfce4-menueditor.ui
%{_mandir}/man1/*


