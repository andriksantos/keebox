---
title: "Blazor – Awesome List with 375 resources"
description: "375 curated Blazor resources: .NET web framework using C#/Razor and HTML that runs in the browser with WebAssembly."
---

# Blazor

.NET web framework using C#/Razor and HTML that runs in the browser with WebAssembly.

!!! info "Source"
    375 resources imported from [AdrienTorris/awesome-blazor](https://github.com/AdrienTorris/awesome-blazor), dedicated to the public domain ([CC0 / Unlicense](https://creativecommons.org/publicdomain/zero/1.0/)). Thanks to its maintainers and contributors. Part of the [KEEBOX Library](index.md) · Category: **Front-End Development**.
## Introduction

## General

- [ASP.NET Blog's archives](https://devblogs.microsoft.com/aspnet/category/blazor/) - Archives of the ASP.NET blog about Blazor.
- [Blazor](https://dotnet.microsoft.com/apps/aspnet/web-apps/client) - Official website of Blazor, from Microsoft.
- [Blazor courses on Microsoft Learn](https://docs.microsoft.com/learn/browse/?expanded=dotnet%2Cazure%2Csurface&products=dotnet%2Cwindows&roles=developer&terms=blazor) - Blazor courses on Microsoft Learn.
- [Blazor-Dev gallery on .NET Foundation](https://dotnet.myget.org/gallery/blazor-dev) - Daily builds of the 'dev' branch of Blazor.
- [Blazor Extensions](https://github.com/BlazorExtensions) - Curated extensions for Microsoft ASP.Net Core Blazor.
- [Blazor University](http://blazor-university.com/) - Unofficial documentation website.
- [Demo](https://blazor-demo.github.io/) - Official basic demo website.
- [Documentation](https://docs.microsoft.com/aspnet/core/blazor) - Official documentation, by Microsoft.
- [eShopOnBlazor](https://github.com/dotnet/eShop) -   Migration of a traditional ASP.NET Web Forms app to Blazor, sample by Microsoft Architecture.
- [FAQ](https://github.com/aspnet/Blazor/wiki/FAQ) - FAQ.
- [GitHub repository](https://github.com/dotnet/aspnetcore) -   The official Blazor repository (which is the ASP.NET Core repository).
- [Introduction to ASP.NET Core](https://docs.microsoft.com/aspnet/core/) - Introduction to ASP.NET Core.
- [Blazor WebAssembly performance best practices](https://docs.microsoft.com/aspnet/core/blazor/webassembly-performance-best-practices) - ASP.NET Core Blazor WebAssembly performance best practices, by Pranav Krishnamoorthy and Steve Sanderson.
- [themesof.net](https://themesof.net/) - .NET 6 planning process.

## Templates

- [BitPlatform Templates](https://github.com/bitfoundation/bitplatform) -   - Solution templates using .Net MAUI and Blazor with out-of-the-box best practices enabling fast and high-quality cross-platform development for web, android, iOS, and Windows with native beautiful Blazor components. The projects created by these templates contain everything required for developing real-world applications, including (but not limited to) CI/CD pipelines, Infra as Code for Azure, localization, multi-mode development (Blazor Server/WASM/Hybrid), builtin bullet proof exception handling, etc. [Read more](https://bitplatform.dev/).
- [BlazorSwa Template](https://github.com/albx/BlazorSwa.Template) - This is a simple template for the .NET CLI which allows to create a Blazor project ready to be deployed in an Azure Static Web Apps. It allows to create an Azure Function project as backend.
- [Clean Architecture with Blazor Server](https://github.com/neozhu/CleanArchitectureWithBlazorServer)   - Another template with MudBlazor and CleanArchitecture approach.
- [CleanAspire](https://github.com/neozhu/cleanaspire) -   - CleanAspire is a cloud-native template powered by Aspire for cloud environments with scalability and offline support. Using .NET 9 Minimal APIs and Blazor WebAssembly, it provides a lightweight, fast foundation for building Progressive Web Applications (PWA) optimized for the cloud.

## Sample Projects

### AI

- [Cledev.OpenAI](https://github.com/lucabriguglia/Cledev.OpenAI) -   .NET 7 SDK for OpenAI with a Blazor Server playground.
- [ExplainFaceRecognition](https://github.com/georg-jung/explain-face-rec) -  Interactive Face Detection & Recognition tutorial with hands-on code samples. State-of-the-art local face AI showcase. Blazor Server & Hybrid.
- [Caveman](https://github.com/francescopaolopassaro/caveman) -   🦴 A self-contained C# prompt compressor for LLMs (GPT-4, Gemma, Llama, …): strips grammatical "noise" and lemmatizes text for up to 70% token reduction, across 50+ embedded languages, with zero NLP-model runtime dependency. Content-aware routing auto-detects JSON/diffs/logs/code/tables and applies the best compression strategy for each; ships `Light`/`Semantic`/`Aggressive` levels and ready-made compression profiles. [NuGet](https://www.nuget.org/packages/Caveman).
- [Caveman.SemanticKernel](https://github.com/francescopaolopassaro/Caveman.SemanticKernel) -   Optional add-on package exposing Caveman's prompt compression, conversation-fitting/summarization, and project-analysis tools as Microsoft Semantic Kernel plugins (kernel functions ready to register with `Kernel.CreateBuilder()`).
- [Caveman.mcp](https://github.com/francescopaolopassaro/Caveman.mcp) -   An MCP (Model Context Protocol) server exposing Caveman's token compression, language detection, content-aware routing and extractive summarization as tools for AI agents and MCP-compatible editors — integrates directly with Claude Code, Cursor, Windsurf and similar.
- [Caveman.PrivacyGuard](https://github.com/francescopaolopassaro/Caveman.PrivacyGuard) -   🛡️ Enterprise-grade PII/privacy analyzer for AI/LLM pipelines: detects, risk-scores and auto-masks sensitive data across 27 EU countries (heuristic regex + Luhn/IBAN/checksum validators + Shannon-entropy analysis), with GDPR/PCI-DSS/NIST-800-53 compliance mapping and runtime-configurable YAML rules. [NuGet](https://www.nuget.org/packages/Caveman.PrivacyGuard).
- [Signs of AI Writing](https://github.com/peopleworks/SignsofAI) -   Free, privacy-first toolkit for writing integrity. An explainable AI-writing linter that suggests a fix for every flagged tell, plus an originality checker that surfaces shared passages as evidence a human judges. Runs almost entirely in the browser, English and Spanish. Blazor WebAssembly. [Demo](https://peopleworks.github.io/SignsofAI/).

### Authentication

- [BlazorBoilerplate](https://github.com/enkodellc/blazorboilerplate) -   Real World Admin Dashboard / Starter kit with IdentityServer4 Material Design. [Demo](https://blazorboilerplate.com).
- [TheIdServer](https://github.com/Aguafrommars/TheIdServer) -   OpenID/Connect server base on IdentityServer4.
- [BlazorWithIdentity](https://github.com/stavroskasidis/BlazorWithIdentity) -   A sample project showcasing a Blazor app using EF Core with Identity authentication.
- [Blorc.OpenIdConnect](https://github.com/WildGums/Blorc.OpenIdConnect) -   The right way to use OpenID Connect on Blazor.
- [BlazorWasmOidcKeycloak](https://github.com/wildermedeiros/BlazorAppWasmAuth) -  Blazor WebAssembly application using OpenID Connect (OIDC) authentication with Microsoft Identity and Keycloak.
- [CodeBeam.UltimateAuth](https://github.com/CodeBeamOrg/UltimateAuth) -   A modern authentication framework for .NET that unifies sessions, cookies and tokens into a single model, with built-in support for Blazor Server and WebAssembly applications. [Docs](https://ultimateauth.com).

### CMS

- [Blogifier](https://github.com/blogifierdotnet/Blogifier) -    ASP.NET Core Blogging application with Blazor Admin Dashboard. [Demo](http://blogifier.net/blog).
- [eShopOnBlazor](https://github.com/dotnet-architecture/eShopOnBlazor) -   Migration of a traditional ASP.NET Web Forms app to Blazor.
- [FluentCMS](https://github.com/fluentcms/FluentCMS) -   FluentCMS is open source AI Driven ASP.NET Core Blazor Content Management System (CMS) [FluentCMS](https://fluentcms.com/).
- [JHipster.NET](https://github.com/jhipster/jhipster-dotnetcore)   [JHipster](https://www.jhipster.tech/) is a well-known platform for generating modern application in java world. [JHipster](https://www.jhipster.tech/) provides a blueprints system that allows to override the default behavior of the generator. JHipster.NET is a blueprint that overrides the back-end part, originally generated in spring boot, by back-end in asp.net core. For the front-end all the common language can be used (angular, react), including Blazor.
- [Oqtane](https://github.com/oqtane/oqtane.framework) -   Oqtane is a CMS & Application Framework for Blazor & .NET MAUI [Oqtane](https://www.oqtane.org).
- [RapidCMS](https://github.com/ThomasBleijendaal/RapidCMS) -   A code-first, extensible Blazor app that generates a CMS for your own database.
- [ZauberCMS](https://github.com/YodasMyDad/ZauberCMS) -   Fully featured, highly customisable and plugin based Blazor CMS, heavily inspired by Umbraco.

### Editors

- [Stilo](https://github.com/francescopaolopassaro/Stilo) -   A professional suite of pure-C# Blazor libraries, zero native dependencies, working in both Blazor Server and WebAssembly: **Stilo.Editor**, a full Microsoft Word–style WYSIWYG HTML editor (Office-style ribbon, Pages mode with millimeter rulers, offline multilingual spell checking, DOCX/PDF/Markdown import & export, dozens of insertable content types from tables to barcodes/QR); and **Stilo.Reports**, a self-contained RDL/RDLC-compatible report designer & viewer (drag-and-drop designer, Tablix with true Matrix pivot, 10 chart types rendered as SVG, barcode/QR items, PDF export). Individual developers get a free annual license. [Stilo.Editor NuGet](https://www.nuget.org/packages/Stilo.Editor) · [Stilo.Reports NuGet](https://www.nuget.org/packages/Stilo.Reports).

### Games

- [Trains.NET](https://github.com/davidwengier/Trains.NET) -   2D game built with .NET and C# on a [Twitch stream](https://www.twitch.tv/davidwengier). Trains is available to play online at [wengier.com/Trains.NET](https://wengier.com/Trains.NET).
- [AsteroidsWasm](https://github.com/aesalazar/AsteroidsWasm) -   Collection of .NET 8 C# applications consuming a single .NET Standard project running in:  Blazor Client (WebAssembly), Blazor Server, Electron (via Blazor Server), WPF, WinForms, MAUI, WinUI 3. [Demo](https://aesalazar.github.io/AsteroidsWasm/).
- [DiabloBlazor](https://github.com/n-stefan/diabloblazor) -   Blazor port of DiabloWeb, making it a double WebAssembly app: a WebAssembly (C#) PWA hosting a WebAssembly (C++) game. [Demo](https://n-stefan.github.io/diabloblazor).
- [Wolfenstein 3D ported to Blazor](https://github.com/JamesRandall/csharp-wolfenstein) -   Wolfenstein 3D ported to modern C# and Blazor. [Article](https://www.jamesdrandall.com/posts/csharp_blazor_wolfenstein_part_1/).
- [ZXSpectrum](https://github.com/EngstromJimmy/ZXSpectrum) -  ZX Spectrum emulator running on Blazor WebAssembly. [Demo](https://zxspectrum.azurewebsites.net/).
- [WordleBlazor](https://github.com/johnt84/WordleBlazorApp) -  Simple clone of popular Wordle game in Blazor. [Demo](https://wordleblazorapp.azurewebsites.net/).
- [Blazor Puzzle #3 - File not found](https://github.com/BlazorPuzzle/Puzzle-3)
- [TabletopCardEngine demo](https://github.com/DigitalAbsurd/TabletopCardEngine) -   Texas Hold'em played and replayed in Blazor WebAssembly, with a live view of the database rows each action writes. [Demo](https://digitalabsurd.github.io/TabletopCardEngine/).

### Hybrid

- [Photino](https://github.com/tryphotino/photino.NET) -   Build native, cross-platform desktop apps that are lighter than light. Photino is a lightweight open-source framework for building native, cross-platform desktop applications with Web UI technology.
- [Blazor + Umbraco Heartcore](https://github.com/umbraco/Umbraco.Headless.Client.Net/tree/master/samples/Umbraco.Headless.Client.Samples.BlazorServer) -  Example of using [Umbraco Heartcore](https://umbraco.com/products/umbraco-heartcore/) with Blazor.
- [Blazor Wasm with ASP.NET Framework 4.x](https://github.com/elgransan/BlazorWasmWithNetFrameworkMVC) - With some tweaks and limitations you can run Blazor Wasm on Net Framework 4.x or in another environment. [Explanation on Medium](https://medium.com/@santiagoc_33226/using-blazor-wasm-with-net-framework-mvc-or-another-old-external-site-7fc0884fcfca).
- [RemoteBlazorWebView](https://github.com/budcribar/RemoteBlazorWebView) -  RemoteBlazorWebView enables you to interact with the user interface of a program developed with either the BlazorWebView WPF control or WinForms control using a web browser.
- [BlazorInAngularDemo](https://github.com/Xenoage/BlazorInAngularDemo) -  Demonstrates how an existing Angular app can be migrated to Blazor gradually by integrating Blazor components, including calling Angular service methods. [Demo](https://xenoage.github.io/BlazorInAngularDemo/).

### IDE

- [Picat Language IDE](https://github.com/andrzejolszak/picat-blazor-monaco-ide/) -  IDE for the [Picat logic programming language](http://picat-lang.org/) based on the Monaco Editor. [Demo](https://andrzejolszak.github.io/picat-blazor-monaco-ide/PicatBlazorMonaco/publish/wwwroot/).

### IoT

- [PresenceLight](https://github.com/isaacrlevin/PresenceLight) -   PresenceLight is a solution to broadcast your various statuses to a Phillips Hue or LIFX light bulb. Some statuses you can broadcast are: your availability in Microsoft Teams, your current Windows 10 theme, and a theme or color of your choosing. [Blog post](https://www.isaaclevin.com/post/presence-light). [Demo video](https://www.youtube.com/playlist?list=PL_IEvQa-oTVtB3fKUclJNNJ1r-Sxtjc-m).
- [Meadow Weather](https://github.com/bradwellsb/blazor-meadow-weather) -  In this sample, a Meadow microcontroller polls data from a LM35 temperature sensor. That data is sent via HTTP request to an API controller endpoint and stored in a database where it can be visualized in a chart using a Blazor web app.

### Machine Learning

- [Scalable sentiment analysis](https://github.com/dotnet/machinelearning-samples/tree/master/samples/csharp/end-to-end-apps/ScalableSentimentAnalysisBlazorWebApp) -   A sample ables to make sentiment analysis prediction/detection of what the user is writing in a very UI interactive app (Blazor based) in the client side and running an ML.NET model (Sentiment analysis based on binary-classification) in the server side.
- [optimizer.ml](https://github.com/jameschch/LeanParameterOptimization) -   A "server-less" general purpose optimization suite for algorithm parameters. Also provides offline optimization of [Quantconnect Lean](https://github.com/QuantConnect/Lean) trading algorithms. [Demo (https://optimizer.ml)](https://optimizer.ml).
- [Baseball Machine Learning Workbench](https://github.com/bartczernicki/MachineLearning-BaseballPrediction-BlazorApp) -   A web application that showcases performing what-if analysis using in-memory Machine Learning models. [Live demo](https://baseballmlworkbench-v1.azurewebsites.net).
- [BlazorML5](https://github.com/sps014/BlazorML5) -  ML5 Machine Learning for Blazor with JSInterop mechanism.

### Mobile

- [Mobile Blazor Bindings](https://aka.ms/mobileblazorbindings) - Experimental Mobile Blazor Bindings - Build native mobile apps with Blazor.

### Rapid Development Framework

- [Oqtane](https://github.com/oqtane/oqtane.framework) -   Oqtane is a CMS & Application Framework for Blazor & .NET MAUI [Oqtane](https://www.oqtane.org).
- [WalkingTec.Mvvm (WTM)](https://github.com/dotnetcore/WTM) -   A development framework based on .NET Core and EF. It supports Blazor, Vue, React and LayUI with one click code generation for CRUD, Import/Export, etc. [Website](https://wtmdoc.walkingtec.cn).

### ToDos

- [TodoApi by David Fowler](https://github.com/davidfowl/TodoApi) -   Todo application by David Fowler in .NET 7 that features an ASP.NET Core hosted Blazor WASM front end application and an ASP.NET Core REST API backend using minimal APIs.
- [ididit!](https://github.com/Jinjinov/Ididit) -   The procrastination friendly habit tracker. ake notes, manage tasks, track habits. [Demo](https://app.ididit.today/).
- [OpenHabitTracker](https://github.com/Jinjinov/OpenHabitTracker) -   Free, open source habit tracker for Web, Windows, Linux, Android, iOS and macOS. Take notes, plan tasks, track habits. [Demo](https://pwa.openhabittracker.net).
- [StudyLife](https://github.com/lukislp/studylife) -   Self-hosted study organizer: calendar, exam/study planner, focus timer, notes and a progress dashboard, with a growing family of add-ons (native app, browser extensions, CLI, VS Code, Telegram, Discord, Home Assistant...) built on Blazor WebAssembly + ASP.NET Core. [Demo](https://studylife-demo.lktec.org).

### Others

- [CleanArchitecture](https://github.com/blazorhero/CleanArchitecture) -   Clean Architecture Template for Blazor WebAssembly Built with MudBlazor Components.
- [BlazorSSR](https://github.com/danroth27/BlazorSSR) -   Server-side rendering (SSR) with Blazor components, by Steve Sanderson.
- [Flight Finder](https://github.com/aspnet/samples/tree/master/samples/aspnetcore/blazor) -   Flight Finder.
- [LinqToTwitter Blazor sample](https://github.com/JoeMayo/LinqToTwitter/tree/main/Samples/LinqToTwitter5/net48/CSharp/AspNetSamples/BlazorDemo) -   LINQ Provider for the Twitter API (Twitter Library).
- [BlazorFileReader](https://github.com/Tewr/BlazorFileReader) -   Read-only File streams in Blazor. [Demo](https://tewr.github.io/BlazorFileReader/).
- [eShopOnBlazor](https://github.com/dotnet-architecture/eShopOnBlazor) -   Migration of a traditional ASP.NET Web Forms app to Blazor.
- [BlazorChatSample](https://github.com/conficient/blazorchatsample) -   Blazor chat demo using SignalR JS client with interop.
- [Blazor.SVGEditor](https://github.com/KristofferStrube/Blazor.SVGEditor) -   A basic HTML SVG Editor written in Blazor WASM.
- [Netflix microfrontend like](https://github.com/piral-samples/netflix-demo) -   A netflix-like portal application with pilets. This sample demonstrates the use of piral to build a dynamic app consisting of various micro frontends. [Demo](https://notflix-demo.samples.piral.cloud/browse).
- [Command and Control, by David Fowler](https://github.com/davidfowl/CommandAndControl) -   This is a sample using Blazor server and SignalR to do command and control. Agents connect to the blazor server application which is hosting a SignalR Hub and we can issue various commands against the connected agents (this feature uses client results).
- [BlazorCRUD](https://github.com/thbst16/BlazorCrud) -   Sample line of business application that illustrates key features of Blazor. [Demo](https://becksblazor.azurewebsites.net/).
- [Money](https://github.com/maraf/Money) -   A money manager implemented using CQRS+ES. [Demo](https://app.money.neptuo.com/).
- [Blazor.SVGEditor](https://github.com/KristofferStrube/Blazor.SVGEditor) -   A basic HTML SVG Editor written in Blazor WASM. [Demo](https://kristofferstrube.github.io/Blazor.SVGEditor/).
- [FFmpegBlazor](https://github.com/sps014/FFmpegBlazor) -   FFmpegBlazor provides ability to utilize ffmpeg.wasm from Blazor Wasm C#. [ffmpeg.wasm](https://github.com/ffmpegwasm/ffmpeg.wasm)    is a pure Webassembly / Javascript port of FFmpeg. It enables video & audio record, convert and stream right inside browsers.
- [Blazor.MediaCaptureStreams](https://github.com/KristofferStrube/Blazor.MediaCaptureStreams) -   A Blazor wrapper for the Media Capture and Streams browser API. The API standardizes ways to request access to local multimedia devices, such as microphones or video cameras. This also includes the MediaStream API, which provides the means to control where multimedia stream data is consumed, and provides some information and configuration options for the devices that produce the media. This project implements a wrapper around the API for Blazor so that we can easily and safely interact with the media streams of the browser. [Demo](https://kristofferstrube.github.io/Blazor.MediaCaptureStreams/).
- [Planning Poker](https://github.com/duracellko/planningpoker4azure) &ndash;  An app to play Planning Poker for distributed teams. The app is implemented using Blazor and shows how to switch between client-side and server-side mode with a configuration change. [Demo](http://planningpoker.duracellko.net).
- [C# Regex Tester online](https://github.com/lsvhome/regex-tester) -  Online tool for verify .Net regex syntax. ([Demo](https://lsvhome.github.io/regex-tester/)).
- [C# Regex Online tool](https://github.com/MichaelSL/blazor-wasm-test-012020) -  Online tool for verify .Net regex syntax, see splits list, table etc. ([Demo](https://dotnet-regex.com/)).
- [Blazor Tour of Heroes](https://github.com/georgemathieson/blazor-tour-of-heroes) - Blazor Tour of Heroes, using
- [Blazor Wake-on-LAN](https://github.com/georg-jung/BlazorWoL) -  Wake-on-LAN app for local networks. Blazor Server + EF Core + DI + CI.
- [BlazingWaffles](https://github.com/gbiellem/BlazingWaffles) -  A Blazor app that wraps [Waffle Generator](https://github.com/SimonCropp/WaffleGenerator). The generator outputs readable gibberish that can be used in place of Lorum Ipsum. [Demo](http://wafflegen.azurewebsites.net/).
- [Unofficial eShopOnContainers](https://github.com/n-stefan/eshoponcontainers) -  Unofficial Blazor WebAssembly client for [eShopOnContainers](https://github.com/dotnet-architecture/eShopOnContainers).
- [BlazorAndTailwind](https://github.com/tesar-tech/BlazorAndTailwind) -   Sample project, guide and tips for setting up [TailwindCSS](https://tailwindcss.com/) in Blazor.
- [BlazorViz interop wrapper for Viz.js](https://github.com/mrzhdev/BlazorViz) -  A sample of generating Graphviz DOT language files and visualising tree data structures. [Demo](https://mrzhdev.github.io/BlazorViz/).
- [BlazorServerImageRecognitionApp](https://github.com/johnt84/BlazorServerImageRecognitionApp) -  Simple Blazor Server app which uses image recognition to identify and extract text printed in an image file uploaded by the user. [Demo](https://blazorimagerecognitionapp.azurewebsites.net/).
- [FootballBlazorApp](https://github.com/johnt84/FootballBlazorApp) -  Simple Football Blazor Server web app displaying fixtures & results, group standings, teams & players and has a player search.  [Demo](https://premierleagueblazorapp.azurewebsites.net/).
- [ComponentBuilder](https://github.com/AchievedOwner/ComponentBuilder) -  -  An automation framework to create Blazor component by `RenderTreeBuilder`.
- [Pointing Party](https://github.com/martijn/PointingParty) -  A tool for distributed agile story point estimation ceremonies, using Blazor WebAssembly and SignalR. [Demo](https://pointingparty.com).
- [SaveHere](https://github.com/gudarzi/savehere) -   Cloud Download Manager for direct links and media files from Youtube/Spotify/etc with media converter and builtin proxy to bypass restrictions.

## Tutorials

- [Blazor workshop](https://github.com/dotnet-presentations/blazor-workshop/) -  Blazor app building workshop by [.NET Foundation](https://www.dotnetfoundation.org/), Blazzing Pizza.
- [NextTechEvent by Coding After Work](https://www.youtube.com/watch?v=Z2EZXY6G5ZU) - Build "NextTechEvent", a site that will help speakers, organizers, and attendees find their next tech event. [Source code](https://github.com/CodingAfterWork/NextTechEvent)  .
- [Archives](https://github.com/AdrienTorris/awesome-blazor/tree/master/Archives) - [2021](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2021.md#tutorials), [2020](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2020.md#tutorials), [2019](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2019.md#tutorials), [2018](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2018.md#tutorials).

## Libraries & Extensions

### Component bundles

- [FAST](https://github.com/microsoft/fast) -    FAST is a collection of technologies built on Web Components and modern Web Standards, designed to help you efficiently tackle some of the most common challenges in website and application design and development. [FAST & Blazor documentation](https://www.fast.design/docs/integrations/blazor/).
- [Blazor Blueprint](https://github.com/blazorblueprintui/ui) -   A shadcn/ui inspired component library for Blazor with 75+ styled components, 15 headless primitives, and 1,640+ icons. Features a two-tier architecture with unstyled primitives for full control and pre-styled components for rapid development. Compatible with existing shadcn themes from shadcn/ui and tweakcn. [Documentation and Demo](https://blazorblueprintui.com).
- [BootstrapBlazor](https://github.com/dotnetcore/BootstrapBlazor) -   A set of enterprise-class UI components based on Bootstrap and Blazor ([Docs as Demo](https://www.blazor.zone/)).
- [Ant Design Blazor](https://github.com/ant-design-blazor/ant-design-blazor) -   A set of enterprise-class UI components based on Ant Design and Blazor. ([Docs as Demo](https://ant-design-blazor.github.io/)).
- [MudBlazor](https://github.com/MudBlazor/MudBlazor) -   MudBlazor is an ambitious Material Design component framework for Blazor with an emphasis on ease of use and clear structure. It is perfect for .NET developers who want to rapidly build web applications without having to struggle with CSS and Javascript. MudBlazor, being written entirely in C#, empowers them to adapt, fix or extend the framework and the multitude of examples in the documentation makes learning MudBlazor very easy. [Documentation](https://mudblazor.com/). [Demo](https://try.mudblazor.com/).
- [MatBlazor](https://github.com/SamProf/MatBlazor) -   MatBlazor comprises a range of components which implement common interaction patterns according to the Material Design specification. [Documents and Demo](https://www.matblazor.com/) , [BoilerPlates with MatBlazor](https://github.com/enkodellc/blazorboilerplate)
- [Blazorise](https://github.com/Megabit/Blazorise) -   Components for Blazor with support for Bootstrap, Bulma, AntDesign and Material CSS. ([Bootstrap Demo](https://bootstrapdemo.blazorise.com/)), ([Bulma Demo](https://bulmademo.blazorise.com/)), ([AntDesign Demo](https://antdesigndemo.blazorise.com/)), ([Material Demo](https://materialdemo.blazorise.com/)).
- [MASA Blazor](https://github.com/BlazorComponent/MASA.Blazor) -   A set of enterprise-class UI components based on Material Design and Blazor. It's an almost perfect copy of Vuetify, and Long-term roadmaps have been mapped out. It is powered by the MASA team and remains free and open source. [Documentation](http://blazor.masastack.com/). [Pro Demo](https://blazor-pro.masastack.com/).
- [Radzen.Blazor](https://github.com/radzenhq/radzen-blazor) -   Free and open-source (MIT, including commercial use) library of 155+ native Blazor components: DataGrid, Scheduler, Gantt, PivotDataGrid, Spreadsheet with XLSX import/export, 30+ chart types, HtmlEditor and more, with Material, Standard, Default, Humanistic and Software themes in light and dark. ([Demos](https://blazor.radzen.com/)).
- [BlazorStrap](https://github.com/chanan/BlazorStrap) -   Material Design components for Blazor. Bootstrap 4 components for Blazor ([Demo](https://chanan.github.io/BlazorStrap/)).
- [BlazorBootstrap](https://github.com/vikramlearning/blazorbootstrap) -   High-performance, lightweight, and responsive blazor bootstrap components in a single package from the developers for the developers. ([Docs as Demo](https://demos.blazorbootstrap.com/)).
- [FluentUI Blazor](https://github.com/microsoft/fluentui-blazor) -   Microsoft's official FluentUI Web Components for Blazor. ([Samples & demo](https://www.fluentui-blazor.net/)).
- [Element-Blazor](https://github.com/Element-Blazor/Element-Blazor/blob/master/README.en.md) -   A blazor component library using Element UI. API imitates Element, CSS directly uses Element's style, HTML structure directly uses Element's HTML structure. [Blazor WebAssembly Version demo](https://blazorwasm.github.io). [Blazor WebAssembly Version PWA Mode demo](https://pwawasm.github.io).
- [ComponentOne Blazor UI Components](https://www.grapecity.com/componentone/blazor-ui-controls) - External link. A fast datagrid, listview, input and other native Blazor components for server and client-side apps.
- [DevExpress Blazor UI Components](https://github.com/DevExpress/RazorComponents) -   A set of native UI Blazor components (including a Data Grid, Pivot Grid, Scheduler, and Charts) for both Blazor server-side and Blazor client-side platforms.
- [Syncfusion Blazor UI Components](https://www.syncfusion.com/blazor-components) -   The most comprehensive native Blazor component library including [Data Grid](https://www.syncfusion.com/blazor-components/blazor-datagrid), [Charts](https://www.syncfusion.com/blazor-components/blazor-charts), [Scheduler](https://www.syncfusion.com/blazor-components/blazor-scheduler), [Diagram](https://www.syncfusion.com/blazor-components/blazor-diagram) and [Document Editor](https://www.syncfusion.com/blazor-components/blazor-word-processor) components. ([Demo](https://blazor.syncfusion.com/demos/)).
- [Blazority](https://github.com/blazority/support) -   Blazor component library based on the Clarity UI design. 30+ components including Datagrid and Tree-view ([Docs & Demos](https://blazority.com)).
- [Material.Blazor](https://github.com/Material-Blazor/Material.Blazor) -   An alternative Material Theme Razor Component Library. Material.Blazor focuses sharply on giving you pure markup from [Google's material-components-web](https://github.com/material-components/material-components-web/tree/master/packages) - we don't try to sit between you and your use of Google's CSS and SASS because they do it better than we ever could. We also have some cool "plus" components. [See our demo and comprehensive documentation](https://material-blazor.com).
- [Majorsoft Blazor Components](https://github.com/majorimi/blazor-components) -   Majorsoft Majorsoft Blazor Components is a set of UI Components and other useful Extensions for Blazor applications. All components are free and available on NuGet. The main goal of this project is to provide an easy to use, feature reach set of customizable components with other useful extensions. [NuGet](https://www.nuget.org/profiles/Blazor.Components) [Demo app](https://blazorextensions.z6.web.core.windows.net/) [Docs](https://github.com/majorimi/blazor-components/tree/master/.github/docs).
- [MComponents](https://github.com/manureini/MComponents) -   Open Source MIT Blazor Components: Grid, Select, Wizard etc.
- [PanoramicData Blazor UI Components](https://github.com/panoramicdata/PanoramicData.Blazor) -   An open source library of Blazor components including Table, Tree, ToolBar and FileExplorer. [Demo](https://panoramicdata.github.io/PanoramicData.Blazor).
- [HAVIT Blazor](https://github.com/havit/Havit.Blazor) -   Bootstrap 5 components + additional components built on top of Bootstrap 5 (grid, autosuggest, message-boxes, atc.). Enterprise project template with gRPC code-first client/server communication, localization and more. [Interactive documentation & Demos](https://havit.blazor.eu).
- [Telerik UI for Blazor](https://www.telerik.com/blazor-ui) - External link (telerik.com). A native set of UI components for Blazor, including grid, charting, and calendar components.
- [Start Blazoring](https://startblazoring.com) - A Blazor starter template built using your choice of [Blazorise](https://blazorise.com/) or [MudBlazor](https://mudblazor.com), with more UI library integration coming. It offers a myriad of features such as user registration, login, password reset, two factor; user management, roles, permissioning; background workers, logging, caching, email templates, localization and many more.
- [TabBlazor](https://github.com/joadan/TabBlazor) -   Blazor Admin theme built on top of [Tabler UI](https://github.com/tabler/tabler). Minimal javascript. [Demo](https://joadan.github.io/TabBlazor/).
- [Blazor.Ionic](https://github.com/kukks/Blazor.Ionic) -   Ionic framework integration for Blazor.
- [Blazor Controls Toolkit](https://blazorct.azurewebsites.net/) - Complete toolset for implementing commercial business applications. It includes the equivalent of all Bootstrap JavaScript components, all html5 input types with widgets fallbacks, advanced editable components like DataGrid, TreeView, DetailView, ModalDetail, DetailList. All components have default customizable templates, and support virtualizazion and Drag & Drop. Component rendering is meta-data driven, so component configuration is in part automatic, and in part can be driven with data annotations. The toolset includes also query tools, to issue complex local or remote queries, changes-tracking tools to send only the changed records to the server, advanced validation attributes, globalization tools, "Behaviors" that modify existing components, state management and save, and more.
- [Blazor.WebForm.Components](https://github.com/Jurioli/Blazor.WebForm.Components) -   ASP.NET Web Forms System.Web.UI.WebControls Razor Components For Blazor WebAssembly. [Demo](https://blazorwebformdemo.github.io/).
- [BlazorOcticons](https://github.com/BlazorOcticons/BlazorOcticons) -  Github [Octicons](https://primer.style/octicons/) created as a `.razor` components and available via the NuGet package. The project [website](https://blazorocticons.net/) is an example using the generated components.
- [ABP Framework](https://github.com/abpframework/abp) -   ABP Framework is a complete infrastructure to create modern web applications by following the best practices and conventions of software development.
- [NeoUI](https://github.com/jimmyps/blazor-shadcn-ui) -   Production-ready shadcn/ui-inspired component library for Blazor. 100+ styled components, 15 headless primitives, 12 chart types, declarative animations, 3,200+ icons, zero-config pre-built CSS, WCAG 2.1 AA, dark mode, 85 theme combinations, and full .NET 10 Auto rendering mode. MIT licensed.
- [Nevron Open Vision Components for Blazor](https://www.nevron.com/products-open-vision) -   Diagram, Chart, Text Editor, Gauge, Barcode, and User Interface components for Blazor. [Demo](https://blazorexamples.nevron.com/).
- [CodeBeam.MudExtensions](https://github.com/CodeBeamOrg/CodeBeam.MudExtensions) -   Useful third party extension components for MudBlazor, from the contributors. +20 components includes Stepper, SpeedDial, Wheel, Splitter, Animate, Popup, Material 3 Switch, Gallery, CodeInput and more.  [Documentation](https://codebeam-mudextensions.pages.dev/).
- [BlazorWinOld](https://github.com/tossnet/Blazor-WinOld) -   A Blazor UI component library bringing back the retro look of Windows 98, XP, 7 and 10 desktop styles, compatible with Blazor Server and WebAssembly. [Documentation](https://tossnet.github.io/Blazor-WinOld/).

### 2D/3D Rendering engines

- [BabylonBlazor](https://github.com/AlexNek/BabylonBlazor) -   This library packages the well-known 3D library [Babylon.js](https://www.babylonjs.com/) into a Razor component that can be used in a C# Blazor project. The library is intended to use for creation of molecules visualization and used limited API of Babylon library. [Demo application](https://babylonblazorapp202208.azurewebsites.net/) which is showing different parts of library [Pubchem Viewer](https://pubchemviewer.azurewebsites.net/). Show chemical information from pubchem.ncbi.nlm.nih.gov.

#### API

- [Blazor.Canvas](https://github.com/excubo-ag/Blazor.Canvas) -   Wrapper library around the HTML canvas API written in C# (no JS dependency) ([Demo](https://excubo-ag.github.io/Blazor.Canvas/)).
- [BlazorIntersectionObserver](https://github.com/ljbc1994/BlazorIntersectionObserver) -  This is a wrapper around the [Intersection Observer API](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API).

#### Charts

- [ChartJs.Blazor](https://github.com/mariusmuntean/ChartJs.Blazor) -   Brings [ChartJs](https://github.com/chartjs/Chart.js) charts to Blazor.
- [GG.Net Data Visualization](https://github.com/pablofrommars/GGNet) -  Interactive and flexible charts for Blazor Web Apps. Taking its inspiration from the highly popular ggpplot2 R package, GG.Net provides natively rich features for your Data Analysis Workflow. Build publication quality charts with just a few lines of code. [Website](https://pablofrommars.github.io/).
- [Blazor-ApexCharts](https://github.com/apexcharts/Blazor-ApexCharts) -   Blazor wrapper for ApexCharts. [Demo](https://joadan.github.io/Blazor-ApexCharts/basic-charts).
- [Plotly.Blazor](https://github.com/LayTec-AG/Plotly.Blazor) -   Brings the charting library [plotly.js](https://github.com/plotly/plotly.js) with over 40 chart types to Blazor ([Demo](https://laytec-ag.github.io/Plotly.Blazor/)).
- [GG.Net Data Visualization](https://github.com/pablofrommars/GGNet) -   Interactive and flexible charts for Blazor Web Apps. Taking its inspiration from the highly popular ggpplot2 R package, GG.Net provides natively rich features for your Data Analysis Workflow. Build publication quality charts with just a few lines of code. [Website](https://pablofrommars.github.io/).
- [ChartJs for Blazor](https://github.com/erossini/BlazorChartjs) -   This is a NuGet package for Blazor to use ChartJs, constantly updated with new features.
- [UnlockedData.Chartist.Blazor](https://github.com/UnlockedData/UnlockedData.Chartist.Blazor) -  Blazor wrapper for [Chartist.js](http://gionkunz.github.io/chartist-js/) bundled with [Chartist.js plugins](http://gionkunz.github.io/chartist-js/plugins.html).
- [BlazorGraphs](https://github.com/EdoParis/BlazorCharts) -   This is a NuGet package to draw lightweight svg charts and gauges for Blazor without js. [blazorgraphs.it](https://www.blazorgraphs.it).

#### CSS

- [BlazorSize](https://github.com/EdCharbeneau/BlazorSize) -   BlazorSize is a JavaScript interop library for Blazor that is used to detect the Browser's current size, change in size, and test media queries.
- [RazorStyle](https://github.com/wihrl/RazorStyle) - A small utility library to allow in-component styling without duplicate `` tags. Also supports programmatically triggered animations.

#### Database

- [DexieNET](https://github.com/b-straub/DexieNET) -   DexieNET aims to be a feature complete .NET wrapper for Dexie.js the famous Javascript IndexedDB wrapper from David Fahlander. It's designed for Blazor and includes an easy to use Razor component. Now with support for DexieCloud in preview.
- [EfCoreNexus](https://github.com/thliborius/EfCoreNexus) -   EfCoreNexus helps integrating the entity framework core into your blazor app. Via reflection it adds your entitiy classes automatically and provides you with basic crud functionality.

#### Datagrids / tables

- [BlazorDatasheet](https://github.com/anmcgrath/BlazorDatasheet) -   Excel-like datasheet component with keyboard navigation, formula, filtering, sorting and more.
- [Grid.Blazor](https://github.com/gustavnavar/Grid.Blazor) -   Grid component with CRUD forms for Blazor and ASP.NET MVC, supporting filtering, sorting, searching, paging, subgrids and others ([Demo](http://gridblazor.azurewebsites.net)).
- [BlazorGrid](https://github.com/Akinzekeel/BlazorGrid) -   Virtualized data grid component with lean markup, focused on displaying remote data. ([Demo & documentation](https://blazorgrid.z6.web.core.windows.net/)).

#### Date & time

- [BlazorDateRangePicker](https://github.com/jdtcn/BlazorDateRangePicker) -   A date range picker component library for Blazor. [Demo](https://BlazorDateRangePicker.azurewebsites.net/).

#### Diagrams

- [Blazor.Diagrams](https://github.com/Blazor-Diagrams) -   Z.Blazor.Diagrams is a fully customizable and extensible all-purpose diagrams library for Blazor (both Server Side and WASM). It was first inspired by the popular React library react-diagrams, but then evolved into something much bigger. ZBD can be used to make advanced diagrams with a custom design. Even the behavior of the library is "hackable" and can be changed to suit your needs.
- [Excubo.Blazor.Diagrams](https://github.com/excubo-ag/Blazor.Diagrams) -   Interactive diagram component (flowcharts, UML, BPMN, ...), customizable and extensible according to user needs (node types, styles). [Demo](https://excubo-ag.github.io/Blazor.Diagrams/).
- [FlowState](https://github.com/sps014/FlowState) -   A high-performance node editor for Blazor. Build visual programming tools, node-based workflows, and interactive graph editors with complete styling control.

#### JavaScript

- [BlazorScriptReload](https://github.com/devessenceinc/BlazorScriptReload) -   A component which provides support for using JavaScript in Blazor Web Applications

#### Maps

- [BlazorGoogleMaps](https://github.com/rungwiroon/BlazorGoogleMaps) -   Blazor interop for GoogleMap library.
- [UnlockedData.Mapael](https://github.com/UnlockedData/UnlockedData.Mapael) -  Blazor wrapper over vector drawing/mapping library. [Jquery Mapael](https://www.vincentbroute.fr/mapael/).

#### Modal, Toast & Notifications

- [Blazored.Modal](https://github.com/Blazored/Modal) -   A JavaScript free modal library for Blazor and Razor Components applications.
- [Blazored.Toast](https://github.com/Blazored/Toast) -   A JavaScript free toast library for Blazor and Razor Component applications.
- [Blazor.Sidepanel](https://github.com/Append-IT/Blazor.Sidepanel) -   A powerful and customizable Sidepanel implementation for Blazor applications.

### Routing & Navigation

- [Blazouter](https://github.com/Taiizor/Blazouter) -   Blazouter brings modern, React Router-inspired routing to Blazor. It provides true nested routes, built-in route guards, lazy loading, per-route layouts and rich transitions — all type-safe and compatible with Server, WebAssembly, and Hybrid (MAUI) hosting models.
- [Routeables](https://github.com/cedric56/Routeables) -   Route-based MVVM navigation for Blazor (Server, WebAssembly and MAUI Hybrid): view models declare routes (`[Routeable("/dogs/{name}")]`) and navigate through a single `IRouter`, with typed route methods, regions and navigation guards. The same view models also run on MAUI, Avalonia, Uno and WPF. [NuGet](https://www.nuget.org/packages/Routeables.Razor).

#### Tabs

- [BlazorXTabs](https://github.com/David-Moreira/BlazorXTabs) -  An extended tabs component library providing various tab features for Blazor.

#### Testing

- [bUnit - a testing library for Blazor components](https://github.com/egil/bunit) -   A testing library for Blazor Components. You can easily define components under test in C# or Razor syntax and verify outcome using semantic HTML diffing/comparison logic. You can easily interact with and inspect components, trigger event handlers, provide cascading values, inject services, mock IJsRuntime, and perform snapshot testing.
- [Verify.Blazor - a snapshot testing library for Blazor components](https://github.com/VerifyTests/Verify.Blazor) -   A snapshot testing library for Blazor Components. Supports rendering Blazor Components to a snapshot file via bunit or via raw Blazor rendering.

#### Others

- [ActualLab.Fusion](https://github.com/ActualLab/Fusion) -   Skip SignalR and gRPC. Build real-time Blazor and MAUI apps while writing just 0.1% of the usual real-time update code. Handle 10× more API requests with the ActualLab.Rpc protocol—or 1000× more with Fusion’s transparent and perfectly coherent caching. [Samples](https://github.com/ActualLab/Fusion.Samples). [Documentation](https://fusion.actuallab.net/).
- [BlazorContextMenu](https://github.com/stavroskasidis/BlazorContextMenu) -   A context menu component for Blazor ([Demo](https://blazor-context-menu-demo.azurewebsites.net/)).
- [Blazored.Typeahead](https://github.com/Blazored/Typeahead) -   Auto-complete textbox with local and remote data source, for both Client-side and Server-Side Blazor.
- [Blazor-DragDrop](https://github.com/Postlagerkarte/blazor-dragdrop) -   Easy-to-use Drag and Drop library for Blazor.
- [BlazorDownloadFile](https://github.com/arivera12/BlazorDownloadFile) -   Blazor download files to the browser from c# without any JavaScript library or dependency. BlazorDownloadFile is the solution to saving files on the client-side, and is perfect for web apps that generates files on the client. However if the file is coming from the server we recommend you to first try to use Content-Disposition attachment response header as it has more cross-browser compatibility.
- [Blazor.FileSystemAccess](https://github.com/KristofferStrube/Blazor.FileSystemAccess) -   A Blazor wrapper for the browser API File System Access. The API makes it possible to read and write to your local file system from the browser both files and directories. [Demo](https://kristofferstrube.github.io/Blazor.FileSystemAccess/).
- [BlazorMemoire](https://github.com/matthetherington/Blazor-Memoire) -   A highly-performant Blazor `` component, similar to [`React.memo`](https://react.dev/reference/react/memo), that freezes its child subtree until explicit dependency keys change, preventing unnecessary re-renders and making lifecycle methods fire only when there's been a true change.
- [Blorc.PatternFly](https://github.com/WildGums/Blorc.PatternFly) -   Blazor wrappers for [PatternFly](https://www.patternfly.org). To view the latest develop branch in action, visit the [demo](http://blorc-patternfly.wildgums.com/) app.
- [Blazor PWA Updater](https://github.com/jsakamoto/Toolbelt.Blazor.PWA.Updater) -   Provide "Update Now" UI and feature to your Blazor PWA that appears when the next version of one is available.
- [BlazorTransitionableRoute](https://github.com/JByfordRew/BlazorTransitionableRoute) -   Allows current and previous route to exist enabling transition animations of UI/UX design systems.
- [Razor.SweetAlert2](https://github.com/Basaingeal/Razor.SweetAlert2) -  Blazor component implementing the popular SweetAlert2 JavaScript Library.
- [BlazorMonaco](https://github.com/serdarciplak/BlazorMonaco) -  Blazor component for Microsoft's [Monaco Editor](https://github.com/Microsoft/monaco-editor) which powers Visual Studio Code. ([Demo](https://serdarciplak.github.io/BlazorMonaco/)).
- [Blazor.Grids](https://github.com/excubo-ag/Blazor.Grids) -  Component library for CSS grids with extra features, such as moving and resizing interactively. Create your own dashboard with ease. ([Demo](https://excubo-ag.github.io/Blazor.Grids/)).
- [Blazor.TreeViews](https://github.com/excubo-ag/Blazor.TreeViews) -  Component library for tree views. ([Demo](https://excubo-ag.github.io/Blazor.TreeViews/)).
- [GEmojiSharp.Blazor](https://github.com/hlaueriksson/GEmojiSharp) -  GitHub Emoji for Blazor ([Demo](https://hlaueriksson.github.io/GEmojiSharp/)).
- [Texnomic.Blazor.hCaptcha](https://github.com/Texnomic/hCaptcha) -  hCaptcha Component for Server-Side Blazor.
- [BlazorLocalizationSample](https://github.com/LazZiya/XLocalizer.Samples/tree/master/BlazorLocalizationSample)   The default project template localized using [XLocalizer](https://github.com/LazZiya/XLocalizer) with online translation and auto resource creating.
- [TimeCalc](https://github.com/michaelrp/TimeCalc) -  An app to help keep track of speed cubing averages on the fly using Blazor WebAssembly. [Demo](https://www.timecalc.app/).
- [BlazorSliders](https://github.com/carlfranklin/BlazorSliders) -  Create multiple panels separated by sliding splitters.
- [Blazor SplitContainer](https://github.com/jsakamoto/Toolbelt.Blazor.SplitContainer) -  A Blazor component to create panes separated by a slidable splitter bar.
- [BlazorTimeline](https://github.com/Morasiu/BlazorTimeline) -   Responsive, vertical timeline component.
- [BlazorTypewriter](https://github.com/ormesam/blazor-typewriter) -  A typewriter effect for Blazor.
- [BlazorMergely](https://github.com/akovac35/BlazorMergely) -  An implementation of Blazor diff and merge component based on Mergely with server side support.
- [MetaMask.Blazor](https://github.com/michielpost/MetaMask.Blazor) -  A library that provides an easy helper to use [MetaMask](https://metamask.io/) with Blazor WebAssembly.
- [Blazor File Drop Zone](https://github.com/jsakamoto/Toolbelt.Blazor.FileDropZone/) -  Surround an "input type=file" element by this Blazor component to making a zone that accepts drag and drops files ([Demo](https://jsakamoto.github.io/Toolbelt.Blazor.FileDropZone/)).
- [Knob](https://github.com/MelihAltintas/Blazor-Knob/) -  Knob Control for Blazor.
- [BlazorCurrentDevice](https://github.com/arivera12/BlazorCurrentDevice) -  Device detection for blazor using current-device.js.
- [BlazorStyledTextArea](https://github.com/JByfordRew/BlazorStyledTextArea) -  A textarea with style. This component essentially remains and works as a textarea but can have any of the text styled based on your application needs. Its simplicity is purposefully designed to avoid the complexities and issues that come with rich text editors.
- [SignaturePad](https://github.com/MarvinKlein1508/SignaturePad) -  A simple to use blazor component to draw custom signatures. [Demo](https://marvinklein1508.github.io/SignaturePad).
- [BlazorInputTags](https://github.com/MarvinKlein1508/BlazorInputTags) -  A simple to use blazor component for both Blazor Server and WebAssembly which adds a basic tag editor to your app. [Demo](https://marvinklein1508.github.io/BlazorInputTags).
- [BlazorTooltips](https://github.com/MarvinKlein1508/BlazorTooltips) -  An implementation of Bootstrap tooltips for both Blazor Server and WebAssembly.  [Demo](https://marvinklein1508.github.io/BlazorTooltips).
- [BlazorBarcodeScanner](https://github.com/sabitertan/BlazorBarcodeScanner) -   Barcode Scanner component for Blazor using zxing-js Interop. [Demo](https://sabitertan.github.io/BlazorBarcodeScanner/).
- [Blazor Transition Group](https://github.com/le-nn/blazor-transition-group) -   A library performing animations when a Blazor component enters or leaves the DOM inspired by [react-transition-group](https://github.com/reactjs/react-transition-group).
- [BlazorGravatar](https://github.com/PSCourtney/BlazorGravatar) -   A Blazor component for integrating Gravatar, Blazor WASM, Server and SSR.
- [BlazorDragDrop](https://github.com/Postlagerkarte/Blazor-DragDrop) -   A simple drag-and-drop library for Blazor components.
- [BlazorTreeViews](https://github.com/excubo-ag/Blazor.TreeViews) -   A customizable tree view component for Blazor applications.
- [IOSwipeView](https://github.com/iolitetech/IOSwipeView) -   Fluid swipe actions and interactive list primitives for Blazor with authentic spring physics, rubber banding, and customizable deletion animations. [Demo](https://iolitetech.github.io/IOSwipeView/).
- [Linq2Dashboard](https://github.com/joadan/Linq2Dashboard) -   Interactive exploration of large in-memory collections: facets with counts, metrics and the matching rows, all updating together on every click. Core engine with no UI dependency plus Blazor components. [Demo](https://joadan.github.io/Linq2Dashboard/).
- [WebFilez](https://github.com/gordon-matt/WebFilez) -   Open source file manager for web written in Blazor. Demos available for Blazor, MVC and React.

### Tools & Utilities

- [Fluxor](https://github.com/mrpmorris/fluxor) -   Zero boilerplate Flux/Redux library for DotNet.
- [Blazored.LocalStorage](https://github.com/Blazored/LocalStorage) -   A library to provide access to local storage in Blazor applications.
- [Blazor-State](https://github.com/TimeWarpEngineering/blazor-state) -   Manage client side state in Blazor using MediatR pipeline.
- [bUnit - a testing library for Blazor components](https://github.com/egil/bunit) -   A testing library for Blazor Components. You can easily define components under test in C# or Razor syntax and verify outcome using semantic HTML diffing/comparison logic. You can easily interact with and inspect components, trigger event handlers, provide cascading values, inject services, mock IJsRuntime, and perform snapshot testing.
- [Cropper.Blazor](https://github.com/CropperBlazor/Cropper.Blazor) -   Cropper.Blazor is a component that wraps around [Cropper.js](https://github.com/fengyuanchen/cropperjs) for cropping images in Blazor. Support Blazor Server, Blazor WebAssembly, Blazor Server Hybrid with MVC and MAUI Blazor Hybrid. [Demo](https://cropperblazor.github.io/demo).
- [TextCopy](https://github.com/CopyText/TextCopy) -   A cross platform package to copy text to and from the clipboard. [Supports Blazor](https://github.com/CopyText/TextCopy#blazor-webassembly) via the [Clipboard Browser API](https://developer.mozilla.org/docs/Web/API/Clipboard).
- [CssBuilder](https://github.com/EdCharbeneau/CssBuilder) -   CssBuilder is a Builder pattern for CSS classes to be used with Razor Components.
- [Blazor.FileSystemAccess](https://github.com/KristofferStrube/Blazor.FileSystemAccess) -   A Blazor wrapper for the browser File System Access API.
- [Blazor.Polyfill](https://github.com/Daddoon/Blazor.Polyfill) -   Polyfills for Blazor (for Internet Explorer 11 support and some other browsers).
- [Blazor I18n/Localization Text](https://github.com/jsakamoto/Toolbelt.Blazor.I18nText) -   Localizing contents text in Blazor ([Demo](https://jsakamoto.github.io/Toolbelt.Blazor.I18nText/)).
- [BlazorGoogleMaps](https://github.com/rungwiroon/BlazorGoogleMaps) -   Blazor interop for GoogleMap library.
- [BlazorWorker](https://github.com/Tewr/BlazorWorker) -   Library for creating DotNet Web Worker threads/multithreading in Blazor. [Live demo](https://tewr.github.io/BlazorWorker).
- [MvvmBlazor](https://github.com/klemmchr/MvvmBlazor) -   BlazorMVVM is a small framework for building Blazor and BlazorServerside apps. With it's simple to use MVVM pattern you can boost up your development speed while minimizing the hazzle to just make it work.
- [Blazor.BrowserExtension](https://github.com/mingyaulee/Blazor.BrowserExtension) -   Develop browser extensions/addons with Blazor WebAssembly. Tested with Google Chrome, Mozilla Firefox and MS Edge.
- [Blazor Analytics](https://github.com/isc30/blazor-analytics) - Blazor extensions for Analytics.
- [Blazor PDF](https://github.com/tossnet/Blazor-PDF) -   Generate de PDF document with iTextSharp from a Blazor Server App.
- [BlazorRouter](https://github.com/hez2010/BlazorRouter) -   BlazorRouter is an awesome router inspired by react-router, providing declarative routing for Blazor.
- [DataJuggler.Blazor.FileUpload](https://github.com/DataJuggler/BlazorFileUpload) -   Wrapper for Steve Sanderson's BlazorFileInput component.
- [BlazorPrettyCode](https://github.com/chanan/BlazorPrettyCode) - Blazor Code Component for documentation sites. [Demo](https://chanan.github.io/BlazorPrettyCode/).
- [Blazor.EventAggregator](https://github.com/mikoskinen/Blazor.EventAggregator) - Lightweight Event Aggregator for Blazor (Razor Components).
- [Blazor Gamepad](https://github.com/jsakamoto/Toolbelt.Blazor.Gamepad) - Provides gamepad API access for Blazor.
- [Blazor Hotkeys2](https://github.com/jsakamoto/Toolbelt.Blazor.Hotkeys2) -   A library to provide configuration-centric keyboard shortcuts for Blazor.
- [BlazorRealm](https://dworthen.github.io/BlazorRealm/docs/quickstart.html) - Redux state management for Blazor.
- [Blazor.LocalFiles](https://github.com/jburman/W8lessLabs.Blazor.LocalFiles) - Open files in your browser and load into Blazor.
- [Blazor.SpeechSynthesis](https://github.com/jsakamoto/Toolbelt.Blazor.SpeechSynthesis) -  A library to provide Speech Synthesis API access for Blazor.
- [Blazor BarCode](https://barcoderesource.com/blazorbarcode.shtml) &ndash; A barcode library for Blazor using barcode fonts.
- [BlazorState.Redux](https://github.com/BerserkerDotNet/BlazorState.Redux) -  Develop Blazor apps with Redux.
- [Howler.Blazor](https://github.com/StefH/Howler.Blazor) -  A Blazor JSInterop wrapper for Howler.js, an audio library.
- [jsMind.Blazor](https://github.com/StefH/jsMind.Blazor) -  A Blazor JSInterop wrapper for jsMind, a MindMapping tool.
- [Blazor Highcharts](https://github.com/Allegiance-Consulting/blazor-highcharts) -  A port of the popular Highcharts library. [Demo](https://allegiance-consulting.github.io/blazor-highcharts/).
- [Blazor.LazyStyleSheet](https://github.com/excubo-ag/Blazor.LazyStyleSheet) -  Lazy loading for CSS style sheets.
- [Blazor.ScriptInjection](https://github.com/excubo-ag/Blazor.ScriptInjection) -   Smart script tags in Blazor components, ideal for lazy loading of javascript files.
- [DnetIndexedDb](https://github.com/amuste/DnetIndexedDb) -  Blazor Library for IndexedDB DOM API.
- [BlazorIndexedDbJs](https://github.com/kattunga/BlazorIndexedDbJs) -  BlazorIndexedDbJs is a wrapper arround IndexedDB DOM API, supports Blazor WASM and Server.
- [Blazor-Color-Picker](https://github.com/tossnet/Blazor-Color-Picker) -  Opens a palette with the Material colors for Blazor application.
- [Blazm.Bluetooth](https://github.com/EngstromJimmy/Blazm.Bluetooth) -  A Blazor library for connecting to devices using Bluetooth.
- [WebBluetooth](https://github.com/KeudellCoding/Blazor.WebBluetooth) -  Blazor service for the experimental WebBluetooth functions. Based on [Blazm.Bluetooth](https://github.com/EngstromJimmy/Blazm.Bluetooth).
- [BlazorApplicationInsights](https://github.com/IvanJosipovic/BlazorApplicationInsights) -  Application Insights for Blazor web applications.
- [Blazor Printing](https://github.com/Append-IT/Blazor.Printing) -  Print and save PDF documents with a native print dialog in a Blazor Server or client Application.
- [BlazorTemplater](https://github.com/conficient/BlazorTemplater) -  Use `.razor` components to render HTML strings for email content.
- [MediaSession.Blazor](https://github.com/zuozishi/MediaSession.Blazor) -  A Blazor JSInterop wrapper for Media Session API. The Media Session API provides a way to customize media notifications. ([Demo](https://zuozishi.github.io/MediaSession.Blazor/)).
- [BlazorAntivirusProtection](https://github.com/stavroskasidis/BlazorWasmAntivirusProtection) -   Antivirus protection for Blazor Wasm projects. This package attempts to guard against false positives from antiviruses that flag Blazor Wasm as malware, until Microsoft gives us an official solution.
- [Phork.Blazor.Reactivity](https://github.com/phorks/phork-blazor-reactivity) -   An unopinionated Blazor state management library that utilizes INotifyPropertyChanged and INotifyCollectionChanged .NET interfaces to automatically detect state changes in components.
- [CodeBeam.GoogleApis.Blazor](https://github.com/CodeBeamOrg/CodeBeam.GoogleApis.Blazor) -   An open-source utility package for GoogleApis in Blazor. Written from scratch and aims easiest of use.
- [Memento](https://github.com/le-nn/memento) -   A simple client-side state management container for Blazor/.NET includes redo/undo and ReduxDevTools support.
- [RxBlazorLight](https://github.com/b-straub/RxBlazorLight) -   RxBlazorLight is a simple reactive wrapper around Blazor components. For now only [MudBlazor](https://mudblazor.com/) components are supported. Build the [RxMudBlazorLightSample](https://github.com/b-straub/RxBlazorLight/tree/main/RxMudBlazorLightSample) and enjoy the reactive [Components](https://github.com/b-straub/RxBlazorLight/tree/main/RxMudBlazorLightTestBase/Components).
- [Pkl.Net](https://github.com/francescopaolopassaro/Pkl.Net) -   A type-safe configuration management library for .NET bringing Apple's **Pkl** configuration language to C#, zero external dependencies. Catches config errors (type mismatches, out-of-range values) at evaluation time instead of at runtime, with a clean typed-deserialization API, an `IConfiguration` extension for ASP.NET Core/Blazor apps, and a public MessagePack encoder/decoder.

### Others

- [Blazor Extensions Home](https://github.com/BlazorExtensions/Home) -  Home for Blazor Extensions.
- [Bolero](https://github.com/fsbolero/Bolero) -   Blazor for F# with hot reloaded templates, type-safe endpoints and routing, remoting, and much more.
- [BlazorFabric](https://github.com/limefrogyank/BlazorFabric) -   Blazor port of Microsoft UI Fabric with fluent design. ([Demo](https://blazorfabric.azurewebsites.net/)).
- [BlazorWebView](https://github.com/jspuij/BlazorWebView) -   Blazor WebView control for WPF, Android, macOS, iOS. Run Blazor on .NET Core and Mono natively inside a Webview. [Documentation](https://jspuij.github.io/BlazorWebView.Docs/pages/index.html).
- [BlazorLazyLoading](https://github.com/isc30/blazor-lazy-loading) -   Production ready lazy loading implementation. Full lazy loading support for WASM and Server (pages, components, dlls) with abstractions to implement modularization if you wish (custom endpoints, custom manifests, etc).
- [Fun.Blazor](https://github.com/slaveOftime/Fun.Blazor) -   This is a project to make F# developer to write blazor easier - Use F# for Blazor, Computation expression (CE) style DSL for internal and third party blazor libraries, Dependency injection, Adaptive and Elmish models, Giraffe style routing, Type safe style.
- [Blazor.DownloadFileFast](https://github.com/StefH/Blazor.DownloadFileFast) -   Fast download of files to the browser from Blazor without any javascript library reference or dependency. ([Demo](https://stefh.github.io/Blazor.DownloadFileFast/)).
- [SpotifyService](https://github.com/tresoneur/SpotifyService) -   A high-level Spotify API library for Blazor WebAssembly projects that enables Spotify playback in the browser, manages OAuth 2.0 authorization, provides easy access to the Spotify Web API and uses IndexedDB caching.
- [Blazor.DynamicJavascriptRuntime.Evaluator](https://github.com/jameschch/Blazor.DynamicJavascriptRuntime.Evaluator) -   Execute dynamic object expressions as Javascript in Blazor client-side apps.
- [Bionic](https://bionicframework.github.io/Documentation/) - An Ionic CLI clone for Blazor projects.
- [EventHorizon Blazor TypeScript Interop Generator](https://github.com/canhorn/EventHorizon.Blazor.TypeScript.Interop.Generator) -  This project takes in a TypeScript type definition file and creates a .NET Core project that will work with the provided Interop abstraction project.
- [Generators.Blazor](https://github.com/excubo-ag/Generators.Blazor) -  Generators.Blazor is a source generator for improving performance in Blazor. The project also contains analyzers to detect common issues in Blazor apps.
- [Blazork8s](https://github.com/weibaohui/blazork8s) -  Manage k8s using balzor with AI,like kubernetes dashboard.

## Source generators

- [BlazorOcticons](https://github.com/BlazorOcticons/BlazorOcticons)   Github [Octicons](https://primer.style/design/foundations/icons/) created as a .razor components using source generator. The generated components are available via the NuGet package, the generator itself is available as a separate NuGet package. The project website is an example using the generated components.
- [BlazorInteropGenerator](https://github.com/surgicalcoder/BlazorInteropGenerator) -   Github [Octicons](https://primer.style/design/foundations/icons/) Generates Blazor -> Javascript strongly typed interop methods, by parsing the Javascript it self and generating extension methods for IJSRuntime.
- [RazorPageRouteGenerator](https://github.com/surgicalcoder/RazorPageRouteGenerator) -   Generates methods with parameters for Razor and Blazor pages, so you can navigate without having to guess URLs or parameters.

## Real-World applications

- [Try .NET](https://github.com/dotnet/try) -   Try .NET provides developers and content authors with tools to create interactive experiences.
- [FairPlayCombined](https://github.com/pticostaricags/FairPlayCombined) -   The FairPlay platform is a set of pre-built customizable solutions created with Blazor.

## Videos

- [.NET Day Online 2026, by JetBrains](https://www.youtube.com/live/adwmjYzQhaU?si=g9SNYD-JnE3c8XPb&t=19792) - October 7, 2026 -  Escape the Monolith: Scaling Blazor with .NET Aspire and Azure Container Apps, with Michael Washington.
- [Blazor Community Standup: Build agentic experiences with the Blazor AI Components](https://www.youtube.com/watch?v=XT6KEenXgEc) - October 6, 2026 -  Modern AI applications are more than chat experiences. Learn how to use the new Blazor AI Components to build agent-centric apps where AI agents actively participate in the user experience, driving workflows, taking actions, and helping users get work done.
- [Explore the Future of ASP.NET Core & Blazor in .NET 11](https://www.youtube.com/watch?v=6c8fpShFjZE) - August 19, 2026 -  What’s next for web development on .NET? In this session, we’ll explore the future direction of ASP.NET Core and Blazor in .NET 11, highlighting the themes, priorities, and opportunities shaping the platform’s next chapter.
- [ASP.NET Community Standup: What's new in .NET 11 Preview 6?](https://www.youtube.com/watch?v=1G3d5YphhcM) - July 21, 2026 -  Join the ASP.NET Core team for a tour of what's new for ASP.NET Core and Blazor in .NET 11 Preview 6: Async minimal API validation, automatic CSRF protection, unions, OpenAPI 3.2, Blazor and SignalR improvements, and more.
- [Blazor Hybrid: One UI for Web, iOS, Android & Desktop (.NET MAUI)](https://www.youtube.com/watch?v=b9siFlZE6XQ) - July 20, 2026 -  Blazor Hybrid + .NET MAUI: build your UI once with Razor components and ship it to the browser, iOS, Android, Windows, and macOS – with full native API access from a single .NET codebase. David Ortinau, Principal Product Manager on the .NET team at Microsoft, breaks down how Blazor Hybrid works under the hood: Razor components hosted in a BlazorWebView, running in one .NET process with no web server on the device. He walks through the .NET MAUI Blazor Web App template, native platform concerns like Android safe areas, and real production-grade Blazor Hybrid apps – Sentence Studio (an AI-powered language learning app orchestrated with .NET Aspire), PolyPilot (an app the .NET MAUI team built entirely with AI agents), and MAUI Sherpa (an open-source toolbox for cross-platform developers). He also shares the .NET 11 roadmap: CoreCLR as the single runtime across platforms (WASM support still in progress), the path to Native AOT, .NET Watch everywhere, a unified Hot Reload pipeline, and MAUI DevFlow – tooling that gives AI coding agents eyes and hands inside your running app.
- [Blazor Community Standup: WebMCP in Action with Blazor](https://www.youtube.com/watch?v=D0oq45aH0RQ) - July 7, 2026 -  Yanislav Ivanov from Telerik joins us to show how Blazor components use WebMCP to expose actions directly to AI agents, enabling natural language prompts to drive real UI interactions.
- [Building for the agentic web with .NET 11](https://www.youtube.com/watch?v=vQ0y8ExNsmQ) - June 2, 2026 -  The demands on modern web apps are increasing. Users expect more performance, airtight security, and even agentic capabilities. What does the next generation of web apps look like on .NET? In .NET 11, ASP.NET Core and Blazor are getting faster and more secure at the core, closely integrated with Aspire for distributed app development, and a new set of building blocks — agents, tools, skills, and components — for building agentic web apps. Get ready to build for the modern agentic web.
- [Blazor Community Standup: ASP.NET Core & Blazor Roadmap for .NET 11](https://www.youtube.com/watch?v=XY_mM2FkxHE) - February 10, 2026 -  Join us for a walkthrough of the ASP.NET Core & Blazor roadmap for .NET 11. We’ll discuss the expected improvements for this release and share progress on current work.
- [Building Agentic UI with Blazor](https://www.youtube.com/watch?v=81k75c4U95s) - December 4, 2025 -  AI is changing the way we use software by introducing natural language, voice, and vision as core interaction modes. This shift calls for a fresh approach to UI design that empowers users through intelligent multi-modal interfaces. This talk will cover how to create agentic UIs with Blazor, using the latest AI-driven interaction patterns. We’ll share practical examples and design methods based on Microsoft’s Human-AI design principles, discuss modern agent-user interaction protocols such as AG-UI, and show how to integrate conversation interfaces into your current websites using NLWeb.
- [Be Authentic with Blazor and Microsoft Entra External ID](https://www.youtube.com/watch?v=JQXDkh6-_Bk) - November 14, 2025 -  Blazor developers love it for its fast web application building, and for building complicated applications in easily manageable modules. Blazor is a little less loved when it comes to authentication though. In this session we hope to change that! Being demo-heavy, we will first set up Microsoft Entra External ID, then we'll implement authentication in a Blazor Web Application using that External ID setup. Allowing external users - whether customers or collaborators - to access our application with RBAC security. By the end of this session, you'll have a template that you can use with your own code - and will have learned some of the traps that I have fallen into.
- [Build better web apps with Blazor in .NET 10](https://www.youtube.com/watch?v=V0Af7y7aMBE) - November 12, 2025 -  Explore the future of web development with Blazor in .NET 10! Learn how Blazor makes it easier to build secure web apps with built-in WebAuthN and passkeys support and scaffolding for adding Entra ID authentication. See how you can more easily monitor your Blazor apps and diagnose issues with improved diagnostics. Discover performance improvements that make your Blazor apps load faster and be more responsive. Finally, learn about new features and improvements that address top pain points in Blazor development, including faster Hot Reload, component state persistence, QuickGrid enhancements, simplified integration testing, and much more.
- [The Future of Web Development with ASP.NET Core & Blazor in .NET 10](https://www.youtube.com/watch?v=xZ26KwGHWE0) - August 14, 2025 -  Explore the future of web development, focusing on new features in ASP.NET Core & Blazor in .NET 10. Learn how ASP.NET Core in makes it easier to build secure AI infused web apps with the latest AI libraries and security standards, like WebAuthn & Passkey support. See how you can more easily monitor and diagnose issues with improved diagnostics and telemetry and boost developer productivity with .NET Aspire. We will also take a look into the future of Blazor for building web apps, Minimal API validation, OpenAPI generations, and more.
- [Modernizing your desktop: From WinForms to Blazor, Azure, and AI](https://www.youtube.com/watch?v=95M-4YLGsVE) - April 28, 2025 -  Got an older tech stack that’s about as fresh as last week’s leftovers? Fear not—modernizing your desktop apps is easier than you think! In this session, we’ll show you how to shift from WinForms to Blazor using .NET, land your apps in Azure for simpler, cloud-based maintenance, and even sprinkle in some AI magic to future-proof your solutions. We’ll share practical tips, real-world examples, and a few cautionary tales—no stale code left behind! Join us for a lively exploration of how to bring your legacy applications roaring into the future.
- [Unboxing Blazor in .NET 10 Preview 2](https://www.youtube.com/watch?v=yBw_KOz1vCA) - April 2, 2025 -  Dan shares the latest enhancements for web developers in .NET 10 Preview 2.
- [Archives](https://github.com/AdrienTorris/awesome-blazor/tree/master/Archives) - [2024](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2024.md#videos), [2023](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2023.md#videos), [2022](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2022.md#videos), [2021](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2021.md#videos), [2020](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2020.md#videos), [2019](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2019.md#videos), [2018](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2018.md#videos), [2017](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2017.md#videos).

## Articles

- [Announcing .NET 11](https://devblogs.microsoft.com/dotnet/announcing-dotnet-11/) - November 10, 2026 - .NET 11 is here with C# 15, faster developer tools, runtime and library improvements, and new capabilities for web, mobile, desktop, and AI apps.
- [Get Ready for .NET Conf 2026!](https://devblogs.microsoft.com/dotnet/get-ready-for-dotnet-conf-2026/) - November 3, 2026 - Join Microsoft November 10-13 for this free, four-day virtual conference and the official launch of .NET 11. We’ll kick things off with two days of sessions from Microsoft product teams, followed by two days of community-led talks from developers around the world.
- [Blazor Welcomes Open-Source Contributions from Infragistics](https://devblogs.microsoft.com/dotnet/blazor-welcomes-infragistics/) - October 27, 2026 - Microsoft is pleased to welcome Infragistics as an active contributor to Blazor! Infragistics has made more than 50 of its Blazor controls free and open source, and its engineers are contributing directly to the framework. Their work includes new Blazor analyzers for .NET 11 and tooling to help you get started with their components.
- [Should I break down my Blazor page into multiple components?](https://www.blazrlytics.com/blog/should-i-break-down-my-blazor-page-into-multiple-components) - October 6, 2026 - Article describing the pros and cons about breaking down a Blazor page into multiple components.
- [Promptless AI-First Blazor Apps](https://www.telerik.com/blogs/promptless-ai-first-blazor-apps) - October 6, 2026 - Normally when we think about AI-based applications, we often think of chat-style apps. These apps consist mainly of a text box, some buttons to add context like images, and a button to start a conversation with an LLM model. However, we can talk about another type of AI-based applications, with a Promptless AI-First approach. Let’s see what it’s about.
- [Visual Studio 2022 Preview release notes](https://learn.microsoft.com/en-us/visualstudio/releases/2022/release-notes-preview#blazorwasmdebuggerimprovements) - July 9, 2024 - This release focuses on quality-of-life enhancements for all developers and workloads. When you use Visual Studio, you want to feel empowered and productive. That's why quality-of-life features are so important: they make coding a smooth and enjoyable experience, free of unnecessary hassles and headaches. We hope you'll love this update.
- [Blazor Basics: Blazor Render Modes in .NET 8](https://www.telerik.com/blogs/blazor-basics-blazor-render-modes-net-8) - June 12, 2024 - This article is about the new Blazor render modes in .NET 8, including ServerInteractivity, WebAssemblyInteractivity, AutoInteractivity and static server-side rendering (SSR).
- [The usage of Blazor.Diagrams](https://www.slaveoftime.fun/blog/the-usage-of-blazor.diagrams) - June 11, 2024 - How to use Blazor.Diagrams.
- [Blazor in .NET 9 Takes Shape (Preview 4 Highlights)](https://www.telerik.com/blogs/blazor-net-9-takes-shape-preview-4-highlights) - June 4, 2024 - .NET 9 is shaping up ahead of its November 2024 release. Here are the highlights for Blazor so far.
- [Avoiding interactivity with Blazor?](https://jonhilton.net/avoiding-blazor-interactivity/) - May 29, 2024 - Avoiding interactivity with Blazor.
- [.NET Announcements & Updates from Microsoft Build 2024](https://devblogs.microsoft.com/dotnet/dotnet-build-2024-announcements/) - May 21, 2024 - .NET Announcements & Updates from Microsoft Build 2024.
- [Archives](https://github.com/AdrienTorris/awesome-blazor/tree/master/Archives) - [2023](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2023.md#articles), [2022](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2022.md#articles), [2021](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2021.md#articles), [2020](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2020.md#articles), [2019](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2019.md#articles), [2018](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2018.md#articles), [2017](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2017.md#articles).

## Podcasts

- [MAUI and Blazor with Beth Massi](https://www.dotnetrocks.com/details/1903) - June 20, 2024 - What's up with MAUI and Blazor? Carl and Richard chat with Beth Massi about the latest MAUI, including the new webview available on GitHub that lets you embed an existing web page into your MAUI app. Beth talks about making apps the way you want to - with a mobile, web, or desktop focus - or making them all! Mixing Blazor and MAUI means you can steer clear of XAML if you prefer. There's no right way to build your clients, and MAUI gives you many choices. Duration: 45 minutes.
- [Chris Sainty: Blazor in Action - Azure DevOps Episode 238](http://azuredevopspodcast.clear-measure.com/chris-sainty-blazor-in-action-episode-238) - March 27, 2023 - Chris is a Microsoft MVP, author, and software engineer with over 17 years of experience with ASP.NET. Passionate about sharing his knowledge with the community, he regularly writes both for his own blog as well as others — such as Visual Studio magazine, Progress Telerik, and StackOverflow. This passion for blogging led to his first book, Blazor in Action, a practical guide to building Blazor applications. He also maintains several popular open-source projects under the GitHub organization, Blazored. When not tapping on a keyboard, Chris is a keen speaker, having delivered talks at both user groups and conferences all over the world. Duration: 41 minutes.
- [.NET Rocks - Blazor United with Javier Nelson and Steve Sanderson](https://www.dotnetrocks.com/details/1838) - March 23, 2023 - What if you didn't have to choose between client-side and server-side Blazor? Carl and Richard talk to Javier Nelson and Steve Sanderson about Blazor United in its early stages of development, providing flexibility at the web component level for client- and server-side rendering. At the simplest level, Blazor United offers server-side rendering when a site is first hit so that you can load the larger client-side components over time. But deeper is the idea that some elements on your web page benefit from being client-side, and some from being server-side, and why should you have to choose only one? Duration: 53 minutes.
- [Steve Sanderson - Blazor, WASI and optimizing tomatoes](https://www.youtube.com/watch?v=1r3FwkUEte0) - July 17, 2022 - At NDC London we sat down with Steve Sanderson and talked about the origin story of Blazor, some of the upcoming things in .NET 7, and what Steve is working on right now. Duration: 35 minutes.
- [WASM Everywhere with Steve Sanderson](https://www.dotnetrocks.com/default.aspx?ShowNum=1801) - July 7, 2022 - WebAssembly is awesome - what else can you do with it? While at NDC London, Carl and Richard talked to Steve Sanderson about his work with WebAssembly, including Blazor. Steve talks about how WebAssembly continues to evolve adding WebAssembly System Integration. This opens the door to the idea that code in the WebAssembly can be run anywhere - any operating system, any language, using whatever compute is available. That gives an option to run code on the client, the server, and anywhere in between. Duration: 55 minutes.
- [Indexing Video using KlipTok with Jeff Fritz](https://www.dotnetrocks.com/default.aspx?ShowNum=1796) - June 2, 2022 - How do you find a great video clip after the fact? Carl and Richard talk to Jeff Fritz about his work building KlipTok, a tool for making Twitch video clips more discoverable and shareable. Jeff digs into the tricky bits of KlipTok, which is all about fast indexing and searching to get to the right clip. The conversation digs into various data storage techniques and using the cloud in a way that doesn't break the bank. Jeff may be a Microsoft employee, but that doesn't mean he uses only Microsoft tools for his projects. Duration: 57 minutes.
- [David Ortinau on .NET MAUI](https://herdingcode.com/herding-code-246-david-ortinau-on-net-maui/) - May 27, 2022 - Jon Galloway talks to David Ortinau about [.NET MAUI](https://docs.microsoft.com/en-us/dotnet/maui/what-is-maui). Duration: 41 minutes. [YouTube video](https://www.youtube.com/watch?v=OyqzWAivI7I).
- [The Unhandled Exception Podcast: Microsoft Build 2022](https://unhandledexceptionpodcast.com/posts/0037-build/) - May 25, 2022 - Microsoft have just had their annual Build conference - which comes with a whole host of exciting announcements and discussions about hot programming topics in the Microsoft developer space. And each year, I long for a podcast episode to come out straight after Build, overviewing them! Well, this year - this podcast aims to do just that! In this episode, I was joined by both Scott Hunter and Gaurav Seth to chat about various topics. Check out the links below for a guide to what we discussed. Duration: 71 minutes.
- [ASP.NET, Blogging, Kuberetes, and more](https://unhandledexceptionpodcast.com/posts/0036-andrewlock/) - May 10, 2022 - The Unhandled Exception Podcast with Andrew Lock (andrewlock.net). He’s the author of the Manning ebook, ASP.NET Core in Action, Second Edition. This episode covers a lot - from the different flavours of ASP.NET, to Kubernetes, Blazor, gRPC, testing, Minimal API, MediatR and more.
- [Umbraco Heartcore and Blazor with Poornima Nayar](https://dotnetcore.show/episode-93-umbraco-heartcore-and-blazor-with-poornima-nayar/) - May 4, 2022 - In this episode we talked with Poornima Nayar about Umbraco Heartcore and where you might use it, Blazor, a little on GraphQL and how it fits very well with mobile apps which communicate with remote APIs. Duration: 59 minutes.
- [In The Core of Blazor](https://www.youtube.com/watch?v=IF_7DPddmcs) - February 12, 2022 - Steve Sanderson talks about his journey into tech, his life, education, career and everything else in between. Duration: 73 minutes.
- [Archives](https://github.com/AdrienTorris/awesome-blazor/tree/master/Archives) - [2021](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2021.md#podcasts), [2020](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2020.md#podcasts), [2019](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2019.md#podcasts), [2018](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2018.md#podcasts), [2017](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2017.md#podcasts).

## Presentations slides

- [Using .NET 5 with the Raspberry Pi](https://www.slideshare.net/PGallagher69/using-net-5-with-the-raspberry-pi) - January 28, 2021 - Using .NET 5 with the Raspberry Pi, on Slideshare.
- [Archives](https://github.com/AdrienTorris/awesome-blazor/tree/master/Archives) - [2020](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2020.md#presentations-slides), [2019](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2019.md#presentations-slides), [2018](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2018.md#presentations-slides).

## Tooling

- [LiveSharp](https://github.com/ionoy/LiveSharp) -   Update `.razor` files and see the updates instantly without reloading the page. Your application state is preserved because there is no need to reload anything. [livesharp.net](https://www.livesharp.net/).
- [Blazor Developer Tools](https://github.com/joe-gregory/blazor-devtools) -   The first visual DevTools for Blazor. Browser extension that adds a "Blazor" tab to Chrome/Edge DevTools with component tree visualization, timeline profiler, flamegraph, and "why did this render?" diagnostics. No code changes required for basic tracking. [blazordevelopertools.com](https://blazordevelopertools.com/).
- [BlazorFiddle](https://blazorfiddle.com) - Blazor .Net Developer Playground and Code Editor in the Browser.
- [Ghostly Hosting](https://github.com/Nix1983/Ghostly-Hosting) -   An interactive CLI tool that turns a fresh Ubuntu VPS into a production-ready hosting environment for Blazor Server apps with automatic SSL, DNS, GitHub deployments, and nginx reverse-proxy.
- [Blazor Minimum Project Templates](https://github.com/jsakamoto/BlazorMinimumTemplates) -   A project templates package of Blazor apps without JavaScript and CSS libraries.
- [Blazor REPL](https://github.com/BlazorRepl/BlazorRepl) -   Write, compile, execute and share Blazor components entirely in the browser - https://blazorrepl.com.
- [Blazor Snippets Visual Studio Code extension](https://marketplace.visualstudio.com/items?itemName=ScottSauber.blazorsnippets) - A Visual Studio Code extension that offers Blazor and Razor snippets.
- [Publish-time Pre-render for Blazor Wasm](https://github.com/jsakamoto/BlazorWasmPreRendering.Build) -  When you publish your Blazor WebAssembly app, this package pre-renders and saves the app as static HTML files in your public folder.
- [Publish SPA for GitHub Pages](https://github.com/jsakamoto/PublishSPAforGitHubPages.Build) -  Add this NuGet package to your Blazor WebAssembly project to easily publish it to GitHub Pages.
- [WebCompiler](https://github.com/excubo-ag/WebCompiler) -   A dotnet global tool for compilation, minification, and compression of scss, css and js.
- [.NET Core](https://www.microsoft.com/net/download/dotnet-core) - .NET Core.
- [Razor+ Visual Studio Code extension](https://marketplace.visualstudio.com/items?itemName=austincummings.razor-plus) - A Visual Studio Code extension that offers improved Razor support.
- [Tracetool](https://github.com/capslock66/Tracetool#Blazor-client--server) -   Tracetool viewer, client Api for Dotnet, Java, Javasvript, C++ , Python, Delphi.
- [Visual Studio](https://www.visualstudio.com/vs/preview) - Latest preview of Visual Studio.
- [Visual Studio Code](https://code.visualstudio.com/) - Visual Studio Code, free, open source and cross-platform code editor.

## Books

- [Learning Blazor](https://learning.oreilly.com/library/view/learning-blazor/9781098113230) - Build Single-Page Apps with WebAssembly and C# (By David Pine via O'Reilly Early Release February 3rd, 2022).
- [Microsoft Blazor: Building Web Applications in .NET 6 and Beyond](https://www.amazon.com/Microsoft-Blazor-Building-Applications-Beyond/dp/1484278445) - A practical and hands-on approach to learning Blazor using .NET 6. (3rd ed. edition (December 8, 2021).
- [Blazor WebAssembly by Example](https://www.amazon.com/Blazor-WebAssembly-Example-project-based-building-ebook/dp/B095X7FH6M) - Blazor WebAssembly by Example: A project-based guide to building web apps with .NET, Blazor WebAssembly, and C# (1st edition published the July 9th, 2021).
- [Blazor in Action](https://www.manning.com/books/blazor-in-action) - An example-driven guide to building reusable UI components and web frontends—all with Blazor, C#, and .NET. (Manning Early Access Program began October 2020).
- [Microsoft Blazor: Building Web Applications in .NET](https://www.amazon.com/Microsoft-Blazor-Building-Applications-NET/dp/1484259270/ref=pd_sbs_2/144-0745230-5007239?pd_rd_w=LPinn&pf_rd_p=3676f086-9496-4fd7-8490-77cf7f43f846&pf_rd_r=V7CQTYC0W8RZAVPVVXA1&pd_rd_r=b34ab9d9-09dd-4eca-9207-f56311bde8d2&pd_rd_wg=9V1tA&pd_rd_i=1484259270&psc=1) - Microsoft Blazor: Building Web Applications in .NET (Second edition published in May 2020).
- [Blazor Revealed](https://www.apress.com/gp/book/9781484243428) - Blazor Revealed, Building Web Applications in .NET (Published February, 2019).
- [Blazor Quick Start Guide: Build web applications using Blazor, EF Core, and SQL Server](https://www.amazon.in/gp/product/178934414X/ref=awesome_blazor) - Blazor Quick Start Guide: Build web applications using Blazor, EF Core, and SQL Server (Published October 31, 2018).
- [Building Blazor Applications: A Developer's Guide](https://www.amazon.com/Building-Blazor-Applications-Developers-Guide/dp/B0DDBG4S3Q/ref=sims_dp_d_dex_ai_speed_loc_mtl_v5_t1_d_sccl_1_2/136-3795973-8719321?pd_rd_w=coqfA&content-id=amzn1.sym.da3a5e11-8f5f-413b-a68b-31ceac43c758&pf_rd_p=da3a5e11-8f5f-413b-a68b-31ceac43c758&pf_rd_r=9Q8447GTE9QT4WTPH5Z6&pd_rd_wg=IAqx1&pd_rd_r=ff570237-8604-4432-b4cd-a726ce880b23&pd_rd_i=B0DDBG4S3Q&psc=1) - Building Blazor Applications: A Developer's Guide (Published August 14, 2024).
- [Mastering Blazor UI: Advanced Custom Components and Design Strategies](https://www.amazon.com/Mastering-Blazor-UI-Components-Strategies/dp/B0DG2RJD1R/ref=sr_1_1?crid=SK6RU9T2BOGD&dib=eyJ2IjoiMSJ9.s5wnoFiu-YggQzMUNkXdPUUkrmyKJs-ffmHU1vbgjlJYGeFcYE04oohzd7hcoj9zCTyfe-R07XyKNQvyU5t7Mw.NRJ3TXh3AQZpXwXQmV5IoCPC9y1T-ybHWaoO9G9DvFY&dib_tag=se&keywords=blazor+gallivan&qid=1728060552&s=books&sprefix=blazor+gallivan%2Cstripbooks%2C127&sr=1-1) - Mastering Blazor UI: Advanced Custom Components and Design Strategies (Published September 3, 2024).

## E-Books

- [Blazor WebAssembly Succinctly](https://www.syncfusion.com/ebooks/blazor_webassembly_succinctly) - August 31, 2020 - Blazor is a framework for creating SPA webpages with either client-side or server-side architectures, using Razor technology written with the C# language. Because client-side Blazor with WebAssembly executes entirely on a user's browser, it’s very fast for many applications. In Blazor WebAssembly Succinctly, Michael Washington will take readers through the core elements of Blazor and then explore additional features by building a sample application. Free e-book.
- [Blazor Succinctly](https://www.syncfusion.com/ebooks/blazor-succinctly) - April 16, 2020 - A free e-book for starting with the Blazor framework.
- [Blazor, A Beginners Guide](https://www.telerik.com/campaigns/blazor/wp-beginners-guide-ebook) - March 18, 2020 - A free e-book for getting started with the Blazor framework. [Examples source code](https://github.com/EdCharbeneau/BlazorBookExamples).
- [Blazor for ASP.NET Web Forms developers](https://dotnet.microsoft.com/learn/aspnet/architecture#blazor-for-web-forms-devs-ebook-swim) - Blazor for ASP.NET Web Forms developers, a free e-book from Microsoft.
- [Using CSLA 5: Blazor and WebAssembly](https://store.lhotka.net/using-csla-5-blazor-and-webassembly) - This book covers the new Blazor UI framework, including how to create server-side and client-side WebAssembly projects, how to implement authentication and authorization, and how to use data binding. It then covers how CSLA .NET supports Blazor, including walking through a complete sample app.
- [An Introduction to Building Applications with Blazor](https://www.amazon.com/Introduction-Building-Applications-Blazor-applications-ebook/dp/B07WPQTT6H) - August 24, 2019 - An Introduction to Building Applications with Blazor: How to get started creating applications using this exciting easy to use Microsoft C# framework
- [Archives](https://github.com/AdrienTorris/awesome-blazor/tree/master/Archives) - [2018](https://github.com/AdrienTorris/awesome-blazor/blob/master/Archives/2018.md#e-books).

## Courses

- [Build a web app with Blazor WebAssembly and Visual Studio Code](https://docs.microsoft.com/learn/modules/build-blazor-webassembly-visual-studio-code/) - Build a web app with Blazor WebAssembly and Visual Studio Code, on Microsoft Learn.
- [DevOps and Docker Support for .NET Core Blazor Applications](https://www.udemy.com/course/devops-and-docker-support-for-net-core-blazor/?ranMID=39197&ranEAID=w6JuN00t%2Fzo&ranSiteID=w6JuN00t_zo-Kv09UYco3AqwmZkipiMIXw&utm_source=aff-campaign&LSNPUBID=w6JuN00t%2Fzo&utm_medium=udemyads) - June 2020 - DevOps and Docker Support for .NET Core Blazor Applications, on Udemy. This Docker Support Course with DevOps concepts using ASP.NET Core Blazor will teach you Dockerisation of Blazor Apps.
- [Programming in Blazor - ASP.NET Core 3.1](https://www.udemy.com/course/programming-in-blazor-aspnet-core) - Create interactive web applications with C#, on Udemy.
- [Creating Blazor Components](https://www.pluralsight.com/courses/creating-blazor-components) - December, 2019 - Building a Blazor app is building components. This course is essential for gaining a good understanding of components. On Pluralsight.
- [Authentication and Authorization in Blazor Applications](https://www.pluralsight.com/courses/authentication-authorization-blazor-applications) - December, 2019 - Learn how to secure your Blazor application using a variety of best practice techniques for authentication and authorization. On Pluralsight.
- [Blazor: Getting Started](https://www.pluralsight.com/courses/getting-started-blazor) - December, 2019 - Learn how to build your first application in a hands-on way using Blazor, Microsoft's solution to use C# to write interactive web UIs without JavaScript. On Pluralsight.
- [Blazor In-Depth Workshop (Blaze Invaders)](https://www.csharpacademy.com/courseinfo/2ccff0ac-4d3e-4d25-9368-6c1474640de5) - December 2019 - Blazor In-Depth Workshop (Blaze Invaders), on C# Academy. Learn serious Blazor concepts while building a working browser based game.
- [Blazor and Razor Components in a nutshell](https://www.udemy.com/course/blazor-and-razor-components-in-a-nutshell/) - October 2019 - Learn how to use a framework that allows you to run your compiled code directly in the browser on top of WebAssembly, a course on Udemy.
- [Blazor on ASP.NET Core 3.0](https://www.skillshare.com/site/join?teacherRef=102575464&t=Blazor-on-ASP.NET-Core-3.0&sku=1662883580) - October 2019 - Blazor on ASP.NET Core 3.0, a course on SkillShare.
- [Blazor First Look on LinkedIn Learning](https://www.linkedin.com/learning/blazor-first-look) - Blazor First Look on LinkedIn Learning. [Source code](https://github.com/Dedac/Beam) .
- [Free Blazor Training Course](https://www.devexpress.com/support/training/blazor/) - DevExpress Blazor free training course [Source code](https://github.com/DevExpress/blazor-training-samples) .
- [Getting Started with Blazor](https://codered.eccouncil.org/course/getting-started-with-blazor) - June 2021 - Discover the Core Concepts of Blazor and learn to create web applications with ease.

## Community

- [Awesome Blazor on Twitter](https://twitter.com/awesomeblazor) - This repository's Twitter feed.
- [BuiltOnBlazor](https://builtonblazor.net) - A showcase of sites running on Blazor
- [Discord](https://discord.com/channels/732297728826277939/732297874062311424) - Blazor channel on the DotNetEvolution discord server.
- [Gitter](https://gitter.im/aspnet/Blazor) - Blazor discussion on Gitter.
- [I Love DotNet](https://github.com/ILoveDotNet/ilovedotnet) -   - This is a .NET knowledge sharing platform with live demos crafted by developers for developers with love using .NET Blazor. [ilovedotnet.org](https://www.ilovedotnet.org).
- [Learn Blazor](https://learn-blazor.com/) - Community documentation on Blazor.
- [Blazor Help Website](https://blazorhelpwebsite.com/) - Blogs and code samples primarily covering server-side Blazor.
- [Practical samples of Blazor](https://github.com/dodyg/practical-aspnetcore/tree/master/projects/blazor) - Practical samples of Blazor.
- [Practical samples of Blazor Server-Side](https://github.com/dodyg/practical-aspnetcore/tree/master/projects/blazor-ss) - Practical samples of Blazor Server-Side.
- [Reddit](https://www.reddit.com/r/Blazor/) - Blazor subreddit.
- [Stack Overflow](https://stackoverflow.com/questions/tagged/blazor) - Blazor questions feed on Stack Overflow.
- [Twitter](https://twitter.com/hashtag/blazor) - Hashtag on Twitter.
- [WebAssemblyMan](https://www.webassemblyman.com/) - Man page for Blazor and WebAssembly.

## Other Languages

- [Blaze of Code](https://blazeofcode.com/) - [Portuguese] Blog about Blazor.
- [Blazor.ru](https://blazor.ru/) - [Russian] Old official documentation website translated in Russian.
- [DevApps.be's podcast #44](http://devapps.be/podcast/blazor-webassembly/) - [French] DevApps.be's podcast #44: "Blazor et WebAssembly vont-ils tuer JavaScript ?".
- [DevApps.be's podcast #47](http://devapps.be/podcast/47-typescript-uno-angular-docfx/) - [French] DevApps.be's podcast #47: "Actualités : TypeScript, Uno, Angular, DocFX, Database".
- [Modern web apps with Blazor](https://media.aspitalia.com/events/VS2019-Blazor.media) - [Italian] Video about Blazor.
- [Blazor Developer Italiani](https://blazordev.it/) - [Italian] Italian Blazor community website with useful articles and events.
- [Playlist - Programando en Blazor](https://www.youtube.com/playlist?list=PL0kIvpOlieSNdIPZbn-mO15YIjRHY2wI9) - [Spanish] Series of videos about Blazor.
- [Insights from the oracle](http://blog.ppedv.de/?tag=Blazor) - [German] Blog about Blazor.
- [ASP.NET Core Blazor 5.0: Blazor WebAssembly und Blazor Server: Moderne Single-Page-Web-Applications mit .NET, C# und Visual Studio](https://www.amazon.de/exec/obidos/ASIN/393427935X/itvisions-21) - German book on Blazor (Published September 15, 2020 with montly Updates).
