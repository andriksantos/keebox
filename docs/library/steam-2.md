---
title: "Steam – Awesome List with 93 resources"
description: "93 curated Steam resources: Digital distribution platform."
---

# Steam

Digital distribution platform.

!!! info "Source"
    93 resources imported from [scholtzm/awesome-steam](https://github.com/scholtzm/awesome-steam), dedicated to the public domain ([CC0 / Unlicense](https://creativecommons.org/publicdomain/zero/1.0/)). Thanks to its maintainers and contributors. Part of the [KEEBOX Library](index.md) · Category: **Miscellaneous**.

<!-- kb-about:start -->

## About this list

Steam is Valve's game distribution platform and also an ecosystem with public APIs, Steamworks for developers, workshop content and a large modding and tools community.

This list focuses on packages and resources for developers: libraries to query the Steam Web API, integrate Steamworks features, read game data and build bots or companion tools. Check each package's maintenance status, since Steam's APIs change over time.

### What you'll find

- **Packages** — 68 links
- **Resources** — 25 links

<!-- kb-about:end -->

## Packages

### Node.js

#### General

- [steam](https://github.com/seishun/node-steam) - Interface directly with Steam servers from Node.js.
- [steam-client](https://github.com/DoctorMcKay/node-steam-client) - API-compatible fork of node-steam's SteamClient.
- [steam-user](https://github.com/DoctorMcKay/node-steam-user) - Feature-rich easy-to-use Steam client.
- [vapor](https://github.com/scholtzm/vapor) - Lightweight Steam client framework.
- [steam-parentbot](https://github.com/dragonbanshee/node-steam-parentbot) - Simple base class for a Steam bot.
- [steamworks-ffi-node](https://github.com/ArtyProf/steamworks-ffi-node) - A Node.js wrapper for Steamworks SDK.

#### WebAPI

- [steam-webapi](https://github.com/DoctorMcKay/node-steam-webapi) - Complete WebAPI wrapper with support for extra HTTP headers sent by Steam.
- [steamapi](https://github.com/lloti/node-steamapi) - A nice Steam API wrapper.

#### Trading

- [steam-trade](https://github.com/seishun/node-steam-trade) - Node.js wrapper around Steam live trading.
- [steam-tradeoffers](https://github.com/Alex7Kom/node-steam-tradeoffers) - Steam Trade Offers for Node.js.
- [steam-tradeoffer-manager](https://github.com/DoctorMcKay/node-steam-tradeoffer-manager) - Simple and sane Steam trade offer management.
- [steam-inventory-stream](https://github.com/timvandam/steam-inventory-stream) - Fetch inventories as readable streams.
- [steam-inventory-api-ng](https://github.com/itsjfx/node-steam-inventory-api-ng) - A Steam Inventory API wrapper with advanced features such as retries and proxy support.

#### Game Interaction

- [steam-gameserver](https://github.com/DoctorMcKay/node-steam-gameserver) - Steam client handler for Gameserver and AnonGameserver account types.
- [tf2](https://github.com/DoctorMcKay/node-tf2) - Interact directly with TF2 game coordinator.
- [csgo](https://github.com/joshuaferrara/node-csgo) - Interact directly with CS:GO game coordinator.
- [dota2](https://github.com/RJacksonm1/node-dota2) - Interact directly with Dota 2 game coordinator.

#### Community & Store Automation

- [steamcommunity](https://github.com/DoctorMcKay/node-steamcommunity) - Interact with steamcommunity.com. Also allows to confirm trade offers.
- [steamstore](https://github.com/DoctorMcKay/node-steamstore) - Interact with store.steampowered.com.
- [steam-weblogon](https://github.com/Alex7Kom/node-steam-weblogon) - Retrieve SteamCommunity cookies if you are running Steam network client.
- [steam-web-api-key](https://github.com/Alex7Kom/node-steam-web-api-key) - Automatically registers and retrieves Steam API key.
- [steam-parental](https://github.com/Alex7Kom/node-steam-parental) - Disable parental lock.

#### Authentication

- [steam-login](https://github.com/cpancake/steam-login) - Simple Connect / Express Steam authentication library.
- [passport-steam](https://github.com/liamcurry/passport-steam) - Steam (OpenID) authentication strategy for Passport and Node.js.
- [meteor-accounts-steam](https://github.com/scholtzm/meteor-accounts-steam) - Steam OpenID integration for Meteor Accounts.

#### Misc

- [steam-resources](https://github.com/seishun/node-steam-resources) - Steam's enums, protobufs and structs.
- [steam-crypto](https://github.com/seishun/node-steam-crypto) - Node.js implementation of Steam crypto.
- [steam-groups](https://github.com/scholtzm/node-steam-groups) - Custom node-steam handler which provides group functions.
- [steamid](https://github.com/DoctorMcKay/node-steamid) - SteamID usage and conversion made easy.
- [steam-totp](https://github.com/DoctorMcKay/node-steam-totp) - Easily generate 2FA codes used by Steam.
- [steam-chat-bot](https://github.com/Steam-Chat-Bot/node-steam-chat-bot) - Simplified interface for a steam chat bot.
- [vdf](https://github.com/RJacksonm1/node-vdf) - vdf to object and vice versa.
- [steamrep](https://github.com/scholtzm/node-steamrep) - Check user's SteamRep reputation.
- [reptf](https://github.com/scholtzm/node-reptf) - Check user's rep.tf reputation.
- [steamapis](https://github.com/itsjfx/node-steamapis) - Module to use the API of [steamapis.com](https://steamapis.com).

### C&#35;

#### General

- [SteamKit2](https://github.com/SteamRE/SteamKit) - .NET library designed to interoperate with Valve's Steam network.
- [SteamAuth](https://github.com/geel9/SteamAuth) - A C# library that provides vital Steam Mobile Authenticator functionality.
- [SteamBot](https://github.com/Jessecar96/SteamBot) - Automated bot software for interacting with steam trade.
- [SteamTradeOffersBot](https://github.com/waylaidwanderer/SteamTradeOffersBot) - SteamBot fork which focuses on trade offers.
- [SteamStandardProject](https://github.com/ObsidianMinor/SteamStandardProject) - A collection of .NET Standard libraries using common types that provide functionality in one or more parts of Steam.

#### Misc

- [BackpackLogin](https://github.com/igeligel/BackpackLogin) - A .NET Standard library for logging into backpack.tf using Steam credentials.
- [TeamFortressOutpostApi](https://github.com/igeligel/TeamFortressOutpostApi) - A .NET Standard class library which allows user to interact with TF2Outpost.

### PHP

- [SteamCommunity](https://github.com/waylaidwanderer/PHP-SteamCommunity) - A PHP library for interacting with the Steam Community website.
- [SteamAuthentication](https://github.com/SmItH197/SteamAuthentication) - Steam OpenID authentication with PHP.
- [SteamAuthOOP](https://github.com/BlackCetha/SteamAuthOOP) - An object-oriented alternative to SteamAuthentication.
- [steam-api](https://github.com/DaMitchell/steam-api-php) - A PHP wrapper for the Steam API.
- [steamid](https://github.com/DoctorMcKay/php-steamid) - SteamID class for PHP.
- [steam-totp](https://github.com/DoctorMcKay/php-steam-totp) - PHP library to deal with Steam's proprietary TOTP algorithm.
- [steam-auth](https://github.com/vikas5914/steam-auth) - An alternative Steam authentication library with Composer support.

### Go

- [steam](https://github.com/0xAozora/steam) - Simple steam library for trading in Go.
- [go-steam](https://github.com/Philipp15b/go-steam) - Steam's protocol in Go.
- [steam-mobileauth](https://github.com/YellowOrWhite/go-steam-mobileauth) - Port of SteamAuth in Go.

### Python

#### General

- [steam](https://github.com/ValvePython/steam) - Module for various interactions with Steam.
- [steamodd](https://github.com/Lagg/steamodd) - Steam tools library.
- [steampy](https://github.com/bukson/steampy) - Fully automated Steam trade offers library with SteamGuard support.
- [SteamAPI](https://github.com/smiley/steamapi) - An object-oriented Python 2.7+ library for accessing the Steam Web API.
- [Steam-Trade](https://github.com/Zwork101/steam-trade) - An asynchronous, event-based trade library.
- [aiosteampy](https://github.com/somespecialone/aiosteampy) - Trade and interact with Steam market, WebAPI, SteamGuard.

#### Game Interaction

- [csgo](https://github.com/ValvePython/csgo) - Python module for interacting with CSGO's Game Coordinator.
- [dota2](https://github.com/ValvePython/dota2) - Python module for interacting with Dota 2's Game Coordinator.

#### Misc

- [vpk](https://github.com/ValvePython/vpk) - Python module for working with Valve's Pack format.
- [vdf](https://github.com/ValvePython/vdf) - Python module for working with Valve's KeyValue format.

### C++

- [SteamPP](https://github.com/seishun/SteamPP) - C++ library to interoperate with Steam servers.

### Java

- [SteamKit-Java](https://github.com/Top-Cat/SteamKit-Java) - Java port of SteamKit.
- [JavaSteam](https://github.com/Longi94/JavaSteam) - Java library that provides an interface to directly interact with Valve's Steam servers.

### Objective-C

- [SteamAuth](https://github.com/michaelchum/SteamAuth) - An iOS wrapper around Steam's OpenID login.

### Ruby

- [steam-trade](https://github.com/OmG3r/steam-trade) - Ruby gem for sending trade offers.

### Rust

- [steamguard-cli](https://github.com/dyc3/steamguard-cli) - Command-line utility for generating Steam 2FA codes and managing Steam confirmations.

## Resources

### General

- [Steam WebAPI @ ValveSoftware](https://developer.valvesoftware.com/wiki/Steam_Web_API)
- [Steam WebAPI @ TF2 Wiki](https://wiki.teamfortress.com/wiki/WebAPI)
- [Steam WebAPI Documentation by xPaw](https://lab.xpaw.me/steam_api_documentation.html)
- [Steam Internal WebAPI Documentation by Revadike](https://github.com/Revadike/UnofficialSteamWebAPI)
- [Steam as OpenID Provider](http://steamcommunity.com/dev)
- [Steam API Key Registration](http://steamcommunity.com/dev/apikey)
- [Steam Error Codes](https://steamerrors.com/) - List of `EResult` codes with possible explanations.

### Tutorials

- [Creating a Steam Trade Bot with Node.js](https://firepowered.org/developer/create-a-steam-trade-bot-with-nodejs-iojs-updated-for-node-steam-v1-0/)
- [Charred's node.js Guide to Steam Bots](https://github.com/charredgrass/nodejs-bot-guide)
- [In-depth Steam Bot Guide with Node.js](https://github.com/andrewda/node-steam-guide)
- [Retrieving 2FA Keys from iOS Device](http://forums.backpack.tf/index.php?/topic/45995-guide-how-to-get-your-shared-secret-from-ios-device-steam-mobile/)

### Posts

- [Item IDs Explained](https://dev.doctormckay.com/topic/332-identifying-steam-items/)
- [Everything Related to Escrow](https://www.reddit.com/r/SteamBot/comments/3udhkd/everything_related_to_escrow/)
- [Understanding Avatar Hash](https://www.reddit.com/r/SteamBot/comments/3cv6k7/problem_downloading_an_avatar_using/)

### Standalone Tools

- [NetHook2](https://github.com/SteamRE/SteamKit/tree/master/Resources/NetHook2) - Intercept Steam client's network messages.
- [NetHook2 Analyzer](https://github.com/SteamRE/SteamKit/tree/master/Resources/NetHookAnalyzer2) - Inspect messages dumped by NetHook2.
- [steam-auth-web-util](http://scholtzm.github.io/steam-auth-web-util/) - Generate 2FA codes directly in your web browser.
- [SteamDesktopAuthenticator](https://github.com/Jessecar96/SteamDesktopAuthenticator) - Desktop implementation of Steam's mobile authenticator app.
- [protonenv](https://github.com/rizkiarm/protonenv) - Simple Proton version and prefix management.
- [steam-desktop-authenticator-multiplatform](https://github.com/tre3p/steam-desktop-authenticator-multiplatform) - Steam desktop authenticator.

### Discussion Boards

- [/r/SteamBot](https://www.reddit.com/r/SteamBot)
- [/r/SteamBot Discord](https://discord.gg/0i5X3oDHJbDUsiGC)
- [/r/nodesteam](https://www.reddit.com/r/nodesteam)
- [DoctorMcKay's Dev Forum](https://dev.doctormckay.com/)
- [node-steam-forum](https://github.com/steam-forward/node-steam-forum)

<!-- kb-related:start -->

## Related lists

More lists in the **Miscellaneous** category of the [KEEBOX Library](index.md):

- [Steam Deck](steam-deck.md)
- [Tech Ethics](tech-ethics.md)
- [Theravada](theravada.md)
- [Transit](transit.md)
- [Site Reliability Engineering](site-reliability-engineering.md)
- [Software Architecture](software-architecture.md)
- [Stacks](stacks-2.md)
- [Standards](standards.md)

<!-- kb-related:end -->
