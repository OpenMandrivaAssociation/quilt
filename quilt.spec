#
# spec file for quilt - patch management scripts
#

Name:		quilt
Summary:	Scripts for working with series of patches
License:	GPLv2
Group:		Development/Other
Version:	0.60
Release:	%mkrel 1
URL:		http://savannah.nongnu.org/projects/quilt
Requires:	coreutils diffutils patch gzip bzip2 perl mktemp gettext
Requires:	diffstat procmail ed
Source:		http://mirrors.zerg.biz/nongnu/quilt/%{name}-%{version}.tar.gz
# sendmail-command is needed for testing purpose
BuildRequires: sendmail-command diffstat procmail ed

%description
The scripts allow to manage a series of patches by keeping
track of the changes each patch makes. Patches can be
applied, un-applied, refreshed, etc.

The scripts are heavily based on Andrew Morton's patch scripts
found at http://www.zip.com.au/~akpm/linux/patches/.


%prep
%setup -q

%build
%configure --with-mta=%{_sbindir}/sendmail --with-diffstat=%{_bindir}/diffstat
make BUILD_ROOT=%{buildroot}

%check
make check

%install
make install BUILD_ROOT=%{buildroot}
mv -f %{buildroot}/%{_docdir}/%{name}/ %{buildroot}/%{_docdir}/%{name}-%{version}/
%{find_lang} %{name}

%files -f %{name}.lang
%defattr(-, root, root)
%config(noreplace) /etc/bash_completion.d/quilt
%config(noreplace) /etc/quilt.quiltrc
%{_bindir}/*
%{_datadir}/emacs/site-lisp/quilt.el
%{_datadir}/%{name}/*
#%{_libdir}/quilt/
%{_mandir}/man1/*.1*
%doc %{_docdir}/%{name}-%{version}
%doc AUTHORS TODO


%changelog
* Sat Mar 03 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.60-1mdv2011.0
+ Revision: 782011
- update to 0.60

* Sun Jan 29 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.51-1
+ Revision: 769583
- new version 0.51

* Thu Sep 03 2009 Frederik Himpe <fhimpe@mandriva.org> 0.48-1mdv2010.0
+ Revision: 428700
- Update to new version 0.48

* Thu Jan 15 2009 Jérôme Soyer <saispo@mandriva.org> 0.47-1mdv2009.1
+ Revision: 329877
- New upstream release

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - fix leaving not owned directories in docdir
    - remove authors from description
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Oct 22 2007 Jérôme Soyer <saispo@mandriva.org> 0.46-1mdv2008.1
+ Revision: 101098
- New release 0.46

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages

* Sat Jun 30 2007 Michael Scherer <misc@mandriva.org> 0.45-2mdv2008.0
+ Revision: 46032
- rebuild on 2008
- fix bug #27931, missing deps on diffstat
- silence %%setup
- Import quilt



* Mon Apr 24 2006 Arnaud Patard <apatard@mandriva.com> 0.45-1mdk
- New version

* Sun Apr  9 2006 Anssi Hannula <anssi@mandriva.org> 0.44-2mdk
- BuildRequires diffstat
- %%mkrel

* Mon Mar  6 2006 Arnaud Patard <apatard@mandriva.com> 0.44-1mdk
- New version
- Enable tests

* Tue Feb  7 2006 Arnaud Patard <apatard@mandriva.com> 0.43-1mdk
- New version

* Thu Aug  4 2005 Arnaud Patard <apatard@mandriva.com> 0.42-1mdk
- New version

* Tue May  3 2005 Arnaud Patard <apatard@mandriva.com> 0.40-1mdk
- New version (add trailing-whitespace check support in quilt refresh)
- Make rpmlint happy :)

* Wed Apr 13 2005 Arnaud Patard <apatard@mandriva.com> 0.39-1mdk
- First version. The spec file is nearly the same as the one shipped
  in the tarball
