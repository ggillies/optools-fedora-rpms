%global debug_package   %{nil}
# https://github.com/go-mgo/mgo
%global import_path     gopkg.in/mgo.v2
%global commit          r2015.01.24
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-gopkg-mgo
Version:        %{commit}
Release:        1%{?dist}
Summary:        The MongoDB driver for Go
License:        BSD
URL:            https://%{import_path}
Source0:        https://github.com/go-mgo/mgo/archive/%{commit}/mgo-%{commit}.tar.gz
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
%{summary}

%package devel
BuildRequires:  golang >= 1.2.1-3
BuildRequires:  golang(gopkg.in/check.v1)
Requires:       golang >= 1.2.1-3
Requires:       golang(gopkg.in/check.v1)
Summary:        %{summary}
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/bson) = %{version}-%{release}
Provides:       golang(%{import_path}/internal/scram) = %{version}-%{release}
Provides:       golang(%{import_path}/sasl) = %{version}-%{release}
Provides:       golang(%{import_path}/txn) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for 
building other packages which use %{project}/%{repo}.

%prep
%setup -q -n mgo-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav bson %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav internal %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav sasl %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav testdb %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav txn %{buildroot}/%{gopath}/src/%{import_path}/

%check
# Disabled due to broken mongodb in rawhide
# GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/bson
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/internal/scram
# Disabled due to broken mongodb in rawhide
# GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/txn

%files devel
%doc README.md LICENSE
%dir %{gopath}/src/%{import_path}
%{gopath}/src/%{import_path}

%changelog
* Sun Apr 19 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.gitr2015.0
- First package for Fedora


