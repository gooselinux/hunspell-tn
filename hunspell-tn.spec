Name: hunspell-tn
Summary: Tswana hunspell dictionaries
%define upstreamid 20060123
Version: 0.%{upstreamid}
Release: 5%{?dist}
Source: http://downloads.translate.org.za/spellchecker/tswana/myspell-tn_ZA-%{upstreamid}.zip
Group: Applications/Text
URL: http://www.translate.org.za/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPL+
BuildArch: noarch

Requires: hunspell

%description
Tswana hunspell dictionaries.

%prep
%setup -q -c -n hunspell-tn

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell
pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
tn_ZA_aliases="tn_BW"
for lang in $tn_ZA_aliases; do
        ln -s tn_ZA.aff $lang.aff
        ln -s tn_ZA.dic $lang.dic
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_tn_ZA.txt
%{_datadir}/myspell/*

%changelog
* Thu Jan 07 2010 Caolan McNamara <caolanm@redhat.com> - 0.20060123-5
- Resolves: rhbz#553269 fix license

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20060123-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060123-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060123-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 30 2008 Caolan McNamara <caolanm@redhat.com> - 0.20060123-2
- add Botswana alias

* Tue Sep 09 2008 Caolan McNamara <caolanm@redhat.com> - 0.20060123-1
- initial version
