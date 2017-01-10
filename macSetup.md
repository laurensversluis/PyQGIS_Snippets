# Setup of OS X for web development

## XCode Command Line Tools

First, you need to install XCode's command line tools.
This installs a lot of tools like `git` which aren't needed for plebeians.

```bash
xcode-select --install
```

If you're actually going to use XCode, just install it from the App Store and do the whole shebang.

## Install Homebrew

[Homebrew](http://brew.sh/) is OS X's package manager.
It makes setting up all your services very easy.

```bash
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### Software development programs

The following packages install all the development tools you need.

```bash
# ATOM for quickly editing code
brew cask install ATOM
# PyCharm as IDE for Python development
brew install Caskroom/versions/pycharm-ce-eap
# IntelliJ as IDE for Java development
brew cask install intellij-idea-ce
# DASH for documentation
brew cask install DASH
# GIT for performing git tasks using command line
brew install git
# GIT-Desktop for doing the same in a gui
brew cask install github-desktop
# Music for during coding
brew cask install spotify
```

### Database
There are many different database systems out there. I find the open-source PostgreSQL one of the best. Although you can install PostgreSQL using Homebrew, the [PostgresApp](https://postgresapp.com) very handy for switching on and off the server. Just download the app and move it to the program folder.

### QGIS environment
QGIS requires the [Geospatial Data Abstraction Library (GDAL)](http://www.gdal.org) to be installed.

```brew install gdal```

You will need to install a new version of python. QGIS requires the Python language and some Python packages to be installed. Although macOS has a version of Python, unfortunately it doesn’t come with the Pip package manager, which makes it easy to install Python packages. I could have installed Pip using the easy_install tool that comes with the system Python, but this method requires using sudo. Sudo commands should be avoided.

The Homebrew version of Python comes with Pip

```brew install python```

Installing Python with Homebrew gives us a version of Python that’s separate from the system Python, so any changes we make to the Homebrew version of Python won’t adversely affect macOS.

QGIS requires a number of python packages that we can install with Pip.

```bash
# Matplotlib, the Python 2D plotting library
pip install matplotlib
# Psycopg2, a Python adapter for the PostgreSQL database
PATH=$PATH:/Applications/Postgres.app/Contents/Versions/9.6/bin pip install psycopg2
```
At this stage, Python was installed and ready to go with the packages required by QGIS. QGIS is also installed with homebrew. I installed the latest Long Term Release which is the most stable version. In my case this was version 2.14. Also I have removed the installation of Grass and the QGISServer tools.

```bash
brew tap homebrew/science
brew tap osgeo/osgeo4mac
brew info qgis-xx # review options
# Installing QGIS with grass 7 and without QGIS server
brew install qgis2-ltr --without-grass --without-server
# Install a program icon in programs
brew linkapps qgis2-ltr
```

### Updating

## Install node.js with nvm

One thing many users do is install node.js globally.
This is easy to get started or fine for servers,
but it makes developing a pain.
If you have to ever run `npm` with `sudo`,
you're doing it wrong!

[nvm](https://github.com/creationix/nvm) is what I think is the best node version manager.
It can be installed with homebrew!
Yes, you use a package manager to install a version manager to install another package manager.
It's stupid, but they all have their strengths.

```bash
brew install nvm
```

Once you've installed nvm,
install the version of node.js you use:

```bash
nvm install 4
```

To make sure each terminal uses the version of node you want,
add this to your `~/.bash_profile` or whichever environment you use:

```env
# load nvm whenever a terminal starts
source ~/.nvm/nvm.sh
# load the version of nvm you want
nvm use 4
```

Now every time you open a window,
it will say which version of node you are using.
This might be annoying,
but it's better than not knowing what version you're using!

> NOTE: `nvm` slows down creating new terminals, so you may just want to use `brew install node` if you only need one version of node.

### Default node.js version

Create a `~/.nvmrc` file with just the version you'd like.

```bash
echo "6" > ~/.nvmrc
```

Then in your `bash_profile`, add the following line:

```bash
nvm use
```

Now, `nvm` will find the nearest `.nvmrc` file and use that version of node whenever the terminal starts.

### Using npm

Don't ever use `sudo`!
You don't need to `sudo npm install -g grunt-cli` or anything anymore.
Just run `npm install -g eslint` and `eslint` will always be in your path.
`nvm` adds these to your `$PATH`.

Don't ever upgrade `npm`!
At least not until node.js and io.js merge.
If anyone ever tells you to `npm update -g npm` or `npm install -g npm`,
tell them to shuttup.

Remember to add `export JOBS=max` in your `~/.bash_profile` so your `npm install`s are faster!

## thefuck?

[thefuck](https://github.com/nvbn/thefuck) is a nifty tool that allows you to fix your previous CLI typos by just typing `fuck`.
It perhaps has the greatest UX of all products, ever.

Installing it is easy:

```bash
brew install thefuck
```

Then alias it as `fuck` (or whatever you want) manually by adding this line to your `~/.bash_profile`:

```env
alias fuck='$(thefuck $(fc -ln -1))'
```

## globstars

OS X, by default, does not support globstars like `**/*.js`.
It may work for certain packages who support it,
but not by default.
To add support for it, install the latest version of bash with `brew install bash`
and follow the instructions at http://mistermorris.com/blog/get-yourself-globstar-bash-4-for-your-mac-terminal/.

Then add the following line to your `~/.bash_profile`:

```bash
echo "shopt -s globstar" >> ~/.bash_profile
```

or just:

```
shopt -s globstar
```

## vim

By default, `vim` installed via `brew` sucks.
Create a `~/.vimrc` with the following:

```
:set nocompatible
syntax on
```

## git

`git` by default doesn't have autocompletion on OS X.
Super easy to [install it](https://github.com/bobthecow/git-flow-completion/wiki/Install-Bash-git-completion):

```bash
brew install bash-completion
```

Then add this line to your `~/.bash_profile`:

```bash
if [ -f `brew --prefix`/etc/bash_completion ]; then
    . `brew --prefix`/etc/bash_completion
fi
```

Make sure your git pushes only the current branch.
Run the following:

```bash
git config --global push.default simple
```

To have git user the OS X Keychain, run this command:

```bash
git config --global credential.helper osxkeychain
```

## Setting up databases

Homebrew makes setting up databases super easy.
First step - install it with Homebrew:

```bash
brew install redis
```

Then you'll see information on your terminal like the following:

```
To reload redis after an upgrade:
    launchctl unload ~/Library/LaunchAgents/homebrew.mxcl.redis.plist
    launchctl load ~/Library/LaunchAgents/homebrew.mxcl.redis.plist
Or, if you don't want/need launchctl, you can just run:
    redis-server /usr/local/etc/redis.conf
```

To read this information again, just type `brew info redis`.
All I do is copy and paste the first 2 commands listed.
Voila!
`redis-server` will always be running!
You won't have to open a bunch of terminals to keep it running!

Rinse and repeat for all your databases.

## brew options

A lot of packages on Homebrew have terrible defaults.
I haven't bothered making a PR to update these defaults,
mostly because I don't have a reason to change the defaults other than, "why not?"

For example, type the following:

```bash
brew options ffmpeg
```

You're probably overloaded with options.
Fun isn't it?
Supposedly, once you install a package with homebrew using specific options,
future updates will use the same options.
I haven't found that to be the case - I have to reinstall `ffmpeg` many times - but I'm not going to try reproducing it.

Have fun reading all the option info and typing commands like:

```bash
brew install ffmpeg --with-faac --with-libssh --with-libvorbis --with-libvpx --with-openssl --with-opus --with-theora --with-webp --with-x265
```

Not only will this install all the dependencies like `webp`,
it will make sure you can pretty much throw anything at `ffmpeg`.

You'll probably have to do the same with `imagemagick` and/or `graphicsmagick`.

## Ruby

Lots of programs use ruby, so be sure to install it!

```bash
brew install ruby
```

## Java

Unfortunately, a lot of programs still require Java.
Install Java by googling "Java OS X".
https://support.apple.com/kb/DL1572?locale=en_US

## DNS Server

Set Google as your computer's DNS server and default search domain,
which will almost always be better than your ISP's default settings.
https://developers.google.com/speed/public-dns/docs/using?hl=en#mac_os

## Other Tools

- [iStat Menus](http://bjango.com/mac/istatmenus/) - help me figure out if something's taking too much CPU, RAM, or network
- [Atom](https://atom.io/) - the best text editor :D
- [Sublime Text](http://www.sublimetext.com/) - the second best text editor
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads) - for VMs, which can't be install using Homebrew

## Maintenance

To update your packages,
simply run:

```bash
brew update
brew upgrade
```

Once in a while, I run ```brew prune``` and ```brew doctor``` to keep my computer in check.
