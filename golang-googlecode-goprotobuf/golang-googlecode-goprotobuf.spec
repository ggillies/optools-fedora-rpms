%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         golang
%global repo            protobuf
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          efd7476481382c195beb33acd8ec2f1527167fb4
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global simport_path    code.google.com/p/goprotobuf

Name:           golang-googlecode-goprotobuf
Version:        0
Release:        0.14.git%{shortcommit}%{?dist}
Summary:        Go support for Google protocol buffers
License:        BSD
URL:            https://%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
ExclusiveArch:  %{ix86} x86_64 %{arm}

BuildRequires:  golang
Requires:       protobuf
Provides:       protoc-gen-go = %{version}-%{release}

%description
This package provides support for protocol buffers in the form of a protocol 
compiler plugin which generates Go source files that, once compiled, can access
and manage protocol buffers.

Install %{name}-devel for the associated support library.

%package devel
BuildRequires:  golang >= 1.2.1-3
Requires:       golang >= 1.2.1-3
Summary:        %{summary}
Provides:       golang(%{import_path}/proto) = %{version}-%{release}
Provides:       golang(%{import_path}/proto/testdata) = %{version}-%{release}
Provides:       golang(%{import_path}/protoc-gen-go) = %{version}-%{release}
Provides:       golang(%{import_path}/protoc-gen-go/descriptor) = %{version}-%{release}
Provides:       golang(%{import_path}/protoc-gen-go/generator) = %{version}-%{release}
Provides:       golang(%{import_path}/protoc-gen-go/internal/grpc) = %{version}-%{release}
Provides:       golang(%{import_path}/protoc-gen-go/plugin) = %{version}-%{release}
Provides:       golang(%{import_path}/protoc-gen-go/testdata/my_test) = %{version}-%{release}
# back compatibility
Provides:       golang(%{simport_path}) = %{version}-%{release}
Provides:       golang(%{simport_path}/proto) = %{version}-%{release}
Provides:       golang(%{simport_path}/proto/testdata) = %{version}-%{release}
Provides:       golang(%{simport_path}/protoc-gen-go) = %{version}-%{release}
Provides:       golang(%{simport_path}/protoc-gen-go/descriptor) = %{version}-%{release}
Provides:       golang(%{simport_path}/protoc-gen-go/generator) = %{version}-%{release}
Provides:       golang(%{simport_path}/protoc-gen-go/internal/grpc) = %{version}-%{release}
Provides:       golang(%{simport_path}/protoc-gen-go/plugin) = %{version}-%{release}
Provides:       golang(%{simport_path}/protoc-gen-go/testdata/my_test) = %{version}-%{release}

%description devel
This package provides  a library that implements run-time support for
encoding (marshaling), decoding (unmarshaling), and accessing protocol
buffers in the Go language.

Install %{name} for the related protocol compiler plugin.

%prep
%setup -q -n %{repo}-%{commit}

mkdir -p src/%{import_path}
cp -R proto protoc-gen-go src/%{import_path}/

%build
unset GOPATH
export GOPATH=$(pwd)
cd protoc-gen-go
go build

%install
install -d %{buildroot}%{_bindir}
install -m 755 protoc-gen-go/protoc-gen-go %{buildroot}/%{_bindir}/protoc-gen-go

# devel
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav protoc-gen-go %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav proto %{buildroot}/%{gopath}/src/%{import_path}/

install -d -p %{buildroot}/%{gopath}/src/%{simport_path}/
cp -rpav protoc-gen-go %{buildroot}/%{gopath}/src/%{simport_path}/
cp -rpav proto %{buildroot}/%{gopath}/src/%{simport_path}/

cd %{buildroot}/%{gopath}/src/%{simport_path}/
# github.com/golang/protobuf -> code.google.com/p/goprotobuf
sed -i 's/"github\.com\/golang\/protobuf/"code\.google\.com\/p\/goprotobuf/g' \
        $(find . -name '*.go')


%check
#GOPATH={buildroot}/{gopath}:{gopath} go test {import_path}/protoc-gen-go/testdata
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/protoc-gen-go/generator
#GOPATH={buildroot}/{gopath}:{gopath} go test {import_path}/proto
#GOPATH={buildroot}/{gopath}:{gopath} go test {import_path}/proto/testdata

%files
%doc AUTHORS CONTRIBUTORS LICENSE README
%{_bindir}/protoc-gen-go

%files devel
%doc AUTHORS CONTRIBUTORS LICENSE README
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}
%{gopath}/src/%{simport_path}

%changelog
* Sat May 09 2015 jchaloup <jchaloup@redhat.com> - 0-0.14.gitefd7476
- Bump to upstream efd7476481382c195beb33acd8ec2f1527167fb4
  related: #1018057

* Thu Mar 05 2015 jchaloup <jchaloup@redhat.com> - 0-0.13.gitc22ae3c
- Bump to upstream c22ae3cf020a21ebb7ae566dccbe90fc8ea4f9ea
  related: #1018057

* Sun Feb 08 2015 jchaloup <jchaloup@redhat.com> - 0-0.12.git7f07925
- Extend Provides for proto/testdata
  related: #1018057

* Fri Jan 30 2015 jchaloup <jchaloup@redhat.com> - 0-0.11.git7f07925
- Provide back compatibility provides
  resolves: #1187495 #1187491 #1187494

* Mon Jan 26 2015 jchaloup <jchaloup@redhat.com> - 0-0.10.git7f07925
- Bump to 7f07925444bb51fa4cf9dfe6f7661876f8852275
  related: #1018057

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.hg61664b8425f3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.hg61664b8425f3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 17 2013 Lokesh Mandvekar <lsm5@redhat.com> - 0-0.7.hg61664b8425f3
- removed double quotes from provides

* Wed Oct 16 2013 Peter Lemenkov <lemenkov@gmail.com> - 0-0.6.hg61664b8425f3
- Added missing buildrequires

* Mon Oct 14 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.5.hg61664b8425f3
- description update

* Mon Oct 14 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.4.hg61664b8425f3
- defattr removed
- docs included in base and devel packages

* Sat Oct 12 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.3.hg61664b8425f3
- testdata directories excluded

* Sat Oct 12 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.2.hg61664b8425f3
- compiler plugin in archful base package
- libraries in noarch (except rhel6) devel subpackage

* Fri Oct 11 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.1.hg61664b8425f3
- Initial fedora package
