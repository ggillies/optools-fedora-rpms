%global debug_package   %{nil}
%global import_path     github.com/codegangsta/cli
%global commit          565493f259bf868adb54d45d5f4c68d405117adf
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           golang-github-codegangsta-cli
Version:        1.2.0
Release:        1%{?dist}
Summary:        Package for building command line apps in Go
License:        MIT
URL:            https://%{import_path}
Source0:        https://%{import_path}/archive/%{version}.tar.gz
BuildArch:      noarch

%description
cli.go is simple, fast, and fun package for building command line apps in Go.
The goal is to enable developers to write fast and distributable command line
applications in an expressive way.

%package devel
# Earliest NVR containing relevant golang macros
BuildRequires:  golang >= 1.2.1-3
Requires:       golang >= 1.2.1-3
Summary:        Package for building command line apps in Go
Provides:       golang(%{import_path}) = %{version}-%{release}

%description devel
cli.go is simple, fast, and fun package for building command line apps in Go.
The goal is to enable developers to write fast and distributable command line
applications in an expressive way.

This package contains library source intended for building other packages
which use codegangsta/cli.

%prep
%setup -n cli-%{version}

%build

%install
install -d -p %{buildroot}%{gopath}/src/%{import_path}
cp -pav *.go %{buildroot}%{gopath}/src/%{import_path}

%check
GOPATH=%{gopath}:%{buildroot}/%{gopath} go test %{import_path}

%files devel
%doc LICENSE README.md
%dir %{gopath}/src/github.com/codegangsta
%dir %{gopath}/src/%{import_path}
%{gopath}/src/%{import_path}/*.go

%changelog
* Thu Aug 21 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.2.0-1
- bump to v1.2.0

* Wed Jul 30 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-1
- 27ecc97192df1bf053a22b04463f2b51b8b8373e tagged 1.1.0
- manage el6 archfulness separately
- remove attr and defattr for fedora

* Fri Jul 25 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-4
- update to master commit 27ecc97192df1bf053a22b04463f2b51b8b8373e

* Mon Jul 21 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-3
- correct cp args

* Wed Jul 16 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-2
- From: Vincent Batts <vbatts@fedoraproject.org>
- remove boiler-plate, to use golang rpm macros instead
- preserve timestamps of copied source
- don't own directories that golang owns

* Sat Jun 28 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-1
- Initial fedora package
