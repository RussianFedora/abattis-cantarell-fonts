%global actualname cantarell

%global fontname abattis-%{actualname}
%global fontconf 31-cantarell.conf

%global archivename1 Cantarell-Bold
%global archivename2 Cantarell-Regular

Name: %{fontname}-fonts
Version: 0.0.8
Release: 1%{?dist}
Summary: Cantarell, a Humanist sans-serif font family

Group: User Interface/X
License: OFL
URL: http://abattis.org/cantarell/
Source0: http://download.gnome.org/sources/cantarell-fonts/0.0/cantarell-fonts-%{version}.tar.xz

# Upstream patches
Patch0: cantarell-cyrillic-support.patch

BuildArch: noarch
BuildRequires: fontpackages-devel
BuildRequires: fontforge
Requires: fontpackages-filesystem

%description
Cantarell is a set of fonts designed by Dave Crossland.
It is a sans-serif humanist typeface family.

%prep
%setup -q -n %{actualname}-fonts-%{version}
%patch0 -p1 -b .cyrillic-support

%build
%configure
make %{?_smp_mflags}
ls -l ./src/
fontforge -lang=ff -c 'Open($1); Generate($2);' src/%{archivename1}.sfd %{archivename1}.otf
fontforge -lang=ff -c 'Open($1); Generate($2);' src/%{archivename2}.sfd %{archivename2}.otf

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p fontconfig/%{fontconf} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%_font_pkg -f %{fontconf} *.otf
%doc COPYING NEWS README

%changelog
* Thu Apr 12 2012 Arkady L. Shane <ashejn@russianfedora.ru> - 0.0.8-1.R
- added upstream patch for ciryllic support

* Wed Mar 28 2012 Richard Hughes <hughsient@gmail.com> - 0.0.8-1
- Update to 0.0.8

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 18 2011 Matthias Clasen <mclasen@redhat.com> - 0.0.7-1
- Update to 0.0.7

* Fri Oct 07 2011 Matěj Cepl <mcepl@redhat.com> - 0.0.6-2
- Making the build EL-6 compatible.

* Wed Jul 6 2011 Matthias Clasen <mclasen@redhat.com> - 0.0.6-1
- Update to 0.0.6

* Mon Feb 21 2011 Cosimo Cecchi <cosimoc@redhat.com> - 0.0.3-1
- Update to 0.0.3

* Fri Feb 18 2011 Cosimo Cecchi <cosimoc@redhat.com> - 0.0.1-4
- Include upstream patch for the fontconfig snippet

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb  8 2011 Stephen Smoogen <ssmoogen@redhat.com> - 0.0.1-2
- Fixed to meet review standards

* Tue Feb  8 2011 Cosimo Cecchi <cosimoc@redhat.com> - 0.0.1-1
- Initial packaging of abattis-cantarell-fonts

