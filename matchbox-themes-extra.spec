%define name 	matchbox-themes-extra
%define version 0.3
%define release 1mdk

Summary: 	Themes for the Matchbox Desktop
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://matchbox.handhelds.org/
License: 	GPL
Group: 		Graphical desktop/Other
Source: 	ftp://ftp.handhelds.org/matchbox/sources/matchbox-themes-extra/%version/%{name}-%{version}.tar.bz2

Buildroot: 	%_tmppath/%name-%version-buildroot
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

