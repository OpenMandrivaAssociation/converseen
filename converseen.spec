%define _desktopdir %{_datadir}/applications
%define oname Converseen
%define _appdatadir %{_datadir}/appdata

Name:		converseen
Version:	0.7.2
Release:	2
Summary:	A batch image conversion tool
License:	GPLv3
Group:		Graphics
URL:		http://converseen.sf.net/
Source0:	https://github.com/Faster3ck/Converseen/archive/v%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	converseen_import.desktop
BuildRequires:	cmake 
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(ImageMagick) >= 6.7.7
BuildRequires:	imagemagick
BuildRequires:	sane-backends >= 1.0.24
BuildRequires:	desktop-file-utils

%description
Converseen is a batch image conversion tool and resizer written in C++ with
Qt4 and Magick++. It allows you to convert images in more than 100
different formats!

%prep
%setup -qn %{oname}-%{version}

chmod -x README.* COPYING
#fix linting in debug
find . -type f -exec chmod -x {} \;

%build
%cmake
%make

%install
%makeinstall_std -C build
# icons and menu entry ,let's do this right
rm -rf \
    %{buildroot}%{_datadir}/pixmaps/%{name}.png %{buildroot}%{_desktopdir}/%name.desktop \
    %{buildroot}%{_datadir}/kde4/services/ServiceMenus/%{name}_import.desktop
# icons
for size in 256x256 128x128 96x96 64x64 48x48 32x32 22x22 16x16 ; do
    install -dm 0755 \
        %{buildroot}%{_datadir}/icons/hicolor/${size}/apps
    convert -strip -resize ${size} res/%{name}.png \
        %{buildroot}%{_datadir}/icons/hicolor/${size}/apps/%{name}.png
done

# menu entry
desktop-file-install  %{SOURCE1} %{buildroot}%{_desktopdir}/%{name}.desktop
# kde integration
install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/kde4/services/ServiceMenus/

# localize
%find_lang %{name} --with-qt

%files -f %{name}.lang 
%doc README.* COPYING
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_desktopdir}/%{name}.desktop
%{_datadir}/kde4/services/ServiceMenus/%{name}_import.desktop
%{_appdatadir}/%{name}.appdata.xml