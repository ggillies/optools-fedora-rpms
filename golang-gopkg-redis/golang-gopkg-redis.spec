%global debug_package   %{nil}
# https://github.com/go-redis/redis
%global import_path     gopkg.in/redis.v2
%global commit          2.3.2
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-gopkg-redis
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Redis client for Golang
License:        BSD
URL:            https://%{import_path}
Source0:        https://github.com/go-redis/redis/archive/v%{shortcommit}/redis-v%{shortcommit}.tar.gz
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
%{summary}

%package devel
BuildRequires:  golang >= 1.2.1-3
BuildRequires:  golang(gopkg.in/bufio.v1)
BuildRequires:  golang(gopkg.in/check.v1)
Requires:       golang >= 1.2.1-3
Requires:       golang(gopkg.in/bufio.v1)
Requires:       golang(gopkg.in/check.v1)
Summary:        %{summary}
Provides:       golang(%{import_path}) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for 
building other packages which use %{import_path}

%prep
%setup -q -n redis-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav testdata %{buildroot}/%{gopath}/src/%{import_path}/

%check
# Tests disabled due to requiring a running redis instance
# GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}

%files devel
%doc README.md LICENSE
%dir %{gopath}/src/%{import_path}
%{gopath}/src/%{import_path}

%changelog
* Thu Apr 23 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.git2.3.2
- First package for Fedora


