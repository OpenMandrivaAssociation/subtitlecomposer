Name:		subtitlecomposer
Version:	0.8.1
Release:	1
Summary:	A text-based subtitles editor
License:	GPLv2+
Group:		Text tools
URL:		  https://subtitlecomposer.kde.org/
Source0:	https://download.kde.org/stable/subtitlecomposer/%{name}-%{version}.tar.xz

BuildRequires:	gettext
BuildRequires:	ffmpeg-devel

BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6OpenGLWidgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Widgets)

BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6Sonnet)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6WidgetsAddons)

BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(icu-io)
BuildRequires:	pkgconfig(libxine)
BuildRequires:	pkgconfig(mpv)
BuildRequires: pkgconfig(OpenSSL)

Requires:	kf6-kio
Requires:	plasma6-kio-extras

%description
A text-based subtitles editor that supports basic operations as well as more
advanced ones, aiming to become an improved version of Subtitle Workshop for
every platform supported by KF6 (KDE Frameworks 6).

Features:

  * Support for multiple formats, including SubRip, MicroDVD, SSA/ASS
    (without advanced styles), MPlayer, TMPlayer and YouTube captions.
  * Live preview of subtitles and video with support for multiple backends
    (GStreamer, MPlayer/2, MPV, Xine, Phonon), audio channel selection and
    full screen mode.
  * Time shifting and adjusting, lines duration calculation, synchronization
    with video, etc.
  * Working with original subtitle and translation.
  * Texts styles (italic, bold, underline, stroke, color), spell checking,
    automatic translation (using Google services), etc.
  * Joining and splitting of files.
  * Automatic detection of errors.
  * Editing of subtitles through scripting (Ruby, Python, JavaScript and other
    languages supported by Kross).

%prep
%autosetup -p1

%build
%cmake -DQT_MAJOR_VERSION:BOOL=6 \
           -DKDE_INSTALL_LIBDIR=%{_lib}
%make_build

%install
%make_install -C build

%find_lang %{name}

# we don't want these
find %{buildroot} -name '*.h' -delete

%files -f %{name}.lang
%doc ChangeLog README.md
%license LICENSE
#{_kf6_bindir}/%{name}
#{_kf6_applicationdir}/org.kde.%{name}.desktop
#config(noreplace) %{_kf6_sysconfdir}/xdg/%{name}rc
#{_kf6_datadir}/%{name}/
#{_kf6_iconsdir}/hicolor/*/*/*.png
#{_kf6_datadir}/mime/packages/%{name}.xml
#{_kf6_metainfodir}/org.kde.subtitlecomposer.appdata.xml
