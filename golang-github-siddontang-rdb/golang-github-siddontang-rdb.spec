%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         siddontang
%global repo            rdb
# https://github.com/siddontang/rdb
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          fc89ed2e418d27e3ea76e708e54276d2b44ae9cf
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Handling Redis RDB format
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
BuildRequires:  golang(github.com/cupcake/rdb)
BuildRequires:  golang(github.com/cupcake/rdb/nopdecoder)
Requires:       golang >= 1.2.1-3
Requires:       golang(github.com/cupcake/rdb)
Requires:       golang(github.com/cupcake/rdb/nopdecoder)
Summary:        %{summary}
Provides:       golang(%{import_path}) = %{version}-%{release}

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

%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}

%files devel
%doc README.md LICENSE
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Thu Apr 16 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.gitfc89ed2
- First package for Fedora


