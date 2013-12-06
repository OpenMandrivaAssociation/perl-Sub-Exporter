%define module  Sub-Exporter

Summary:	A sophisticated exporter for custom-built routines
Name:		perl-%{module}
Version:	0.982
Release:	13
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Sub/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Data::OptList)
BuildRequires:	perl-devel

%description 
This module allows to (re)name a sub.

%prep
%setup -qn %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Sub
%{_mandir}/man3/*

