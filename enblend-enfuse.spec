Summary:	Image blending with multiresolution splines
Name:		enblend-enfuse
Version:	4.1.1
Release:	2
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/enblend/%{name}-%{version}.tar.gz
# Source0-md5:	9bc34f423f3bee35150ab593211da4a2
URL:		http://enblend.sourceforge.net/
BuildRequires:	OpenEXR-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-devel
BuildRequires:	glew-devel
BuildRequires:	lcms-devel
#BuildRequires:	libgomp-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	pkg-config
BuildRequires:	vigra-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enblend is a tool for compositing images. Given a set of images that
overlap in some irregular way, Enblend overlays them in such a way
that the seam between the images is invisible, or at least very
difficult to see. Enblend does not line up the images for you. Use a
tool like Hugin to do that.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
#	--enable-openmp
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/enblend
%attr(755,root,root) %{_bindir}/enfuse
%{_mandir}/man1/enblend.1*
%{_mandir}/man1/enfuse.1*

