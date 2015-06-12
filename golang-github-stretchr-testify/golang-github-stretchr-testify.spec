%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         stretchr
%global repo            testify
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          33a31e5dbed8302d5ab7e6d12b416e95c2c4ebc0
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global bootstrap       1

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Go code (golang) set of packages that provide many tools for testifying that your code will behave as you intend
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
%if 0%{bootstrap} == 0
BuildRequires:  golang(github.com/stretchr/objx)
%endif
Requires:       golang >= 1.2.1-3
Summary:        %{summary}
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/assert) = %{version}-%{release}
Provides:       golang(%{import_path}/http) = %{version}-%{release}
Provides:       golang(%{import_path}/mock) = %{version}-%{release}
Provides:       golang(%{import_path}/require) = %{version}-%{release}
Provides:       golang(%{import_path}/suite) = %{version}-%{release}

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
cp -rpav require %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav suite %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav http %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav assert %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav mock %{buildroot}/%{gopath}/src/%{import_path}/

%check
%if 0%{bootstrap} == 0
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/require
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/suite
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/assert
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/mock
%endif

%files devel
%doc README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Tue Feb 03 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.git33a31e5
- First package for Fedora


