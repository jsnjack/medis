%define name medis
%define version %(node -p -e "require('./package.json').version")
%define desktop_file %{name}.desktop


Name: %{name}
Version: %{version}
Release: 1%{?dist}
Summary: GUI for Redis

License: MIT
URL: https://github.com/jsnjack/medis/

Source0: %{desktop_file}

Requires: /bin/sh
AutoProv: no
AutoReq: no
Provides: %{name} = %{version}-%{RELEASE}

BuildRequires: nodejs
BuildRequires: npm
BuildRequires: desktop-file-utils
BuildRequires: xdg-utils

%description
GUI for Redis

%prep
# npm install
# npm run build


%build
# npm run rpm_build


%install
install -d %{buildroot}%{_datarootdir}/%{name}
cp -aR dist/app-linux-x64/* %{buildroot}%{_datarootdir}/%{name}
install -d %{buildroot}%{_bindir}/
ln -sf %{_datarootdir}/%{name}/app  %{buildroot}%{_bindir}/medis
desktop-file-install %{SOURCE0}


%post
xdg-icon-resource install --novendor --size 1024 %{_datarootdir}/%{name}/resources/app/icns/Icon1024.png medis

%files
%{_datarootdir}/%{name}/
%{_bindir}/medis
%{_datarootdir}/applications/%{desktop_file}

%changelog
