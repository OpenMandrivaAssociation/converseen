%define _desktopdir %{_datadir}/applications
%define oname Converseen
%define _appdatadir %{_datadir}/appdata

Name:		converseen
Version:	0.9.8.0
Release:	1
Summary:	A batch image conversion tool
License:	GPLv3
Group:		Graphics
URL:		http://converseen.sf.net/
Source0:	https://github.com/Faster3ck/Converseen/archive/v%{version}/%{oname}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	converseen_import.desktop
BuildRequires:	cmake 
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(ImageMagick) >= 7.0
BuildRequires:	imagemagick
BuildRequires:	sane-backends >= 1.0.24
BuildRequires:	desktop-file-utils
# do not remove. Sflo
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Help)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Magick++)

%description
Converseen is a batch image conversion tool and resizer written in C++ with
Qt4 and Magick++. It allows you to convert images in more than 100
different formats!

%prep
%setup -qn %{oname}-%{version}

chmod -x README.* COPYING
#fix linting in debug
find . -type f -exec chmod -x {} \;

# fix png rgb 
pushd res
find . -type f -name "*.png" -exec convert {} -strip {} \;
popd

%build
%cmake
%make

%install
%makeinstall_std -C build

# localize
%find_lang %{name} --with-qt

%files -f %{name}.lang 
%doc README.* COPYING
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_desktopdir}/%{name}.desktop
%{_datadir}/kservices5/ServiceMenus/%{name}_import.desktop
%{_appdatadir}/%{name}.appdata.xml
