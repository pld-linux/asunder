#
# TODO:
# - check BR-s and R-s
# - translations
#
Summary:	A graphical Audio CD ripper and encoder
Summary(pl.UTF-8):Graficzny ripper płyt Audio CD
Name:		asunder
Version:	0.8.1
Release:	0.1
License:	GPLv2
Group:		Applications/File
Source0:	http://littlesvr.ca/asunder/releases/%{name}-%{version}.tar.gz
# Source0-md5:	75cbd3c99db2bc977b53e39946f8ea86
URL:		http://littlesvr.ca/asunder/
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	gtk+2-devel >= 2.4
BuildRequires:	libcddb-devel >= 0.9.5
Requires:	cdparanoia
Requires:	libcddb >= 0.9.5
Suggests:	vorbis-tools
Suggests:	flac
Suggests:	lame
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It allows to save tracks from an Audio CD as WAV, MP3, OGG, and/or
FLAC.

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
#man page is not currently available
#%{_mandir}/man1/asunder.1*
