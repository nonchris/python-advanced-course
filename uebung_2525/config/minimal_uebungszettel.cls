\ProvidesClass{config/minimal_uebungszettel}
\LoadClass[11pt]{scrartcl}

\RequirePackage{amsfonts}
\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage{amsthm}
\RequirePackage{array}
\RequirePackage[ngerman]{babel}
\RequirePackage[left=2.5cm,right=2.5cm,top=3cm,bottom=3cm]{geometry}
\RequirePackage{bm}
\RequirePackage{xcolor}
\RequirePackage{enumitem}
\RequirePackage{ifthen}
\RequirePackage[utf8]{inputenc}
\RequirePackage{listings}
\RequirePackage{graphicx}
\RequirePackage{tikz}
\RequirePackage{tikz-cd}
\RequirePackage{mathrsfs}
\RequirePackage{mathtools}
\RequirePackage[hyphens]{url}
\RequirePackage{verbatim}
\RequirePackage{xspace}
\RequirePackage{hyperref}
\RequirePackage[all]{hypcap}

% Allow to break links after / and after -
\def\UrlBreaks{\do\/\do-}
\setlist[enumerate]{label=\emph{(\arabic*)}}

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{scrartcl}}
\ProcessOptions\relax

% Course metadata used by sheets.
\providecommand{\itswg}{false}
\makeatletter
\newcommand*{\vorlesung}[1]{\def\@vorlesung{#1}}
\newcommand*{\semester}[1]{\def\@semester{#1}}
\newcommand*{\assi}[1]{\def\@assi{#1}}
\newcommand*{\tutor}[1]{\def\@tutor{#1}}
\newcommand*{\hinweis}[1]{\def\@hinweis{#1}}
\newcommand*{\ausgabe}[1]{\def\@ausgabe{#1}}
\newcommand*{\abgabe}[1]{\def\@abgabe{#1}}

\renewcommand\maketitle{
  \begin{center}
    {\textbf{\Large \@vorlesung}\par}
    \vspace{0.4em}
    {\textbf{\large \@title}\par}
    \vspace{0.4em}
    {\@semester\par}
    \vspace{1.2em}
    \xdef\@author{\@author}\ifx\@author\@empty\else\@author\par\fi
    \xdef\@assi{\@assi}\ifx\@assi\@empty\else\@assi\par\fi
    \xdef\@tutor{\@tutor}\ifx\@tutor\@empty\else\@tutor\par\fi
    \vspace{1.0em}
    \xdef\@ausgabe{\@ausgabe}\ifx\@ausgabe\@empty\else Ausgabe: \@ausgabe\par\fi
    \xdef\@abgabe{\@abgabe}\ifx\@abgabe\@empty\else Abgabe: \@abgabe\par\fi
  \end{center}
  \vspace{0.8em}
  \noindent\emph{\@hinweis}
  \vspace{0.7cm}
  \global\let\maketitle\relax
  \global\let\@author\@empty
  \global\let\author\relax
  \global\let\@date\@empty
  \global\let\date\relax
  \global\let\@title\@empty
  \global\let\title\relax
  \global\let\@vorlesung\@empty
  \global\let\vorlesung\relax
  \global\let\@semester\@empty
  \global\let\semester\relax
  \global\let\@assi\@empty
  \global\let\assi\relax
  \global\let\@tutor\@empty
  \global\let\tutor\relax
  \global\let\@hinweis\@empty
  \global\let\hinweis\relax
  \global\let\@ausgabe\@empty
  \global\let\ausgabe\relax
  \global\let\@abgabe\@empty
  \global\let\abgabe\relax
  \global\let\and\relax
}
\makeatother

\makeatletter
\newcommand\footnoteref[1]{\protected@xdef\@thefnmark{\ref{#1}}\@footnotemark}
\makeatother

\newcommand{\todo}[1]{\textbf{\color{red}#1}}

\theoremstyle{definition}
\newtheorem{aufg}{Aufgabe}
\newtheorem{aufg_schw}[aufg]{Aufgabe*}
\newtheorem*{hinw}{Lösungshinweise}
\renewcommand{\labelenumi}{\alph{enumi})}
\renewcommand{\labelenumii}{\Alph{enumii})}

\setlength{\headheight}{2.0\baselineskip}

% Listing setup and color scheme.
\lstset{
  language=Matlab,
  basicstyle=\footnotesize,
  numbers=left,
  stepnumber=1,
  showstringspaces=false,
  tabsize=1,
  breaklines=true,
  breakatwhitespace=false,
  frame=single,
  numberstyle=\tiny\color{colorgray},
  numbersep=6pt,
  xleftmargin=3pt,
  xrightmargin=3pt
}

\lstdefinelanguage{plain}{
  basicstyle=\normalsize\ttfamily\color{black},
  numberstyle=\footnotesize,
  numbersep=5pt
}

\lstdefinelanguage{plsmall}{
  basicstyle=\small\ttfamily\color{black},
  numberstyle=\scriptsize,
  numbersep=4pt
}

\lstdefinelanguage{pltiny}{
  basicstyle=\scriptsize\ttfamily\color{black},
  numbers=none
}

\lstdefinelanguage{pltinytiny}{
  basicstyle=\tiny\ttfamily\color{black},
  numbers=none
}

\lstset{language=plsmall}

\newcommand{\lpl}[1]{\lstinline[language=plain]{#1}}
\newcommand{\lplsmall}[1]{\lstinline[language=plsmall]{#1}}

\definecolor{col_keywords}{HTML}{000000}
\definecolor{col_classes}{HTML}{0057AE}
\definecolor{col_members}{HTML}{644A9B}
\definecolor{col_string}{HTML}{BF0303}
\definecolor{col_preproc}{HTML}{006E28}

\lstdefinelanguage{py}[]{Python}{
  basicstyle=\normalsize\ttfamily\color{black},
  numberstyle=\scriptsize,
  numbersep=5pt,
  commentstyle=\color{black!50}\ttfamily,
  stringstyle=\color{col_string},
  deletekeywords={bool, complex, dict, float, int, list, print, set, tuple, frozenset},
  keywords=[2]{__init__, __name__},
  keywords=[3]{bool, complex, float, int, list, print, set, tuple, frozenset},
  keywordstyle=\bfseries\color{col_keywords},
  keywordstyle=[2]\color{col_classes},
  keywordstyle=[3]\bfseries\color{col_members}
}

\lstdefinelanguage{pysmall}[]{py}{
  basicstyle=\small\ttfamily\color{black},
  numberstyle=\scriptsize,
  numbersep=4pt
}

\lstdefinelanguage{pytiny}[]{py}{
  basicstyle=\scriptsize\ttfamily\color{black},
  numbers=none
}

\lstdefinelanguage{pytinytiny}[]{py}{
  basicstyle=\tiny\ttfamily\color{black},
  numbers=none
}

\newcommand{\lpy}[1]{\lstinline[language=py]{#1}}
\newcommand{\lpysmall}[1]{\lstinline[language=pysmall]{#1}}
