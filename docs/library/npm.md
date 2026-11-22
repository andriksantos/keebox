---
title: "npm – Awesome List with 101 resources"
description: "101 curated npm resources: Package manager."
---

# npm

Package manager.

!!! info "Source"
    101 resources imported from [sindresorhus/awesome-npm](https://github.com/sindresorhus/awesome-npm), dedicated to the public domain ([CC0 / Unlicense](https://creativecommons.org/publicdomain/zero/1.0/)). Thanks to its maintainers and contributors. Part of the [KEEBOX Library](index.md) · Category: **Programming Languages**.
## Articles

- [Small focused modules](https://github.com/sindresorhus/ama/issues/10#issuecomment-117766328)
- [Unix philosophy and Node.js](http://blog.izs.me/post/48281998870/unix-philosophy-and-nodejs) - Write programs that do one thing and do it well.
- [Writing small modules](https://web.archive.org/web/20180302125059/https://substack.net/how_I_write_modules)
- [Semver: A Primer](https://nodesource.com/blog/semver-a-primer/) *(Must read!)*
- [Semver: Tilde and Caret](https://nodesource.com/blog/semver-tilde-and-caret/)
- [Offline installation of npm packages](https://addyosmani.com/blog/using-npm-offline/)
- [Task automation with npm run](https://web.archive.org/web/20180302164842/http://substack.net/task_automation_with_npm_run)
- [How to use npm as a build tool](https://www.keithcirkel.co.uk/how-to-use-npm-as-a-build-tool/)
- [Install npm packages globally without sudo on macOS and Linux](https://github.com/sindresorhus/guides/blob/main/npm-global-without-sudo.md)
- [Optimizing the footprint of an npm package](https://medium.com/@goldglovecb/npm-needs-a-personal-trainer-537e0f8859c6)
- [The Art of Node](https://github.com/maxogden/art-of-node#modules) - An introduction to Node.js and client-side development with npm.
- [Why npm scripts?](https://css-tricks.com/why-npm-scripts/) - An introduction to npm scripts with common packages and scripts, as well as a boilerplate project.

## Tools

### Web

- [npms](https://npms.io) - Superb package search with deep analysis of package quality using a [myriad of metrics](https://npms.io/about).
- [NodeICO](https://nodei.co/) - Package badges.
- [Libraries.io](https://libraries.io/npm) - Package discovery.
- [npm-stat](http://npm-stat.com) - Statistics charts for packages.
- [npmgraph](http://npm.anvaka.com) - Visualization of dependencies.
- [npm trends](http://www.npmtrends.com) - Compare package download counts over time.
- [npm-top](https://gist.github.com/bcoe/dcc961b869bbf6685002) - npm users by downloads.
- [npm semver calculator](http://semver.npmjs.com) - Visually explore what versions of a package a semver range matches.
- [ghub.io](https://ghub.io) - Redirects to the GitHub repo of an npm package.
- [moiva](https://moiva.io) - Discover and compare packages.
- [npmx.dev](https://npmx.dev) - Fast and modern viewer for the npm registry.

### Browser extensions

- [Octo-Linker](https://chrome.google.com/webstore/detail/octo-linker/jlmafbaeoofdegohdhinkhilhclaklkp) - Chrome extension to navigate across npm packages on GitHub with ease.
- [npm-hub](https://chrome.google.com/webstore/detail/npm-hub/kbbbjimdjbjclaebffknlabpogocablj) - Chrome extension to explore npm dependencies on GitHub repos.
- [github-npm-stats](https://chrome.google.com/webstore/detail/github-npm-stats/oomfflokggoffaiagenekchfnpighcef) - View npm download stats on GitHub.
- [npm-search-update](https://chrome.google.com/webstore/detail/npm-search-update/kagpoplamlmaonpddimnnigiojimihnh) - Chrome extension to quickly search for dependencies and monitor changes from the npm registry.

### CLI

- [zsh-better-npm-completion](https://github.com/lukechilds/zsh-better-npm-completion) - Better ZSH completion for npm.
- [npkill](https://github.com/voidcosmos/npkill) - Easily find and remove old and heavy node_modules folders.

## Packages

### Publishing

- [np](https://github.com/sindresorhus/np) - A better `npm publish`.
- [publish-please](https://github.com/inikulin/publish-please) - Publish packages safely and gracefully.
- [npm-release](https://github.com/phuu/npm-release) - Making releasing to npm so easy a kitten could probably do it™.
- [pkgfiles](https://github.com/timoxley/pkgfiles) - List all files which would be published in a package.
- [release-it](https://github.com/webpro/release-it) - Automate releases for Git repositories and/or npm packages. Changelog generation, GitHub/GitLab releases, etc.
- [semantic-release](https://github.com/semantic-release/semantic-release) - Fully automated package publishing.

### Registry

- [npm-name](https://github.com/sindresorhus/npm-name-cli) - Check whether a package name is available on npm.
- [package-json](https://github.com/sindresorhus/package-json) - Get the package.json of a package from the npm registry.
- [latest-version](https://github.com/sindresorhus/latest-version-cli) - Get the latest version of an npm package.
- [npm-keyword](https://github.com/sindresorhus/npm-keyword) - Get a list of npm packages with a certain keyword.
- [npm-user](https://github.com/sindresorhus/npm-user) - Get user info of an npm user.
- [npm-email](https://github.com/sindresorhus/npm-email) - Get the email of an npm user.
- [npm-user-packages](https://github.com/kevva/npm-user-packages-cli) - Get packages by an npm user.
- [dpn](https://github.com/gillstrom/dpn) - Get the dependents of a user's npm packages.
- [npm-stats](https://github.com/hughsk/npm-stats) - Get data from an npm registry.
- [npm-cli-login](https://github.com/postmanlabs/npm-cli-login) - Log in to npm.
- [nrm](https://github.com/Pana/nrm) - Registry manager.
- [npm-register](https://github.com/dickeyxxx/npm-register) - Easy to set up and maintain npm registry and proxy.
- [verdaccio](https://github.com/verdaccio/verdaccio) - Lightweight private npm proxy registry.
- [cloudsmith](https://cloudsmith.io/l/npm-registry/) - A fully managed package management SaaS with support for public and private npm registries (and many others).
- [RepoFlow](https://www.repoflow.io) - A simple and easy-to-use package management platform, available for both cloud and self-hosted deployments.

### Other

- [npm-home](https://github.com/sindresorhus/npm-home) - Open the npm page of a package.
- [gh-home](https://github.com/sindresorhus/gh-home) - Open the GitHub page of a package.
- [david](https://github.com/alanshaw/david) - Check if your package dependencies are out of date.
- [npm-check](https://github.com/dylang/npm-check) - Check for outdated, incorrect, and unused dependencies, as well as interactive update.
- [npm-upgrade](https://github.com/th0r/npm-upgrade) - Update outdated npm dependencies interactively.
- [npm-shrinkwrap](https://github.com/uber/npm-shrinkwrap) - A consistent shrinkwrap tool.
- [npm-windows-upgrade](https://github.com/felixrieseberg/npm-windows-upgrade) - Upgrade npm on Windows.
- [generator-nm](https://github.com/sindresorhus/generator-nm) - Scaffold out an npm package.
- [package-up](https://github.com/sindresorhus/package-up) - Find the closest package.json file.
- [read-package-up](https://github.com/sindresorhus/read-package-up) - Read the closest package.json file.
- [normalize-package-data](https://github.com/npm/normalize-package-data) - Normalize package metadata.
- [package-config](https://github.com/sindresorhus/package-config) - Get namespaced config from the closest package.json.
- [npm-run-path](https://github.com/sindresorhus/npm-run-path) - Run locally installed binaries in the terminal by name like with global ones.
- [local-npm](https://github.com/nolanlawson/local-npm) - Use npm [offline](https://addyosmani.com/blog/using-npm-offline/).
- [npe](https://github.com/zeke/npe) - CLI for inspecting and editing properties in package.json.
- [engine-deps](https://github.com/samccone/engine-deps) - Manage Node.js version specific dependencies with ease.
- [enpeem-search](https://github.com/amovah/enpeem-search) - Search packages by scraping the npm web search.
- [npm-issues](https://github.com/seanzarrin/npm-issues) - Search known issues of all your packages at once.
- [john](https://github.com/davej/john) - Make npm3's flat dependencies easier to find and sort.
- [ntl](https://github.com/ruyadorno/ntl) - Interactive CLI menu to list & run npm tasks.
- [decheck](https://github.com/egoist/decheck) - Explore dependencies of npm packages in the command-line.
- [shrinkpack](https://github.com/JamieMason/shrinkpack) - Lock down your dependencies and install offline.
- [redrun](https://github.com/coderaiser/redrun) - Expand scripts from package.json to improve execution speed.
- [package-size](https://github.com/egoist/package-size) - Get the bundle size of an npm package.
- [synp](https://github.com/imsnif/synp) - Convert yarn.lock to package-lock.json and vice versa.
- [npm-run-all](https://github.com/mysticatea/npm-run-all) - CLI tool to run multiple npm-scripts in parallel or serial.
- [onchange](https://github.com/Qard/onchange) - Watch files and folders and run a command when something changed.
- [cli-error-notifier](https://github.com/micromata/cli-error-notifier) - Sends native desktop notifications when npm scripts fail.
- [luna](https://github.com/rvpanoz/luna) - App to manage npm dependencies.
- [emma-cli](https://github.com/maticzav/emma-cli) - Interactive CLI package search utility.
- [lockfile-lint](https://github.com/lirantal/lockfile-lint) - Lint lockfiles for improved security and trust policies to mitigate malicious package injection and insecure lockfile resources.

## Clients

- [yarn](https://github.com/yarnpkg/yarn) - Fast, reliable, and secure dependency management.
- [npm](https://github.com/npm/cli) - The official client.
- [pnpm](https://github.com/pnpm/pnpm) - Fast, disk space efficient package manager.

## Tips

### Run scripts

### Lifecycle scripts

## FAQ

- [Check in node_modules vs. shrinkwrap](http://stackoverflow.com/questions/11459733/check-in-node-modules-vs-shrinkwrap)
- [What is the difference between Bower and npm?](http://stackoverflow.com/questions/18641899/what-is-the-difference-between-bower-and-npm)
- [What does `^` mean in package.json versioning?](http://stackoverflow.com/questions/22137778/what-does-mean-in-package-json-versioning)
- [Find the version of an installed npm package](http://stackoverflow.com/questions/10972176/find-the-version-of-an-installed-npm-package)
- [What's the difference between dependencies, devDependencies, and peerDependencies in package.json?](http://stackoverflow.com/questions/18875674/whats-the-difference-between-dependencies-devdependencies-and-peerdependencies)

## Community

- [`#npm` on Freenode](http://webchat.freenode.net/?channels=npm)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/npm)
- [Reddit](https://www.reddit.com/r/npm)
- [Twitter](https://twitter.com/npmjs)
- [Blog](https://blog.npmjs.org)

## Documentation

- [Official](https://docs.npmjs.com)
- [Troubleshooting](https://github.com/npm/npm/wiki/Troubleshooting)
- [Semantic versioning](https://docs.npmjs.com/getting-started/semantic-versioning)
- [Fixing npm permissions](https://docs.npmjs.com/getting-started/fixing-npm-permissions)
- [package.json](https://docs.npmjs.com/files/package.json)
- [npm run script](https://docs.npmjs.com/cli/run-script)
- [Stats API](https://github.com/npm/download-counts)
