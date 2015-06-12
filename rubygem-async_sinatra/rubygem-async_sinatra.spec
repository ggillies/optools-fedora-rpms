# Generated from async_sinatra-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name async_sinatra

Name: rubygem-%{gem_name}
Version: 1.1.0
Release: 1%{?dist}
Summary: Sinatra plugin to perform asynchronous responses inside of the Sinatra framework
Group: Development/Languages
License: MIT
URL: http://github.com/raggi/async_sinatra
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildRequires: rubygem(minitest) 
BuildRequires: rubygem(eventmachine)
BuildRequires: rubygem(sinatra)
BuildRequires: rubygem(rack-test)
BuildRequires: rubygem(tilt)
BuildRequires: rubygem(rack-protection)
# BuildRequires: rubygem(rubyforge) >= 2.0.4
# BuildRequires: rubygem(hoe-doofus) >= 1.0
# BuildRequires: rubygem(hoe-seattlerb) >= 1.2
# BuildRequires: rubygem(hoe-git) >= 1.3
# BuildRequires: rubygem(hoe-gemspec2) >= 1.0
# BuildRequires: rubygem(eventmachine) >= 0.12.11
# BuildRequires: rubygem(hoe) => 3.5
# BuildRequires: rubygem(hoe) < 4
BuildArch: noarch
%if 0%{?fedora} <= 20 || 0%{?el7}
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
A Sinatra plugin to provide convenience whilst performing asynchronous
responses inside of the Sinatra framework running under async webservers.
To properly utilise this package, some knowledge of EventMachine and/or
asynchronous patterns is recommended.
Currently, supporting servers include:
* Thin
* Rainbows
* Zbatery.


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

rm -f %{buildroot}%{gem_instdir}/.gemtest


# Run the test suite
%check
pushd .%{gem_instdir}
%if 0%{?fedora} > 0
sed -i "s/MiniTest::Unit::TestCase/Minitest::Test/" ./test/test_async.rb
%endif
ruby -Ilib -Itest -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.rdoc
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/test

%changelog
* Tue Jan 27 2015 Graeme Gillies <ggillies@redhat.com> - 1.1.0-1
- Initial package
