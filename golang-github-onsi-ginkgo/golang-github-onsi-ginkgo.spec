%global provider	github
%global provider_tld	com
%global project		onsi
%global repo		ginkgo
%global commit		dbb5c6caf33238b57facc1d975b1aaca6b90288c
# https://github.com/onsi/ginkgo
%global import_path	%{provider}.%{provider_tld}/%{project}/%{repo}
%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%global debug_package	%{nil}

Name:		golang-%{provider}-%{project}-%{repo}
Version:	1.1.0
Release:	1%{?dist}
Summary:	A Golang BDD Testing Framework
License:	MIT
URL:		http://%{import_path}
Source0:	https://github.com/%{project}/%{repo}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
%{summary}.

%package devel
BuildRequires:	golang >= 1.2.1-3
BuildRequires:	golang(github.com/onsi/gomega)
Requires:	golang >= 1.2.1-3
Requires:	golang(github.com/onsi/gomega)
Summary:	%{summary}
Provides: golang(%{import_path}) = %{version}-%{release}
Provides: golang(%{import_path}/config) = %{version}-%{release}
Provides: golang(%{import_path}/ginkgo/convert) = %{version}-%{release}
Provides: golang(%{import_path}/ginkgo/interrupthandler) = %{version}-%{release}
Provides: golang(%{import_path}/ginkgo/nodot) = %{version}-%{release}
Provides: golang(%{import_path}/ginkgo/testrunner) = %{version}-%{release}
Provides: golang(%{import_path}/ginkgo/testsuite) = %{version}-%{release}
Provides: golang(%{import_path}/ginkgo/watch) = %{version}-%{release}
Provides: golang(%{import_path}/internal/codelocation) = %{version}-%{release}
Provides: golang(%{import_path}/internal/containernode) = %{version}-%{release}
Provides: golang(%{import_path}/internal/failer) = %{version}-%{release}
Provides: golang(%{import_path}/internal/leafnodes) = %{version}-%{release}
Provides: golang(%{import_path}/internal/remote) = %{version}-%{release}
Provides: golang(%{import_path}/internal/spec) = %{version}-%{release}
Provides: golang(%{import_path}/internal/specrunner) = %{version}-%{release}
Provides: golang(%{import_path}/internal/suite) = %{version}-%{release}
Provides: golang(%{import_path}/internal/testingtproxy) = %{version}-%{release}
Provides: golang(%{import_path}/internal/writer) = %{version}-%{release}
Provides: golang(%{import_path}/reporters) = %{version}-%{release}
Provides: golang(%{import_path}/reporters/stenographer) = %{version}-%{release}
Provides: golang(%{import_path}/types) = %{version}-%{release}

%description devel
%{summary}.

This package contains library source intended for 
building other packages which use p/%{repo}.

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}/
cp -pav {config,ginkgo,integration,internal,reporters,types} %{buildroot}/%{gopath}/src/%{import_path}/

%check
#go test can not be done as there is a circular dependency between golang-github-onsi-ginkgo and golang-github-onsi-gomega package

%files devel
%doc README.md LICENSE CHANGELOG.md 
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Thu Apr 23 2015 jchaloup <jchaloup@redhat.com> - 1.1.0-1
- Bump to upstream dbb5c6caf33238b57facc1d975b1aaca6b90288c
  resolves: #1214619

* Sat Feb 07 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git17ea479
- Add buildtime dependency on github.com/onsi/gomega
- Fix installtime dependency on github.com/onsi/gomega
  related: #1148456

* Fri Feb 06 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git17ea479
- Bump to upstream 17ea479729ee427265ac1e913443018350946ddf
  related: #1148456

* Mon Oct 13 2014 jchaloup <jchaloup@redhat.com> - 0-0.2.git90d6a47
- BuildArch to ExclusiveArch

* Wed Oct 01 2014 Jan Chaloupka <jchaloup@redhat.com> - 0-0.1.git90d6a47
- First package for Fedora




