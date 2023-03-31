Name:		texlive-volumes
Version:	15878
Release:	2
Summary:	Typeset only parts of a document, with complete indexes etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/volumes
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/volumes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/volumes.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/volumes.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package helps you if you want to produce separate printed
volumes from one LaTeX document, as well as one comprehensive,
"all-inclusive" version. It suppresses the part of the table of
contents that are not typeset, while counters, definitions,
index entries etc. are kept consistent throughout the input
file.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/volumes/nowtoaux.sty
%{_texmfdistdir}/tex/latex/volumes/volumes.sty
%doc %{_texmfdistdir}/doc/latex/volumes/README
%doc %{_texmfdistdir}/doc/latex/volumes/volumes.pdf
#- source
%doc %{_texmfdistdir}/source/latex/volumes/volumes.dtx
%doc %{_texmfdistdir}/source/latex/volumes/volumes.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
