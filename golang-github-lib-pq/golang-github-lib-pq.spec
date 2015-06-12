%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         lib
%global repo            pq
# https://github.com/lib/pq
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          e51fec16be7847e24d0270a5ce1f95cf2482b5e9
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Pure Go Postgres driver for database/sql
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
Provides:       golang(%{import_path}/hstore) = %{version}-%{release}
Provides:       golang(%{import_path}/listen_example) = %{version}-%{release}
Provides:       golang(%{import_path}/oid) = %{version}-%{release}

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
cp -rpav certs %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav hstore %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav listen_example %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav oid %{buildroot}/%{gopath}/src/%{import_path}/

%check
# Disabled as it requires a running postgresql server
# GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}
# GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/hstore

%files devel
%doc CONTRIBUTING.md LICENSE.md README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Tue Apr 14 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.gite51fec1
- First package for Fedora


