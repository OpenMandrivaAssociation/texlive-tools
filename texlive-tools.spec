Name:		texlive-tools
Version:	72739
Release:	1
Summary:	The LaTeX standard tools bundle
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/required/tools
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tools.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tools.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tools.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A collection of (variously) simple tools provided as part of
the LaTeX required tools distribution, comprising the packages:
afterpage, array, bm, calc, dcolumn, delarray, enumerate,
fileerr, fontsmpl, ftnright, hhline, indentfirst, layout,
longtable, multicol, rawfonts, showkeys, somedefs, tabularx,
theorem, trace, varioref, verbatim, xr, and xspace.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tools
%doc %{_texmfdistdir}/doc/latex/tools
#- source
%doc %{_texmfdistdir}/source/latex/tools

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
