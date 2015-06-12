%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         cupcake
%global repo            rdb
# https://github.com/cupcake/rdb
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          3454dcabd33cb8ea8261ffd6a45f4d836eb504cc
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Redis RDB parser for Go 
License:        MIT
URL:            https://%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
%{summary}

%package devel
BuildRequires:  golang >= 1.2.1-3
BuildRequires:  golang(launchpad.net/gocheck)
Requires:       golang >= 1.2.1-3
Requires:       golang(launchpad.net/gocheck)
Summary:        %{summary}
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/crc64) = %{version}-%{release}
Provides:       golang(%{import_path}/nopdecoder) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for 
building other packages which use %{project}/%{repo}.

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav crc64 %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav examples %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav fixtures %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav nopdecoder %{buildroot}/%{gopath}/src/%{import_path}/

%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}

%files devel
%doc README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Thu Apr 16 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.git3454dca
- First package for Fedora


