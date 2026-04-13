%global		debug_package %{nil}

%define		oname Converseen
%define		_desktopdir %{_datadir}/applications
%define		_appdatadir %{_datadir}/appdata

Summary:		A batch image conversion tool
Name:		converseen
Version:		0.15.2.2
Release:		1
License:		GPLv3
Group:		Graphics
Url:		https://converseen.fasterland.net/
Source0:	https://github.com/Faster3ck/Converseen/archive/v%{version}/%{oname}-%{version}.tar.gz
Source1:	converseen.desktop
Source2:	converseen_import.desktop
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

%description
This is a batch image conversion tool and resizer written in C++ with Qt6 and
Magick++. It allows you to convert images in more than 100 different formats!

%files -f %{name}.lang 
%doc CHANGELOG README.md
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_desktopdir}/net.fasterland.%{name}.desktop
%{_datadir}/kio/servicemenus/%{name}_import.desktop
%{_datadir}/metainfo/%{name}.appdata.xml

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{oname}-%{version}

chmod -x README.* 
# Fix linting in debug
find . -type f -exec chmod -x {} \;

# Fix png rgb 
pushd res
	find . -type f -name "*.png" -exec magick {} -strip {} \;
popd


%build
%cmake .. -DUSE_QT6=YES
%make_build


%install
%make_install -C build

%find_lang %{name} --with-qt
