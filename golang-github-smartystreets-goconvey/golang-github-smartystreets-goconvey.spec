%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         smartystreets
%global repo            goconvey
# https://github.com/smartystreets/goconvey
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          eb2e83c1df892d2c9ad5a3c85672da30be585dfd
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global bootstrap 1

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        GoConvey is a tool for writing better go tests
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
BuildRequires:  golang(github.com/jtolds/gls)
%if %{bootstrap} == 0
BuildRequires:  golang(github.com/smartystreets/assertions)
%endif
Requires:       golang >= 1.2.1-3
Requires:       golang(github.com/jtolds/gls)
%if %{bootstrap} == 0
Requires:       golang(github.com/smartystreets/assertions)
%endif
Summary:        %{summary}
Provides:       golang(%{import_path}/convey) = %{version}-%{release}
Provides:       golang(%{import_path}/convey/gotest) = %{version}-%{release}
Provides:       golang(%{import_path}/convey/reporting) = %{version}-%{release}
Provides:       golang(%{import_path}/examples) = %{version}-%{release}
Provides:       golang(%{import_path}/web/server/api) = %{version}-%{release}
Provides:       golang(%{import_path}/web/server/contract) = %{version}-%{release}
Provides:       golang(%{import_path}/web/server/executor) = %{version}-%{release}
Provides:       golang(%{import_path}/web/server/messaging) = %{version}-%{release}
Provides:       golang(%{import_path}/web/server/parser) = %{version}-%{release}
Provides:       golang(%{import_path}/web/server/system) = %{version}-%{release}
Provides:       golang(%{import_path}/web/server/watch) = %{version}-%{release}
Provides:       golang(%{import_path}/web/server/watch/integration_testing/sub) = %{version}-%{release}

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
cp -rpav convey %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav examples %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav web %{buildroot}/%{gopath}/src/%{import_path}/
find %{buildroot}/%{gopath}/src/%{import_path}/ -name '.gitignore' -exec rm {} \;

%check
%if %{bootstrap} == 0
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/convey
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/convey/reporting
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/examples
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/web/server/api
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/web/server/executor
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/web/server/parser
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/web/server/system
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/web/server/watch
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/web/server/watch/integration_testing/sub
%endif

%files devel
%doc CONTRIBUTING.md LICENSE.md README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Tue Apr 14 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.giteb2e83c
- First package for Fedora


