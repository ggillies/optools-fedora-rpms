%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         couchbase
%global repo            cbauth
# https://github.com/couchbase/cbauth
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          f75435015eb8b6be3321ad92b256876c04632857
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global bootstrap       1

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        cbauth is simple way to get credentials to access cluster services
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
%if %{bootstrap} == 0
BuildRequires:  golang(github.com/couchbase/go-couchbase)
%endif
BuildRequires:  golang(github.com/couchbase/gomemcached/client)
Requires:       golang >= 1.2.1-3
Requires:       golang(github.com/couchbase/go-couchbase)
Requires:       golang(github.com/couchbase/gomemcached/client)
Summary:        %{summary}
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/cbauthimpl) = %{version}-%{release}
Provides:       golang(%{import_path}/metakv) = %{version}-%{release}
Provides:       golang(%{import_path}/revrpc) = %{version}-%{release}
Provides:       golang(%{import_path}/saslauthd) = %{version}-%{release}

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
cp -rpav cbauthimpl %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav cmd %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav metakv %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav revrpc %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav saslauthd %{buildroot}/%{gopath}/src/%{import_path}/

%check
%if %{bootstrap} == 0
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/metakv
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/saslauthd
%endif

%files devel
%doc LICENSE
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Wed Apr 15 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.gitf754350
- First package for Fedora


