Name:          awf-gtk4
Version:       2.8.1
Release:       1
Summary:       Theme preview application for GTK 4
Summary(fr):   Application d'aperçu de thème pour GTK 4
License:       GPLv3+
Group:         Development/Basic
URL:           https://github.com/luigifab/awf-extended
Source0:       %{url}/archive/v%{version}/awf-extended-%{version}.tar.gz

BuildRequires: aspell-fr
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: desktop-file-utils
BuildRequires: libnotify-devel >= 0.7.0
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: gtk4.0-devel
Requires:      gtk4.0
Requires:      libnotify >= 0.7.0
Requires:      hicolor-icon-theme

%description %{expand:
A widget factory is a theme preview application for GTK. It displays the
various widget types provided by GTK in a single window allowing to see
the visual effect of the applied theme.

This package provides the GTK 4 version.}

%description -l fr %{expand:
La fabrique à widgets est une application d'aperçu de thème pour GTK. Elle
affiche les différents types de widgets fournis par GTK dans une seule
fenêtre permettant de voir l'effet visuel du thème appliqué.

Ce paquet fournit la version GTK 4.}


%prep
%setup -q -n awf-extended-%{version}
sed -i 's/ -eq 2/ -eq -1/g' configure.ac
sed -i 's/ -eq 3/ -eq -1/g' configure.ac

%build
autoreconf -fi
%configure
%make_build

%install
%make_install
install -dm 755 %{buildroot}%{_datadir}/applications/
desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ data/%{name}.desktop

install -dm 755 %{buildroot}%{_datadir}/icons/hicolor/
for file in data/icons/*/*/awf.png; do mv $file ${file/\/awf.png/\/%{name}.png}; done
for file in data/icons/*/*/awf.svg; do mv $file ${file/\/awf.svg/\/%{name}.svg}; done
cp -a data/icons/* %{buildroot}%{_datadir}/icons/hicolor/

install -Dpm 644 data/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -Dpm 644 data/%{name}.fr.1 %{buildroot}%{_mandir}/fr/man1/%{name}.1

for file in src/po/*.po; do
  code=$(basename "$file" .po)
  install -dm 755 %{buildroot}%{_datadir}/locale/$code/LC_MESSAGES/
  msgfmt src/po/$code.po -o %{buildroot}%{_datadir}/locale/$code/LC_MESSAGES/%{name}.mo
done
%find_lang %{name} --with-man

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}.1*


%changelog
* Mon Mar 03 2025 Fabrice Creuzot <code@luigifab.fr> - 2.8.1-1
- Initial OpenMandriva package release
