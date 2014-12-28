Summary:	A graphical Audio CD ripper and encoder
Summary(pl.UTF-8):	Graficzny ripper płyt CD Audio
Name:		asunder
Version:	2.2
Release:	2
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://littlesvr.ca/asunder/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	4996860f552879fd8abdc87d1c6c7530
URL:		http://littlesvr.ca/asunder/
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	intltool
BuildRequires:	libcddb-devel >= 0.9.5
BuildRequires:	pkgconfig
Requires:	cdparanoia-III
Requires:	gtk+2 >= 2:2.4.0
Requires:	libcddb >= 0.9.5
Suggests:	flac
Suggests:	lame
Suggests:	vorbis-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Asunder is a graphical Audio CD ripper and encoder for Linux. You can
use it to save tracks from an Audio CD as any of WAV, MP3, OGG, FLAC,
WavPack, Musepack, AAC, and Monkey's Audio files.

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

%{__mv} $RPM_BUILD_ROOT%{_localedir}/bs{_BA,}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/ur{_PK,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO NEWS
%attr(755,root,root) %{_bindir}/asunder
%{_desktopdir}/asunder.desktop
%{_pixmapsdir}/asunder.png
