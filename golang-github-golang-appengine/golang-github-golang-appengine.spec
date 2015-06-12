%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         golang
%global repo            appengine
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          1c3fdc51e1021e4822cf8475c97d3a14a2a6648e
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global rimport_path    google.golang.org/appengine

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Go App Engine for Managed VMs
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
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(github.com/golang/protobuf/proto)
Requires:       golang >= 1.2.1-3
Requires:       golang(golang.org/x/net/context)
Requires:       golang(github.com/golang/protobuf/proto)
Summary:        %{summary}
Provides:       golang(%{rimport_path}) = %{version}-%{release}
Provides:       golang(%{rimport_path}/channel) = %{version}-%{release}
Provides:       golang(%{rimport_path}/datastore) = %{version}-%{release}
Provides:       golang(%{rimport_path}/delay) = %{version}-%{release}
Provides:       golang(%{rimport_path}/demos/guestbook) = %{version}-%{release}
Provides:       golang(%{rimport_path}/demos/helloworld) = %{version}-%{release}
Provides:       golang(%{rimport_path}/file) = %{version}-%{release}
Provides:       golang(%{rimport_path}/image) = %{version}-%{release}
Provides:       golang(%{rimport_path}/internal) = %{version}-%{release}
Provides:       golang(%{rimport_path}/internal/aetesting) = %{version}-%{release}
Provides:       golang(%{rimport_path}/internal/app_identity) = %{version}-%{release}
Provides:       golang(%{rimport_path}/internal/base) = %{version}-%{release}
Provides:       golang(%{rimport_path}/internal/channel) = %{version}-%{release}
Provides:       golang(%{rimport_path}/internal/datastore) = %{version}-%{release}
Provides:       golang(%{rimport_path}/internal/image) = %{version}-%{release}
Provides:       golang(%{rimport_path}/internal/log) = %{version}-%{release}
Provides:       golang(%{rimport_path}/internal/mail) = %{version}-%{release}
Provides:       golang(%{rimport_path}/internal/memcache) = %{version}-%{release}
Provides:       golang(%{rimport_path}/internal/modules) = %{version}-%{release}
Provides:       golang(%{rimport_path}/internal/remote_api) = %{version}-%{release}
Provides:       golang(%{rimport_path}/internal/search) = %{version}-%{release}
Provides:       golang(%{rimport_path}/internal/taskqueue) = %{version}-%{release}
Provides:       golang(%{rimport_path}/internal/urlfetch) = %{version}-%{release}
Provides:       golang(%{rimport_path}/internal/user) = %{version}-%{release}
Provides:       golang(%{rimport_path}/internal/xmpp) = %{version}-%{release}
Provides:       golang(%{rimport_path}/log) = %{version}-%{release}
Provides:       golang(%{rimport_path}/mail) = %{version}-%{release}
Provides:       golang(%{rimport_path}/memcache) = %{version}-%{release}
Provides:       golang(%{rimport_path}/module) = %{version}-%{release}
Provides:       golang(%{rimport_path}/remote_api) = %{version}-%{release}
Provides:       golang(%{rimport_path}/search) = %{version}-%{release}
Provides:       golang(%{rimport_path}/taskqueue) = %{version}-%{release}
Provides:       golang(%{rimport_path}/urlfetch) = %{version}-%{release}
Provides:       golang(%{rimport_path}/user) = %{version}-%{release}
Provides:       golang(%{rimport_path}/xmpp) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for 
building other packages which use %{project}/%{repo}.

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{rimport_path}/
cp -pav *.go %{buildroot}/%{gopath}/src/%{rimport_path}/
cp -rpav xmpp %{buildroot}/%{gopath}/src/%{rimport_path}/
cp -rpav user %{buildroot}/%{gopath}/src/%{rimport_path}/
cp -rpav urlfetch %{buildroot}/%{gopath}/src/%{rimport_path}/
cp -rpav taskqueue %{buildroot}/%{gopath}/src/%{rimport_path}/
cp -rpav search %{buildroot}/%{gopath}/src/%{rimport_path}/
cp -rpav remote_api %{buildroot}/%{gopath}/src/%{rimport_path}/
cp -rpav module %{buildroot}/%{gopath}/src/%{rimport_path}/
cp -rpav memcache %{buildroot}/%{gopath}/src/%{rimport_path}/
cp -rpav mail %{buildroot}/%{gopath}/src/%{rimport_path}/
cp -rpav log %{buildroot}/%{gopath}/src/%{rimport_path}/
cp -rpav internal %{buildroot}/%{gopath}/src/%{rimport_path}/
cp -rpav image %{buildroot}/%{gopath}/src/%{rimport_path}/
cp -rpav file %{buildroot}/%{gopath}/src/%{rimport_path}/
cp -rpav demos %{buildroot}/%{gopath}/src/%{rimport_path}/
cp -rpav delay %{buildroot}/%{gopath}/src/%{rimport_path}/
cp -rpav datastore %{buildroot}/%{gopath}/src/%{rimport_path}/
cp -rpav channel %{buildroot}/%{gopath}/src/%{rimport_path}/

chmod -x %{buildroot}/%{gopath}/src/%{rimport_path}/internal/datastore/datastore_v3.proto

%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{rimport_path}
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{rimport_path}/xmpp
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{rimport_path}/user
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{rimport_path}/taskqueue
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{rimport_path}/search
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{rimport_path}/remote_api
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{rimport_path}/module
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{rimport_path}/memcache
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{rimport_path}/mail
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{rimport_path}/log
#GOPATH={buildroot}/{gopath}:{gopath} go test {rimport_path}/internal
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{rimport_path}/delay
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{rimport_path}/datastore
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{rimport_path}/channel

%files devel
%doc README.md LICENSE
%{gopath}/src/%{rimport_path}

%changelog
* Thu Jan 22 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git1c3fdc5
- First package for Fedora
  resolves: #1185082
