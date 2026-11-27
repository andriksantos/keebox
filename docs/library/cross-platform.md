---
title: "Cross-Platform – Awesome List with 69 resources"
description: "69 curated Cross-Platform resources: Writing cross-platform code on Node.js."
---

# Cross-Platform

Writing cross-platform code on Node.js.

!!! info "Source"
    69 resources imported from [bcoe/awesome-cross-platform-nodejs](https://github.com/bcoe/awesome-cross-platform-nodejs), dedicated to the public domain ([CC0 / Unlicense](https://creativecommons.org/publicdomain/zero/1.0/)). Thanks to its maintainers and contributors. Part of the [KEEBOX Library](index.md) · Category: **Platforms**.

<!-- kb-about:start -->

## About this list

**Cross-Platform** — writing cross-platform code on Node.js. This page brings together 69 links about Cross-Platform, grouped into 5 sections. The largest sections are **Libraries**, **Applications**, **Resources**, a good place to start if you are exploring the topic for the first time. It belongs to the **Platforms** category of the KEEBOX Library; see the related lists at the end of the page for neighbouring topics.

### What you'll find

- **Resources** — 5 links
- **Applications** — 19 links
- **Libraries** — 41 links
- **Known issues** — 3 links
- **See also** — 1 link

<!-- kb-about:end -->

## Resources

- [Core Node.js documentation](https://nodejs.org/en/docs/) - Especially the [`os`](https://nodejs.org/api/os.html), [`path`](https://nodejs.org/api/path.html), [`fs`](https://nodejs.org/api/fs.html), [`process`](https://nodejs.org/api/process.html) and [`child_process`](https://nodejs.org/api/child_process.html) modules.
- [Cross-platform Node.js guide](https://github.com/ehmicky/cross-platform-node-guide) - How to write cross-platform Node.js code.
- [Microsoft Node.js Guidelines](https://github.com/Microsoft/nodejs-guidelines) - Tips, tricks, and resources for working with Node.js on Microsoft platforms.
- [Writing Cross-Platform Node.js](http://shapeshed.com/writing-cross-platform-node/) - Great tutorial covering many common issues that arise when writing cross-platform code: path creation, script execution, newline characters.
- [Cross-platform terminal characters](https://github.com/ehmicky/cross-platform-terminal-characters) - All the characters that work on most terminals and most operating systems.

## Applications

### Development environment

- [Node.js](https://nodejs.org/en/download/) - Node.js installer for various platforms.
- [nvm-windows](https://github.com/coreybutler/nvm-windows) - Manage multiple installations of Node.js on a Windows computer.
- [nvm](https://github.com/creationix/nvm) / [n](https://github.com/tj/n) - Node version manager for macOS/Linux.
- [npm-windows-upgrade](https://github.com/felixrieseberg/npm-windows-upgrade) - Upgrade npm on Windows.
- [windows-build-tools](https://github.com/felixrieseberg/windows-build-tools) - Install C++ Build Tools for Windows using npm.

### Continuous integration

- [AppVeyor](http://www.appveyor.com/) - Focused on Windows. Free tiers are available for OSS projects.
- [Travis](https://travis-ci.org/) - Windows/macOS/Linux. Free for OSS projects.
- [Azure Pipelines](https://azure.microsoft.com/en-us/services/devops/pipelines/) - Windows/macOS/Linux. Free for OSS projects with 10 parallel jobs.
- [GitHub Actions](https://github.com/features/actions) - Windows/macOS/Linux. GitHub Actions makes it easy to automate all your software workflows.
- [Gitlab CI](https://docs.gitlab.com/ee/ci/) - Windows/macOS/Linux. GitLab CI/CD is a tool built into GitLab for software development.

### Virtualization

- [ievms](https://github.com/amichaelparker/ievms) - Automated installer for the free virtual machine images that Microsoft provides for testing on multiple versions of IE. These images can be useful for cross-platform testing various technologies, however make sure you read and understand Microsoft's licensing.
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads) - General purpose software for running x86 virtual machines.
- [Docker](https://www.docker.com/) - Software platform to create, deploy and manage virtualized application containers on a common operating system, with an ecosystem of allied tools.

### Compatibility

- [Wine](https://www.winehq.org/) - Run Windows API calls on Linux, Mac, BSD and Solaris.
- [Cygwin](https://www.cygwin.com/) - Run POSIX on Windows.
- [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10) - Run the Linux command line on Windows (ELF binary execution, system calls, filesystem, Bash, core utilities, common applications).
- [MinGW](http://www.mingw.org/) - `gcc` on Windows.
- [msys](http://www.mingw.org/wiki/msys) / [Git Bash](https://gitforwindows.org/) - Bash on Windows.

### Databases

- [Redis](https://github.com/tporadowski/redis) - Native port of Redis for Windows.

## Libraries

### OS identification

- [is-windows](https://github.com/jonschlinkert/is-windows) - Detect whether the current platform is Windows.
- [is-wsl](https://github.com/sindresorhus/is-wsl) - Detect whether current platform is WSL (Windows Subsystem for Linux).
- [getos](https://github.com/retrohacker/getos) - Retrieve the current OS, including Linux distribution.
- [os-name](https://github.com/sindresorhus/os-name) - Get the name of the current operating system.
- [systeminformation](https://github.com/sebhildebrandt/systeminformation) - Hardware/software system information.

### Shell

- [execa](https://github.com/sindresorhus/execa) - Cross-platform implementation of `child_process.{execFile,exec}`.
- [gulp-execa](https://github.com/ehmicky/gulp-execa) - Cross-platform command execution in Gulp.js.
- [cross-spawn](https://github.com/IndigoUnited/node-cross-spawn) - Cross-platform implementation of `child_process.spawn()`.
- [shelljs](https://github.com/shelljs/shelljs) - Cross-platform Unix shell commands.
- [node-windows](https://github.com/coreybutler/node-windows) - Windows support for Node.js scripts (daemons, eventlog, UAC, etc).
- [log-symbols](https://github.com/sindresorhus/log-symbols) - Colored symbols for various log levels with Windows fallbacks.
- [figures](https://github.com/sindresorhus/figures) - Unicode symbols with Windows fallbacks.
- [clipboardy](https://github.com/sindresorhus/clipboardy) / [clipboard-cli](https://github.com/sindresorhus/clipboard-cli) - Cross-platform copy/paste.

### Environment

- [cross-env](https://github.com/kentcdodds/cross-env) - Set environment variables cross-platform.
- [user-home](https://github.com/sindresorhus/user-home) - Get the path to the user home directory. Cross-platform.
- [username](https://github.com/sindresorhus/username) - Get the current username.
- [osenv](https://github.com/npm/osenv) - Cross-platform environment variables.
- [is-elevated](https://github.com/sindresorhus/is-elevated) - Check if the process is running with elevated privileges.
- [which](https://github.com/npm/node-which) - Cross-platform implementation of Unix's `which`.

### Filesystem

- [rimraf](https://github.com/isaacs/rimraf) / [del](https://github.com/sindresorhus/del) - Delete files and folders. Cross-platform.
- [make-dir](https://github.com/sindresorhus/make-dir) - Cross-platform `mkdir -p`.
- [readdirp](https://github.com/paulmillr/readdirp) - Recursive version of `fs.readdir()`.
- [cpy](https://github.com/sindresorhus/cpy) - Copy files. Cross-platform.
- [chokidar](https://github.com/paulmillr/chokidar) - Improved cross-platform file watching.
- [graceful-fs](https://github.com/isaacs/node-graceful-fs) - Improves the `fs` module, especially on Windows.
- [fs-extra](https://github.com/jprichardson/node-fs-extra) - Combines `graceful-fs` with better JSON file reading and promises.
- [any-path](https://github.com/bcoe/any-path) - Use Windows and POSIX paths interchangeably when fetching values from an object.
- [dev-null-cli](https://github.com/sindresorhus/dev-null-cli) - Cross-platform `/dev/null`.
- [global-cache-dir](https://github.com/ehmicky/global-cache-dir) - Get the global OS-specific cache directory.

### Signals

- [fkill](https://github.com/sindresorhus/fkill) - Kill processes. Cross-platform.
- [signal-exit](https://github.com/tapjs/signal-exit) - Cross-platform `exit` handler.
- [human-signals](https://github.com/ehmicky/human-signals) - Human-friendly process signals.

### Processes

- [ps-list](https://github.com/sindresorhus/ps-list) - Get running processes.
- [process-exists](https://github.com/sindresorhus/process-exists) - Check if a process exists.

### Streams

- [noop-stream](https://github.com/sindresorhus/noop-stream) - Cross-platform `fs.createReadStream('/dev/null')`.
- [random-bytes-readable-stream](https://github.com/sindresorhus/random-bytes-readable-stream) - Cross-platform `fs.createReadStream('/dev/urandom')`.

### Desktop UI

- [open](https://github.com/sindresorhus/open) - Opens stuff like websites, files, executables. Cross-platform.
- [node-notifier](https://github.com/mikaelbr/node-notifier) - Cross-platform desktop notifications.

### Windows registry

- [node-winreg](https://github.com/fresc81/node-winreg) - Access the Windows registry.
- [rage-edit](https://github.com/MikeKovarik/rage-edit) - Access/modify the Windows registry.
- [windows-registry-node](https://github.com/CatalystCode/windows-registry-node) - Access/modify the Windows registry and set file associations.

## Known issues

- [cmd.exe unicode woes](https://github.com/nodejs/node-v0.x-archive/issues/7940) - By default, `cmd.exe` does not display Unicode characters on Windows.
- [spawn issues](https://github.com/nodejs/node-v0.x-archive/issues/2318) - `child_process.spawn()` behavior is not consistent between Windows and Linux.
- [exec() behavior between shells](https://github.com/isaacs/spawn-wrap#contracts-and-caveats) - Depending on the shell being used, e.g., bash vs. dash, `child_process.exec()` has inconsistent exit behavior.

## See also

- [awesome-desktop-js](https://github.com/styfle/awesome-desktop-js) - List of tools to build JavaScript applications on the desktop.

<!-- kb-related:start -->

## Related lists

More lists in the **Platforms** category of the [KEEBOX Library](index.md):

- [Deno](deno.md)
- [DigitalOcean](digitalocean.md)
- [DOS](dos.md)
- [Electron](electron.md)
- [Backstage](backstage.md)
- [Bluetooth Low Energy](bluetooth-low-energy.md)
- [Cloudflare](cloudflare.md)
- [Core](core.md)

<!-- kb-related:end -->
