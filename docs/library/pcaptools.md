---
title: "PCAPTools – Awesome List with 10 resources"
description: "10 curated PCAPTools resources: Curated PCAPTools resources."
---

# PCAPTools

Curated PCAPTools resources.

!!! info "Source"
    10 resources imported from [caesar0301/awesome-pcaptools](https://github.com/caesar0301/awesome-pcaptools), dedicated to the public domain ([CC0 / Unlicense](https://creativecommons.org/publicdomain/zero/1.0/)). Thanks to its maintainers and contributors. Part of the [KEEBOX Library](index.md) · Category: **Networking**.

<!-- kb-about:start -->

## About this list

**PCAPTools**. This page brings together 0 links about PCAPTools, grouped into 0 sections. It belongs to the **Networking** category of the KEEBOX Library; see the related lists at the end of the page for neighbouring topics.

<!-- kb-about:end -->

### Capture tools

- [usbmon](https://www.kernel.org/doc/Documentation/usb/usbmon.txt) - a subsystem of Linux kernel to capture usb packets.
- [USBPcap](https://github.com/desowin/usbpcap) - a solution for Windows.

### Analysis

- [USBPcapOdinDumper](https://github.com/KOLANICH/USBPcapOdinDumper) - transforms .pcap files with `usbmon` and `USBPcap` frames format of captures from flashing an Android phone with Odin or [Heimdall](https://gitlab.com/BenjaminDobell/Heimdall) into a set of files with frames payload. Useful for reverse-engineering. Has a modular architecture easily transformable for other applications formats.
- [BPF for Ultrix](https://www.tcpdump.org/other/bpfext42.tar.Z): A distribution of BPF for Ultrix 4.2, with both source code and binary modules.
- [BPF+](https://andrewbegel.com/papers/bpf.pdf): Exploiting Global Data-flow Optimization in a Generalized Packet Filter Architecture By Andrew Begel, Steven McCanne, and Susan Graham.
- [FFT-FGN-C](https://github.com/caesar0301/awesome-pcaptools/blob/HEAD/ftp://ita.ee.lbl.gov/html/contrib/fft_fgn_c.html): is a program for synthesizing a type of self-similar process known as fractional Gaussian noise. The program is fast but approximate. Fractional Gaussian noise is only one type of self-similar process. When using this program for synthesizing network traffic, you must keep in mind that it may be that the traffic you seek is better modeled using one of the other processes.
- [Haka](http://www.haka-security.org/): An open source security oriented language which allows to describe protocols and apply security policies on (live) captured traffic. The scope of Haka language is twofold. First of all, it allows to write security rules in order to filter/alter/drop unwanted packets and log and report malicious activities. Second, Haka features a grammar enabling to specify network protocols and their underlying state machine.
- [RIPE-NCC Hadoop for PCAP](https://github.com/RIPE-NCC/hadoop-pcap): A Hadoop library to read packet capture (PCAP) files. Bundles the code used to read PCAPs. Can be used within MapReduce jobs to natively read PCAP files. Also features a Hive Serializer/Deserializer (SerDe) to query PCAPs using SQL like commands.
- [Traffic Data Repository at the WIDE Project](https://www2.sonycsl.co.jp/person/kjc/papers/freenix2000/): It becomes increasingly important for both network researchers and operators to know the trend of network traffic and to find anomaly in their network traffic. This paper describes an on-going effort within the WIDE project to collect a set of free tools to build a traffic data repository containing detailed information of our backbone traffic. Traffic traces are collected by tcpdump and, after removing privacy information, the traces are made open to the public. We review the issues on user privacy, and then, the tools used to build the WIDE traffic repository. We will report the current status and findings in the early stage of our IPv6 deployment.
- [Usenix93 Paper on BPF](https://www.tcpdump.org/papers/bpf-usenix93.pdf): The libpcap interface supports a filtering mechanism based on the architecture in the BSD packet filter. BPF is described in the 1993 Winter Usenix paper "The BSD Packet Filter: A New Architecture for User-level Packet Capture".

<!-- kb-related:start -->

## Related lists

More lists in the **Networking** category of the [KEEBOX Library](index.md):

- [Real-Time Communications](real-time-communications.md)
- [SNMP](snmp.md)
- [Cilium](cilium.md)

<!-- kb-related:end -->
