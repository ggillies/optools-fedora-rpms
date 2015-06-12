# Generated from sensu-logger-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sensu-logger

Name: rubygem-%{gem_name}
Version: 1.0.0
Release: 1%{?dist}
Summary: The Sensu logger library
Group: Development/Languages
License: MIT
URL: https://github.com/sensu/sensu-logger
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildRequires: rubygem(rspec) 
BuildRequires: rubygem(eventmachine)
BuildRequires: rubygem(sensu-em)
BuildRequires: rubygem(multi_json)
BuildArch: noarch
%if 0%{?fedora} <= 20 || 0%{?el7}
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
The Sensu logger library.


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

rm -f %{buildroot}%{gem_instdir}/{.gitignore,.travis.yml}


# Run the test suite
%check
pushd .%{gem_instdir}
sed -i '/^.*codeclimate-test-reporter.*$/d' spec/helpers.rb
sed -i /CodeClimate::TestReporter.start/d spec/helpers.rb
rspec -Ilib spec
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/Gemfile

%files doc
%doc %{gem_docdir}
%{gem_instdir}/spec
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/Rakefile

%changelog
* Tue Jan 27 2015 Graeme Gillies <ggillies@redhat.com> - 1.0.0-1
- Initial package
