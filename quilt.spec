%define debug_package %{nil}

#
# spec file for quilt - patch management scripts
#

Name:		quilt
Summary:	Scripts for working with series of patches
License:	GPLv2
Group:		Development/Other
Version:	0.64
Release:	1
URL:		https://savannah.nongnu.org/projects/quilt
Requires:	coreutils diffutils patch gzip bzip2 perl mktemp gettext
Requires:	diffstat procmail ed
Source0:	http://download.savannah.guu.org/releases/quilt/%{name}-%{version}.tar.gz
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
%config(noreplace) /etc/bash_completion.d/quilt
%config(noreplace) /etc/quilt.quiltrc
%{_bindir}/*
%{_datadir}/emacs/site-lisp/quilt.el
%{_datadir}/%{name}/*
#%{_libdir}/quilt/
%{_mandir}/man1/*.1*
%doc %{_docdir}/%{name}-%{version}
%doc AUTHORS TODO
