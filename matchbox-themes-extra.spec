%define name 	matchbox-themes-extra
%define version 0.3
%define release %mkrel 5

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
