%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         bencaron
%global repo            gosensu
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          11934645244245e1a0a687a1ce46be2cf6d38d7c
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Gosensu is an golang wrapper around the Sensu API
License:        MIT
URL:            https://%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif
BuildRequires:  golang(github.com/stretchr/testify)

%description
%{summary}

%package devel
BuildRequires:  golang >= 1.2.1-3
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

%check
# Disabled due to requiring working networking
# export SENSU_SERVER_URL="http://hidden-ravine-4272.herokuapp.com"
# GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}

%files devel
%doc README.md LICENSE
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Mon Feb 02 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.git1193464
- First package for Fedora


