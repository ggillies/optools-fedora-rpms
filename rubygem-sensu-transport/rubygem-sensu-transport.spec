# Generated from sensu-transport-2.4.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sensu-transport

Name: rubygem-%{gem_name}
Version: 2.4.0
Release: 1%{?dist}
Summary: The Sensu transport abstraction library
Group: Development/Languages
License: MIT
URL: https://github.com/sensu/sensu-transport
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildRequires: rubygem(rspec) 
BuildRequires: rubygem-eventmachine
BuildRequires: rubygem-sensu-em
BuildRequires: rubygem-amqp
BuildArch: noarch

%description
The Sensu transport abstraction library.


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
# Disabled due to reliance on running rabbitmq infrastructure
# rspec -Ilib --tag ~ssl spec
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/Gemfile

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/spec
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Fri Jan 23 2015 Graeme Gillies <ggillies@redhat.com> - 2.4.0-1
- Initial package
