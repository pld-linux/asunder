Summary:	A graphical Audio CD ripper and encoder
Summary(pl.UTF-8):	Graficzny ripper płyt CD Audio
Name:		asunder
Version:	1.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://littlesvr.ca/asunder/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	f4f9ac6a1d3120b7a75823936b319b53
URL:		http://littlesvr.ca/asunder/
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libcddb-devel >= 0.9.5
BuildRequires:	pkgconfig
Requires:	cdparanoia-III
Requires:	gtk+2 >= 2:2.4.0
Requires:	libcddb >= 0.9.5
Suggests:	flac
Suggests:	lame
Suggests:	vorbis-tools
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It allows to save tracks from an Audio CD as WAV, MP3, Ogg, and/or
FLAC.

%description -l pl.UTF-8
Ten program pozwala zapisywać ścieżki z płyt CD Audio jako pliki WAV,
MP3, Ogg lub FLAC.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO NEWS
%attr(755,root,root) %{_bindir}/asunder
%{_desktopdir}/asunder.desktop
%{_pixmapsdir}/asunder.png
