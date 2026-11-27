"""Append original guide + FAQ sections to the hub pages flagged by Google
as 'Crawled - currently not indexed'. Idempotent (marker comments)."""
import re, sys, os
DOCS = sys.argv[1]
A, B = '<!-- kb-guide:start -->', '<!-- kb-guide:end -->'

G = {}

G['gamedev'] = '''## How to choose an engine

The right tool depends more on the game you want to finish than on the most powerful feature list:

- **2D games and first projects:** Godot, Defold or GameMaker let you see results in a few hours. Godot is free and open source with no royalties; GameMaker has its own scripting language and a long track record with indie hits.
- **3D and larger teams:** Godot 4, O3DE and Stride cover 3D. If you need console ports or an asset store, compare licensing terms carefully before committing.
- **Code-first developers:** frameworks like raylib, LÖVE, MonoGame or Bevy give you full control and no editor lock-in, at the cost of building more tools yourself.
- **Browser games:** Phaser for 2D and Babylon.js for 3D run anywhere without installation, which is ideal for game jams and portfolios.

A practical rule: make one very small game — a single level, start to finish — with two candidate engines before deciding. You will learn more from that than from any comparison table.

## Frequently asked questions

??? question "What is the best free game engine for beginners?"
    Godot is the most common recommendation: it is free, open source, lightweight and has a large community with tutorials in English and Spanish. Defold and GameMaker are also beginner-friendly options for 2D.

??? question "Do I need to know how to draw to make a game?"
    No. Many developers start with free asset packs and placeholder shapes. Tools such as Aseprite, Blender, Tiled and LDtk help when you are ready to create your own art and levels.

??? question "Where can I publish my first game?"
    itch.io is the easiest place for free or pay-what-you-want games and game jam entries. Steam and mobile stores require more preparation, fees and store assets.

## Keep exploring

- [GameMaker resources](library/gamemaker.md) · [libGDX](library/libgdx.md) · [Haxe game development](library/haxe-game-development.md)
- [Game engine development](library/game-engine-development.md) · [Game production](library/game-production.md) · [Learn game development](library/learn-gamedev.md)
- [Open-source games](library/open-source-games.md) · [Game datasets](library/game-datasets.md)
'''

G['mobile'] = '''## Native or cross-platform?

Most teams today start with a cross-platform framework and go native only where they need it:

- **Flutter** compiles to native code and draws its own UI, so apps look identical on Android and iOS. A strong choice for custom, brand-heavy interfaces.
- **React Native with Expo** is the fastest path for teams that already know React and JavaScript or TypeScript. Expo handles builds, updates and many device APIs for you.
- **Kotlin Multiplatform and Compose Multiplatform** share business logic (and optionally UI) while keeping full access to native platform code. Popular with Android teams moving into iOS.
- **Ionic and Capacitor** wrap a web app in a native shell. Good for internal tools and content apps when you already have a web front end.
- **Native (Kotlin or Swift)** is still the best option for apps that depend heavily on the camera, background work, widgets or the newest platform features.

Whatever you choose, plan early for push notifications, deep links, offline storage, analytics and app store review — they take more time than the first screens.

## Frequently asked questions

??? question "Which framework should I learn first for mobile apps?"
    If you already know JavaScript, start with React Native and Expo. If you are starting from zero or want a very polished custom UI, Flutter is easier to learn as a whole package. For an Android-only career, learn Kotlin and Jetpack Compose.

??? question "Can I build an iOS app without a Mac?"
    You can write and test the code on Windows or Linux with Flutter or Expo, and use cloud build services such as Expo EAS to produce the iOS build. To publish on the App Store you still need an Apple Developer account.

??? question "How do I test a mobile app on real devices?"
    Use the emulators included with Android Studio and Xcode for daily work, then test on at least one real low-end Android phone. Tools such as Maestro and Detox automate end-to-end tests on devices.

## Keep exploring

- [iOS development](ios.md) · [Swift](swift.md) · [Flutter resources](library/flutter.md) · [Android resources](library/android.md)
- [Mobile web development](library/mobile-web-development.md) · [Testing & QA](testing.md)
'''

G['testing'] = '''## Building a testing strategy

A useful way to plan tests is the testing pyramid: many fast unit tests, fewer integration and API tests, and a small set of end-to-end tests that cover the flows that make you money.

1. **Unit tests** (Jest, Vitest, pytest, JUnit) check functions and components in milliseconds. Run them on every save and every commit.
2. **API and contract tests** catch breaking changes between services before they reach users. Mock external services so tests stay reliable.
3. **End-to-end tests** (Playwright, Cypress) simulate a real user in a browser. Keep them focused on critical paths such as sign-up, checkout and login.
4. **Load tests** (k6, Locust) show how your system behaves under traffic before a launch or a marketing campaign.
5. **Visual tests** compare screenshots to catch layout bugs that functional tests miss.

Run everything in continuous integration, and treat flaky tests as bugs: a test suite nobody trusts is worse than a smaller one that always tells the truth.

## Frequently asked questions

??? question "Playwright or Cypress?"
    Both are excellent. Playwright supports Chromium, Firefox and WebKit, multiple tabs and several languages (JavaScript, Python, Java, .NET). Cypress has a very friendly interactive runner and is popular in JavaScript front-end teams. For new projects, Playwright is the more flexible default.

??? question "How much test coverage do I need?"
    There is no universal number. Aim for high coverage of business logic and critical flows, and do not chase 100% on simple glue code. A rising coverage trend matters more than a fixed target.

??? question "What should I test first in a project with no tests?"
    Start with an end-to-end test of the most important user flow, then add unit tests every time you fix a bug, so the same bug cannot return.

## Keep exploring

- [Testing resources in the Library](library/testing.md) · [Playwright](library/playwright.md) · [Selenium](library/selenium.md) · [k6 load testing](library/k6.md)
- [DevOps](devops.md) · [Security](security.md)
'''

G['extensions'] = '''## Building a productive setup

Extensions are most useful when they remove friction you feel every day. A good starting setup for most developers:

- **Code quality:** a formatter (Prettier) and a linter (ESLint or your language's equivalent) configured to run on save, plus Error Lens to show problems inline.
- **Git:** GitLens or the built-in source control view to see who changed a line and why.
- **Language support:** the official extension for each language you use, which provides IntelliSense, debugging and refactoring through the language server.
- **Browser:** developer tools for your framework (React, Vue), an accessibility checker and a JSON viewer.

Install extensions one at a time and remove the ones you have not used in a month. Too many extensions slow down the editor and can conflict with each other. Prefer extensions from verified publishers, since they can read your code and files.

## Frequently asked questions

??? question "VS Code, Neovim or a JetBrains IDE?"
    VS Code is the most popular free editor and has the largest extension marketplace. Neovim is fast and keyboard-driven, ideal if you enjoy configuring your own tools. JetBrains IDEs (IntelliJ, PyCharm, WebStorm) offer deeper refactoring out of the box.

??? question "Are browser extensions safe for developers?"
    Only install extensions you need, from known publishers, and review the permissions they request. Use a separate browser profile for development so test extensions do not have access to your personal accounts.

??? question "How do I share my extension setup with my team?"
    In VS Code, add a `.vscode/extensions.json` file with recommended extensions to the repository, and commit shared settings like formatter rules in `.vscode/settings.json` or in `.editorconfig`.

## Keep exploring

- [Neovim](library/neovim.md) · [Vim](library/vim.md) · [WebExtensions](library/webextensions.md)
- [Online tools](online-tools.md) · [Cheatsheets](cheatsheets.md)
'''

for slug, body in G.items():
    p = os.path.join(DOCS, slug + '.md')
    s = open(p, encoding='utf-8').read()
    s = re.sub(re.escape(A) + r'.*?' + re.escape(B) + r'\n*', '', s, flags=re.S).rstrip() + '\n'
    s += '\n' + A + '\n\n' + body.strip() + '\n\n' + B + '\n'
    open(p, 'w', encoding='utf-8').write(s)
    print(slug, len(s.split()), 'words')
