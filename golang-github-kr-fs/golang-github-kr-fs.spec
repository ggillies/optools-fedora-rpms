%global provider	github
%global provider_tld	com
%global project		kr
%global repo		fs
%global commit		2788f0dbd16903de03cb8186e5c7d97b69ad387b

%global import_path	%{provider}.%{provider_tld}/%{project}/%{repo}
%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%global debug_package	%{nil}

Name:		golang-%{provider}-%{project}-%{repo}
Version:	0
Release:	0.1.git%{shortcommit}%{?dist}
Summary:	Provides Go filesystem-related functions
License:	BSD
URL:		http://%{import_path}
Source0:	https://%{import_path}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
BuildArch:	noarch

%description
%{summary}

%package devel
BuildRequires:	golang >= 1.2.1-3
Requires:	golang >= 1.2.1-3
Summary:	%{summary}
Provides:	golang(%{import_path}) = %{version}-%{release}

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
%doc LICENSE Readme
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%dir %{gopath}/src/%{import_path}
%{gopath}/src/%{import_path}/*.go

%changelog
* Wed Oct 01 2014 Jan Chaloupka <jchaloup@redhat> - 0-0.1.git2788f0d
- First package for Fedora





