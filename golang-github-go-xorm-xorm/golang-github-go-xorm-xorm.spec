%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         go-xorm
%global repo            xorm
# https://github.com/go-xorm/xorm
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          276fc097cbd031c610aab2195eec7b4d771fb9fd
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Simple and Powerful ORM for Go
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
BuildRequires:  golang(github.com/go-sql-driver/mysql)
BuildRequires:  golang(github.com/go-xorm/core)
BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/mattn/go-sqlite3)
Requires:       golang >= 1.2.1-3
Requires:       golang(github.com/go-sql-driver/mysql)
Requires:       golang(github.com/go-xorm/core)
Requires:       golang(github.com/lib/pq)
Requires:       golang(github.com/mattn/go-sqlite3)
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
cp -rpav docs %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav examples %{buildroot}/%{gopath}/src/%{import_path}/

%check

%files devel
%doc CONTRIBUTING.md README_CN.md README.md LICENSE
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Tue Apr 14 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.git276fc09
- First package for Fedora


