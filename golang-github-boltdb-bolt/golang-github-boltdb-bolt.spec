%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         boltdb
%global repo            bolt
# https://github.com/boltdb/bolt
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          3b449559cf34cbcc74460b59041a4399d3226e5a
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        A low-level key/value database for Go
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
Summary:       %{summary}
BuildRequires: golang >= 1.2.1-3
BuildRequires: golang(github.com/codegangsta/cli)
Requires:      golang >= 1.2.1-3
Requires:      golang(github.com/codegangsta/cli)
Provides:      golang(%{import_path}) = %{version}-%{release}

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

# copy directories
for file in ./* ; do
    if [ -d $file ]; then
        cp -rpav $file %{buildroot}%{gopath}/src/%{import_path}/
    fi
done

%check
# tests run too long

%files devel
%doc README.md LICENSE
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Wed Apr 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git3b44955
- First package for Fedora


