---
title: "ADS-B – Awesome List with 55 resources"
description: "55 curated ADS-B resources: Technology broadcasting aircraft's identity, position, and data periodically."
---

# ADS-B

Technology broadcasting aircraft's identity, position, and data periodically.

!!! info "Source"
    55 resources imported from [rickstaa/awesome-adsb](https://github.com/rickstaa/awesome-adsb), dedicated to the public domain ([CC0 / Unlicense](https://creativecommons.org/publicdomain/zero/1.0/)). Thanks to its maintainers and contributors. Part of the [KEEBOX Library](index.md) · Category: **Hardware**.
## Docs and Quickstarts

- [ADS-B Docker guide](https://sdr-enthusiasts.gitbook.io/ads-b/) - Everything you want to know about ADS-B reception, decoding and sharing.
- [ADS-B equipment guide](https://sdr-enthusiasts.gitbook.io/ads-b/intro/equipment-needed) - A excellent ADS-B hardware guide written by the community.
- [PiAware ADS-B tutorial](https://flightaware.com/adsb/piaware/build/) - FlightAware's ADS-B setup tutorial.
- [ADSB-B transponders guide](https://www.sportys.com/blog/ads-b-out-questions-1090-978/) - A guide explaining the difference between 978 and 1090 MHz transponders.

## Books and Articles

- [The 1090 Megahertz Riddle - Junzi Sun](https://mode-s.org/decode/index.html) - A Guide to Decoding Mode S and ADS-B Signals.

## ADS-B Aggregators

### Open source orientated

- [airplanes.live](https://airplanes.live) - The mission of Airplanes.Live is to aggregate and provide access to a comprehensive repository of unfiltered aviation data.  Offers map and free API.
- [ADSB One](https://adsb.one) - A one-stop resource for all aero-related information and a community-driven aggregator for aero-feed data legally dedicated to the public interest.
- [adsb.fi](https://adsb.fi) - A community-driven flight tracker with hundreds of feeders worldwide that provides open and unfiltered access to worldwide air traffic data.
- [ADSB.lol](https://adsb.lol) - A completely open-source and community-driven flight tracker that displays and provides [ODbL-licensed](https://opendatacommons.org/licenses/odbl/summary/) data via a [free API](https://api.adsb.lol/) as well as [free historical data](https://github.com/adsblol/globe_history).

### Community driven

- [ADSBHub.org](https://www.adsbhub.org) - A service for real-time ADS-B data sharing and exchange between plane tracking enthusiasts, plane spotters, radio amateurs and professionals interested in developing ADS-B-related software.
- [TheAirTraffic](https://theairtraffic.com) - A community-driven ADS-B aggregator dedicated to keeping the air-tracking data on their site open and unfiltered.
- [PlaneSpotters.net](https://www.planespotters.net) - A civil aviation database and aggregator with a large collection of aircraft photos and information.
- [Plane.watch](https://www.plane.watch) - A community hosted flight tracker.
- [www.live-military-mode-s.eu](https://www.live-military-mode-s.eu) - A community driven flight tracker that is focused at tracking military aircraft.
- [adsb.chaos-consulting.de](https://adsb.chaos-consulting.de) - A non-commercial tracker for flights, ships, and radiosondes managed by enthusiasts. Focuses on the contributions of individual feeding stations.

### Non-profits

- [Opensky Network](https://opensky-network.org) - The OpenSky Network is a non-profit association based in Switzerland that provides open access to flight tracking control data. It was set up as a research project by several universities and government entities to improve the security, reliability and efficiency of the airspace.

### Commercial

- [FlightAware](https://flightaware.com)[^1] - An American multinational technology company that provides real-time, historical, and predictive flight tracking data and products.
- [FlightRadar24](https://www.flightradar24.com)[^1] - A Swedish internet-based service that shows real-time aircraft flight tracking information on a map.
- [RadarBox](https://www.radarbox.com)[^1] - A Tampa-based global flight tracking and data services company that offers worldwide commercial and general aviation flight tracking.
- [ADS-B Exchange](https://www.adsbexchange.com/) - A flight tracking company that offers high fidelity, stable, and secure flight tracking service. It was started by volunteers and flight enthusiasts but was recently acquired by [JETNET](https://www.jetnet.com/).
- [PlaneFinder.net](https://planefinder.net)[^1] - A United Kingdom-based real-time flight tracking service shows global flight data like flight numbers, how fast an aircraft moves, elevation, and travel destination.
- [AvDelphi](https://www.avdelphi.com) - An aviation data and services company that shows airframes, registrations, types, airports and flights, radar and nav points, and owner and flight histories.
- [RadarVirtuel](https://www.radarvirtuel.com) - A flight data collector that offers premium features. Its primary focus is collecting information about traffic around smaller airports worldwide.

### Other

- [Airframes.io](https://app.airframes.io/) - Airframes is an aircraft-related aggregation service that receives ACARS, VDL, HFDL, and SATCOM data from volunteers worldwide. It collaborates closely with ADS-B aggregators and works with ADS-B data internally.
- [gcmb.io](https://gcmb.io/adsb/adsb) - ADS-B data from ABSBHub.org published via the MQTT protocol.

## Software

### General

- [readsb](https://github.com/wiedehopf/readsb) - ADS-B decoder swiss knife.
- [dump1090](https://github.com/MalcolmRobb/dump1090) - A simple Mode S decoder for RTLSDR devices.
- [flightmon](https://github.com/mik3y/flightmon) - Simple command-line "GUI" for showing current dump1090/readsb data.
- [sdr-enthusiasts/plane-alert-db](https://github.com/sdr-enthusiasts/plane-alert-db) - A list of exciting aircraft - Governments, Dictators, Military, Historical and just plain odd.
- [junzis/pyModeS](https://github.com/junzis/pyModeS) - A python decoder for Mode S and ADS-B signals.
- [adsb_actions](https://github.com/eastham/adsb_actions) - Python tool to detect, act on, and visualize ADS-B traffic and events.

### Feeding

- [sdr-enthusiasts/docker-adsb-ultrafeeder](https://github.com/sdr-enthusiasts/docker-adsb-ultrafeeder) - All-in-one ADSB container with readsb, tar1090, graphs1090, autogain, multi-feeder, and mlat-hub built in.
- [adsbfi/adsb-fi-scripts](https://github.com/adsbfi/adsb-fi-scripts) - Easy to use feeder install script for feeding to adsb.fi.
- [adsblol/feed](https://github.com/adsblol/feed) - Easy to use, container-based MLAT/ADS-B/ACARS/VDL2 multi feed client. Powered by [SDR-Enthusiasts](https://github.com/sdr-enthusiasts) images.
- [adsb.im](https://adsb.im/home) - Simple to use ADS-B Feeder Images. Setup a single board computer (such as Raspberry Pi) to receive and share aircraft ADS-B position reports without command line/terminal skills required. Allows sharing data with both open-source and commercial flight tracking websites.

### Visualisation

- [wiedehopf/tar1090](https://github.com/wiedehopf/tar1090) - A great way to view your ADS-B data.
- [amnesica/BelugaProject](https://github.com/amnesica/BelugaProject) - A web application that displays data of one or multiple, local ADS-B feeders and AIS-data along with additional information on a map interface in the browser.
- [Grafana](https://grafana.com/) - Open source analytics and monitoring solution for every database.
- [AndrewCTF/velocity](https://github.com/AndrewCTF/velocity) - A self-hosted flight and ship tracker on a 3D globe that records every position it sees so you can replay any moment, and folds in your own receiver's tar1090 or readsb feed.
- [blindp3w/readsbstats](https://github.com/blindp3w/readsbstats) - Self-hosted flight history and statistics web UI for readsb. Stores positions in SQLite with per-flight track maps, a flagged aircraft gallery, a watchlist, a Telegram bot and receiver metrics.

### Apps

- [d4rken/adsb-meta-tracker](https://github.com/d4rken/adsb-meta-tracker) - An Android ADS-B Meta Tracker that shows metadata about ADS-B aggregators.
- [AirPing](https://airping.app) - An iOS app that turns your tar1090 or readsb instance into a mobile flight tracker.
- [Overhead 1090](https://overhead1090.com) - Native iPhone, iPad and Apple TV client for PiAware/dump1090-compatible receivers with a live radar map, logbook, daily reports and notable-sighting alerts. Local-network only, paid app.

### Social

- [docker-planefence](https://github.com/kx1t/docker-planefence) - A little tool that can be used to log, display and tweet the aircraft that come within range of your receiver (i.e. the fence).
- [Jxck-S/plane-notify](https://github.com/Jxck-S/plane-notify) - Notify if a selected plane has taken off or landed using OpenSky or ADS-B Exchange data.

## ADS-B Derived Data

- [aircraft-flight-schedules](https://github.com/MrAirspace/aircraft-flight-schedules) - Open-source datasets featuring global, high-level flight schedules extracted from worldwide aircraft ADS-B position transmissions (2024+ onwards). Covers all flights globally as long as within coverage of the [ADSBlol](https://adsb.lol/) initiative.

## Hardware

### SBC

- [Raspberry Pi](https://www.raspberrypi.org/) - Small single-board computers developed in the United Kingdom.
- [Orange Pi](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-5.html) - Single-board computers created using OS cost-effective hardware.
- [Banana Pi](https://banana-pi.org/) - Single-bard computers created by a Chinese open-source hardware community.

### Receivers

- [FlightAware ADS-B USB receivers](https://flightaware.store/collections/radio-dongles) - ADS-B USB receivers made by FlightAware.
- [AirNav RadarBox ADS-B USB receivers](https://www.radarbox.com/store) - ADS-B USB receivers made by RadarBox.
- [RTL-SDR DONGLES](https://www.rtl-sdr.com/buy-rtl-sdr-dvb-t-dongles/) - A premium RTL-SDR dongle provider focused on maintaining fair retail pricing.

### Filters

- [FlightAware Signal filters](https://flightaware.store/collections/signal-filters) - Different signal filters made by FlightAware.

### Antennas

- [Vinnant antennas](https://vinnant.sk/) - Specialized premium antennas made in Slovakia.
- [DPD antennas](https://dpdproductions.com/) - High-quality antennas for various radio services produced in the USA.
