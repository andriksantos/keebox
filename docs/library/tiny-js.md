---
title: "Tiny JS – Awesome List with 79 resources"
description: "79 curated Tiny JS resources: Frontend libraries that fit into 2 kB with dependencies."
---

# Tiny JS

Frontend libraries that fit into 2 kB with dependencies.

!!! info "Source"
    79 resources imported from [thoughtspile/awesome-tiny-js](https://github.com/thoughtspile/awesome-tiny-js), dedicated to the public domain ([CC0 / Unlicense](https://creativecommons.org/publicdomain/zero/1.0/)). Thanks to its maintainers and contributors. Part of the [KEEBOX Library](index.md) · Category: **Front-End Development**.

<!-- kb-about:start -->

## About this list

**Tiny JS** — frontend libraries that fit into 2 kB with dependencies. This page brings together 79 links about Tiny JS, grouped into 13 sections. The largest sections are **Text Search**, **State Managers**, **UI Frameworks**, a good place to start if you are exploring the topic for the first time. It belongs to the **Front-End Development** category of the KEEBOX Library; see the related lists at the end of the page for neighbouring topics.

### What you'll find

- **UI Frameworks** — 8 links
- **Event Emitters** — 3 links
- **State Managers** — 12 links
- **Routers and URL Utils** — 6 links
- **API Layer** — 4 links
- **I18N** — 4 links
- **Dates and Time** — 8 links
- **Generic Utilities** — 4 links
- **Validation** — 5 links
- **Unique ID Generation** — 4 links
- **Colors** — 4 links
- **Touch Gestures** — 4 links
- …and 1 more sections

<!-- kb-about:end -->

## UI Frameworks

- [preact](https://github.com/preactjs/preact) - React-like API (pre-hooks). Cool ecosystem of similarly tiny tools and components. Highly recommended.
- [hyperapp](https://github.com/jorgebucaran/hyperapp) - vDOM framework with pure JS syntax and immutable state,
- [redom](https://github.com/redom/redom) - Hyperapp-style templates with _imperative_ event listeners and updates,
- [fre](https://github.com/frejs/fre) - React-like library with hooks and concurrency,
- [van](https://github.com/vanjs-org/van) - vDOM-based framework optimized for no-build setups,
- [superfine](https://github.com/jorgebucaran/superfine) - Hyperapp with state & effect hooks removed,
- [arrowjs](https://github.com/justin-schroeder/arrow-js) - Tagged templates + reactive data,
- [umbrella](https://github.com/franciscop/umbrella) - jQuery-style DOM manipulation library,

## Event Emitters

- [mitt](https://github.com/developit/mitt) - Plain event emitter that I use on most projects,
- [nanoevents](https://github.com/ai/nanoevents) - Nicer unsubscribe API, but no `*` event,
- [onfire.js](https://github.com/hustcc/onfire.js) - Also has `.once` method,

## State Managers

- [zustand](https://github.com/pmndrs/zustand) - Simple stores with pleasant actions and selectors. Vanilla , React
- [nanostores](https://github.com/nanostores/nanostores) - Modular store with good tree-shaking support,  vanilla, + React  extra. Supports all the top frameworks.
- [exome](https://github.com/marcisbee/exome) - Atomic stores with lots of framework connectors,  + React  extra. Supports all the top frameworks.
- [storeon](https://github.com/storeon/storeon) - Minimal redux-styled store with lots of framework connectors, . React extra  + Vue, Svelte, Angular.
- [unistore](https://github.com/developit/unistore) - Centralized store with actions,  + React
- [teaful](https://github.com/teafuljs/teaful) - Store with useState-like API, , including React / preact connector.

### Signals

- [@preact/signals](https://github.com/preactjs/signals) - The OG signals from preact  core,  with react integration.
- [usignal](https://github.com/WebReflection/usignal) - A smaller signal implementation,
- [hyperactiv](https://github.com/elbywan/hyperactiv) - 4 functions to make objects observable and listen to changes,
- [flimsy](https://github.com/fabiospampinato/flimsy) - Signals from Solid (it _almost_ fit into UI frameworks category itself). Author warning: _it's probably buggy._

### Reactive Programming

- [flyd](https://github.com/paldepind/flyd) - Rx-styled event streams,
- [callbag-basics](https://github.com/staltz/callbag-basics) - Rx-style event streams,

## Routers and URL Utils

- [wouter](https://github.com/molefrog/wouter) - Declarative router for React / preact, , also available as a standalone hook:
- [@nanostores/router](https://github.com/nanostores/router) - Routes as a nanostores store (framework-agnostic),
- [navaid](https://github.com/lukeed/navaid) - History-based observable router,
- [matchit](https://github.com/lukeed/matchit) - Route parser and matcher in
- [regexparam](https://github.com/lukeed/regexparam) - Convert path to regexp in
- [qss](https://github.com/lukeed/qss) - Parse querystrings in . Not sure you need it, [URL API](https://developer.mozilla.org/en-US/docs/Web/API/URL) support is good.

## API Layer

- [redaxios](https://github.com/developit/redaxios) - Drop-in axios replacement for modern browsers,
- [wretch](https://github.com/elbywan/wretch) - Chainable API with error processing and lots of extra plugins,
- [gretchen](https://github.com/truework/gretchen) - Chainable API with type-safe errors,
- [unfetch](https://github.com/developit/unfetch) - Loose fetch polyfill,

## I18N

- [@nanostores/i18n](https://github.com/nanostores/i18n) - Detect locale, load dictionaries, format dates / numbers,  including nanostores.
- [eo-locale](https://github.com/ibitcy/eo-locale) - Interpolation and dates / numbers, , or  with react bindings.
- [rosetta](https://github.com/lukeed/rosetta) - Bare-bones template strings (`{ {hello}}, { {username}}`) and custom functions for everyting else,
- [lingui](https://github.com/lingui/js-lingui) - Small core with template strings,

## Dates and Time

- [date-fns](https://github.com/date-fns/date-fns/) - Not tiny as a whole, but [most functions](https://bundlephobia.com/package/date-fns) are under 1 kB each (format and parse are quite heavy).
- [dayjs](https://github.com/iamkun/dayjs) - _Almost_ moment.js-compatible API, covers most use cases,
- [tinytime](https://github.com/aweary/tinytime) - Simple date / time formatter: `{h}:{mm} -> 9:33`,
- [tinydate](https://github.com/lukeed/tinydate) - Date / time formatter, only supports padded numeric output (`September -> 09`),
- [time-stamp](https://github.com/jonschlinkert/time-stamp) - More of the same,
- [ms](https://github.com/vercel/ms) - Parse & format ms durations, e.g. `"1m"  60000`,
- [timeago.js](https://github.com/hustcc/timeago.js) - Format dates into stuff like _X minutes ago_ or _in X hours,_
- [fromnow](https://github.com/lukeed/fromnow) - More of the same,

## Generic Utilities

- [remeda](https://github.com/remeda/remeda) - 90 tree-shakable helpers [(list).](https://bundlephobia.com/package/remeda)
- [rambda](https://github.com/selfrefactor/rambda) - 187 tree-shakable helpers [(list).](https://bundlephobia.com/package/rambda)
- [just](https://github.com/angus-c/just) - 82 helpers in separate packages [(list).](https://anguscroll.com/just/)
- [@fxts/core](https://github.com/marpple/FxTS) - 96 tree-shakable helpers. Lazy evaluation support.

## Validation

- [v8n](https://github.com/imbrn/v8n) - zod-style API with fine-grained checks: `v8n().string().minLength(5).first("H").last("o")`. No tree shaking,
- [banditypes](https://github.com/thoughtspile/banditypes) - The smallest validation library:
- [superstruct](https://github.com/ianstormtaylor/superstruct) - The most popular modular validation library with good tree-shaking,
- [valibot](https://github.com/fabian-hiller/valibot) - Another modular validation library,
- [deep-waters](https://github.com/antonioru/deep-waters) - Composable functional validators, .

## Unique ID Generation

- [@lukeed/uuid](https://github.com/lukeed/uuid) - Real UUIDs,
- [nanoid](https://github.com/ai/nanoid) - Random IDs with larger alphabet,
- [uid](https://github.com/lukeed/uid) - More of the same,
- [hexoid](https://github.com/lukeed/hexoid) - Hexadecimal IDs,

## Colors

- [colord](https://github.com/omgovich/colord) - Manipulate colors and convert between spaces, . Extra features come as plugins, 150b to 1.5 kB each.
- [colr](https://github.com/stayradiated/colr) - More of the same,
- [polychrome](https://github.com/cdonohue/polychrome) - More of the same,
- [randomcolor](https://github.com/davidmerfield/randomColor) - Attractive random colors with configuration.

## Touch Gestures

- [alloyfinger](https://github.com/AlloyTeam/AlloyFinger) - Pan, swipe, tap, doubletap, longpress, _and_ pinch / rotate. My personal favorite. .
- [tinygesture](https://github.com/sciactive/tinygesture) - Configurable pan, swipe, tap, doubletap, longpress. .
- [pointer-tracker](https://github.com/GoogleChromeLabs/pointer-tracker) - Unified interface for mouse, touch and pointer events,
- [detect-it](https://github.com/rafgraph/detect-it) - Detect present and primary input method (touch / mouse) and supported events,

## Text Search

- [js-search](https://github.com/bvaughn/js-search) - Feature-rich and customizable: multi-field indices, stop words, custom stemmers and tokenizers.
- [ndx](https://github.com/localvoid/ndx) - Similar to js-search, differs in [ranking](https://kmwllc.com/index.php/2020/03/20/understanding-tf-idf-and-bm-25/) and is less strict for multi-word queries [(compare)](https://leeoniya.github.io/uFuzzy/demos/compare.html?libs=js-search,ndx,Wade&search=twilight%20sag). Supports field weights.
- [wade](https://github.com/kbrsh/wade) - Also similar, [(compare)](https://leeoniya.github.io/uFuzzy/demos/compare.html?libs=js-search,Wade,ndx&search=twilight%20sag)
- [libsearch](https://github.com/thesephist/libsearch) - Index-free search (slower, but easier to use) with sane ordering
- [stemmer](https://github.com/words/stemmer) -
- [porter-stemmer](https://github.com/jedp/porter-stemmer) -

### Fuzzy search

- [fuzzy](https://github.com/mattyork/fuzzy) - Index-free, can highlight matches.
- [fuzzy-search](https://github.com/wouterrutgers/fuzzy-search) - With stateful index.
- [fzy.js](https://github.com/jhawthorn/fzy.js) - Matches one string at a time, tree-shakeable scores and match highlighting.  total, or ~150 bytes for `hasMatch` only.
- [fuzzysearch](https://github.com/bevacqua/fuzzysearch) -  One string at a time, does not compute score / rank.
- [liquidmetal](https://github.com/rmm5t/liquidmetal) - Quicksilver algorithm, prioritizes matches at start of word for command abbreviations (e.g. `gp` -> `git push`). One string at a time.
- [quick-score](https://github.com/fwextensions/quick-score) - Another quicksilver-based lib, tweaked for long strings. Built-in list filtering and sorting,  or 1.2 kB for single-string scoring.
- [fuzzyset](https://github.com/Glench/fuzzyset.js) - Find misspellings, e.g. missipissi -> Missisipi,  Commercial usage costs $42.

<!-- kb-related:start -->

## Related lists

More lists in the **Front-End Development** category of the [KEEBOX Library](index.md):

- [Tips](tips.md)
- [Web Animation](web-animation.md)
- [Web Audio](web-audio.md)
- [Web Components](web-components.md)
- [Svelte](svelte.md)
- [SVG](svg.md)
- [Tailwind CSS](tailwind-css.md)
- [Text Editing](text-editing.md)

<!-- kb-related:end -->
