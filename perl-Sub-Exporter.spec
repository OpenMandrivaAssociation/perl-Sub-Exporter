%define module  Sub-Exporter

Name:		perl-%{module}
Version:	0.982
Release:	8
Summary:	A sophisticated exporter for custom-built routines
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Sub/%{module}-%{version}.tar.gz
BuildRequires:	perl(Data::OptList)
BuildRequires:	perl-devel
BuildArch:	noarch

%description 
This module allows to (re)name a sub.

%prep
%setup -q -n %{module}-%{version}

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.982-7mdv2012.0
+ Revision: 765661
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.982-5
+ Revision: 667314
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0.982-4mdv2011.0
+ Revision: 609165
- rebuild

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.982-2mdv2010.0
+ Revision: 440657
- rebuild

* Sat Jan 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.982-1mdv2009.1
+ Revision: 330403
- update to new version 0.982

* Fri Oct 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.981-1mdv2009.1
+ Revision: 296906
- update to new version 0.981

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.980-1mdv2009.1
+ Revision: 292343
- update to new version 0.980

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.979-2mdv2009.0
+ Revision: 268727
- rebuild early 2009.0 package (before pixel changes)

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.979-1mdv2009.0
+ Revision: 201869
- update to new version 0.979

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.978-1mdv2008.1
+ Revision: 111151
- update to new version 0.978

* Sat Sep 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.976-1mdv2008.0
+ Revision: 77698
- update to new version 0.976

* Thu Aug 30 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.975-1mdv2008.0
+ Revision: 75183
- import perl-Sub-Exporter


* Wed Aug 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.975-1mdv2008.0
- first mdv release
