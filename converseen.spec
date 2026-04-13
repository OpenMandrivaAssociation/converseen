%define oname Converseen
%global debug_package %{nil}

Name:		converseen
Version:	0.15.2.2
Release:	1
Summary:	A batch image conversion tool
License:	GPLv3
Group:		Graphics
URL:		https://converseen.fasterland.net/
Source0:	https://github.com/Faster3ck/Converseen/archive/v%{version}/%{oname}-%{version}.tar.gz

BuildSystem:    cmake
BuildOption:    -DUSE_QT6=yes

BuildRequires:		cmake >= 3.16
BuildRequires:		desktop-file-utils
BuildRequires:		imagemagick
BuildRequires:		make
BuildRequires:		sane-backends >= 1.0.24
BuildRequires:		ghostscript-devel
BuildRequires:		cmake(Qt6LinguistTools)
BuildRequires:		pkgconfig(gl)
BuildRequires:		pkgconfig(ImageMagick) >= 7.0
# do not remove. Sflo
BuildRequires:		pkgconfig(libpng)
BuildRequires:		pkgconfig(Magick++)
BuildRequires:		pkgconfig(Qt6Core)
BuildRequires:		pkgconfig(Qt6Gui)
BuildRequires:		pkgconfig(Qt6Help)
BuildRequires:		pkgconfig(Qt6Network)
BuildRequires:		pkgconfig(Qt6Widgets)
BuildRequires:		pkgconfig(vulkan)
BuildRequires:    gettext

%description
Converseen is a batch image conversion tool and resizer written in C++ with
Qt6 and Magick++. It allows you to convert images in more than 100
different formats!

%prep
%setup -qn %{oname}-%{version}

%files -f %{name}.lang
%license COPYING.txt
%doc README.* 
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/net.fasterland.%{name}.desktop
%{_datadir}/kio/servicemenus/%{name}_import.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
