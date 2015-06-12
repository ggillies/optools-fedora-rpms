%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         smartystreets
%global repo            assertions
# https://github.com/smartystreets/assertions
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          4727d767ce8a81811c40eedc2a836c85aebb4d09
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global bootstrap       0

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Fluent assertion-style functions. Created for goconvey's convey package
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
%if %{bootstrap}
BuildRequires:  golang(github.com/smartystreets/goconvey/convey/reporting)
%endif
Requires:       golang >= 1.2.1-3
%if %{bootstrap}
Requires:       golang(github.com/smartystreets/goconvey/convey/reporting)
%endif
Summary:        %{summary}
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/internal/oglematchers) = %{version}-%{release}
Provides:       golang(%{import_path}/internal/oglemock) = %{version}-%{release}
Provides:       golang(%{import_path}/internal/oglemock/generate) = %{version}-%{release}
Provides:       golang(%{import_path}/internal/oglemock/generate/test_cases) = %{version}-%{release}
Provides:       golang(%{import_path}/internal/oglemock/generate/test_cases/complicated_pkg) = %{version}-%{release}
Provides:       golang(%{import_path}/internal/oglemock/generate/test_cases/renamed_pkg) = %{version}-%{release}
Provides:       golang(%{import_path}/internal/oglemock/sample/mock_io) = %{version}-%{release}
Provides:       golang(%{import_path}/internal/ogletest) = %{version}-%{release}
Provides:       golang(%{import_path}/internal/ogletest/test_cases) = %{version}-%{release}
Provides:       golang(%{import_path}/internal/ogletest/test_cases/mock_image) = %{version}-%{release}
Provides:       golang(%{import_path}/should) = %{version}-%{release}

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
cp -rpav internal %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav should %{buildroot}/%{gopath}/src/%{import_path}/
find %{buildroot}/%{gopath}/src/%{import_path}/ -name '.gitignore' -exec rm {} \;

%check
%if %{bootstrap}
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/internal/oglematchers
%endif

%files devel
%doc LICENSE.md README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Tue Apr 14 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.git4727d76
- First package for Fedora


