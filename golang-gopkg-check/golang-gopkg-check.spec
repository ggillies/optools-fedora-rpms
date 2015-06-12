%global debug_package   %{nil}
%global commit          91ae5f88a67b14891cfd43895b01164f6c120420
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global provider        gopkg
%global provider_tld    in
%global repo            check
%global version         v1
%global import_path     %{provider}.%{provider_tld}/%{repo}.%{version}
%global import_path_sec launchpad.net/gocheck

# github.com/motain/gocheck, cloned from github.com/go-check/check on Oct 23, 2013
%global mcommit         10bfe0586b48cbca10fe6c43d6e18136f25f8c0c
%global mscommit        %(c=%{mcommit}; echo ${c:0:7})
%global mimport_path    github.com/motain/gocheck

Name:           golang-gopkg-%{repo}
Version:        0
Release:        4%{?dist}
Summary:        Rich testing for the Go language
License:        BSD
# gopkg.in/check.v1
URL:            http://%{import_path}
Source0:	https://github.com/go-%{repo}/%{repo}/archive/%{mcommit}/%{repo}-%{mscommit}.tar.gz
Source1:        https://github.com/go-%{repo}/%{repo}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
Obsoletes:	golang-launchpad-gocheck
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
%{summary}

%package devel
BuildRequires:  golang >= 1.2.1-3
Requires:       golang >= 1.2.1-3
Summary:        %{summary}
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:	golang(%{import_path_sec}) = %{version}-%{release}
Provides:	golang(%{mimport_path}) = %{version}-%{release}
Obsoletes:	golang-launchpad-gocheck-devel

%description devel
%{summary}

This package contains library source intended for 
building other packages which use %{import_path}.

%prep
%setup -n %{repo}-%{mcommit} -q
%setup -n %{repo}-%{commit} -q -T -b 1

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}/
install -d -p %{buildroot}/%{gopath}/src/%{import_path_sec}/
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path_sec}/
pushd ../%{repo}-%{mcommit}
install -d -p %{buildroot}/%{gopath}/src/%{mimport_path}/
cp -pav *.go %{buildroot}/%{gopath}/src/%{mimport_path}/

%check
#GOPATH={buildroot}{gopath}:{gopath} go test {import_path}

%files devel
%doc LICENSE README.md
# once src/gopkg.in gets into golang package, remove the line bellow
%{gopath}/src/%{import_path}
%dir %{gopath}/src/launchpad.net
%{gopath}/src/%{import_path_sec}
%dir %{gopath}/src/github.com/motain
%{gopath}/src/github.com/motain/gocheck

%changelog
* Tue Jan 13 2015 jchaloup <jchaloup@redhat.com> - 0-4
- Add github.com/motain/gocheck into Provides
  related: #1151779

* Tue Jan 13 2015 jchaloup <jchaloup@redhat.com> - 0-3
- Add github.com/motain/gocheck into devel subpackage
  related: #1151779

* Tue Dec 09 2014 jchaloup <jchaloup@redhat.com> - 0-2
- Obsolete golang-launchpad-gocheck-devel with devel subpackage
  related: #1151779

* Fri Oct 10 2014 Jan Chaloupka <jchaloup@redhat.com> - 0-1
- First package for Fedora
