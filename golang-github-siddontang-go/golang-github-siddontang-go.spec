%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         siddontang
%global repo            go
# https://github.com/siddontang/go
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          530a23162549a31baa14dfa3b647a9eccee8878f
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Golang library by siddontang
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
BuildRequires:  golang(github.com/gorilla/websocket)
BuildRequires:  golang(gopkg.in/check.v1)
BuildRequires:  golang(gopkg.in/mgo.v2/bson)
Requires:       golang >= 1.2.1-3
Requires:       golang(github.com/gorilla/websocket)
Requires:       golang(gopkg.in/check.v1)
Requires:       golang(gopkg.in/mgo.v2/bson)
Summary:        %{summary}
Provides:       golang(%{import_path}/arena) = %{version}-%{release}
Provides:       golang(%{import_path}/bson) = %{version}-%{release}
Provides:       golang(%{import_path}/bytes2) = %{version}-%{release}
Provides:       golang(%{import_path}/cache) = %{version}-%{release}
Provides:       golang(%{import_path}/config) = %{version}-%{release}
Provides:       golang(%{import_path}/exec2) = %{version}-%{release}
Provides:       golang(%{import_path}/filelock) = %{version}-%{release}
Provides:       golang(%{import_path}/hack) = %{version}-%{release}
Provides:       golang(%{import_path}/ioutil2) = %{version}-%{release}
Provides:       golang(%{import_path}/list2) = %{version}-%{release}
Provides:       golang(%{import_path}/log) = %{version}-%{release}
Provides:       golang(%{import_path}/num) = %{version}-%{release}
Provides:       golang(%{import_path}/ring) = %{version}-%{release}
Provides:       golang(%{import_path}/rpc) = %{version}-%{release}
Provides:       golang(%{import_path}/snappy) = %{version}-%{release}
Provides:       golang(%{import_path}/sync2) = %{version}-%{release}
Provides:       golang(%{import_path}/tb) = %{version}-%{release}
Provides:       golang(%{import_path}/time2) = %{version}-%{release}
Provides:       golang(%{import_path}/timingwheel) = %{version}-%{release}
Provides:       golang(%{import_path}/websocket) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for 
building other packages which use %{project}/%{repo}.

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav arena %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav bson %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav bytes2 %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav cache %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav config %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav exec2 %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav filelock %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav hack %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav ioutil2 %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav list2 %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav log %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav num %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav ring %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav rpc %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav snappy %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav sync2 %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav tb %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav time2 %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav timingwheel %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav websocket %{buildroot}/%{gopath}/src/%{import_path}/

%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/arena
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/bson
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/bytes2
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/cache
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/config
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/exec2
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/filelock
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/hack
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/ioutil2
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/list2
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/log
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/num
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/ring
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/rpc
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/snappy
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/sync2
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/time2
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/timingwheel
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/websocket

%files devel
%doc README.md LICENSE
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Thu Apr 16 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.git530a231
- First package for Fedora


