# Generated from tzinfo-data-1.2014.10.gem by gem2rpm -*- rpm-spec -*-
%global gem_name tzinfo-data

Name: rubygem-%{gem_name}
Version: 1.2014.10
Release: 2%{?dist}
Summary: Timezone Data for TZInfo
Group: Development/Languages
License: MIT
URL: http://tzinfo.github.io
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby >= 1.8.7
BuildRequires: rubygem-minitest
BuildArch: noarch
%if 0%{?fedora} <= 20 || 0%{?el7}
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
TZInfo::Data contains data from the IANA Time Zone database packaged as Ruby
modules for use with TZInfo.


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




# Run the test suite
%check
pushd .%{gem_instdir}
# Disabled due to tests not being included
# testrb -Ilib test/ts_all.rb
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/.yardopts

%changelog
* Mon Jun 01 2015 Graeme Gillies <ggillies@redhat.com> - 1.2014.10-2
- Added explicit provides for EL7

* Mon Jan 05 2015 Graeme Gillies <ggillies@redhat.com> - 1.2014.10-1
- Initial package
