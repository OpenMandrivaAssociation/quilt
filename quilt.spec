#
# spec file for quilt - patch management scripts
#

Name:		quilt
Summary:	Scripts for working with series of patches
License:	GPL
Group:		Development/Other
Version:	0.46
Release:	%mkrel 2
URL:		http://savannah.nongnu.org/projects/quilt
Requires:	coreutils diffutils patch gzip bzip2 perl mktemp gettext
Requires:	diffstat
Source:		quilt-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
# sendmail-command is needed for testing purpose
BuildRequires: sendmail-command  diffstat

%description
The scripts allow to manage a series of patches by keeping
track of the changes each patch makes. Patches can be
applied, un-applied, refreshed, etc.

The scripts are heavily based on Andrew Morton's patch scripts
found at http://www.zip.com.au/~akpm/linux/patches/.


%prep
%setup -q

%build
%configure
make BUILD_ROOT=$RPM_BUILD_ROOT

%check
make check

%install
rm -rf $RPM_BUILD_ROOT
make install BUILD_ROOT=$RPM_BUILD_ROOT
# mv -f $RPM_BUILD_ROOT/etc/quilt.quiltrc $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}/
%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%config(noreplace) /etc/bash_completion.d/quilt
%config(noreplace) /etc/quilt.quiltrc
/usr/bin/guards
/usr/bin/quilt
/usr/share/quilt/
%{_libdir}/quilt/
/etc/bash_completion.d/quilt
%doc %{_mandir}/man1/guards.*
%doc %{_mandir}/man1/quilt.*
%doc %{_docdir}/%{name}-%{version}/
