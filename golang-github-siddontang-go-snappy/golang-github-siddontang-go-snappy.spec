%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         siddontang
%global repo            go-snappy
# https://github.com/siddontang/go-snappy
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          d8f7bb82a96d89c1254e5a6c967134e1433c9ee2
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Fork from code.google.com/p/snappy-go 
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
Provides:       golang(%{import_path}/snappy) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for 
building other packages which use %{project}/%{repo}.

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav lib %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav snappy %{buildroot}/%{gopath}/src/%{import_path}/

%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/snappy

%files devel
%doc LICENSE README AUTHORS
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Thu Apr 16 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.gitd8f7bb8
- First package for Fedora


