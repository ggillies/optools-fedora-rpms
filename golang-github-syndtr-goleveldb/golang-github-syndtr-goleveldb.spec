%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         syndtr
%global repo            goleveldb
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          012f65f74744ed62a80abac6e9a8c86e71c2b6fa
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.2.git%{shortcommit}%{?dist}
Summary:        LevelDB key/value database in Go
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
BuildRequires:  golang(github.com/onsi/ginkgo)
BuildRequires:  golang(github.com/onsi/ginkgo/config)
BuildRequires:  golang(github.com/onsi/gomega)
BuildRequires:  golang(github.com/syndtr/gosnappy/snappy)
Requires:       golang >= 1.2.1-3
Requires:       golang(github.com/onsi/ginkgo)
Requires:       golang(github.com/onsi/ginkgo/config)
Requires:       golang(github.com/onsi/gomega)
Requires:       golang(github.com/syndtr/gosnappy/snappy)
Summary:        %{summary}
Provides:       golang(%{import_path}/leveldb) = %{version}-%{release}
Provides:       golang(%{import_path}/leveldb/cache) = %{version}-%{release}
Provides:       golang(%{import_path}/leveldb/comparer) = %{version}-%{release}
Provides:       golang(%{import_path}/leveldb/errors) = %{version}-%{release}
Provides:       golang(%{import_path}/leveldb/filter) = %{version}-%{release}
Provides:       golang(%{import_path}/leveldb/iterator) = %{version}-%{release}
Provides:       golang(%{import_path}/leveldb/journal) = %{version}-%{release}
Provides:       golang(%{import_path}/leveldb/memdb) = %{version}-%{release}
Provides:       golang(%{import_path}/leveldb/opt) = %{version}-%{release}
Provides:       golang(%{import_path}/leveldb/storage) = %{version}-%{release}
Provides:       golang(%{import_path}/leveldb/table) = %{version}-%{release}
Provides:       golang(%{import_path}/leveldb/testutil) = %{version}-%{release}
Provides:       golang(%{import_path}/leveldb/util) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for 
building other packages which use %{project}/%{repo}.

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav manualtest %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav leveldb %{buildroot}/%{gopath}/src/%{import_path}/

%check
#GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/leveldb
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/leveldb/util
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/leveldb/table
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/leveldb/storage
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/leveldb/memdb
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/leveldb/journal
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/leveldb/iterator
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/leveldb/filter
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/leveldb/cache

%files devel
%doc README.md LICENSE
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Sun May 10 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.git012f65f
- Bump to upstream 012f65f74744ed62a80abac6e9a8c86e71c2b6fa
  resolves: #1220163

* Sat Feb 07 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gite9e2c8f
- First package for Fedora
  resolves: #1190418
