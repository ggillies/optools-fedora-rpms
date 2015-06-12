%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         garyburd
%global repo            redigo
# https://github.com/garyburd/redigo
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          535138d7bcd717d6531c701ef5933d98b1866257
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Go client for Redis
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
Requires:       golang >= 1.2.1-3
Summary:        %{summary}
Provides:       golang(%{import_path}/internal) = %{version}-%{release}
Provides:       golang(%{import_path}/internal/redistest) = %{version}-%{release}
Provides:       golang(%{import_path}/redis) = %{version}-%{release}
Provides:       golang(%{import_path}/redisx) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for 
building other packages which use %{project}/%{repo}.

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav internal %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav redis %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav redisx %{buildroot}/%{gopath}/src/%{import_path}/

%check
# Tests disabled due to requiring a running redis instance
# GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/redis
# GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/redisx

%files devel
%doc
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Wed Apr 15 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.git535138d
- First package for Fedora


