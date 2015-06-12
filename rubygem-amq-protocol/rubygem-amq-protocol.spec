%global gem_name amq-protocol

Name: rubygem-%{gem_name}
Version: 1.9.2
Release: 3%{?dist}
Summary: AMQP 0.9.1 encoder & decoder
Group: Development/Languages
License: MIT
URL: http://github.com/ruby-amqp/amq-protocol
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
Requires: rubygems
%if 0%{?fedora} >= 22
BuildRequires: rubygem(rspec2)
%else
BuildRequires: rubygem(rspec)
%endif
BuildArch: noarch
%if 0%{?fc20} || 0%{?el7}
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
amq-protocol is an AMQP 0.9.1 serialization library for Ruby. It is not an
AMQP client: amq-protocol only handles serialization and deserialization.
If you want to write your own AMQP client, this gem can help you with that.


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

# Remove effin_utf8 dependency as it has no effect on ruby 2.0 and higher
sed -i /effin_utf8/d Gemfile
sed -i /effin_utf8/d spec/spec_helper.rb
# Remove bundler as we don't use it as part of the packaging process
sed -e "/require 'bundler\/setup'/d" -i spec/spec_helper.rb

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

# Remove unnecessary gemspec file
rm .%{gem_instdir}/%{gem_name}.gemspec

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

rm -f %{buildroot}%{gem_instdir}/{.gitignore,.gitmodules,.rspec,.travis.yml}


# Run the test suite
%check
pushd .%{gem_instdir}
%if 0%{?fedora} >= 22
rspec2 -Ilib spec
%else
rspec -Ilib spec
%endif
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/ChangeLog.md
%license %{gem_instdir}/LICENSE
%doc %{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/spec
%exclude %{gem_instdir}/benchmarks
%exclude %{gem_instdir}/profiling
%exclude %{gem_instdir}/generate.rb
%exclude %{gem_instdir}/codegen
%exclude %{gem_instdir}/Rakefile


%files doc
%doc %{gem_docdir}

%changelog
* Fri Apr 10 2015 Graeme Gillies <ggillies@redhat.com> - 1.9.2-3
- Cleaned spec file to be more readable

* Wed Mar 25 2015 Graeme Gillies <ggillies@redhat.com> - 1.9.2-2
- Cleaned up spec file as per feedback from review (%%license,
  remove extra gemspec, explicit rubygems-requires)
- Added in conditional Provides for epel-7 builds

* Fri Jan 30 2015 Graeme Gillies <ggillies@redhat.com> - 1.9.2-1
- Initial package
