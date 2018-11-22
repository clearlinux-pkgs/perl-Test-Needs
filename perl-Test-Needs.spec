#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Needs
Version  : 0.002005
Release  : 14
URL      : http://search.cpan.org/CPAN/authors/id/H/HA/HAARG/Test-Needs-0.002005.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/H/HA/HAARG/Test-Needs-0.002005.tar.gz
Summary  : 'Skip tests when modules not available'
Group    : Development/Tools
License  : Artistic-1.0-Perl
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


%prep
%setup -q -n Test-Needs-0.002005

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
/usr/lib/perl5/vendor_perl/5.28.0/Test/Needs.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Needs.3
