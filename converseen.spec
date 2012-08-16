Name:		converseen
Version:	0.5.1
Release:	1
Summary:	A batch image conversion tool
License:	GPLv3
Group:		Graphics
URL:		http://converseen.sf.net/
Source0:	http://downloads.sourceforge.net/project/converseen/Converseen/Converseen%200.5/%{version}/%{name}-%{version}.tar.bz2
Patch0:		converseen-fix-desktop-entries.patch
BuildRequires:  imagemagick
BuildRequires:	cmake
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
%makeinstall_std -C build

%files
%doc README INSTALL COPYING
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/kde4/services/ServiceMenus/%{name}_import.desktop
%{_datadir}/%{name}/*.qm
