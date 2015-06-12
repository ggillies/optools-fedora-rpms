%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         couchbase
%global repo            go-couchbase
# https://github.com/couchbase/go-couchbase
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          5406cdd3c9786ac22d3c8d7d6b5d8b01846d7e99
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global bootstrap       1

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Couchbase client in Go
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
%if %{bootstrap} == 0
BuildRequires:  golang(github.com/couchbase/cbauth)
%endif
BuildRequires:  golang(github.com/couchbase/gomemcached)
BuildRequires:  golang(github.com/couchbase/gomemcached/client)
Requires:       golang >= 1.2.1-3
Requires:       golang(github.com/couchbase/cbauth)
Requires:       golang(github.com/couchbase/gomemcached)
Requires:       golang(github.com/couchbase/gomemcached/client)
Summary:        %{summary}
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/cbdatasource) = %{version}-%{release}
Provides:       golang(%{import_path}/util) = %{version}-%{release}

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
cp -rpav cbdatasource %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav examples %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav populate %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav tools %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav util %{buildroot}/%{gopath}/src/%{import_path}/

%check
%if %{bootstrap} == 0
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/cbdatasource
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/cbdatasource/example
%endif

%files devel
%doc LICENSE
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Wed Apr 15 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.git5406cdd
- First package for Fedora


