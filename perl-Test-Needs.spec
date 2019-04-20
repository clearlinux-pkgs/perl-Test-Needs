#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Needs
Version  : 0.002006
Release  : 22
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Test-Needs-0.002006.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Test-Needs-0.002006.tar.gz
Summary  : 'Skip tests when modules not available'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-Needs-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Test::Needs - Skip tests when modules not available
SYNOPSIS
# need one module
use Test::Needs 'Some::Module';

%package dev
Summary: dev components for the perl-Test-Needs package.
Group: Development
Provides: perl-Test-Needs-devel = %{version}-%{release}

%description dev
dev components for the perl-Test-Needs package.


%package license
Summary: license components for the perl-Test-Needs package.
Group: Default

%description license
license components for the perl-Test-Needs package.


%prep
%setup -q -n Test-Needs-0.002006

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-Needs
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-Needs/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Test/Needs.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Needs.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-Needs/LICENSE
