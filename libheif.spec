%global optflags %{optflags} -O3

%define major 1
%define libname %mklibname heif %{major}
%define devname %mklibname heif -d

Summary:	libheif is a ISO/IEC 23008-12:2017 HEIF file format decoder and encoder
Name:		libheif
Version:	1.12.0
Release:	2
Group:		System/Libraries
License:	LGPLv2 and GPLv2
URL:		http://www.libheif.org/
Source0:	https://github.com/strukturag/libheif/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libde265)
BuildRequires:	pkgconfig(x265)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
Requires:	libde265

%description
libheif is an ISO/IEC 23008-12:2017 HEIF file format decoder and encoder.

HEIF is a new image file format employing HEVC (h.265) image coding for the
best compression ratios currently possible.

libheif makes use of libde265 for the actual image decoding and x265 for
encoding. Alternative codecs for, e.g., AVC and JPEG can be provided as
plugins.

%package -n %{libname}
Summary:	Libraries for %{name}
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libname}
%{libname} contains the libraries for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	heif-devel = %{EVRD}

%description -n %{devname}
The %{devname} package contains libraries and header files for
developing applications that use %{name}.

%package gdk-pixbuf
Summary:	GDK-Pixbuf plugin for handling HEIF files
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}

%description gdk-pixbuf
GDK-Pixbuf plugin for handling HEIF files

%prep
%autosetup -p1
./autogen.sh
%configure

%build
%make_build

%install
%make_install
find %{buildroot} -name '*.*a' -delete

%files
%doc README.md
%{_bindir}/*
%{_datadir}/mime/packages/avif.xml
%{_datadir}/mime/packages/heif.xml
%{_datadir}/thumbnailers/heif.thumbnailer
%{_mandir}/man1/*.1.*

%files gdk-pixbuf
%{_libdir}/gdk-pixbuf-*/*/loaders/libpixbufloader-heif.so

%files -n %{libname}
%{_libdir}/*%{name}*.so.%{major}*

%files -n %{devname}
%{_includedir}/%{name}/
%{_libdir}/*%{name}*.so
%{_libdir}/pkgconfig/libheif.pc
