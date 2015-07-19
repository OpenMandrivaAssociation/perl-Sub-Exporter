%define module  Sub-Exporter
%define upstream_version 0.987

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	6
Summary:	A sophisticated exporter for custom-built routines
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Sub/Sub-Exporter-%{upstream_version}.tar.gz
BuildRequires:	perl(Data::OptList)
BuildRequires:	perl-devel
BuildArch:	noarch

%description 
This module allows to (re)name a sub.

%prep
%setup -q -n %{module}-%{upstream_version}

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
%{_mandir}/*/*


