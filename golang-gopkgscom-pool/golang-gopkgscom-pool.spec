%global debug_package   %{nil}
# https://github.com/rainycape/pool
%global import_path     gopkgs.com/pool.v1
%global commit          c850f092aad1780cbffff25f471c5cc32097932a
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-gopkgscom-pool
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        sync.Pool compatibility layer for for Go - falls back to a channel based pool in Go < 1.3 
License:        ASL 2.0
URL:            https://%{import_path}
Source0:        https://github.com/rainycape/pool/archive/%{commit}/pool-%{shortcommit}.tar.gz
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
%{summary}

%package devel
BuildRequires:  golang >= 1.2.1-3
Requires:       golang >= 1.2.1-3
Summary:        %{summary}
Provides:       golang(%{import_path}) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for 
building other packages which use %{import_path}

%prep
%setup -q -n pool-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}/

%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}

%files devel
%doc README.md LICENSE
%dir %{gopath}/src/%{import_path}
%{gopath}/src/%{import_path}

%changelog
* Mon Apr 27 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.gitc850f09
- First package for Fedora


