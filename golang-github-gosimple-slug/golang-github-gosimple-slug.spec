%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         gosimple
%global repo            slug
# https://github.com/gosimple/slug
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          a2392a4a87fa0366cbff131d3fd421f83f52492f
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        URL-friendly slugify with multiple languages support
License:        MPLv2.0
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
BuildRequires:  golang(gopkgs.com/unidecode.v1)
Requires:       golang >= 1.2.1-3
Requires:       golang(gopkgs.com/unidecode.v1)
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
%doc README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Mon Apr 27 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.gita2392a4
- First package for Fedora


