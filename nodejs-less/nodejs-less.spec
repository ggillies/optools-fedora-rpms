%{?nodejs_find_provides_and_requires}

Name:           nodejs-less
Version:        1.7.0
Release:        2%{?dist}
Summary:        Less.js The dynamic stylesheet language

# cssmin.js is licensed under BSD license
# everything else is ASL 2.0
License:        ASL 2.0 and BSD

URL:            http://lesscss.org
Source0: http://registry.npmjs.org/less/-/less-%{version}.tgz

# Since we're installing this in a global location, fix the require()
# calls to point there.
Patch0001: 0001-Require-include-files-from-the-default-location.patch

BuildArch:      noarch
BuildRequires:  nodejs-devel
BuildRequires:  nodejs-packaging
Requires:       nodejs
ExclusiveArch: %{nodejs_arches} noarch

Provides:  lessjs = %{version}-%{release}
Obsoletes: lessjs < 1.3.3-2

%description
LESS extends CSS with dynamic behavior such as variables, mixins, operations
and functions. LESS runs on both the client-side (Chrome, Safari, Firefox)
and server-side, with Node.js and Rhino.

%prep
%setup -q -n package

%patch0001 -p1

# Remove pre-built files from the dist/ directory
rm -f dist/*.js

# enable compression using ycssmin
%nodejs_fixdep ycssmin '~1.0.1'

%build
# Nothing to be built, we're just carrying around flat files

%check
make %{?_smp_mflags} test


%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{nodejs_sitelib}/less
chmod a+x bin/lessc
cp -rp bin package.json lib/less/* %{buildroot}/%{nodejs_sitelib}/less

# Install /usr/bin/lessc
ln -s %{nodejs_sitelib}/less/bin/lessc \
      %{buildroot}%{_bindir}

%nodejs_symlink_deps

%files
%doc LICENSE README.md CHANGELOG.md CONTRIBUTING.md
%{_bindir}/lessc
%{nodejs_sitelib}/less


%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 05 2014 Stephen Gallagher <sgallagh@redhat.com> 1.7.0-1
- New upstream release 1.7.0
- https://github.com/less/less.js/blob/v1.7.0/CHANGELOG.md
- Add support for rulesets in variables and passed to mixins to allow wrapping
- Change luma to follow the w3c spec, luma is available as luminance. Contrast
  still uses luma so you may see differences if your threshold % is close to
  the existing calculated luma.
- Upgraded clean css which means the --selectors-merge-mode is now renamed
  --compatibility
- Add support for using variables with @keyframes, @namespace, @charset
- Support property merging with +_ when spaces are needed and keep + for comma
  separated
- Imports now always import once consistently- a race condition meant
  previously certain configurations would lead to a different ordering of
  files
- Fix support for `.mixin(@args...)` when called with no args (e.g.
  `.mixin();`)
- Do unit conversions with min and max functions. Don't pass through if not
  understood, throw an error
- Allow % to be passed on its own to the unit function e.g. `unit(10, %)`
- Fix a bug when comparing a unit value to a non-unit value if the unit-value
  was the multiple of another unit (e.g. cm, mm, deg etc.)
- Fix mixins with media queries in import reference files not being put into
  the output (they now output, they used to incorrectly not)
- Fix lint mode- now reports all errors
- Fixed a small scope issue with & {} selector rulesets incorrectly making
  mixins visible- regression from 1.6.2
- Browser- added log level "debug" at 3 to get less logging, The default has
  changed so unless you set the value to the default you won't see a
  difference
- Browser- logLevel takes effect regardless of the environment (production/dev)
- Browser- added postProcessor option, a function called to post-process the
  css before adding to the page
- Browser- use the right request for file access in IE

* Tue Feb 25 2014 Stephen Gallagher <sgallagh@redhat.com> 1.6.3-1
- New upstream release 1.6.3
- https://github.com/less/less.js/blob/v1.6.3/CHANGELOG.md
- Fix issue with calling toCSS twice not working in some situations (like with
  bootstrap 2)
- The Rhino release is fixed!
- ability to use uppercase colours
- Fix a nasty bug causing syntax errors when selector interpolation is preceded
  by a long comment (and some other cases)
- Fix a major bug with the variable scope in guards on selectors (e.g. not
  mixins)
- Fold in & when () { to the current selector rather than duplicating it
- fix another issue with array prototypes
- add a url-args option which adds a value to all urls (for cache busting)
- Round numbers to 8 decimal places - thereby stopping javascript precision
  errors
- some improvements to the default() function in more complex scenarios
- improved missing '{' and '(' detection

* Mon Jan 13 2014 Stephen Gallagher <sgallagh@redhat.com> - 1.6.1-1
- New upstream release 1.6.1
- https://github.com/less/less.js/blob/v1.6.1/CHANGELOG.md
- support ^ and ^^ shadow dom selectors
- fix sourcemap selector (used to report end of the element or selector) and
  directive position (previously not supported)
- fix parsing empty less files
- error on (currently) ambiguous guards on multiple css selectors
- older environments - protect against typeof regex returning function
- Do not use default keyword
- use innerHTML in tests, not innerText
- protect for-in in case Array and Object prototypes have custom fields

* Thu Jan 02 2014 Stephen Gallagher <sgallagh@redhat.com> - 1.6.0-1
- New upstream release 1.6.0
- https://github.com/less/less.js/blob/v1.6.0/CHANGELOG.md
- Properties can be interpolated, e.g. @{prefix}-property: value;
- a default function has been added only valid in mixin definitions to
  determine if no other mixins have been matched
- Added a plugins option that allows specifying an array of visitors run on the
  less AST
- Performance improvements that may result in approx 20-40% speed up
- Javascript evaluations returning numbers can now be used in
  calculations/functions
- fixed issue when adding colours, taking the alpha over 1 and breaking when
  used in colour functions
- when adding together 2 colours with non zero alpha, the alpha will now be
  combined rather than added
- the advanced colour functions no longer ignore transparency, they blend that
  too
- Added --clean-option and cleancssOptions to allow passing in clean css
  options
- rgba declarations are now always clamped e.g. rgba(-1,258,258, -1) becomes
  rgba(0, 255, 255, 0)
- Fix possible issue with import reference not bringing in styles (may not be a
  bugfix, just a code tidy)
- Fix some issues with urls() being prefixed twice and unquoted urls in mixins
  being processed each time they are called
- Fixed error messages for undefined variables in javascript evaluation
- Fixed line/column numbers from math errors

* Tue Nov 26 2013 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-1
- New upstream release 1.5.1
- https://github.com/less/less.js/blob/v1.5.1/CHANGELOG.md
- Added source-map-URL option
- Fixed a bug which meant the minimised 1.5.0 browser version was not wrapped,
  meaning it interfered with require js
- Fixed a bug where the browser version assume port was specified
- Added the ability to specify variables on the command line
- Upgraded clean-css and fixed it from trying to import
- correct a bug meaning imports weren't synchronous (syncImport option
  available for full synchronous behaviour)
- better mixin matching behaviour with calling multiple classes e.g. .a.b.c;

* Tue Oct 22 2013 Stephen Gallagher <sgallagh@redhat.com> - 1.5.0-1
- New upstream release 1.5.0
- https://github.com/less/less.js/blob/v1.5.0/CHANGELOG.md
- sourcemap support
- support for import inline option to include css that you do NOT want less to
  parse e.g. `@import (inline) "file.css";`
- better support for modifyVars (refresh styles with new variables, using a
  file cache), is now more resiliant
- support for import reference option to reference external css, but not output
  it. Any mixin calls or extend's will be output.
- support for guards on selectors (currently only if you have a single
  selector)
- allow property merging through the +: syntax
- Added min/max functions
- Added length function and improved extract to work with comma seperated
  values
- when using import multiple, sub imports are imported multiple times into
  final output
- fix bad spaces between namespace operators
- do not compress comment if it begins with an exclamation mark
- Fix the saturate function to pass through when using the CSS syntax
- Added svg-gradient function
- Added no-js option to lessc (in browser, use javascriptEnabled: false) which
  disallows JavaScript in less files
- switched from the little supported and buggy cssmin (previously ycssmin) to
  clean-css
- support transparent as a color, but not convert between rgba(0, 0, 0, 0) and
  transparent
- remove sys.puts calls to stop deprecation warnings in future node.js releases
- Browser: added logLevel option to control logging (2 = everything, 1 = errors
  only, 0 = no logging)
- Browser: added errorReporting option which can be "html" (default) or
  "console" or a function
- Now uses grunt for building and testing
- A few bug fixes for media queries, extends, scoping, compression and import
  once.
- if you don't pass a strict maths option, font size/line height options are
  output correctly again
- npmignore now include .gitattributes
- property names may include capital letters
- various windows path fixes (capital letters, multiple // in a path)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 05 2013 Stephen Gallagher <sgallagh@redhat.com> - 1.4.1-1
- New upstream release 1.4.1
- https://github.com/less/less.js/blob/v1.4.1/CHANGELOG.md
- Fix syncImports and yui-compress option, as they were being ignored
- Fixed several global variable leaks
- Handle getting null or undefined passed as the options object

* Tue Jun 18 2013 Stephen Gallagher <sgallagh@redhat.com> - 1.4.0-1
- New upstream release 1.4.0
- https://github.com/cloudhead/less.js/blob/master/CHANGELOG.md
- support for :extend() in selectors (e.g. input:extend(.button) {}) and &
  :extend(); in ruleset (e.g. input { &:extend(.button all); })
- maths is now only done inside brackets. This means font: statements, media
  queries and the calc function can use a simpler format without being escaped.
  Disable this with --strict-maths-off in lessc and strictMaths:false in
  JavaScript.
- units are calculated, e.g. 200cm+1m = 3m, 3px/1px = 3. If you use units
  inconsistently you will get an error. Suppress this error with
  --strict-units-off in lessc or strictUnits:false in JavaScript
- (~"@var") selector interpolation is removed. Use @{var} in selectors to have
  variable selectors
- default behaviour of import is to import each file once. @import-once has
  been removed.
- You can specify options on imports to force it to behave as css or less
  @import (less) "file.css" will process the file as less
- variables in mixins no longer 'leak' into their calling scope
- added data-uri function which will inline an image into the output css. If
  ieCompat option is true and file is too large, it will fallback to a url()
- significant bug fixes to our debug options
- other parameters can be used as defaults in mixins e.g. .a(@a, @b:@a)
- an error is shown if properties are used outside of a ruleset
- added extract function which picks a value out of a list,
  e.g. extract(12 13 14, 3) => 3
- added luma, hsvhue, hsvsaturation, hsvvalue functions
- added pow, pi, mod, tan, sin, cos, atan, asin, acos and sqrt math functions
- added convert function, e.g. convert(1rad, deg) => value in degrees
- lessc makes output directories if they don't exist
- lessc @import supports https and 301's
- lessc "-depends" option for lessc writes out the list of import files used in
  makefile format
- lessc "-lint" option just reports errors
- support for namespaces in attributes and selector interpolation in attributes
- other bug fixes
- strictUnits now defaults to false and the true case now gives more useful but
  less correct results, e.g. 2px/1px = 2px
- Process ./ when having relative paths
- add isunit function for mixin guards and non basic units
- extends recognise attributes
- exception errors extend the JavaScript Error
- remove es-5-shim as standard from the browser
- Fix path issues with windows/linux local paths
- change strictMaths to strictMath. Enable this with --strict-math=on in lessc
  and strictMath:true in JavaScript.
- change lessc option for strict units to --strict-units=off
- fix passing of strict maths option

* Tue Jun 18 2013 Stephen Gallagher <sgallagh@redhat.com> - 1.3.3-5
- Use correct build architectures

* Mon May 06 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.3.3-4
- enable compression using ycssmin

* Wed Apr 10 2013 Stephen Gallagher <sgallagh@redhat.com> - 1.3.3-3
- Fix BuildRequires to include nodejs-devel

* Tue Apr 09 2013 Stephen Gallagher <sgallagh@redhat.com> - 1.3.3-2
- Rename package to nodejs-less

* Tue Apr 09 2013 Stephen Gallagher <sgallagh@redhat.com> - 1.3.3-1
- Upgrade to new upstream release and switch to proper Node.js packaging
- New upstream release 1.3.3
    * Fix critical bug with mixin call if using multiple brackets
    * When using the filter contrast function, the function is passed through if
      the first argument is not a color
- New upstream release 1.3.2
    * browser and server url re-writing is now aligned to not re-write (previous
      lessc behaviour)
    * url-rewriting can be made to re-write to be relative to the entry file
      using the relative-urls option (less.relativeUrls option)
    * rootpath option can be used to add a base path to every url
    * Support mixin argument seperator of ';' so you can pass comma seperated
      values. e.g. .mixin(23px, 12px;);
    * Fix lots of problems with named arguments in corner cases, not behaving
      as expected
    * hsv, hsva, unit functions
    * fixed lots more bad error messages
    * fix @import-once to use the full path, not the relative one for
      determining if an import has been imported already
    * support :not(:nth-child(3))
    * mixin guards take units into account
    * support unicode descriptors (U+00A1-00A9)
    * support calling mixins with a stack when using & (broken in 1.3.1)
    * support @namespace and namespace combinators
    * when using %% with colour functions, take into account a colour is out of
      256
    * when doing maths with a %% do not divide by 100 and keep the unit
    * allow url to contain %% (e.g. %%20 for a space)
    * if a mixin guard stops execution a default mixin is not required
    * units are output in strings (use the unit function if you need to get the
      value without unit)
    * do not infinite recurse when mixins call mixins of the same name
    * fix issue on important on mixin calls
    * fix issue with multiple comments being confused
    * tolerate multiple semi-colons on rules
    * ignore subsequant @charset
    * syncImport option for node.js to read files syncronously
    * write the output directory if it is missing
    * change dependency on cssmin to ycssmin
    * lessc can load files over http
    * allow calling less.watch() in non dev mode
    * don't cache in dev mode
    * less files cope with query parameters better
    * sass debug statements are now chrome compatible
    * modifyVars function added to re-render with different root variables

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 19 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.3.1-4
- Unbundle cssmin.js from the sources
- Throw an error when --yui-compress is passed at the lessc command line
- Convert assorted %%prep actions into patches

* Wed Dec 19 2012 Matthias Runge <mrunge@redhat.com> - 1.3.1-3
- include LICENSE and README.md

* Wed Dec 19 2012 Matthias Runge <mrunge@redhat.com> - 1.3.1-2
- minor spec cleanup
- clear dist-dir
- license clearification

* Thu Dec 13 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.3.1-1
- Update to the 1.3.1 release
- Fix versioning bugs, get the tarball from a cleaner, tagged location

* Mon Sep 17 2012 Matthias Runge <mrunge@redhat.com> - 1.3.0-20120917git55d6e5a.1
- initial packaging
