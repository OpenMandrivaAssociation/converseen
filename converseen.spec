Name:		converseen
Version:	0.4.9
Release:	%mkrel 1
Summary:	A batch image conversion tool
License:	GPLv3
Group:		Graphics
URL:		http://converseen.sf.net/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		converseen-fix-desktop-entries.patch
BuildRequires:	cmake >= 2.4
BuildRequires:	gcc-c++
BuildRequires:	qt4-devel
BuildRequires:	imagemagick-devel
BuildRequires:	sane-backends

%description
Converseen is a batch image conversion tool and resizer written in C++ with
Qt4 and Magick++. It allows you to convert images in more than 100
different formats!

%prep
%setup -q
%apply_patches

%build
%cmake
%make


%install
%__rm -rf %{buildroot}
%makeinstall_std -C build

%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc README INSTALL COPYING
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/kde4/services/ServiceMenus/%{name}_import.desktop
%{_datadir}/%{name}/*.qm




%changelog
* Mon Feb 20 2012 Andrey Bondrov <abondrov@mandriva.org> 0.4.9-1mdv2012.0
+ Revision: 777914
- imported package converseen


* Wed Feb 01 2012 Giovanni Mariani <mc2374@mclink.it> 0.4.9-69.1mib2010.2
- New release 0.4.9

* Wed Jan 18 2012 Giovanni Mariani <mc2374@mclink.it> 0.4.8-69.1mib2010.2
- New release 0.4.8

* Sat Dec 10 2011 Giovanni Mariani <mc2374@mclink.it> 0.4.7-69.1mib2010.2
- Ported to Mdv 2010.2 from a Fedora 16 package by the MIB
