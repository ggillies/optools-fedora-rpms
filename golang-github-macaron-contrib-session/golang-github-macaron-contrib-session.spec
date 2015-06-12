%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         macaron-contrib
%global repo            session
# https://github.com/macaron-contrib/session
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          31e841d95c7302b9ac456c830ea2d6dfcef4f84a
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Package session is a middleware that provides the session management of Macaron
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
BuildRequires:  golang(github.com/Unknwon/com)
BuildRequires:  golang(github.com/Unknwon/macaron)
BuildRequires:  golang(github.com/bradfitz/gomemcache/memcache)
BuildRequires:  golang(github.com/couchbase/go-couchbase)
BuildRequires:  golang(github.com/go-sql-driver/mysql)
BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/lunny/nodb)
BuildRequires:  golang(github.com/lunny/nodb/config)
BuildRequires:  golang(github.com/siddontang/ledisdb/config)
BuildRequires:  golang(github.com/siddontang/ledisdb/ledis)
BuildRequires:  golang(github.com/smartystreets/goconvey/convey)
BuildRequires:  golang(gopkg.in/ini.v1)
BuildRequires:  golang(gopkg.in/redis.v2)
Requires:       golang >= 1.2.1-3
Requires:       golang(github.com/Unknwon/com)
Requires:       golang(github.com/Unknwon/macaron)
Requires:       golang(github.com/bradfitz/gomemcache/memcache)
Requires:       golang(github.com/couchbase/go-couchbase)
Requires:       golang(github.com/go-sql-driver/mysql)
Requires:       golang(github.com/lib/pq)
Requires:       golang(github.com/lunny/nodb)
Requires:       golang(github.com/lunny/nodb/config)
Requires:       golang(github.com/siddontang/ledisdb/config)
Requires:       golang(github.com/siddontang/ledisdb/ledis)
Requires:       golang(github.com/smartystreets/goconvey/convey)
Requires:       golang(gopkg.in/ini.v1)
Requires:       golang(gopkg.in/redis.v2)
Summary:        %{summary}
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/couchbase) = %{version}-%{release}
Provides:       golang(%{import_path}/ledis) = %{version}-%{release}
Provides:       golang(%{import_path}/memcache) = %{version}-%{release}
Provides:       golang(%{import_path}/mysql) = %{version}-%{release}
Provides:       golang(%{import_path}/nodb) = %{version}-%{release}
Provides:       golang(%{import_path}/postgres) = %{version}-%{release}
Provides:       golang(%{import_path}/redis) = %{version}-%{release}

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
cp -rpav couchbase %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav ledis %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav memcache %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav mysql %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav nodb %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav postgres %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav redis %{buildroot}/%{gopath}/src/%{import_path}/

%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/ledis
# Disabled due to requiring running memached
# GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/memcache
# Disabled due to requiring running mysql
# GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/mysql
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/nodb
# Disabled due to requiring running postgres
# GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/postgres
# Disabled due to requiring running redis
# GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/redis

%files devel
%doc README.md LICENSE
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Wed Apr 15 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.git31e841d
- First package for Fedora


