%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         BurntSushi
%global repo            toml
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          2ceedfee35ad3848e49308ab0c9a4f640cfb5fb2
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.3.git%{shortcommit}%{?dist}
Summary:        TOML parser and encoder for Go with reflection
License:        BSD
URL:            https://%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
ExclusiveArch:  %{ix86} x86_64 %{arm}
Provides:       tomlv = %{version}-%{release}

%description
%{summary}

%package devel
BuildRequires:  golang >= 1.2.1-3
Requires:       golang >= 1.2.1-3
Summary:        TOML parser and encoder for Go with reflection
Provides:       golang(%{import_path}) = %{version}-%{release}
BuildArch:      noarch

%description devel
%{summary}

%prep
%setup -q -n %{repo}-%{commit}

%build
mkdir -p _build/src/github.com/BurntSushi
ln -sf $(pwd) _build/src/github.com/BurntSushi/toml
export GOPATH=$(pwd)/_build:%{gopath}
cd cmd/tomlv
go build .

%install
install -d %{buildroot}/%{_bindir}
install -p -m 755 ./cmd/tomlv/tomlv %{buildroot}%{_bindir}/tomlv
install -d %{buildroot}/%{gopath}/src/%{import_path}
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}

%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}

%files
%defattr(-,root,root,-)
%{_bindir}/tomlv

%files devel
%doc COPYING README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%dir %{gopath}/src/%{import_path}
%{gopath}/src/%{import_path}/*.go

%changelog
* Thu Oct 23 2014 jchaloup <jchaloup@redhat.com> - 0-0.3.git2ceedfe
- Bump to upstream 2ceedfee35ad3848e49308ab0c9a4f640cfb5fb2
- spec file polishing to follow go draft
  related: #1120865

* Mon Sep 22 2014 jchaloup <jchaloup@redhat.com> - 0-0.2.gitbd2bdf7
- do not own golang directories
- defattr and attr not needed

* Mon Sep 22 2014 jchaloup <jchaloup@redhat.com> - 0-0.1.gitbd2bdf7
- accomodated changes from Vincent Batts
- gopath is in the rpm macros, and set exclusive arch too, to prevent s390 builds
- move the buildarch noarch to the devel, since it is source only
- preserve timestamps of source copied and as an added perk
- the tomlv command provided in this project is useful for validating *.toml files
- go test

* Thu Jul 17 2014 Colin Walters <walters@verbum.org>
- Initial package
