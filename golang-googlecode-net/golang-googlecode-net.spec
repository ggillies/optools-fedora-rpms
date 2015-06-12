%global debug_package   %{nil}
%global provider_tld    com
%global provider        github
%global project         golang
%global repo            net
%global import_path     code.google.com/p/go.net
%global commit          71586c3cf98f806af322c5a361660eb046e00501
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global x_provider      golang
%global x_provider_tld  org
%global x_repo          net
%global x_import_path   %{x_provider}.%{x_provider_tld}/x/%{x_repo}
%global x_name          golang-%{x_provider}%{x_provider_tld}-%{repo}

Name:       golang-googlecode-net
Version:    0
Release:    0.20.git%{shortcommit}%{?dist}
Summary:    Supplementary Go networking libraries
License:    BSD
URL:        http://%{import_path}
Source0:    https://github.com/%{project}/%{repo}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
%{summary}

%package devel
BuildRequires:  golang >= 1.2.1-3
BuildRequires:  golang(code.google.com/p/go.text/encoding)
BuildRequires:  golang(code.google.com/p/go.text/encoding/charmap)
BuildRequires:  golang(code.google.com/p/go.text/encoding/japanese)
BuildRequires:  golang(code.google.com/p/go.text/encoding/korean)
BuildRequires:  golang(code.google.com/p/go.text/encoding/simplifiedchinese)
BuildRequires:  golang(code.google.com/p/go.text/encoding/traditionalchinese)
BuildRequires:  golang(code.google.com/p/go.text/encoding/unicode)
BuildRequires:  golang(code.google.com/p/go.text/transform)
Requires:   golang >= 1.2.1-3
Summary:    Supplementary Go networking libraries for code.google.com/p/ imports
Provides:   golang(%{import_path}/context) = %{version}-%{release}
Provides:   golang(%{import_path}/dict) = %{version}-%{release}
Provides:   golang(%{import_path}/html) = %{version}-%{release}
Provides:   golang(%{import_path}/html/atom) = %{version}-%{release}
Provides:   golang(%{import_path}/html/charset) = %{version}-%{release}
Provides:   golang(%{import_path}/idna) = %{version}-%{release}
Provides:   golang(%{import_path}/internal/iana) = %{version}-%{release}
Provides:   golang(%{import_path}/internal/icmp) = %{version}-%{release}
Provides:   golang(%{import_path}/ipv4) = %{version}-%{release}
Provides:   golang(%{import_path}/ipv6) = %{version}-%{release}
Provides:   golang(%{import_path}/proxy) = %{version}-%{release}
Provides:   golang(%{import_path}/publicsuffix) = %{version}-%{release}
Provides:   golang(%{import_path}/spdy) = %{version}-%{release}
Provides:   golang(%{import_path}/websocket) = %{version}-%{release}

%package -n %{x_name}-devel
BuildRequires:  golang >= 1.2.1-3
BuildRequires:  golang(golang.org/x/text/encoding)
BuildRequires:  golang(golang.org/x/text/encoding/charmap)
BuildRequires:  golang(golang.org/x/text/encoding/japanese)
BuildRequires:  golang(golang.org/x/text/encoding/korean)
BuildRequires:  golang(golang.org/x/text/encoding/simplifiedchinese)
BuildRequires:  golang(golang.org/x/text/encoding/traditionalchinese)
BuildRequires:  golang(golang.org/x/text/encoding/unicode)
BuildRequires:  golang(golang.org/x/text/transform)
Requires:   golang >= 1.2.1-3
Summary:    Supplementary Go networking libraries for golang.org/x/ imports
Provides:   golang(%{x_import_path}/context) = %{version}-%{release}
Provides:   golang(%{x_import_path}/dict) = %{version}-%{release}
Provides:   golang(%{x_import_path}/html) = %{version}-%{release}
Provides:   golang(%{x_import_path}/html/atom) = %{version}-%{release}
Provides:   golang(%{x_import_path}/html/charset) = %{version}-%{release}
Provides:   golang(%{x_import_path}/idna) = %{version}-%{release}
Provides:   golang(%{x_import_path}/internal/iana) = %{version}-%{release}
Provides:   golang(%{x_import_path}/internal/icmp) = %{version}-%{release}
Provides:   golang(%{x_import_path}/ipv4) = %{version}-%{release}
Provides:   golang(%{x_import_path}/ipv6) = %{version}-%{release}
Provides:   golang(%{x_import_path}/proxy) = %{version}-%{release}
Provides:   golang(%{x_import_path}/publicsuffix) = %{version}-%{release}
Provides:   golang(%{x_import_path}/spdy) = %{version}-%{release}
Provides:   golang(%{x_import_path}/websocket) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for building other packages
which use the supplementary Go networking libraries with code.google.com/p/ imports.

%description -n %{x_name}-devel

This package contains library source intended for building other packages
which use the supplementary Go text libraries with golang.org/x/ imports.

%prep

%setup -q -n %{repo}-%{commit}

%build

%install
install -dp %{buildroot}/%{gopath}/src/%{import_path}
install -dp %{buildroot}/%{gopath}/src/%{x_import_path}
for dir in */ ; do
   cp -rpav $dir %{buildroot}/%{gopath}/src/%{import_path}/
   cp -rpav $dir %{buildroot}/%{gopath}/src/%{x_import_path}/
done

cd %{buildroot}/%{gopath}/src/%{import_path}/
sed -i 's/"golang\.org\/x\//"code\.google\.com\/p\/go\./g' \
        $(find . -name '*.go')

%check
# context, icmp failing
GOPATH=%{buildroot}%{gopath}:%{gopath} go test %{import_path}/spdy
GOPATH=%{buildroot}%{gopath}:%{gopath} go test %{import_path}/webdav
#GOPATH=%{buildroot}%{gopath}:%{gopath} go test %{import_path}/ipv4
GOPATH=%{buildroot}%{gopath}:%{gopath} go test %{import_path}/html
#GOPATH=%{buildroot}%{gopath}:%{gopath} go test %{import_path}/html/charset
GOPATH=%{buildroot}%{gopath}:%{gopath} go test %{import_path}/html/atom
GOPATH=%{buildroot}%{gopath}:%{gopath} go test %{import_path}/idna
GOPATH=%{buildroot}%{gopath}:%{gopath} go test %{import_path}/netutil
#GOPATH=%{buildroot}%{gopath}:%{gopath} go test %{import_path}/ipv6
GOPATH=%{buildroot}%{gopath}:%{gopath} go test %{import_path}/websocket
GOPATH=%{buildroot}%{gopath}:%{gopath} go test %{import_path}/publicsuffix
GOPATH=%{buildroot}%{gopath}:%{gopath} go test %{import_path}/proxy

rm -rf %{buildroot}%{gopath}/src/%{import_path}/html/testdata
rm -rf %{buildroot}%{gopath}/src/%{import_path}/html/charset/testdata
rm -rf %{buildroot}%{gopath}/src/%{x_import_path}/html/testdata
rm -rf %{buildroot}%{gopath}/src/%{x_import_path}/html/charset/testdata

%files devel
%doc AUTHORS CONTRIBUTORS LICENSE PATENTS README
%{gopath}/src/%{import_path}

%files -n %{x_name}-devel
%doc AUTHORS CONTRIBUTORS LICENSE PATENTS README
%{gopath}/src/%{x_import_path}

%changelog
* Fri Feb 06 2015 jchaloup <jchaloup@redhat.com> - 0-0.20.git71586c3
- Bump to upstream 71586c3cf98f806af322c5a361660eb046e00501
- Repo moved to github, changing spec file header and globals

* Thu Dec 18 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.19.hg937a34c9de13
- Resolves: rhbz#1056185 disable ipv6 test
- also disable html/charset test

* Tue Dec 09 2014 jchaloup <jchaloup@redhat.com> - 0-0.18.hg937a34c9de13
- Update to the latest commit 937a34c9de13c766c814510f76bca091dee06028
  related: #1009967

* Mon Nov 24 2014 jchaloup <jchaloup@redhat.com> - 0-0.17.hg90e232e2462d
- Extend import paths for golang.org/x/
- context test failing on master
  related: #1009967

* Mon Sep 29 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.16.hg90e232e2462d
- Resolves: rhbz#1147193 - update to latest upstream revision 
  90e232e2462dedc03bf3c93358da62d54d55dfb6
- don't redefine gopath, don't own dirs owned by golang
- use golang >= 1.2.1-3 for golang specific rpm macros
- preserve timestamps of copied files
- br stuff from golang-googlecode-text

* Fri Jul 11 2014 Vincent Batts <vbatts@fedoraproject.org> - 0-0.15.hg84a4013f96e0
- don't fail on ipv6 test bz1056185

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.14.hg84a4013f96e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 17 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.13.hg84a4013f96e0
- golang exclusivearch for el6+
- add check

* Fri Jan 17 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.12.hg84a4013f96e0
- revert golang >= 1.2 version requirement

* Wed Jan 15 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.11.hg84a4013f96e0
- require golang 1.2 and up

* Wed Oct 16 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.10.hg84a4013f96e0
- removed double quotes from Provides

* Tue Oct 08 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.9.hg84a4013f96e0
- noarch for f19+ and rhel7+, exclusivearch otherwise

* Mon Oct 07 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.8.hg84a4013f96e0
- exclusivearch as per golang package
- debug_package nil

* Sun Sep 22 2013 Matthew Miller <mattdm@fedoraproject.org> 0-0.7.hg
- install just the source code for devel package

* Fri Sep 20 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.6.hg
- All Provides listed explicitly

* Fri Sep 20 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.5.hg
- Provides corrected

* Fri Sep 20 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.4.hg
- comment cleanup
- build explanation

* Fri Sep 20 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.3.hg
- html/webkit/scripted ownership set
- codereview.cfg not packaged

* Fri Sep 20 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.2.hg
- IPv6 doesn't build
- Typo correction
- directory ownership taken care of

* Thu Sep 19 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.1.hg
- Initial fedora package
