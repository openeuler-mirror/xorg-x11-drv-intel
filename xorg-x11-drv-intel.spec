%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/drivers

Name:			xorg-x11-drv-intel	
Version:		2.99.917	
Release:		45
Summary:		Xorg X11 Intel video driver
License:		MIT
URL:			http://www.x.org
Source0:		https://src.fedoraproject.org/repo/pkgs/xorg-x11-drv-intel/xf86-video-intel-20180618.tar.bz2/sha512/50d7f8ec10db8200700c2de804c21987c903b347615c004e9f5334c1f2b189fafdc049469e1491d651bbcd8df2968c1247d0f4d2a3dc6c7d885a40ad577a5101/xf86-video-intel-20180618.tar.bz2
Source1:    	make-git-snapshot.sh

ExclusiveArch:  %{ix86} x86_64 ia64
BuildRequires:	autoconf automake libtool xorg-x11-server-devel libX11-devel libXinerama-devel
BuildRequires:  libXcursor-devel libXdamage-devel libXext-devel libXfixes-devel libXrandr-devel
BuildRequires:  libXrender-devel libXtst-devel libXvMC-devel libXfont2-devel mesa-libGL-devel
BuildRequires:  libdrm-devel kernel-headers libudev-devel libxcb-devel xcb-util-devel python3
BuildRequires:	cairo-devel libXScrnSaver-devel libXScrnSaver libXext-devel pixman-devel libXv-devel

Requires:		Xorg %(xserver-sdk-abi-requires ansic) polkit
Requires:		Xorg %(xserver-sdk-abi-requires videodrv)

Patch0000:    	intel-gcc-pr65873.patch
Patch0001:     	0001-sna-Avoid-clobbering-output-physical-size-with-xf86O.patch
Patch0002:     	0001-Fix-build-on-F28-and-later.patch
Patch0003:     	0001-Fix-build-on-i686.patch

%description
X.Org X11 Intel video driver.

%package_help

%prep
%autosetup -n xf86-video-intel-20180618 -p1

%build
autoreconf -f -i -v
%configure --enable-kms-only --with-default-dri=3 --enable-tools
%make_build  V=1

%install
%make_install 
%delete_la
rm -f %{buildroot}%{_libdir}/libI*XvMC.so

%ldconfig_scriptlets

%files
%defattr(-,root,root)
%doc AUTHORS
%license COPYING
%{driverdir}/intel_drv.so
%{_bindir}/intel-virtual-output
%{_libdir}/libIntelXvMC.so.1*
%{_libexecdir}/xf86-video-intel-backlight-helper
%{_datadir}/polkit-1/actions/org.x.xf86-video-intel.backlight-helper.policy

%files 		help
%defattr(-,root,root)
%doc README NEWS
%{_mandir}/man4/i*

%changelog
* Fri Sep 11 2020 lunankun <lunankun@huawei.com> - 2.99.917-45
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix source0 url

* Tue Aug 18 2020 lingsheng <lingsheng@huawei.com> - 2.99.917-44
- Add buildrequire libXv-devel to fix build

* Tue Mar 10 2020 songnannan <songnannan2@huawei.com> - 2.99.917-43
- Package init
