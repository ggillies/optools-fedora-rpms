# Generated from msgpack-0.5.9.gem by gem2rpm -*- rpm-spec -*-
%global gem_name msgpack

Name: rubygem-%{gem_name}
Version: 0.5.11
Release: 1%{?dist}
Summary: MessagePack, a binary-based efficient data interchange format
Group: Development/Languages
License: ASL 2.0
URL: http://msgpack.org/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby-devel
BuildRequires:  rubygem-rspec
# BuildRequires: rubygem(rake-compiler) => 0.8.3
# BuildRequires: rubygem(rake-compiler) < 0.9
# BuildRequires: rubygem(rspec) => 2.11
# BuildRequires: rubygem(rspec) < 3
# BuildRequires: rubygem(json) => 1.7
# BuildRequires: rubygem(json) < 2
# BuildRequires: rubygem(yard) => 0.8.2
# BuildRequires: rubygem(yard) < 0.9
%if 0%{?fc20} || 0%{?el7}
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
MessagePack is a binary-based efficient object serialization library. It
enables to exchange structured objects between many languages like JSON. But
unlike JSON, it is very fast and small.


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
cp -ar .%{gem_extdir_mri}/{gem.build_complete,%{gem_name}} %{buildroot}%{gem_extdir_mri}/
%endif

%if 0%{?rhel} >= 7
mkdir -p %{buildroot}%{gem_extdir_mri}/lib/%{gem_name}
cp -ar .%{gem_instdir}/lib/%{gem_name}/%{gem_name}.so %{buildroot}%{gem_extdir_mri}/lib/%{gem_name}
%endif

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

rm -f %{buildroot}%{gem_instdir}/{.gitignore,.travis.yml}

# Run the test suite
%check
pushd .%{gem_instdir}
rm -rf spec/jruby
rspec -Ilib -I%{buildroot}%{gem_extdir_mri} spec
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/ChangeLog
%doc %{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/msgpack.org.md

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/spec/
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/doclib/


%changelog
* Mon Jan 05 2015 Graeme Gillies <ggillies@redhat.com> - 0.5.11-1
- Initial package
