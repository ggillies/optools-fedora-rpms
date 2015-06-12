%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         syndtr
%global repo            gosnappy
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          156a073208e131d7d2e212cb749feae7c339e846
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.2.git%{shortcommit}%{?dist}
Summary:        Implementation of the Snappy compression format for Go
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
Requires:       golang >= 1.2.1-3
Summary:        %{summary}
Provides:       golang(%{import_path}/snappy) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for 
building other packages which use %{project}/%{repo}.

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav snappy %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav lib %{buildroot}/%{gopath}/src/%{import_path}/

%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/snappy

%files devel
%doc LICENSE README
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Sun May 10 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.git156a073
- Bump to upstream 156a073208e131d7d2e212cb749feae7c339e846
  resolves: #1220164

* Sat Feb 07 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitce8acff
- First package for Fedora
  resolves: #1190411
