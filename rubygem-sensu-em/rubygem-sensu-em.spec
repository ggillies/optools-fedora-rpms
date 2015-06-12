# Generated from sensu-em-2.4.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sensu-em

Name: rubygem-%{gem_name}
Version: 2.4.0
Release: 1%{?dist}
Summary: Ruby/EventMachine library
Group: Development/Languages
License: Ruby and GPLv2
URL: http://rubyeventmachine.com
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby-devel 
BuildRequires: rubygem(test-unit)
BuildRequires: rubygem(eventmachine)
# BuildRequires: rubygem(yard) >= 0.8.5.2
# BuildRequires: rubygem(bluecloth)
%if 0%{?fedora} <= 20 || 0%{?el7}
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
EventMachine implements a fast, single-threaded engine for arbitrary network
communications. It's extremely easy to use in Ruby. EventMachine wraps all
interactions with IP sockets, allowing programs to concentrate on the
implementation of network protocols. It can be used to create both network
servers and clients. To create a server or client, a Ruby program only needs
to specify the IP address and port, and provide a Module that implements the
communications protocol. Implementations of several standard network protocols
are provided with the package, primarily to serve as examples. The real goal
of EventMachine is to enable programs to easily interface with other programs
using TCP/IP, especially if custom protocols are required.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%if 0%{?fedora} > 0
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/
%endif

%if 0%{?rhel} >= 7
mkdir -p %{buildroot}%{gem_extdir_mri}/lib
cp -ar .%{gem_instdir}/lib/* %{buildroot}%{gem_extdir_mri}/lib
%endif

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

rm -f %{buildroot}%{gem_instdir}/{.gitignore,.travis.yml,.yardopts,eventmachine.gemspec,java/.gitignore,java/.project,java/.classpath}

# Run the test suite
%check
pushd .%{gem_instdir}
# Disable tests requiring networking
sed -i '4,21 s/^/#/' tests/test_resolver.rb
sed -i '31,41 s/^/#/' tests/test_resolver.rb
sed -i '133,157 s/^/#/' tests/test_basic.rb
sed -i '17,28 s/^/#/' tests/test_get_sock_opt.rb
sed -i '17,28 s/^/#/' tests/test_set_sock_opt.rb
sed -i '14,26 s/^/#/' tests/test_unbind_reason.rb
rm -f tests/test_httpclient.rb
rm -f tests/test_httpclient2.rb
rm -f tests/test_idle_connection.rb
rm -f tests/test_ssl_methods.rb
rm -f tests/test_ssl_verify.rb
rm -f tests/test_ssl_echo_data.rb
# Disable all tests on EL7 due to https://bugs.ruby-lang.org/issues/9432
%if 0%{?fedora} > 0
ruby -Itests:lib -e 'Dir.glob "./tests/**/test_*.rb", &method(:require)'
%endif
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/GNU
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/Gemfile

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/docs/DocumentationGuidesIndex.md
%doc %{gem_instdir}/docs/GettingStarted.md
%doc %{gem_instdir}/docs/old/ChangeLog
%doc %{gem_instdir}/docs/old/DEFERRABLES
%doc %{gem_instdir}/docs/old/EPOLL
%doc %{gem_instdir}/docs/old/INSTALL
%doc %{gem_instdir}/docs/old/KEYBOARD
%doc %{gem_instdir}/docs/old/LEGAL
%doc %{gem_instdir}/docs/old/LIGHTWEIGHT_CONCURRENCY
%doc %{gem_instdir}/docs/old/PURE_RUBY
%doc %{gem_instdir}/docs/old/RELEASE_NOTES
%doc %{gem_instdir}/docs/old/SMTP
%doc %{gem_instdir}/docs/old/SPAWNED_PROCESSES
%doc %{gem_instdir}/docs/old/TODO
%{gem_instdir}/tests
%{gem_instdir}/examples
%{gem_instdir}/Rakefile
%{gem_instdir}/java
%{gem_instdir}/rakelib

%changelog
* Tue Jan 27 2015 Graeme Gillies <ggillies@redhat.com> - 2.4.0-1
- Initial package
