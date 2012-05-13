%global actualname cantarell

%global fontname abattis-%{actualname}
%global fontconf 31-cantarell.conf

%global archivename1 Cantarell-Bold
%global archivename2 Cantarell-Regular

Name: %{fontname}-fonts
Version: 0.0.8
Release: 2%{?dist}
Summary: Cantarell, a Humanist sans-serif font family

Group: User Interface/X
License: OFL
URL: http://abattis.org/cantarell/
Source0: http://download.gnome.org/sources/cantarell-fonts/0.0/cantarell-fonts-%{version}.tar.xz

# Upstream patches
Patch0: cantarell-cyrillic-support.patch
Patch1: f4702e57e3d53d2d90838e656b5f30ff7303798e.patch
Patch2: a5e211b1c01f64d9e9423df21a7ac7c5125b6020.patch
Patch3: 7b93bc60b7c5255214cbc2bb651a6e775e7b2c77.patch
Patch4: 5db73d985d1a0a80926f51e24fe51ce68661d3fe.patch
Patch5: baedd0429453adcf9e18143ac9b6139669b2f898.patch
Patch6: 99096b1c66732056f24f7c730e51ae04aff3eee5.patch
Patch7: dcd1b5e7d7d4ea13f43500b3c9239063c424d4e5.patch
Patch8: cf5b2aa7c88e327dc4ae51d95ca6f4805ac45a89.patch
Patch9: 2b5c1564408c5e36bb8af94832c0bc6eace5df3d.patch
Patch10: 0eca3105a37d5eacd17dd45ebecb2d987322958e.patch

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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

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
* Mon May 14 2012 Arkady L. Shane <ashejn@russianfedora.ru> - 0.0.8-2.R
- many upstream patches

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

