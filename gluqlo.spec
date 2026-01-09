Name:           gluqlo
Version:        1.0.1
Release:        1%{?dist}
Summary:        Gluqlo is a SDL remake of well-known awesome Fliqlo screensaver

License:        MIT
URL:            https://github.com/Philogag/gluqlo
Source0:        https://github.com/Philogag/gluqlo/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  make g++ SDL_gfx-devel SDL_ttf-devel
Requires:       SDL_gfx SDL_ttf

%global debug_package %{nil}

%description
Gluqlo (or Глюкало, if you prefer) is a SDL remake of well-known awesome Fliqlo screensaver which is originally avaliable for Windows and OSX platforms only. Gluqlo is inspired by (and to some extent is based on) noflipqlo aka Now Open Flipqlo 2.0 by Jacek Kuźniarski. Currently it's very close to original Fliqlo (as I hope).

%prep
%autosetup


%build
%make_build


%install
strip gluqlo
install -m 0755 -D gluqlo %{buildroot}/usr/libexec/xscreensaver/gluqlo
install -m 0644 -D gluqlo.ttf %{buildroot}/usr/share/gluqlo/gluqlo.ttf
install -m 0644 -D gluqlo.png %{buildroot}/usr/share/pixmaps/gluqlo.png
install -m 0644 -D gluqlo.xml %{buildroot}/usr/share/xscreensaver/config/gluqlo.xml
install -m 0644 -D gluqlo.desktop %{buildroot}/usr/share/applications/screensavers/gluqlo.desktop


%files
%license LICENSE
%doc README.md
/usr/libexec/xscreensaver/gluqlo
/usr/share/gluqlo/gluqlo.ttf
/usr/share/pixmaps/gluqlo.png
/usr/share/xscreensaver/config/gluqlo.xml
/usr/share/applications/screensavers/gluqlo.desktop


%changelog
* Fri Jan 09 2026 philogag <philogag@qq.com>
- 
