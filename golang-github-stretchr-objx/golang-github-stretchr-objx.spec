%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         stretchr
%global repo            objx
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          cbeaeb16a013161a98496fad62933b1d21786672
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global bootstrap 1

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Go package for dealing with maps, slices, JSON and other data
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
%if 0%{bootstrap} == 0
BuildRequires:  golang(github.com/stretchr/testify)
%endif
Requires:       golang >= 1.2.1-3
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
cp -rpav codegen %{buildroot}/%{gopath}/src/%{import_path}/

%check
%if 0%{bootstrap} == 0
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}
%endif

%files devel
%doc LICENSE.md README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Tue Feb 03 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.gitcbeaeb1
- First package for Fedora


