# SPEC file overview:
# https://docs.fedoraproject.org/en-US/quick-docs/creating-rpm-packages/#con_rpm-spec-file-overview
# Fedora packaging guidelines:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/

%define pkg_version 0.2.0
%global debug_package %{nil}

Name: hid-lenovo-tp1gen3
Version: %{pkg_version}
Release: 0%{?dist}
Summary: HID kernel module for Thinkpad X1 Tablet Gen 3
BuildArch: noarch
License: MIT
URL: https://github.com/amosbird/linux-tp1gen3
Source0: %{name}-%{version}.tar.bz2

BuildRequires: dkms
Requires: dkms

%description
HID kernel module for Thinkpad X1 Tablet Gen 3

%prep
%setup -q -n linux-tp1gen3
tar xvf %{SOURCE0}

%build

%install
mkdir -p %{buildroot}/%{_prefix}/src/hid-lenovo-tp1gen3-%{pkg_version}
cp -a ./hid/src/* %{buildroot}/%{_prefix}/src/hid-lenovo-tp1gen3-%{pkg_version}

%post
occurrences=/usr/sbin/dkms status | grep "%{name}" | grep "%{version}" | wc -l
if [ ! occurrences > 0 ];
then
    /usr/sbin/dkms add -m %{name} -v %{version}
fi
/usr/sbin/dkms build -m %{name} -v %{version}
/usr/sbin/dkms install -m %{name} -v %{version}

%preun
/usr/sbin/dkms remove -m %{name} -v %{version} --all

%files
%defattr(-, root, root, -)
%{_prefix}/src/hid-lenovo-tp1gen3-%{pkg_version}/

%changelog


