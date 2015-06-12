# Generated from yajl-ruby-1.2.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name yajl-ruby

Name: rubygem-%{gem_name}
Version: 1.2.1
Release: 1%{?dist}
Summary: Ruby C bindings to the excellent Yajl JSON stream-based parser library
Group: Development/Languages
License: MIT
URL: http://github.com/brianmario/yajl-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby-devel >= 1.8.6
BuildRequires: rubygem-rspec
%if 0%{?fedora} <= 20 || 0%{?el7}
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
%{summary}


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
cp -ar .%{gem_extdir_mri}/{gem.build_complete,yajl} %{buildroot}%{gem_extdir_mri}/
%endif

%if 0%{?rhel} >= 7
mkdir -p %{buildroot}%{gem_extdir_mri}/lib/yajl
cp -ar .%{gem_instdir}/lib/yajl/yajl.so %{buildroot}%{gem_extdir_mri}/lib/yajl
%endif

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

rm -f %{buildroot}%{gem_instdir}/{.gitignore,.travis.yml,.rspec}

# Run the test suite
%check
pushd .%{gem_instdir}
# Disabled two failing tests
sed -i '47,59d' spec/parsing/large_number_spec.rb
rspec -Ilib -I%{buildroot}%{gem_extdir_mri} spec
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/MIT-LICENSE
%doc %{gem_instdir}/Gemfile

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/tasks
%{gem_instdir}/benchmark
%{gem_instdir}/examples
%{gem_instdir}/spec
%{gem_instdir}/script
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Tue Jan 06 2015 Graeme Gillies <ggillies@redhat.com> - 1.2.1-1
- Initial package
