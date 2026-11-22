---
title: "Audio Over IP – Awesome List with 28 resources"
description: "28 curated Audio Over IP resources: Reliably transmit uncompressed, low-latency audio over an IP (layer 3) network."
---

# Audio Over IP

Reliably transmit uncompressed, low-latency audio over an IP (layer 3) network.

!!! info "Source"
    28 resources imported from [Mo-way/awesome-aoip](https://github.com/Mo-way/awesome-aoip), dedicated to the public domain ([CC0 / Unlicense](https://creativecommons.org/publicdomain/zero/1.0/)). Thanks to its maintainers and contributors. Part of the [KEEBOX Library](index.md) · Category: **Media**.
## Tools

- [Network Audio Controller](https://github.com/chris-ritsen/network-audio-controller) - Reverse engineered Dante Controller. Supports Web GUI and command line.
- [Pipewire AES67](https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/AES67) - Show AES67 streams as native audio devices on Linux.
- [Merging ALSA RAVENNA/AES67 Driver](https://bitbucket.org/MergingTechnologies/ravenna-alsa-lkm/src/master/) - Open source driver that doesn't accept contributions.
- [AES67 Linux Daemon](https://github.com/bondagit/aes67-linux-daemon) - Fork of Merging's driver with an open source web server.
- [AES67 Monitor](https://github.com/philhartung/aes67-monitor) - Cross platform AES67 monitoring app.
- [JackTrip](https://jacktrip.github.io/jacktrip/) - An open source tool for transmitting real-time audio over LAN and WAN.
- [LinuxPTP](https://linuxptp.sourceforge.net/) - PTP IEEE 1588 for Linux. Provides various tools, e.g. `ptp4l` and `phc2sys`.
- [PAM](https://github.com/martim01/pam) - FOSS AES67 capable audio monitor.
- [Snapcast](https://github.com/badaix/snapcast/tree/develop) - FOSS project for a Sonos-like multiroom solution, using a custom TCP-based protocol.
- [Ravennakit SDK](https://github.com/soundondigital/ravennakit) - Provides a cross-platform C++ SDK for professional networked audio using AES67, RAVENNA, and ST2110-30.
- [Inferno](https://gitlab.com/lumifaza/inferno) - Open source implementation of Dante AoIP in Rust ([GitHub mirror](https://github.com/teodly/inferno/)).
- [ROC-streaming](https://roc-streaming.org/) - A tool for streaming audio over IP networks using UDP or RTP, specialized for real-time streaming. You write the stream to one end and read it from another end. Roc handles all the complexities.

### Closed Source

- [Aneman](https://www.merging.com/aneman/) - **A**udio **NE**twork **MAN**ager, the Ravenna equivalent for Dante controller.
- [PTP Track Hound](https://www.ptptrackhound.com/) - PTP network traffic analysis tool (cross-platform, basic free version available).

## Organizations

- [IPMX](https://ipmx.io/about/) - A proposed set of open standards and specifications for control, copy protection, connection management and security.
- [Audinate](https://audinate.com) - Its proprietary Dante technology is the most popular AoIP solution by far.
- [Ravenna](https://www.ravenna-network.com/) - Second most popular AoIP solution, which is more open than Dante.

## Education

- [Networked Audio Products](https://rhconsulting.uk/blog/) - A census of AoIP products, conducted every year (current: [2025](https://rhconsulting.uk/blog/networked-audio-products-2025/)).
- [Dante Certification](https://www.getdante.com/resources/training/dante-certification-program/) - Understanding Dante helps to understand AoIP. The training requires an account. I recommend lv 1 and lv 2.
- [Ravenna Resources](https://www.ravenna-network.com/resources/) - Webinars and slides by Andreas Hildebrand about Ravenna, AES67, SMPTE 2110, PTP and IPMX.
- [Connecting Dante with AES67](https://download.yamaha.com/files/tcm:39-868466/) - Setting up AES67 to and from a Dante devices. This guide by Yamaha contains intricacies missing in Audinate docs.

## Standards

- [AES67](https://www.aes.org/publications/standards/search.cfm?docID=96), public [draft](https://aes2.org/standards-blog/call-for-comment-on-draft-revised-aes67-xxxx-high-performance-streaming-audio-over-ip-interoperability/) - The open standard for Audio over IP.
- [NMOS](https://github.com/AMWA-TV/nmos) - REST APIs for controlling network media devices.
- [SMPTE ST 2110-30](https://www.smpte.org/standards/st2110), public [version](https://pub.smpte.org/latest/st2110-30/st2110-30-2017.pdf) - AES67 based audio transport in a video stream. Adds some contains to AES67.

## Security

- [IPMX PEP Draft](https://web.archive.org/web/20250402090003/https://static.vsf.tv/download/technical_recommendations/VSF_TR-10-13_2024-01-19.pdf) - The VSF used to host a draft on IPMX encryption (linked the archived copy).
- [Dante Encryption](https://www.getdante.com/products/network-management/dante-media-encryption/) - Dante encrypts media streams, but requires a cloud connection for encrypted control traffic.
- [Vulnerability assessment of the Dante Protocol](https://ritcsec.wordpress.com/2020/04/28/reverse-engineering-and-vulnerability-assessment-of-the-dante-protocol/) - This article looks at the low-level implementation of Dante protocol.
- [Secuirty analysis of PTP paper](https://web.archive.org/web/20250823221404/http://lersse-dl.ece.ubc.ca/record/123/files/123.pdf) - A paper from 2025 explaining which attack vectors on PTP exist in theory.
