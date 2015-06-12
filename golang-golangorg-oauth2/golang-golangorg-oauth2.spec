%global debug_package   %{nil}
# https://github.com/golang/oauth2
%global import_path     golang.org/x/oauth2
%global commit          ec6d5d770f531108a6464462b2201b74fcd09314
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-golangorg-oauth2
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Go OAuth2 https://godoc.org/golang.org/x/oauth2
License:        BSD
URL:            https://%{import_path}
Source0:        https://github.com/golang/oauth2/archive/%{commit}/oauth2-%{shortcommit}.tar.gz
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
%{summary}

%package devel
BuildRequires:  golang >= 1.2.1-3
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(google.golang.org/appengine/urlfetch)
BuildRequires:  golang(google.golang.org/appengine)
BuildRequires:  golang(google.golang.org/cloud/compute/metadata)
Requires:       golang >= 1.2.1-3
Requires:       golang(golang.org/x/net/context)
Requires:       golang(google.golang.org/appengine/urlfetch)
Requires:       golang(google.golang.org/appengine)
Requires:       golang(google.golang.org/cloud/compute/metadata)
Summary:        %{summary}
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/clientcredentials) = %{version}-%{release}
Provides:       golang(%{import_path}/facebook) = %{version}-%{release}
Provides:       golang(%{import_path}/github) = %{version}-%{release}
Provides:       golang(%{import_path}/google) = %{version}-%{release}
Provides:       golang(%{import_path}/internal) = %{version}-%{release}
Provides:       golang(%{import_path}/jws) = %{version}-%{release}
Provides:       golang(%{import_path}/jwt) = %{version}-%{release}
Provides:       golang(%{import_path}/linkedin) = %{version}-%{release}
Provides:       golang(%{import_path}/odnoklassniki) = %{version}-%{release}
Provides:       golang(%{import_path}/paypal) = %{version}-%{release}
Provides:       golang(%{import_path}/vk) = %{version}-%{release}


%description devel
%{summary}

This package contains library source intended for 
building other packages which use %{import_path}

%prep
%setup -q -n oauth2-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav clientcredentials %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav facebook %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav github %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav google %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav internal %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav jws %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav jwt %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav linkedin %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav odnoklassniki %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav paypal %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav vk %{buildroot}/%{gopath}/src/%{import_path}/

%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/clientcredentials
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/google
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/internal
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/jwt

%files devel
%doc CONTRIBUTING.md README.md LICENSE AUTHORS
%dir %{gopath}/src/%{import_path}
%{gopath}/src/%{import_path}

%changelog
* Wed Apr 29 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.gitec6d5d7
- First package for Fedora


