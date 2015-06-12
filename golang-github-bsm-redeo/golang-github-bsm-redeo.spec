%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         bsm
%global repo            redeo
# https://github.com/bsm/redeo
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          436f4440f2ee191b0bfbdf9d12894fe0f1eedd9b
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Framework for building redis-protocol compatible TCP servers/services
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
BuildRequires:  golang(github.com/onsi/ginkgo)
BuildRequires:  golang(github.com/onsi/gomega)
Requires:       golang >= 1.2.1-3
Requires:       golang(github.com/onsi/ginkgo)
Requires:       golang(github.com/onsi/gomega)
Summary:        %{summary}
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/info) = %{version}-%{release}

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
cp -rpav _examples %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav info %{buildroot}/%{gopath}/src/%{import_path}/

%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/info

%files devel
%doc README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Wed Apr 15 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.git436f444
- First package for Fedora


