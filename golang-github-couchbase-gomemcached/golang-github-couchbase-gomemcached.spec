%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         couchbase
%global repo            gomemcached
# https://github.com/couchbase/gomemcached
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          8cddcf4617f49a7f28610a5594e575d398a9496d
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        A memcached binary protocol toolkit for go
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
Requires:       golang >= 1.2.1-3
Summary:        %{summary}
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/client) = %{version}-%{release}
Provides:       golang(%{import_path}/debug) = %{version}-%{release}
Provides:       golang(%{import_path}/server) = %{version}-%{release}

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
cp -rpav client %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav debug %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav gocache %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav server %{buildroot}/%{gopath}/src/%{import_path}/

%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/client
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/server

%files devel
%doc LICENSE
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Wed Apr 22 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.git8cddcf4
- First package for Fedora


