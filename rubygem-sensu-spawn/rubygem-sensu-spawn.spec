# Generated from sensu-spawn-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sensu-spawn

Name: rubygem-%{gem_name}
Version: 1.1.0
Release: 1%{?dist}
Summary: The Sensu spawn process library
Group: Development/Languages
License: MIT
URL: https://github.com/sensu/sensu-spawn
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildRequires: rubygem(rspec) 
BuildRequires: rubygem(eventmachine)
BuildRequires: rubygem(sensu-em)
BuildRequires: rubygem(em-worker)
BuildRequires: rubygem(childprocess)
# BuildRequires: rubygem(ffi)
BuildArch: noarch
%if 0%{?fedora} <= 20 || 0%{?el7}
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
The Sensu spawn process library.


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

# Change version of rubygem-childprocess
sed -i 's/0.5.3/0.5.5/' %{gem_name}.gemspec
sed -i 's/0.5.3/0.5.5/' lib/sensu/spawn.rb

# Disable rubygem-codeclimate-test-reporter
sed -i '/^.*codeclimate-test-reporter.*$/d' %{gem_name}.gemspec
sed -i '/^.*codeclimate-test-reporter.*$/d' spec/helpers.rb
sed -i '/^.*CodeClimate::TestReporter.start.*$/d' spec/helpers.rb

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

rm -f %{buildroot}%{gem_instdir}/{.gitignore,.travis.yml}


# Run the test suite
%check
pushd .%{gem_instdir}
rspec -Ilib spec
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/Gemfile

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/spec

%changelog
* Tue Jan 27 2015 Graeme Gillies <ggillies@redhat.com> - 1.1.0-1
- Initial package
