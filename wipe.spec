Summary:	Cryptographically secure file wiping utility
Summary(pl):	Narzêdzie do kryptograficznie bezpiecznego kasowania plików
Name:		wipe
Version:	0.20
Release:	1
License:	GPL
Group:		Applications/File
Source0:	http://abaababa.ouvaton.org/wipe/%{name}-%{version}.tar.gz
# Source0-md5:	dbf3027f46d014dc899a1cdf2ed93d00
Patch0:		%{name}-Makefile.patch
URL:		http://abaababa.ouvaton.org/wipe/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wipe is a tool for cryptographically secure file deletion from
magnetic media, to prevent using advanced recovery techniques like
magnetic force microscopy (MFM). Wipe will repeadetly overwrites
special patterns to the files to be destroyed, using the fsync() call
and/or the O_SYNC bit to force disk access. In normal mode, 34
patterns are used (of which 8 are random).

%description -l pl
Wipe jest narzêdziem, s³u¿±cym do kryptograficznie bezpiecznego
kasowania plików z no¶ników magnetycznych tak, by uniemo¿liwiæ próby
ich odtworzenia przy pomocy zaawansowanych technik takich jak
mikroskopia magnetyczna MFM. Wipe wielokrotnie nadpisuje dany plik
specjalnymi maskami, u¿ywaj±c fsync() i/lub bitu O_SYNC dla
zapewnienia dostêpu do dysku. W normalnym trybie wipe u¿ywa 34 masek,
z których 8 jest losowych.

%prep
%setup -q
%patch -p1

%build
%{__make} \
	%{_os} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install wipe $RPM_BUILD_ROOT%{_bindir}
install wipe.1 $RPM_BUILD_ROOT%{_mandir}/man1


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README secure_del.html

%attr(755,root,root) %{_bindir}/wipe
%{_mandir}/man1/*
