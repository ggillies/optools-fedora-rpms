# Generated from em-redis-unified-0.5.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name em-redis-unified

Name: rubygem-%{gem_name}
Version: 0.5.0
Release: 1%{?dist}
Summary: An eventmachine-based implementation of the Redis protocol
Group: Development/Languages
License: MIT
URL: http://github.com/portertech/em-redis
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildRequires: rubygem-rspec
BuildRequires: rubygem(eventmachine)
BuildArch: noarch
%if 0%{?fedora} <= 20 || 0%{?el7}
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
An eventmachine-based implementation of the Redis protocol.


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

rm -f %{buildroot}%{gem_instdir}/.gitignore


# Run the test suite
%check
pushd .%{gem_instdir}
# Disabled due to unmet dependencies (rubygem-bacon)
# rspec -Ilib spec
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Tue Jan 27 2015 Graeme Gillies <ggillies@redhat.com> - 0.5.0-1
- Initial package
