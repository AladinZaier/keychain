Name:      keychain
Version:   2.2.0
Release:   1
Summary:   ssh-agent manager for OpenSSH and commercial SSH2
Vendor:    Gentoo Technologies, Inc.
Packager:  Rajiv Manglani <rajiv@gentoo.org>
URL:       http://www.gentoo.org/proj/en/keychain.xml
Source0:   %{name}-%{version}.tar.bz2
License:   GPL v2
Group:     Applications/Internet
BuildArch: noarch
Requires:  bash openssh-clients sh-utils
Prefix:    /usr/bin
BuildRoot: %{_tmppath}/%{name}-root

%description
Keychain is an extremely handy OpenSSH and commercial SSH2-compatible RSA/DSA
key management application. It acts as a front-end to ssh-agent, allowing you
to easily have one long-running ssh-agent process per system, rather than per
login session. This dramatically reduces the number of times you need to enter
your passphrase from once per new login session to once every time your local
machine is rebooted.

%prep
%setup -q

%build

%install
[ $RPM_BUILD_ROOT != / ] && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir} $RPM_BUILD_ROOT/%{_mandir}/man1
install -m0755 keychain $RPM_BUILD_ROOT/%{_bindir}/keychain
install -m0644 keychain.1 $RPM_BUILD_ROOT/%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
     %{_bindir}/*
%doc %{_mandir}/*/*
%doc ChangeLog COPYING keychain.pod README

%changelog
* Wed Apr 21 2004 Aron Griffis <agriffis@gentoo.org>
- Update to 2.2.0

* Wed Mar 5 2003 Rajiv Aaron Manglani <rajiv@gentoo.org>
- Initial build.
