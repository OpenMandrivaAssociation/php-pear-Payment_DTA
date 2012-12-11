%define		_class		Payment
%define		_subclass	DTA
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.4.1
Release:	%mkrel 2
Summary:	Creates DTA files containing money transactions (Germany)
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Payment_DTA/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
%{upstream_name} provides function to create DTA files used in Germany to
exchange information about money transactions with banks or online
banking programs.


%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{upstream_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-2mdv2012.0
+ Revision: 742263
- fix major breakage by careless packager

* Tue Apr 19 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-1
+ Revision: 656065
- 1.4.1

* Wed Dec 29 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-1mdv2011.0
+ Revision: 625898
- 1.4.0

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.2-3mdv2011.0
+ Revision: 613760
- the mass rebuild of 2010.1 packages

* Sat Nov 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.2-2mdv2010.1
+ Revision: 467942
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Fri Jul 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.2-1mdv2010.0
+ Revision: 394096
- update to new version 1.3.2

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.1-1mdv2010.0
+ Revision: 383557
- update to new version 1.3.1

* Wed Dec 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.1-1mdv2009.1
+ Revision: 315172
- update to new version 1.2.1

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-9mdv2009.0
+ Revision: 237056
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.2.0-8mdv2008.1
+ Revision: 136415
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-8mdv2007.0
+ Revision: 82525
- Import php-pear-Payment_DTA

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-8mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-7mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-6mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-5mdk
- fix deps

* Fri Jul 22 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-4mdk
- fix the package.xml file so it will register

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-1mdk
- initial Mandriva package (PLD import)

