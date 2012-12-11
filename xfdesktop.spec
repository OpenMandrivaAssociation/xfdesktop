%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Desktop manager for the Xfce Desktop Environment
Name:		xfdesktop
Version:	4.10.0
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
Patch5:		%{name}-4.6.0-default-mdv-color.patch
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	xfce4-panel-devel >= 4.10.0
BuildRequires:	exo-devel >= 0.8.0
BuildRequires:	thunar-devel >= 1.4.0
BuildRequires:	pkgconfig(libwnck-1.0)
BuildRequires:	xfconf-devel >= 4.10.0
BuildRequires:	garcon-devel >= 0.2.0
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.10.0
BuildRequires:	pkgconfig(libnotify)
Conflicts:      xfce-utils <= 4.8.3-1
Requires:	mandriva-theme
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


%changelog
* Sat May 05 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.10.0-1
+ Revision: 796424
- adjust buildrequires version
- update to new version 4.10.0

* Sun Apr 15 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.3-1
+ Revision: 791203
- finally fix file list
- fix file list
- update to new version 4.9.3

* Sat Apr 07 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.2-3
+ Revision: 789691
- add conflicts on xfce-utils

* Fri Apr 06 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.2-2
+ Revision: 789510
- replace xfce-utils with xfce4-session as a requirement

* Thu Apr 05 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.2-1
+ Revision: 789486
- update to new version 4.9.2
- disable patch 5 for now
- drop old stuff from spec file

* Fri Sep 23 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.3-1
+ Revision: 701022
- update to new version 4.8.3

* Sat Apr 23 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.2-2
+ Revision: 656777
- add missing buildrequires on libnotify-devel

* Sat Apr 23 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.2-1
+ Revision: 656775
- update to new version 4.8.2

* Sat Mar 12 2011 Funda Wang <fwang@mandriva.org> 4.8.1-2
+ Revision: 643890
- rebuild to obsolete old packages

* Thu Feb 03 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.1-1
+ Revision: 635405
- update to new version 4.8.1

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.0-1
+ Revision: 632765
- update to new version 4.8.0

* Fri Jan 07 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.5-1mdv2011.0
+ Revision: 629645
- update to new version 4.7.5

* Wed Dec 08 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.4-1mdv2011.0
+ Revision: 616399
- update to new version 4.7.4

* Sat Dec 04 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.3-1mdv2011.0
+ Revision: 609368
- update to new version 4.7.3

* Sat Nov 06 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.2-2mdv2011.0
+ Revision: 594167
- enable support for activators on desktop
- drop conditionals in spec file for mdv older than 200900

* Sat Nov 06 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.2-1mdv2011.0
+ Revision: 593847
- update to new version 4.7.2

* Sat Sep 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.0-1mdv2011.0
+ Revision: 579591
- disable launchers icons
- update to new version 4.7.0
- adjust buildrequires
- update file list

* Fri Jul 16 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.2-1mdv2011.0
+ Revision: 553895
- update to new version 4.6.2

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-2mdv2010.1
+ Revision: 543222
- rebuild for mdv 2010.1

* Tue Apr 21 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-1mdv2010.0
+ Revision: 368580
- update to new version 4.6.1

* Sun Apr 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-5mdv2009.1
+ Revision: 364235
- drop patch0, completely useless
- Patch5: rediff
- Patch1: no need to call xfce_menu_init() from the stub
- Patch2: call gdk_flush() after removing X properties
- Patch3: reload image and icon view
- Patch4: default acction to accept for delete dialgos
- Patch6: reload desktop when the 1st img is added to an img list
- Patch7: auto select images as they are added to the list

* Wed Mar 18 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-4mdv2009.1
+ Revision: 357514
- exclude xfce-applications.menu, provide better one layout in next release of mandriva-xfce-config

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-3mdv2009.1
+ Revision: 349422
- rebuild
- rebuild whole xfce

* Fri Feb 27 2009 Jérôme Soyer <saispo@mandriva.org> 4.6.0-1mdv2009.1
+ Revision: 345759
- New upstream release

* Tue Jan 27 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.99.1-1mdv2009.1
+ Revision: 334208
- update to new version 4.5.99.1
- menu-editor is dead

* Wed Jan 14 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.93-1mdv2009.1
+ Revision: 329519
- update to new version 4.5.93

* Sat Nov 15 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.92-1mdv2009.1
+ Revision: 303564
- update to new version 4.5.92 (Xfce 4.6 Beta 2 Hopper)
- add full path for the Source0

* Fri Oct 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.91-1mdv2009.1
+ Revision: 294732
- Xfce4.6 beta1 is landing on cooker
- disable all patches, some of them could be still usefull, will investigate this later
- tune up buildrequires
- fix file list

* Mon Oct 13 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-23mdv2009.1
+ Revision: 293353
- Patch7: new version

* Thu Sep 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-22mdv2009.0
+ Revision: 288184
- Patch11: do not force disable double buffering (fixes a lot of flickering issues and memory usage)

* Fri Sep 19 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-21mdv2009.0
+ Revision: 285985
- patch7: rediff
- Patch7: new version (from xfce upstream bug #4365)

* Fri Sep 05 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-20mdv2009.0
+ Revision: 281252
- Patch7: new version of patch

* Tue Aug 19 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-19mdv2009.0
+ Revision: 273493
- Patch7: use XDG_DESKTOP_DIR environment variable for desktop directory

* Sat Jun 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-18mdv2009.0
+ Revision: 229716
- Patch9: activate menu items (upstream bug #3652)
- Patch10: add zoom option for backdrop

* Mon Jun 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-17mdv2009.0
+ Revision: 219437
- fix file list

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon May 19 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-16mdv2009.0
+ Revision: 208982
- Patch8: simplify freeing code

* Sun May 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-15mdv2009.0
+ Revision: 205608
- change sysconfdir from /etc/X11/xdg to /etc/xdg only for Mandriva releases newer than 2008.1

* Mon May 05 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-14mdv2009.0
+ Revision: 201354
- Patch7: do not hardcode desktop directory to /home/someuser/Desktop, use instead XDG_DESKTOP_DIR which uses localised desktop directory (Xfce upstream bug #4062)

* Tue Apr 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-13mdv2009.0
+ Revision: 192379
- set explicit requires on mandriva-xfce-config, so this should prevent empty menus issue

* Tue Mar 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-12mdv2008.1
+ Revision: 188643
- Patch6: fix settings_register_callback assertion

* Mon Mar 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-11mdv2008.1
+ Revision: 188427
- Patch5: set default Mandriva colors (based on x11-server patch)
- Patch3: rediff
- Patch4: obey X-MandrivaLinux-.hidden

* Fri Feb 29 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-10mdv2008.1
+ Revision: 176642
- Patch2: fix more mem leaks

* Thu Feb 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-9mdv2008.1
+ Revision: 176205
- Patch3: fix relocation while building on x86_64
- Patch2: fix memory leak in menu code

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 17 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-8mdv2008.1
+ Revision: 121176
- add patch 2 (show Eject for all removeable media, not only for disks)

  + Thierry Vignaud <tv@mandriva.org>
    - do not package big ChangeLog

* Thu Dec 06 2007 Jérôme Soyer <saispo@mandriva.org> 4.4.2-7mdv2008.1
+ Revision: 116069
- Add backdrop patch

* Wed Nov 28 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-6mdv2008.1
+ Revision: 113691
- update to the latest tarball

* Fri Nov 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-5mdv2008.1
+ Revision: 111653
- drop requires on ia_ora-gnome, which were not used at all

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-4mdv2008.1
+ Revision: 110151
- new license policy
- remove not needed buildrequires
- do not package COPYING, add NEWS and ChangeLog instead

  + Jérôme Soyer <saispo@mandriva.org>
    - Fix BuildRequires and Requires
    - Bump Release

* Sun Nov 18 2007 Jérôme Soyer <saispo@mandriva.org> 4.4.2-1mdv2008.1
+ Revision: 109977
- New release 4.4.2

* Fri Sep 21 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-8mdv2008.0
+ Revision: 91887
- exclude config files, which are now in mandriva-xfce-config package
- drop old and useless menu scripts

* Tue Sep 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-7mdv2008.0
+ Revision: 89665
- requires xfce-utils
- rediff patch 6

* Sat Aug 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-5mdv2008.0
+ Revision: 71413
- provide patch 11 (fix mouse's button behaviour against gtk2-2.11.x)

* Tue Jun 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-4mdv2008.0
+ Revision: 44305
- own only those configure files which are belong to this package

* Mon Jun 04 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-3mdv2008.0
+ Revision: 35002
- add P10 (fix memleak)
- add P9 (sets caption and icon for menu button)
- add P8 (show wallpaper by default)
- provide P7 (use wallpaper from mandriva-theme)
- set requires on ia_ora-gnome
- update description
- drop __libtoolize
- disable compiling static files rather than removing them
- use macros in %%post and %%postun
- spec file clean

* Fri May 25 2007 Jérôme Soyer <saispo@mandriva.org> 4.4.1-2mdv2008.0
+ Revision: 31090
- Add Xubuntu patches and Mandriva default theme

* Fri Apr 20 2007 Jérôme Soyer <saispo@mandriva.org> 4.4.1-1mdv2008.0
+ Revision: 16126
- New release 4.4.1


* Thu Feb 01 2007 Lev Givon <lev@mandriva.org> 4.4.0-2mdv2007.0
+ Revision: 115832
- Add thunar-devel build requirement needed by new desktop file icon
  feature.

* Tue Jan 23 2007 plouf <plouf> 4.4.0-1mdv2007.1
+ Revision: 112328
- New release 4.4.0

* Fri Dec 15 2006 Jérôme Soyer <saispo@mandriva.org> 4.3.99.2-1mdv2007.1
+ Revision: 97239
- Remove patch0
- New release 4.3.99.2
- Import xfdesktop

* Tue Jul 11 2006 Charles A Edwards <eslrahc@mandriva.org> 4.3.90.2-1mdv2007.0
- 4.3.90.2 (Xfce-4.4 beta2)
- disable mdk menu patch for the moment

* Wed Apr 26 2006 Jerome Soyer <saispo@mandriva.org> 4.3.90.1-1mdk
- Tue Apr 18 2006 trem <trem@mandriva.org> 4.3.90.1-1mdk
- 4.3.90.1

* Sat Mar 11 2006 Marcel Pol <mpol@mandriva.org> 4.3.0-0.svn_r20246.1mdk
- svn r20246
- buildrequires exo-devel

* Tue Feb 07 2006 Marcel Pol <mpol@mandriva.org> 4.3.0-0.svn_r19739.1mdk
- 4.3.0 svn r19739
- require mandriva-theme
- rediff P0, P3
- add more menu locales to P2
- don't run libtoolize

* Fri Jan 13 2006 Marcel Pol <mpol@mandriva.org> 4.2.3-1mdk
- 4.2.3
- remove more unneeded devel files
- fix permissions of postrun script

* Fri Jun 03 2005 Marcel Pol <mpol@mandriva.org> 4.2.2-2mdk
- add menu_method_postrun.sh to remove submenu from menu2.xml

* Wed May 25 2005 Marcel Pol <mpol@mandriva.org> 4.2.2-1mdk
- 4.2.2
- %%mkrel
- requires desktop-common-data

* Wed Mar 16 2005 Charles A Edwards <eslrahc@mandrake.org> 4.2.1-1mdk
- 4.2.1

* Mon Mar 07 2005 Marcel Pol <mpol@mandrake.org> 4.2.0-4mdk
- P3: define default backdrop
- use www-browser, require mandrake_desk

* Sat Feb 05 2005 Charles A Edwards <eslrahc@mandrake.org> 4.2.0-3mdk
- update menu-method to include icons
  Thanks to Roman Moravcik <morgan@pobox.sk>

* Sat Jan 22 2005 Marcel Pol <mpol@mandrake.org> 4.2.0-2mdk
- group: Graphical desktop/Xfce
- remove unneeded devel files

* Tue Jan 18 2005 Charles A Edwards <eslrahc@mandrake.org> 4.2.0-1mdk
- 4.2.0 Final

* Tue Dec 28 2004 Marcel Pol <mpol@mandrake.org> 4.1.99.3-2mdk
- buildrequires xfce-panel-devel

* Sat Dec 25 2004 Marcel Pol <mpol@mandrake.org> 4.1.99.3-1mdk
- 4.1.99.3 (4.2.0 RC 3)
- rediff P0
- drop P1, merged upstream

* Sun Dec 12 2004 Charles A Edwards <eslrahc@mandrake.org> 4.1.99.2-1mdk
- 4.1.99.2 (4.2.0 RC 2)
- disable P0 and P1

* Thu Nov 18 2004 Marcel Pol <mpol@mandrake.org> 4.1.99.1-4mdk
- Patch2: use mandrake menu, disable xdg menu
- update menu-method to produce valid xml file

* Wed Nov 17 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 4.1.99.1-3mdk
- Regenerate patch0 (and make Marcel happy :)

* Wed Nov 17 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 4.1.99.1-2mdk
- Patch1: fix UTF8 in desktop file

* Tue Nov 16 2004 Marcel Pol <mpol@mandrake.org> 4.1.99.1-1mdk
- 4.1.99.1
- s/XFce/Xfce
- disable P0 for now
- update filelist

* Sat Oct 02 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 4.0.6-2mdk
- Patch0: fix background dithering

* Tue Jul 13 2004 Charles A Edwards <eslrahc@mandrake.org> 4.0.6-1mdk
- 4.0.6
- reenable libtoolize

* Sun Apr 18 2004 Charles A Edwards <eslrahc@mandrake.org> 4.0.5-1mdk
- 4.0.5

* Sat Apr 10 2004 Charles A Edwards <eslrahc@mandrake.org> 4.0.4-1mdk
- 4.0.4

