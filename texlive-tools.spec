%global tl_name tools
%global tl_revision 79234

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	The LaTeX standard tools bundle
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/required/tools
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tools.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tools.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tools.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A collection of (variously) simple tools provided as part of the LaTeX
required tools distribution, comprising the packages: afterpage, array,
bm, calc, dcolumn, delarray, enumerate, fileerr, fontsmpl, ftnright,
hhline, indentfirst, layout, longtable, multicol, rawfonts, shellesc,
showkeys, somedefs, tabularx, theorem, trace, varioref, verbatim, xr,
and xspace.

