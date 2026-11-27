---
title: "SSH – Awesome List with 103 resources"
description: "103 curated SSH resources: Curated SSH resources."
---

# SSH

Curated SSH resources.

!!! info "Source"
    103 resources imported from [moul/awesome-ssh](https://github.com/moul/awesome-ssh), dedicated to the public domain ([CC0 / Unlicense](https://creativecommons.org/publicdomain/zero/1.0/)). Thanks to its maintainers and contributors. Part of the [KEEBOX Library](index.md) · Category: **Development Environment**.

<!-- kb-about:start -->

## About this list

**SSH**. This page brings together 103 links about SSH, grouped into 3 sections. The largest sections are **Apps**, **Resources**, **Libraries**, a good place to start if you are exploring the topic for the first time. It belongs to the **Development Environment** category of the KEEBOX Library; see the related lists at the end of the page for neighbouring topics.

### What you'll find

- **Apps** — 80 links
- **Libraries** — 10 links
- **Resources** — 13 links

<!-- kb-about:end -->

## Apps

### `.ssh/config`

- [`assh`](https://github.com/moul/assh) [](https://github.com/moul/advanced-ssh-config) - Transparent wrapper (ProxyCommand) that adds regex, aliases, gateways, includes, dynamic hostnames to *SSH* and `ssh-config`. _Previously: `advanced-ssh-config`_
- [storm](https://github.com/emre/storm) [](https://github.com/emre/storm) - Manage your *SSH* like a boss.
- [ansible-ssh-config](https://github.com/gaqzi/ansible-ssh-config) [](https://github.com/gaqzi/ansible-ssh-config) - Letting *Ansible* manage `ssh_config`.
- [ec2ssh](https://github.com/mirakui/ec2ssh) [](https://github.com/mirakui/ec2ssh) - A `ssh_config` manager for *AWS EC2*.
- [ssh-config](https://github.com/dbrady/ssh-config) [](https://github.com/dbrady/ssh-config) - A tool to help manage your `.ssh/config` file.

### Tools using the *SSH* protocol

- [scp](http://linux.die.net/man/1/scp) - Secure remote file copy utility over *SSH*.
- [rsync](https://rsync.samba.org) - Fast incremental transfer utility that supports *SSH*.
- [sftp](https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol) - File transfer protocol over *SSH*.
- [curl](http://curl.haxx.se) - Command line tool and library to transfer data (support `sftp`).

### Servers

- [sshportal](https://github.com/moul/sshportal) [](https://github.com/moul/sshportal) - simple, fun, and transparent SSH (& Telnet) Bastion Server
- [ssh2docker](https://github.com/moul/ssh2docker) [](https://github.com/moul/ssh2docker) - *SSH* server to Docker containers.
- [ssh-proxy](https://github.com/ml-tooling/ssh-proxy) [](https://github.com/ml-tooling/ssh-proxy) - Dockerized SSH bastion to proxy SSH connections to arbitrary containers.
- [whosthere](https://github.com/FiloSottile/whosthere) [](https://github.com/FiloSottile/whosthere) - A *SSH* server that knows who you are. `$ ssh whoami.filippo.io`.
- [sshfront](https://github.com/gliderlabs/sshfront) [](https://github.com/gliderlabs/sshfront) - Programmable *SSH* frontend.
- [ssh-chat](https://github.com/shazow/ssh-chat) [](https://github.com/shazow/ssh-chat) - Chat over *SSH*.
- [sshcommand](https://github.com/dokku/sshcommand) [](https://github.com/dokku/sshcommand) - Turn *SSH* into a thin client specifically for your app.
- [sshmuxd](https://github.com/joushou/sshmuxd) [](https://github.com/joushou/sshmuxd) - `sshmux` frontend.
- [x84](https://github.com/jquast/x84) [](https://github.com/jquast/x84) - A *python* `telnet`/`ssh` server for modern *UTF-8* and classic *cp437* network virtual terminals. In spirit of classic software such as *ami/x*, *teleguard*, *renegade*, *iniquity*.
- [teleport](https://github.com/gravitational/teleport) [](https://github.com/gravitational/teleport) - Modern *SSH* server for clusters and teams.
- [ShellHub](https://github.com/shellhub-io/shellhub) [](https://github.com/shellhub-io/shellhub) - A *SSH* gateway for remotely accessing any Linux device behind firewall and NAT.

### Network

- [Mosh](https://mosh.mit.edu) - The mobile shell.
- [sshfs](https://github.com/libfuse/sshfs) [](https://github.com/libfuse/sshfs) - Filesystem client based on the *SSH* File Transfer Protocol.
- [ngrok](https://github.com/inconshreveable/ngrok) [](https://github.com/inconshreveable/ngrok) - Introspected tunnels to localhost.
- [localtunnel](https://github.com/progrium/localtunnel) [](https://github.com/progrium/localtunnel) - Expose localhost servers to the Internet.
- [sshuttle](https://github.com/sshuttle/sshuttle) [](https://github.com/sshuttle/sshuttle) - Transparent proxy server that works as a poor man's *VPN*. Forwards over `ssh`. Doesn't require admin. Works with *Linux* and *MacOS*. Supports *DNS tunneling*.
- [sshttp](https://github.com/stealth/sshttp) [](https://github.com/stealth/sshttp) - *SSH*/*HTTP(S)* multiplexer. Run a webserver and a `sshd` on the same port w/o changes.
- [switcher](https://github.com/jamescun/switcher) [](https://github.com/jamescun/switcher) - Run *SSH* and *HTTP(S)* on the same port.
- [sslh](https://github.com/yrutschle/sslh) [](https://github.com/yrutschle/sslh) - Applicative Protocol Multiplexer (i.e: *SSH* + *HTTPS*).
- [tund](https://github.com/aphyr/tund) [](https://github.com/aphyr/tund) - *SSH* reverse tunnel daemon.
- [autossh](http://www.harding.motd.ca/autossh/) - Automatically respawn *SSH* session after network interruption.
- [wssh](https://github.com/aluzzardi/wssh) [](https://github.com/aluzzardi/wssh) - *SSH* to WebSockets Bridge.
- [docker-volume-sshfs](https://github.com/vieux/docker-volume-sshfs) [](https://github.com/vieux/docker-volume-sshfs) - `sshfs` docker volume plugin.
- [quicssh](https://github.com/moul/quicssh) [](https://github.com/moul/quicssh) - QUIC proxy for SSH
- [sshpiper](https://github.com/tg123/sshpiper) [](https://github.com/tg123/sshpiper) - The missing reverse proxy for ssh scp.
- [sshhub](https://sshhub.de) - Web Service: access your SSH servers behind firewalls (ssh-teamviewer).

### Multiplexers

- [tmux](https://tmux.github.io) - Terminal multiplexer.
- [clusterssh](https://github.com/duncs/clusterssh) [](https://github.com/duncs/clusterssh) - Cluster admin via *SSH*.
- [tmux-cssh](https://github.com/dennishafemann/tmux-cssh) [](https://github.com/dennishafemann/tmux-cssh) - `tmux` with a *ClusterSSH*-like behavior.
- [tm](https://github.com/Ganneff/tm) [](https://github.com/Ganneff/tm) - `tmux` manager / helper.
- [i2cssh](https://github.com/wouterdebie/i2cssh) [](https://github.com/wouterdebie/i2cssh) - `csshX` like *SSH* tool for *iTerm2*.
- [ClusterSSH](http://sourceforge.net/projects/clusterssh/) - Controls a number of `xterm` windows via a single graphical console.

### *SSH* keys / Authentication

- [authy-ssh](https://github.com/authy/authy-ssh) [](https://github.com/authy/authy-ssh) - Easy *two-factor* authentication for *SSH* servers.
- [github-auth](https://github.com/chrishunt/github-auth) [](https://github.com/chrishunt/github-auth) - *SSH* key management for GitHub users.
- [cipherhub](https://github.com/substack/cipherhub) [](https://github.com/substack/cipherhub) - Encrypt messages based on *SSH* public keys with easy import from GitHub.
- [Slack notifications](http://www.ryanbrink.com/slack-ssh-session-notifications/) ([archived version](https://web.archive.org/web/20160505202303/http://www.ryanbrink.com/slack-ssh-session-notifications/)) - Guide to setup Slack notifications (can be modified for other services).
- [totp-ssh-fluxer](https://github.com/benjojo/totp-ssh-fluxer) [](https://github.com/benjojo/totp-ssh-fluxer) - A way to make sure your `sshd` port changes every 30 seconds.
- [github-keygen](https://github.com/dolmen/github-keygen) [](https://github.com/dolmen/github-keygen) - Easy creation of secure *SSH* configuration for your GitHub account(s).
- [kr](https://github.com/KryptCo/kr) [](https://github.com/KryptCo/kr) - Kr agent that route access request to the paired mobile phone where Kryptonite is installed.
- [ServerAuth](https://serverauth.com) - Automatically sync SSH access across servers
- [HIBA](https://github.com/google/hiba) [](https://github.com/google/hiba) - Central management of access to a fleet of machines without pushing authorized_users files.

### *SSH* agent

- [ssh-ident](https://github.com/ccontavalli/ssh-ident) [](https://github.com/ccontavalli/ssh-ident) - Different agents and different keys for different projects, with `ssh`.
- [oh-my-zsh/plugins/ssh-agent](https://github.com/robbyrussell/oh-my-zsh) [](https://github.com/robbyrussell/oh-my-zsh) - `ssh-agent` plugin for `zsh`.
- [sshecret](https://github.com/thcipriani/sshecret) - Automatically create and manage multiple agents for multiple keys.

### Tools

- [xxh](https://github.com/xxh/xxh) [](https://github.com/xxh/xxh) - Bring your favorite shell wherever you go through the ssh.
- [sshrc](https://github.com/danrabinowitz/sshrc) [](https://github.com/danrabinowitz/sshrc) - Bring your `.bashrc`, `.vimrc`, etc. with you when you `ssh`.
- [kyrat](https://github.com/fsquillace/kyrat) [](https://github.com/fsquillace/kyrat) - SSH wrapper script that brings your dotfiles always with you on Linux and OSX.
- [ssh-vault](https://github.com/ssh-vault/ssh-vault) [](https://github.com/ssh-vault/ssh-vault) - encrypt/decrypt files using ssh keys
- [ssh-ping](https://github.com/vaporup/ssh-tools) [](https://github.com/vaporup/ssh-tools) - check if host is reachable using ssh_config
- [SSHPry v2](https://github.com/nopernik/SSHPry2.0) [](https://github.com/nopernik/SSHPry2.0) - Spy & Control os SSH Connected client's TTY
- [redial](https://github.com/taypo/redial) [](https://github.com/taypo/redial) - Terminal Based SSH Session Manager for Unix Systems

### Automation

- [Ansible](https://github.com/ansible/ansible) [](https://github.com/ansible/ansible) - App deployment, configuration management and orchestration over *SSH*.
- [rtop](https://github.com/rapidloop/rtop) [](https://github.com/rapidloop/rtop) - Interactive, remote system monitoring tool based on *SSH*.
- [DSH - Dancer's shell / distributed shell](https://www.netfort.gr.jp/~dancer/software/dsh.html.en) - Wrapper for executing multiple remote shell commands from one command line.
- [parallel-ssh](https://github.com/ParallelSSH/parallel-ssh) [](https://github.com/ParallelSSH/parallel-ssh) - Provides parallel versions of OpenSSH and related tools.
- [SSH Power Tool](https://code.google.com/p/sshpt/) - Execute commands and upload files to many servers simultaneously without using pre-shared keys.

### Web

- [Secure Shell chrome extension](https://chrome.google.com/webstore/detail/secure-shell/pnhechapfaindjhompbnflcldabbghjo?hl=en)
- [GateOne](https://github.com/liftoff/GateOne) [](https://github.com/liftoff/GateOne) - HTML5-powered terminal emulator and *SSH* client.
- [KeyBox](https://github.com/skavanagh/KeyBox) [](https://github.com/skavanagh/KeyBox) - Web-based *SSH* console that centrally manages administrative access to systems.
- [Apache Guacamole](https://guacamole.incubator.apache.org/) - Apache Guacamole is a HTML5 based clientless remote desktop gateway. It supports standard protocols like VNC, RDP, and SSH.
- [SSHmon](https://github.com/hpello/sshmon) [](https://github.com/hpello/sshmon) - Real-time GUI to monitor SSH connections and establish port forwardings.

### Testing / Honeypots

- [ssh-hammer](https://github.com/shazow/ssh-hammer) [](https://github.com/shazow/ssh-hammer) - *SSH* load testing tool.
- [kippo](https://github.com/desaster/kippo) [](https://github.com/desaster/kippo) - *SSH* Honeypot.
- [cowrie](https://github.com/micheloosterhof/cowrie) [](https://github.com/micheloosterhof/cowrie) - *SSH* Honeypot (based on kippo).
- [sshmitm](http://linux.die.net/man/8/sshmitm) - *SSH* monkey-in-the-middle.
- [ssh-audit](https://github.com/arthepsy/ssh-audit) [](https://github.com/arthepsy/ssh-audit) - A tool for *SSH* server auditing.
- [sshesame](https://github.com/jaksi/sshesame) [](https://github.com/jaksi/sshesame) - A fake SSH server that lets everyone in and logs their activity.

### Alternatives to *SSH*

- [GoTTY](https://github.com/yudai/gotty) [](https://github.com/yudai/gotty) - Share your terminal as web application.
- [telnet](http://www.telnet.org/htm/faq.htm) - An unencrypted network protocol and an application used to connect to remote computers and issue commands.
- [ttyd](https://github.com/tsl0922/ttyd) [](https://github.com/tsl0922/ttyd) - Share your terminal over the web.
- [rsh](https://en.wikipedia.org/wiki/Remote_Shell) - An unencrypted network protocol and application used to connect to remote computers and issue commands.

## Libraries

    - [libssh](https://www.libssh.org) - The *SSH* library.
    - [crypto/ssh](https://godoc.org/golang.org/x/crypto/ssh) - Built-in *SSH* client and server library.
    - [sftp](https://github.com/pkg/sftp) [](https://github.com/pkg/sftp) - *SFTP* support for the go.crypto/ssh package.
    - [go-sshkit](https://github.com/shazow/go-sshkit) [](https://github.com/shazow/go-sshkit) - Toolkit for building *SSH* servers and clients in Go.
    - [Socker](https://github.com/cosiner/socker) [](https://github.com/cosiner/socker) - Library for Go to simplify the use of *SSH*.
    - [go-sshkeys](https://github.com/moul/go-sshkeys) - Golang SSH Keys manipulation library
    - [jsch](http://www.jcraft.com/jsch/) - Pure *java*, *BSD* licensed, *SSH2* client library.
    - [ssh2](https://github.com/mscdex/ssh2) [](https://github.com/mscdex/ssh2) - *SSH2* client and server modules written in pure *JavaScript* for *node.js*.
    - [paramiko](https://github.com/paramiko/paramiko) [](https://github.com/paramiko/paramiko) - Native *Python* *SSHv2* protocol library.
    - [net-ssh](https://github.com/net-ssh/net-ssh) [](https://github.com/net-ssh/net-ssh) - Pure *Ruby* implementation of an *SSH* (protocol 2) client.

## Resources

### Tutorials

- [How to use *SSH* to Connect to a Remote Server](https://www.digitalocean.com/community/tutorials/how-to-use-ssh-to-connect-to-a-remote-server-in-ubuntu)
- [Best practices](https://blog.0xbadc0de.be/archives/300)
- [Granting Temporary Access to Your Servers (Using Signed *SSH* Keys)](http://linux-audit.com/granting-temporary-access-to-servers-using-signed-ssh-keys/)
- [How to SSH login without a password](https://www.rosehosting.com/blog/ssh-login-without-password-using-ssh-keys/)
- [Gist: SSH Recipes](https://gist.github.com/mjalajel/beaa91a5f8d04ebb464c2c28da01406a) - Collection of recipes for writing awesome ssh config files.

### Security

- [01/14/2016](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2016-0777) - Integer Overflow `CVE 2016 077[7-8]`.
- [Security/Guidelines/OpenSSH - MozillaWiki](https://wiki.mozilla.org/Security/Guidelines/OpenSSH) - `sshd\_config` for `6.7+`, `5.3`.
- [Applied-Crypto-Hardening](https://github.com/BetterCrypto/Applied-Crypto-Hardening) [](https://github.com/BetterCrypto/Applied-Crypto-Hardening) - `sshd\_config` for `6.X`

### Documentation

- [man page](http://linux.die.net/man/1/ssh)
- [Specifications (OpenSSH)](http://www.openssh.com/specs.html)
- [Wikipedia article](https://en.wikipedia.org/wiki/Secure_Shell)

### Community

- [StackOverflow](http://stackoverflow.com/questions/tagged/ssh)
- [ServerFault](http://serverfault.com/questions/tagged/ssh)

<!-- kb-related:start -->

## Related lists

More lists in the **Development Environment** category of the [KEEBOX Library](index.md):

- [Terminals Are Sexy](terminals-are-sexy.md)
- [WezTerm](wezterm.md)
- [Fish](fish.md)
- [Git Hooks](git-hooks.md)
- [GitHub Actions](github-actions.md)
- [Hyper](hyper.md)
- [Pinned Gists](pinned-gists.md)
- [Shell](shell.md)

<!-- kb-related:end -->
