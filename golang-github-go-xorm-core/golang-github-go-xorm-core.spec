%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         go-xorm
%global repo            core
# https://github.com/go-xorm/core
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          0c84d4c49e1d83083d451918456c5fc75da741e2
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Lightweight & Compitable wrapper of database/sql 
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
BuildRequires:  golang(github.com/mattn/go-sqlite3)
Requires:       golang >= 1.2.1-3
Requires:       golang(github.com/go-sql-driver/mysql)
Requires:       golang(github.com/mattn/go-sqlite3)
Summary:        %{summary}
Provides:       golang(%{import_path}) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for 
building other packages which use %{project}/%{repo}.

%prep
%setup -q -n %{repo}-%{commit}
# Change check from mysql to sqlite
sed -i 's/string = "mysql"/string = "sqlite3"/g' db_test.go

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}/

%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}

%files devel
%doc README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Tue Apr 14 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.git0c84d4c
- First package for Fedora


