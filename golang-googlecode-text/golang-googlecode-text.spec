%global debug_package   %{nil}
%global provider_tld    com
%global provider        google
%global provider_prefix code
%global project         p
%global repo            text
%global import_path     %{provider_prefix}.%{provider}.%{provider_tld}/%{project}/go.%{repo}
%global rev             5b2527008a4c8988ca9dc6f010ebfb9dae67150b
%global shortrev        %(r=%{rev}; echo ${r:0:12})

%global x_provider      golang
%global x_provider_tld  org
%global x_repo          text
%global x_import_path   %{x_provider}.%{x_provider_tld}/x/%{x_repo}
%global x_name          golang-%{x_provider}%{x_provider_tld}-%{repo}

Name:       golang-%{provider}%{provider_prefix}-%{repo}
Version:    0
Release:    0.3.hg%{shortrev}%{?dist}
Summary:    Supplementary Go text libraries
License:    CC-BY
URL:        http://%{import_path}
Source0:    https://%{repo}.go.%{provider}%{provider_prefix}.%{provider_tld}/archive/%{rev}.tar.gz
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
%{summary}

%package devel
BuildRequires:  golang >= 1.2.1-3
Requires:   golang >= 1.2.1-3
Summary:    Supplementary Go text libraries for code.google.com/p/ imports
Provides:   golang(%{import_path}/cldr) = %{version}-%{release}
Provides:   golang(%{import_path}/collate) = %{version}-%{release}
Provides:   golang(%{import_path}/collate/build) = %{version}-%{release}
Provides:   golang(%{import_path}/collate/colltab) = %{version}-%{release}
Provides:   golang(%{import_path}/collate/tools/colcmp) = %{version}-%{release}
Provides:   golang(%{import_path}/display) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding/charmap) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding/japanese) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding/korean) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding/simplifiedchinese) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding/traditionalchinese) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding/unicode) = %{version}-%{release}
Provides:   golang(%{import_path}/internal/triegen) = %{version}-%{release}
Provides:   golang(%{import_path}/internal/ucd) = %{version}-%{release}
Provides:   golang(%{import_path}/language) = %{version}-%{release}
Provides:   golang(%{import_path}/transform) = %{version}-%{release}
Provides:   golang(%{import_path}/unicode/norm) = %{version}-%{release}

%package -n %{x_name}-devel
BuildRequires:  golang >= 1.2.1-3
Requires:   golang >= 1.2.1-3
Summary:    Supplementary Go text libraries for golang.org/x/ imports
Provides:   golang(%{x_import_path}/cldr) = %{version}-%{release}
Provides:   golang(%{x_import_path}/collate) = %{version}-%{release}
Provides:   golang(%{x_import_path}/collate/build) = %{version}-%{release}
Provides:   golang(%{x_import_path}/collate/colltab) = %{version}-%{release}
Provides:   golang(%{x_import_path}/collate/tools/colcmp) = %{version}-%{release}
Provides:   golang(%{x_import_path}/display) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding/charmap) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding/japanese) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding/korean) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding/simplifiedchinese) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding/traditionalchinese) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding/unicode) = %{version}-%{release}
Provides:   golang(%{x_import_path}/internal/triegen) = %{version}-%{release}
Provides:   golang(%{x_import_path}/internal/ucd) = %{version}-%{release}
Provides:   golang(%{x_import_path}/language) = %{version}-%{release}
Provides:   golang(%{x_import_path}/transform) = %{version}-%{release}
Provides:   golang(%{x_import_path}/unicode/norm) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for building other packages
which use the supplementary Go text libraries with code.google.com/p/ imports.

%description -n %{x_name}-devel

This package contains library source intended for building other packages
which use the supplementary Go text libraries with golang.org/x/ imports.

%prep
%setup -qn %{repo}.go-%{shortrev}

%build

%install

install -dp %{buildroot}%{gopath}/src/%{import_path}
install -dp %{buildroot}%{gopath}/src/%{x_import_path}
for dir in */ ; do
   cp -rpav $dir %{buildroot}%{gopath}/src/%{import_path}/
   cp -rpav $dir %{buildroot}%{gopath}/src/%{x_import_path}/
done

cd %{buildroot}/%{gopath}/src/%{import_path}
# from https://groups.google.com/forum/#!topic/golang-nuts/eD8dh3T9yyA, first post
sed -i 's/"golang\.org\/x\//"code\.google\.com\/p\/go\./g' \
        $(find . -name '*.go')

%check
for dir in $(find . -mindepth 0 -maxdepth 3 -type d); do
break
# test fails for transform
    if [[ $(find $dir -maxdepth 1 -name *_test.go | wc -l) != '0' && $dir != "./transform" ]]; then
        GOPATH=%{gopath}:%{buildroot}%{gopath} go test %{import_path}/$dir
    fi

done

# delete encoding/testdata
rm -rf %{buildroot}%{gopath}/src/%{import_path}/encoding/testdata
rm -rf %{buildroot}%{gopath}/src/%{x_import_path}/encoding/testdata

%files devel
%doc AUTHORS CONTRIBUTORS LICENSE PATENTS README
%{gopath}/src/%{import_path}

%files -n %{x_name}-devel
%doc AUTHORS CONTRIBUTORS LICENSE PATENTS README
%{gopath}/src/%{x_import_path}

%changelog
* Tue Dec 09 2014 jchaloup <jchaloup@redhat.com> - 0-0.3.hg5b2527008a4c
- Update to the latest commit 5b2527008a4c8988ca9dc6f010ebfb9dae67150b
  related: #1056285

* Fri Nov 21 2014 jchaloup <jchaloup@redhat.com> - 0-0.2.hg024681b033be
- Extend import paths for golang.org/x/
- Choose the correct architecture
  related: #1056285

* Sun Sep 28 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.1.hg024681b033be
- Resolves: rhbz#1056285 - Initial package
