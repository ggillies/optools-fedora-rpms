%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         go-bufio
%global repo            bufio
# https://github.com/go-bufio/bufio
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          fe7b595919dec00e50dd74eda9aa8c697856fe91
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global import_path_sec gopkg.in/bufio.v1

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        This is a fork of the http://golang.org/pkg/bufio/ package. It adds ReadN method
License:        BSD
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
Requires:       golang >= 1.2.1-3
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
install -d -p %{buildroot}/%{gopath}/src/%{import_path_sec}/
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path_sec}/

%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}

%files devel
%doc README.md LICENSE
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}
%{gopath}/src/%{import_path_sec}

%changelog
* Thu Apr 23 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.gitfe7b595
- First package for Fedora


