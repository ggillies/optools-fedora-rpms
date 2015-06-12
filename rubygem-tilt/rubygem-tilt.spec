%global gem_name tilt

%global bootstrap 1

Summary: Generic interface to multiple Ruby template engines
Name: rubygem-%{gem_name}
Version: 1.4.1
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/rtomayko/%{gem_name}
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Make the test suite MiniTest 5.x compatible. This was done for tilt 2.x.
# https://github.com/rtomayko/tilt/commit/11331fd93629834a851bb8466bec8eae55c21a5f
# https://github.com/rtomayko/tilt/commit/4ab6c9299d0e1d5ad0e500490973c53a3a76b64a
Patch0: rubygem-tilt-1.4.1-minitest5.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
%if 0%{bootstrap} < 1
BuildRequires: rubygem(creole)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(nokogiri)
BuildRequires: rubygem(erubis)
BuildRequires: rubygem(haml)
BuildRequires: rubygem(builder)
BuildRequires: rubygem(maruku)
BuildRequires: rubygem(RedCloth)
BuildRequires: rubygem(redcarpet)
BuildRequires: rubygem(coffee-script)
BuildRequires: rubygem(therubyracer)
BuildRequires: rubygem(wikicloth)

# BuildRequires: rubygem(asciidoctor)
#BuildRequires: rubygem(kramdown)
# Markaby test fails. It is probably due to rather old version found in Fedora.
# https://github.com/rtomayko/tilt/issues/96
# BuildRequires: rubygem(markaby)
#BuildRequires: rubygem(rdiscount)
%endif
%if 0%{?fc20} || 0%{?el7}
Provides: rubygem(%{gem_name}) = %{version}
%endif

BuildArch: noarch

%description
Generic interface to multiple Ruby template engines


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires:%{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

pushd .%{gem_instdir}
%patch0 -p1
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
%if 0%{bootstrap} < 1
pushd %{buildroot}%{gem_instdir}
LANG=en_US.utf8 ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%endif

%files
%dir %{gem_instdir}
%{_bindir}/%{gem_name}
%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/Gemfile
%{gem_instdir}/bin
%{gem_libdir}
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/TEMPLATES.md
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/HACKING
%{gem_instdir}/Rakefile
%{gem_instdir}/test


%changelog
* Fri May 15 2015 Graeme Gillies <ggillies@redhat.com> - 1.4.1-3
- Added in explicit provides for EL7 builds

* Wed Jan 21 2015 Vít Ondruch <vondruch@redhat.com> - 1.4.1-2
- Make the test suite MiniTest 5.x compatible to fix the FTBFS.

* Thu Jun 19 2014 Vít Ondruch <vondruch@redhat.com> - 1.4.1-1
- Update to tilt 1.4.1.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 15 2013 Vít Ondruch <vondruch@redhat.com> - 1.3.7-2
- Enable test suite.

* Mon Apr 15 2013 Vít Ondruch <vondruch@redhat.com> - 1.3.7-1
- Update to tilt 1.3.7.

* Mon Apr 15 2013 Vít Ondruch <vondruch@redhat.com> - 1.3.5-2
- Fix unowned directory (rhbz#912046).

* Thu Mar 07 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.5-1
- Updated to Tilt 1.3.5.
- Remove patches merged upstream.

* Thu Feb 28 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.3-7
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jul 23 2012 Vít Ondruch <vondruch@redhat.com> - 1.3.3-5
- Fixes RDoc >= 3.10 compatibility.
- Enabled coffee-script and redcarpet tests.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.3-3
- Allowed running the tests.

* Tue Jan 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.3-2
- Rebuilt for Ruby 1.9.3.
- Introduced %%bootstrap macro to deal with dependency loop for BuildRequires.

* Mon Jan 16 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.3-1
- Updated to tilt 1.3.3.
- Removed patch that fixed BZ #715713, as it is a part of this version.
- Excluded unnecessary files.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Vít Ondruch <vondruch@redhat.com> - 1.3.2-1
- Updated to the tilt 1.3.2.
- Test suite for erubis, haml, builder and RedCloth template engines enabled.

* Fri Jun 24 2011 Vít Ondruch <vondruch@redhat.com> - 1.2.2-3
- Fixes FTBFS (rhbz#715713).

* Thu Feb 10 2011 Vít Ondruch <vondruch@redhat.com> - 1.2.2-2
- Test moved to doc subpackage
- %%{gem_name} macro used whenever possible.

* Mon Feb 07 2011 Vít Ondruch <vondruch@redhat.com> - 1.2.2-1
- Initial package
