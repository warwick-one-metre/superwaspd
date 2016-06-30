Name:      onemetre-superwasp-client
Version:   1.8
Release:   0
Url:       https://github.com/warwick-one-metre/superwaspd
Summary:   SuperWASP weather log client for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4

%description
Part of the observatory software for the Warwick one-meter telescope.

superwasp is a commandline utility that queries the SuperWASP weather log daemon.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/superwasp %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/superwasp %{buildroot}/etc/bash_completion.d/superwasp

%files
%defattr(0755,root,root,-)
%{_bindir}/superwasp
/etc/bash_completion.d/superwasp

%changelog
