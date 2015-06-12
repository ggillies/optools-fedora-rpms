%global debug_package   %{nil}
# https://github.com/vmihailenco/msgpack
%global import_path     gopkg.in/vmihailenco/msgpack.v2
%global commit          61a9533424bd3e41b0a72e106aad32a4ebbc26be
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-gopkg-vmihailenco-msgpack
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Msgpack encoding for Golang
License:        BSD
URL:            https://%{import_path}
Source0:        https://github.com/vmihailenco/msgpack/archive/%{shortcommit}/msgpack-%{shortcommit}.tar.gz
# Removed as it's only needed for tests and is depreciated upstream
Patch0:         golang-gopkg-vmihailenco-msgpack-patch-out-go-msgpack.patch
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
%{summary}

%package devel
BuildRequires:  golang >= 1.2.1-3
BuildRequires:  golang(github.com/ugorji/go/codec)
BuildRequires:  golang(gopkg.in/check.v1)
Requires:       golang >= 1.2.1-3
Requires:       golang(github.com/ugorji/go/codec)
Requires:       golang(gopkg.in/check.v1)
Summary:        %{summary}
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/codes) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for 
building other packages which use %{project}/%{repo}.

%prep
%setup -q -n msgpack-%{commit}
%patch0

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav codes %{buildroot}/%{gopath}/src/%{import_path}/


%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}

%files devel
%doc README.md LICENSE
%dir %{gopath}/src/%{import_path}
%{gopath}/src/%{import_path}

%changelog
* Thu Apr 16 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.git61a9533
- First package for Fedora
