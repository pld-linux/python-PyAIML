#
%define		mod_package		PyAIML
%define		aiml_package		standard-aiml
#
Summary:	Pure-Python AIML (Artificial Intelligence Markup Language) interpreter module
Summary(pl.UTF-8):	Moduł interpretera AIML (Artificial Intelligence Markup Language) dla języka Python
Name:		python-%{mod_package}
Version:	0.8.5
Release:	0.1
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pyaiml/%{mod_package}-%{version}.tar.bz2
# Source0-md5:	c51cb5743ea467d4eedb2112e5a19c6d
Source1:	http://dl.sourceforge.net/pyaiml/%{aiml_package}.tar.bz2
# Source1-md5:	bb3689854846e769d9000796e2c33587
URL:		http://pyaiml.sourceforge.net/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyAIML implements an interpreter for AIML, the Artificial Intelligence
Markup Language developed by Dr. Richard Wallace of the A.L.I.C.E.
Foundation. It can be used to implement a conversational AI program.

%description -l pl.UTF-8
PyAIML jest implementacją interpretera języka AIML (Artificial
Intelligence Markup Language), stworzonego przez Dr Richarda Wallace'a
z Fundacji A.L.I.C.E. Może być użyty do stworzenia konwersacyjnego
programu SI.

%prep
%setup -q -n %{mod_package}-%{version} -T -b 0 -a 1

%build
find -type f -exec sed -i -e 's|#!.*python.*|#!%{_bindir}/python|g' "{}" ";"
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{mod_package}
install -d $RPM_BUILD_ROOT%{_datadir}/aiml

python ./setup.py install --optimize=2 --root=$RPM_BUILD_ROOT
%py_postclean
install $RPM_BUILD_ROOT%{_usr}/Lib/site-packages/aiml/self-test.aiml $RPM_BUILD_ROOT%{_datadir}/%{mod_package}
mv standard $RPM_BUILD_ROOT%{_datadir}/aiml
install std-startup.xml $RPM_BUILD_ROOT%{_datadir}/aiml
rm -rf $RPM_BUILD_ROOT%{_usr}/Lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt CHANGES.txt SUPPORTED_TAGS.txt TODO.txt
%dir %{py_sitescriptdir}/aiml
%{py_sitescriptdir}/aiml/*.py[co]
%dir %{_datadir}/%{mod_package}
%{_datadir}/%{mod_package}/*
%dir %{_datadir}/aiml
%{_datadir}/aiml/*
