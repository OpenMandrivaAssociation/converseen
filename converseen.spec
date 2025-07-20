%define _desktopdir %{_datadir}/applications
%define oname Converseen
%define _appdatadir %{_datadir}/appdata

Name:		converseen
Version:	0.15.0.2
Release:	1
Summary:	A batch image conversion tool
License:	GPLv3
Group:		Graphics
URL:		https://converseen.fasterland.net/
Source0:	https://github.com/Faster3ck/Converseen/archive/v%{version}/%{oname}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	converseen_import.desktop
BuildRequires:	cmake 
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:	pkgconfig(ImageMagick) >= 7.0
BuildRequires:	imagemagick
BuildRequires:	sane-backends >= 1.0.24
BuildRequires:	desktop-file-utils
# do not remove. Sflo
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Help)
BuildRequires:	pkgconfig(Qt6Network)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Magick++)

%description
Converseen is a batch image conversion tool and resizer written in C++ with
Qt5 and Magick++. It allows you to convert images in more than 100
different formats!

%prep
%setup -qn %{oname}-%{version}

chmod -x README.* 
#fix linting in debug
find . -type f -exec chmod -x {} \;

# fix png rgb 
pushd res
find . -type f -name "*.png" -exec convert {} -strip {} \;
popd

%build
%cmake
%make_build

%install
%make_install -C build

# localize
%find_lang %{name} --with-qt

%files -f %{name}.lang 
%doc README.* 
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_desktopdir}/net.fasterland.%{name}.desktop
%{_datadir}/kio/servicemenus/%{name}_import.desktop
%{_appdatadir}/metainfo/%{name}.appdata.xml
