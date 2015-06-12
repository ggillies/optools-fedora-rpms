%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         siddontang
%global repo            ledisdb
# https://github.com/siddontang/ledisdb
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          68932326409a78e10ae6bf8b809b556940e0eb4a
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        a high performance NoSQL powered by Go 
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
BuildRequires:  golang(launchpad.net/gocheck)
BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/alicebob/miniredis)
BuildRequires:  golang(github.com/boltdb/bolt)
BuildRequires:  golang(github.com/codegangsta/cli)
BuildRequires:  golang(github.com/cupcake/rdb)
BuildRequires:  golang(github.com/cupcake/rdb/crc64)
BuildRequires:  golang(github.com/cupcake/rdb/nopdecoder)
BuildRequires:  golang(github.com/edsrzf/mmap-go)
BuildRequires:  golang(github.com/onsi/ginkgo)
BuildRequires:  golang(github.com/onsi/ginkgo/config)
BuildRequires:  golang(github.com/onsi/gomega)
BuildRequires:  golang(github.com/siddontang/go/log)
BuildRequires:  golang(github.com/siddontang/go/snappy)
BuildRequires:  golang(github.com/siddontang/go/hack)
BuildRequires:  golang(github.com/siddontang/go/num)
BuildRequires:  golang(github.com/siddontang/go/filelock)
BuildRequires:  golang(github.com/siddontang/go/ioutil2)
BuildRequires:  golang(github.com/siddontang/go/sync2)
BuildRequires:  golang(github.com/siddontang/go/bson)
BuildRequires:  golang(github.com/siddontang/goredis)
BuildRequires:  golang(github.com/siddontang/rdb)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/iterator)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/opt)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/util)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/comparer)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/testutil)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/memdb)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/storage)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/journal)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/errors)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/filter)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/cache)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/table)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb)
BuildRequires:  golang(github.com/syndtr/gosnappy/snappy)
BuildRequires:  golang(github.com/ugorji/go/codec)
BuildRequires:  golang(gopkg.in/vmihailenco/msgpack.v2)
BuildRequires:  golang(gopkg.in/check.v1)
BuildRequires:  golang(gopkg.in/mgo.v2/bson)
Requires:       golang >= 1.2.1-3
Requires:       golang(launchpad.net/gocheck)
Requires:       golang(github.com/BurntSushi/toml)
Requires:       golang(github.com/alicebob/miniredis)
Requires:       golang(github.com/boltdb/bolt)
Requires:       golang(github.com/codegangsta/cli)
Requires:       golang(github.com/cupcake/rdb)
Requires:       golang(github.com/cupcake/rdb/crc64)
Requires:       golang(github.com/cupcake/rdb/nopdecoder)
Requires:       golang(github.com/edsrzf/mmap-go)
Requires:       golang(github.com/onsi/ginkgo)
Requires:       golang(github.com/onsi/ginkgo/config)
Requires:       golang(github.com/onsi/gomega)
Requires:       golang(github.com/siddontang/go/log)
Requires:       golang(github.com/siddontang/go/snappy)
Requires:       golang(github.com/siddontang/go/hack)
Requires:       golang(github.com/siddontang/go/num)
Requires:       golang(github.com/siddontang/go/filelock)
Requires:       golang(github.com/siddontang/go/ioutil2)
Requires:       golang(github.com/siddontang/go/sync2)
Requires:       golang(github.com/siddontang/go/bson)
Requires:       golang(github.com/siddontang/goredis)
Requires:       golang(github.com/siddontang/rdb)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/iterator)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/opt)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/util)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/comparer)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/testutil)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/memdb)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/storage)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/journal)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/errors)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/filter)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/cache)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/table)
Requires:       golang(github.com/syndtr/goleveldb/leveldb)
Requires:       golang(github.com/syndtr/gosnappy/snappy)
Requires:       golang(github.com/ugorji/go/codec)
Requires:       golang(gopkg.in/vmihailenco/msgpack.v2)
Requires:       golang(gopkg.in/check.v1)
Requires:       golang(gopkg.in/mgo.v2/bson)
Summary:        %{summary}
Provides:       golang(%{import_path}/config) = %{version}-%{release}
Provides:       golang(%{import_path}/ledis) = %{version}-%{release}
Provides:       golang(%{import_path}/rpl) = %{version}-%{release}
Provides:       golang(%{import_path}/server) = %{version}-%{release}
Provides:       golang(%{import_path}/store) = %{version}-%{release}
Provides:       golang(%{import_path}/store/boltdb) = %{version}-%{release}
Provides:       golang(%{import_path}/store/driver) = %{version}-%{release}
Provides:       golang(%{import_path}/store/goleveldb) = %{version}-%{release}
Provides:       golang(%{import_path}/store/leveldb) = %{version}-%{release}
Provides:       golang(%{import_path}/store/mdb) = %{version}-%{release}
Provides:       golang(%{import_path}/store/rocksdb) = %{version}-%{release}
Provides:       golang(%{import_path}/vendor/gomdb) = %{version}-%{release}
Provides:       golang(%{import_path}/vendor/lua) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for 
building other packages which use %{project}/%{repo}.

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
rm -rf Godeps
rm -rf vendor
cp -rpav cmd %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav config %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav doc %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav etc %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav ledis %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav rpl %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav server %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav store %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav tools %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav upgrade %{buildroot}/%{gopath}/src/%{import_path}/

%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/config
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/ledis
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/rpl
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/server
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/store

%files devel
%doc README.md LICENSE
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Wed Apr 15 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.git6893232
- First package for Fedora


