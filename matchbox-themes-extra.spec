%define name 	matchbox-themes-extra
%define version 0.3
%define release %mkrel 6

Summary: 	Themes for the Matchbox Desktop
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://matchbox-project.org
License: 	GPLv2+
Group: 		Graphical desktop/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: 	http://matchbox-project.org/sources/matchbox-themes-extra/%version/%{name}-%{version}.tar.bz2
BuildArch:	noarch

%description
Extra themes for the Matchbox Desktop

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README TODO
%_iconsdir/*
%_datadir/themes/*


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3-6mdv2011.0
+ Revision: 620301
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.3-5mdv2010.0
+ Revision: 429964
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 0.3-4mdv2009.0
+ Revision: 252056
- rebuild
- fix no-buildroot-tag
- kill re-definition of %%buildroot on Pixel's request

* Tue Nov 06 2007 Funda Wang <fwang@mandriva.org> 0.3-2mdv2008.1
+ Revision: 106257
- Rebuild
- import matchbox-themes-extra


* Tue Jul 27 2004 Austin Acton <austin@mandrake.org> 0.3-1mdk
- initial package

