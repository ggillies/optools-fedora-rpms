%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         gorilla
%global repo            websocket
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          ecff5aabe41f13b4cdf897e3c0c9bbccbe552a29
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.2.git%{shortcommit}%{?dist}
Summary:        A WebSocket implementation for Go
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
cp -rpav examples %{buildroot}/%{gopath}/src/%{import_path}/

%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}

%files devel
%doc README.md LICENSE AUTHORS
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Mon Apr 20 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.gitecff5aa
- Bump to upstream ecff5aabe41f13b4cdf897e3c0c9bbccbe552a29
  resolves: #1196361

* Wed Feb 25 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitab5b3a6
- First package for Fedora
  resolves: #1196361
