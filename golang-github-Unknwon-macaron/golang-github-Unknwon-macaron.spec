%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         Unknwon
%global repo            macaron
# https://github.com/Unknwon/macaron
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          93de4f3fad97bf246b838f828e2348f46f21f20a
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Package macaron is a high productive and modular design web framework in Go
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
BuildRequires:  golang(github.com/Unknwon/com)
BuildRequires:  golang(github.com/smartystreets/goconvey/convey)
BuildRequires:  golang(gopkg.in/ini.v1)
Requires:       golang >= 1.2.1-3
Requires:       golang(github.com/Unknwon/com)
Requires:       golang(github.com/smartystreets/goconvey/convey)
Requires:       golang(gopkg.in/ini.v1)
Summary:        %{summary}
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/inject) = %{version}-%{release}

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
cp -rpav fixtures %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav inject %{buildroot}/%{gopath}/src/%{import_path}/

%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/inject

%files devel
%doc README.md LICENSE
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Tue Apr 14 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.git93de4f3
- First package for Fedora


