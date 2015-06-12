%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         go-ini
%global repo            ini
# https://github.com/go-ini/ini
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path_sec gopkg.in/ini.v1
%global commit          177219109c97e7920c933e21c9b25f874357b237
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Package ini provides INI file read and write functionality in Go
License:        ASL 2.0
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
BuildRequires:  golang(github.com/smartystreets/goconvey/convey)
BuildRequires:  golang(github.com/smartystreets/assertions)
Requires:       golang >= 1.2.1-3
Requires:       golang(github.com/smartystreets/goconvey/convey)
BuildRequires:  golang(github.com/smartystreets/assertions)
Summary:        %{summary}
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path_sec}) = %{version}-%{release}

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
cp -rpav testdata %{buildroot}/%{gopath}/src/%{import_path}/
install -d -p %{buildroot}/%{gopath}/src/%{import_path_sec}/
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path_sec}/
cp -rpav testdata %{buildroot}/%{gopath}/src/%{import_path_sec}/

%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}

%files devel
%doc README.md README_ZH.md LICENSE
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}
%{gopath}/src/%{import_path_sec}

%changelog
* Tue Apr 21 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.git1772191
- First package for Fedora


