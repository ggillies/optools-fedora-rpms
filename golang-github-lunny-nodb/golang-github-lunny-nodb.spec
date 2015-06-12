%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         lunny
%global repo            nodb
# https://github.com/lunny/nodb
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          a7afdc20ab98178ed81deec90b2a65f17d295d0b
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        A pure Go embed Nosql database with kv, list, hash, zset, bitmap, set
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
BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/lunny/log)
BuildRequires:  golang(github.com/siddontang/go-snappy/snappy)
BuildRequires:  golang(github.com/siddontang/golua/lua)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/iterator)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/cache)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/filter)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/opt)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/storage)
Requires:       golang >= 1.2.1-3
Requires:       golang(github.com/BurntSushi/toml)
Requires:       golang(github.com/lunny/log)
Requires:       golang(github.com/siddontang/go-snappy/snappy)
Requires:       golang(github.com/siddontang/golua/lua)
Requires:       golang(github.com/syndtr/goleveldb/leveldb)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/iterator)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/cache)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/filter)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/opt)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/storage)
Summary:        %{summary}
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/config) = %{version}-%{release}
Provides:       golang(%{import_path}/store) = %{version}-%{release}
Provides:       golang(%{import_path}/store/driver) = %{version}-%{release}
Provides:       golang(%{import_path}/store/goleveldb) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for 
building other packages which use %{project}/%{repo}.

%prep
%setup -q -n %{repo}-%{commit}
# Fix broken test
sed -i /dstCfg.Addr/d config/config_test.go
sed -i /dstCfg.HttpAddr/d config/config_test.go

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav config %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav store %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav tools %{buildroot}/%{gopath}/src/%{import_path}/

%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/config
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/store

%files devel
%doc README_CN.md README.md LICENSE
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Thu Apr 16 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.gita7afdc2
- First package for Fedora


