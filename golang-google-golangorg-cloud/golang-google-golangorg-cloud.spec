%global debug_package   %{nil}
%global provider        google
%global provider_sub    golang
%global provider_tld    org
%global repo            cloud
%global import_path     %{provider}.%{provider_sub}.%{provider_tld}/%{repo}
%global commit          2e43671e4ad874a7bca65746ff3edb38e6e93762
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{provider_sub}%{provider_tld}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Google Cloud Platform APIs related types and common functions
License:        ASL 2.0
URL:            https://%{import_path}
Source0:        https://code.googlesource.com/gocloud/+archive/%{commit}.tar.gz
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
%{summary}

%package devel
BuildRequires:    golang >= 1.2.1-3
BuildRequires:    golang(golang.org/x/net/context)
BuildRequires:    golang(google.golang.org/api/container/v1beta1)
BuildRequires:    golang(google.golang.org/api/googleapi)
BuildRequires:    golang(google.golang.org/api/pubsub/v1beta1)
BuildRequires:    golang(google.golang.org/api/storage/v1)
BuildRequires:    golang(google.golang.org/appengine)
BuildRequires:    golang(google.golang.org/appengine/file)
BuildRequires:    golang(google.golang.org/appengine/urlfetch)
BuildRequires:    golang(github.com/golang/protobuf/proto)
# cyclic deps, used in tests and examples
#BuildRequires:    golang(golang.org/x/oauth2)
#BuildRequires:    golang(golang.org/x/oauth2/google)
Requires:       golang >= 1.2.1-3
Requires:       golang(golang.org/x/net/context)
Requires:       golang(google.golang.org/api/container/v1beta1)
Requires:       golang(google.golang.org/api/googleapi)
Requires:       golang(google.golang.org/api/pubsub/v1beta1)
Requires:       golang(google.golang.org/api/storage/v1)
Requires:       golang(google.golang.org/appengine)
Requires:       golang(google.golang.org/appengine/file)
Requires:       golang(google.golang.org/appengine/urlfetch)
Requires:       golang(github.com/golang/protobuf/proto)
#Requires:       golang(golang.org/x/oauth2)
#Requires:       golang(golang.org/x/oauth2/google)
Summary:        %{summary}
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/compute/metadata) = %{version}-%{release}
Provides:       golang(%{import_path}/container) = %{version}-%{release}
Provides:       golang(%{import_path}/datastore) = %{version}-%{release}
Provides:       golang(%{import_path}/examples/pubsub/cmdline) = %{version}-%{release}
Provides:       golang(%{import_path}/examples/storage/appengine) = %{version}-%{release}
Provides:       golang(%{import_path}/examples/storage/appenginevm) = %{version}-%{release}
Provides:       golang(%{import_path}/internal) = %{version}-%{release}
Provides:       golang(%{import_path}/internal/datastore) = %{version}-%{release}
Provides:       golang(%{import_path}/internal/testutil) = %{version}-%{release}
Provides:       golang(%{import_path}/pubsub) = %{version}-%{release}
Provides:       golang(%{import_path}/storage) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for 
building other packages which use %{import_path}.

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}/
for dir in compute container datastore examples internal pubsub storage; do
    cp -rpav $dir %{buildroot}/%{gopath}/src/%{import_path}/
done

%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}
#GOPATH={buildroot}/{gopath}:{gopath} go test {import_path}/datastore
#GOPATH={buildroot}/{gopath}:{gopath} go test {import_path}/pubsub
#GOPATH={buildroot}/{gopath}:{gopath} go test {import_path}/storage

%files devel
%doc AUTHORS CONTRIBUTING.md CONTRIBUTORS LICENSE README.md
%{gopath}/src/%{import_path}

%changelog
* Thu Jan 22 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git1c3fdc5
- First package for Fedora
  resolves: #1185281

