%global provider	github
%global provider_tld	com
%global project		onsi
%global repo		gomega
%global commit		8adf9e1730c55cdc590de7d49766cb2acc88d8f2

%global import_path	%{provider}.%{provider_tld}/%{project}/%{repo}
%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%global debug_package	%{nil}

Name:		golang-%{provider}-%{project}-%{repo}
Version:	0
Release:	0.3.git%{shortcommit}%{?dist}
Summary:	Ginkgo's Preferred Matcher Library
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
Requires:	golang >= 1.2.1-3
Requires:	golang(github.com/onsi/gomega)
Summary:	%{summary}
Provides:	golang(%{import_path}) = %{version}-%{release}
Provides:	golang(%{import_path}/format) = %{version}-%{release}
Provides:	golang(%{import_path}/gbytes) = %{version}-%{release}
Provides:	golang(%{import_path}/gexec) = %{version}-%{release}
Provides:	golang(%{import_path}/gexec/_fixture/firefly) = %{version}-%{release}
Provides:	golang(%{import_path}/ghttp) = %{version}-%{release}
Provides:	golang(%{import_path}/internal/assertion) = %{version}-%{release}
Provides:	golang(%{import_path}/internal/asyncassertion) = %{version}-%{release}
Provides:	golang(%{import_path}/internal/fakematcher) = %{version}-%{release}
Provides:	golang(%{import_path}/internal/testingtsupport) = %{version}-%{release}
Provides:	golang(%{import_path}/matchers) = %{version}-%{release}
Provides:	golang(%{import_path}/types) = %{version}-%{release}

%description devel
%{summary}.

This package contains library source intended for 
building other packages which use %{project}/%{repo}.

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}/
cp -pav {format,gbytes,gexec,ghttp,internal,matchers,types} %{buildroot}/%{gopath}/src/%{import_path}/

%check
#go test can not be done as there is a circular dependency between golang-github-onsi-ginkgo and golang-github-onsi-gomega package

%files devel
%doc README.md LICENSE CHANGELOG.md 
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%dir %{gopath}/src/%{import_path}/format
%dir %{gopath}/src/%{import_path}/gbytes
%dir %{gopath}/src/%{import_path}/gexec
%dir %{gopath}/src/%{import_path}/ghttp
%dir %{gopath}/src/%{import_path}/internal
%dir %{gopath}/src/%{import_path}/matchers
%dir %{gopath}/src/%{import_path}/types
%{gopath}/src/%{import_path}/*.go
%{gopath}/src/%{import_path}/*/*

%changelog
* Fri Feb 06 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git8adf9e1
- Bump to upstream 8adf9e1730c55cdc590de7d49766cb2acc88d8f2
  related: #1148452

* Mon Oct 13 2014 jchaloup <jchaloup@redhat.com> - 0-0.2.gita0ee4df
- BuildArch to ExclusiveArch

* Wed Oct 01 2014 root - 0-0.1.git90d6a47
- First package for Fedora




