%global debug_package   %{nil}
# https://github.com/rainycape/unidecode
%global import_path     gopkgs.com/unidecode.v1
%global commit          4deae2c05236b41cc39f8144ac87a837ba974d40
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-gopkgscom-unidecode
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Unicode transliterator in Golang - Replaces non-ASCII characters with their ASCII approximations
License:        ASL 2.0
URL:            https://%{import_path}
Source0:        https://github.com/rainycape/unidecode/archive/%{commit}/unidecode-%{shortcommit}.tar.gz
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
%{summary}

%package devel
BuildRequires:  golang >= 1.2.1-3
BuildRequires:  golang(gopkgs.com/pool.v1)
Requires:       golang >= 1.2.1-3
Requires:       golang(gopkgs.com/pool.v1)
Summary:        %{summary}
Provides:       golang(%{import_path}) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for 
building other packages which use %{import_path}

%prep
%setup -q -n unidecode-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}/

%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}

%files devel
%doc README.md LICENSE
%dir %{gopath}/src/%{import_path}
%{gopath}/src/%{import_path}

%changelog
* Mon Apr 27 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.git4deae2c
- First package for Fedora


