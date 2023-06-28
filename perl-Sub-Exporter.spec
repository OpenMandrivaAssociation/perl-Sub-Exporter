%define module  Sub-Exporter

Name:		perl-%{module}
Version:	0.989
Release:	3
Summary:	A sophisticated exporter for custom-built routines
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Sub::Exporter
Source0:	http://www.cpan.org/modules/by-module/Sub/Sub-Exporter-%{version}.tar.gz
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Data::OptList)
BuildRequires:	perl-devel
BuildArch:	noarch

%description 
This module allows to (re)name a sub.

%prep
%autosetup -p1 -n %{module}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%install
%make_install

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Sub
%{_mandir}/*/*


