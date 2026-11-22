---
title: "Progressive Enhancement – Awesome List with 52 resources"
description: "52 curated Progressive Enhancement resources: Curated Progressive Enhancement resources."
---

# Progressive Enhancement

Curated Progressive Enhancement resources.

!!! info "Source"
    52 resources imported from [jbmoelker/progressive-enhancement-resources](https://github.com/jbmoelker/progressive-enhancement-resources), dedicated to the public domain ([CC0 / Unlicense](https://creativecommons.org/publicdomain/zero/1.0/)). Thanks to its maintainers and contributors. Part of the [KEEBOX Library](index.md) · Category: **Front-End Development**.
## The Concept

- [Progressive Enhancement: It's about the content](http://cognition.happycog.com/article/progressive-enhancement-its-about-the-content) - Sharing content is the core of the web. Progressive Enhancement ensures access to content.
- [The Role of Enhancement in Web Design](https://www.nngroup.com/articles/enhancement/) - From the concept of enhancement to the criteria and rules for enriching the user interface.
- [Understanding Progressive Enhancement](http://alistapart.com/article/understandingprogressiveenhancement) - Apply technologies in an intelligent way, layer-upon-layer, to craft an amazing experience.
- [Designing with Progressive Enhancement](https://www.filamentgroup.com/dwpe/) - *The book* (400+ pages) on Progressive Enhancement.
- [Adaptive Web Design](http://adaptivewebdesign.info/2nd-edition/) - Book on Progressive Enhancement from content to design and interaction.
- [Detecting (HTML5) features](http://diveinto.html5doctor.com/detect.html) - Intro to different feature detection techniques with examples and demos.
- [Progressive Web Apps](https://infrequently.org/2015/06/progressive-apps-escaping-tabs-without-losing-our-soul/) - Enhancing web sites into native-like apps (progressive, not hybrid).

## Strategies

- [The Content-out Approach](https://articles.uie.com/progressive_enhancement/) - Provide wide access to content without technological restrictions.
- [Make the page usable with only HTML](https://www.gov.uk/service-manual/technology/using-progressive-enhancement#make-the-page-usable-with-only-html) - This sets the baseline for every device and browser.
- [Test Driven Progressive Enhancement](http://alistapart.com/article/testdriven) - Core functional experience enhanced after testing capabilities.
- [Cut the mustard](http://responsivenews.co.uk/post/18948466399/cutting-the-mustard) - Set a threshold for collection of enhancements.
- [Grade components, not browsers](https://www.filamentgroup.com/lab/grade-the-components.html
- [Feature vs Browser vs Form factor detection](http://www.html5rocks.com/en/tutorials/detection/) - As different strategies to tune your app to its environment.
- [Server-side device detection](https://www.smashingmagazine.com/2014/07/server-side-device-detection-with-javascript/) - Use user-agent and other HTTP header info combined with a device database to conditionally serve files.
- [Writing polyfills](https://addyosmani.com/blog/writing-polyfills/) - If your baseline is still too high for some browsers, consider [polyfills](https://remysharp.com/2010/10/08/what-is-a-polyfill) (aka [Regressive Enhancement](https://twitter.com/SlexAxton/status/25600963629)).
- [Application Shell Architecture](https://medium.com/google-developers/instant-loading-web-apps-with-an-application-shell-architecture-7c0c2f10c73) - Setup for instant loading web apps.

## Feature Detection

- [CSS feature queries](https://www.sitepoint.com/an-introduction-to-css-supports-rule-feature-queries/) ([`CSS.supports()`](https://developer.mozilla.org/en/docs/Web/API/CSS/supports) & [`@supports()`](https://developer.mozilla.org/en-US/docs/Web/CSS/@supports)) - Natively test if specific CSS feature is supported using JS method or CSS declaration.
- [Feature Detect ES6](https://www.npmjs.com/package/feature-detect-es6) - Detect which ES2015 features are available.
- [SVG requiredFeatures](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/requiredFeatures) - Render SVG elements only if their `[requiredFeatures]` evaluate to true.
- [Modernizr](https://modernizr.com/) - Extensive feature detection suite (supports custom builds).
- [Feature.js](http://featurejs.com/) - Lightweight feature detection suite.
- [Conditioner.js](http://conditionerjs.com/) - Conditionally load JS modules based on directives in HTML attributes.
- [EnhanceJS](https://www.filamentgroup.com/lab/introducing-enhancejs-smarter-safer-apply-progressive-enhancement.html) - Lets you asynchronously load CSS & JS after a set pre-defined feature tests.

## Testing Methods

- [Open Device Lab](https://opendevicelab.com/) - Lets you *test manually on actual devices* (for free).
- [Text browsers](https://en.wikipedia.org/wiki/Text-based_web_browser) - Good way to test if your content is accessible at the baseline. Try [Lynx](http://lynx.browser.org/) for example.
- [Testing in Opera Mini](https://dev.opera.com/articles/making-sites-work-opera-mini/#testing-in-opera-mini) - Download the app, emulate on desktop, setup to test local websites. (Opera Mini accounts for over 5% browser usage world wide)
- [cURL](https://curl.haxx.se/docs/manual.html) - Web page to see the pre-rendered source code of a page.
- [Browserling](https://www.browserling.com/) - Lets you manually test web pages in different versions of browsers on Windows and Android platforms.
- [Run Internet Explorer using Virtual Machines](https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/mac/) - To test IE browsers on other platforms.
- [Device emulators and simulators](https://developers.google.com/web/tools/chrome-devtools/iterate/device-mode/testing-other-browsers?hl=en#device-emulators-and-simulators)
- [Configure *Desired Capabilities* in Selenium](https://github.com/SeleniumHQ/selenium/wiki/DesiredCapabilities) - Run automated browser tests in different scenarios.
- Continuously run automated tests in different browsers using [BrowserStack](https://www.browserstack.com/), [Saucelabs](https://saucelabs.com/) or other alternatives.
- [Lighthouse](https://github.com/GoogleChrome/lighthouse) - Audit and meassure performance of Progressive Web Apps (via cli or [Chrome extension](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk)).
- [Progressive Enhancement checklist (1st edition, HTML)](http://adaptivewebdesign.info/1st-edition/read/chapter-6.html#the-progressive-enhancement-checklist), [Checklist of 2nd edition (PDF)](http://adaptivewebdesign.info/2nd-edition/checklist.pdf) - Actionable list to check you've applied Progressive Enhancement best practices. Part of [Adaptive Web Design book](http://adaptivewebdesign.info/).
- [CSS Feature Toggles](https://chrome.google.com/webstore/detail/css-feature-toggles/aeinmfddnniiloadoappmdnffcbffnjg) - Chrome DevTools extension to toggle support of selected CSS features for testing progressive enhancement fallbacks.

## Examples

### Custom Form Elements

- [Fancy radio buttons](https://www.sitepoint.com/replacing-radio-buttons-without-replacing-radio-buttons/) - Based on HTML radio buttons, visually enhanced using CSS pseudo classes and elements.
- [Checkboxes & radio buttons](https://www.filamentgroup.com/dwpe/checkbox-radiobutton/) - With custom focus, hover and checked state. Enhanced asynchronously.
- [Toggle switch](https://ghinda.net/css-toggle-switch/) - Checkbox or radios, visually enhanced to sliding toggle switches using CSS only.
- [5-star rating](http://lea.verou.me/2011/08/accessible-star-rating-widget-with-pure-css/) - Based on HTML radio buttons, visually enhanced using CSS pseudo classes and elements.
- [jQuery slider](https://github.com/filamentgroup/jQuery-Slider) - Accessible, custom slider widget based on a standard HTML select.
- [jQuery custom file input](https://www.filamentgroup.com/lab/jquery-custom-file-input-book-designing-with-progressive-enhancement.html) - Article and library.
- [React isomorphic form](https://github.com/ghengeveld/react-isomorphic-form/) - Set of React form components which can be pre-rendered & handled server-side. They are enhanced client-side without losing state.

### Data Visualisations

- [Timeline](https://css-tricks.com/progressive-enhancement-data-visualizations/) - From definition list to SVG illustration (article with demos).
- [Charts](https://www.filamentgroup.com/lab/update-to-jquery-visualize-accessible-charts-with-html5-from-designing-with.html) - From data table to themed charts using HTML5 canvas (article and library).

### Images

- [Responsive Carousel](http://filamentgroup.github.io/responsive-carousel/test/functional/fade-auto.html) - List of images enhanced into responsive carousel with various behaviour options.
- [Lazy Progressive Enhancement](https://github.com/tvler/lazy-progressive-enhancement) - Lazy load images inside `` tags. (note: Evergreen browsers only)

### Menus

- [Progressive hamburger menu](http://heydonworks.com/practical_aria_examples/#hamburger) - List of links in footer enhanced to off-canvas menu.

### Page Navigation

- [Barba.js](http://barbajs.org/) - Add page transitions with event hooks, cache and prefetch support.
- [SmoothState.js](https://github.com/miguel-perez/smoothState.js) - Add page transitions with event hooks, cache and prefetch support. (requires jQuery).
- [jquery-pjax](https://github.com/defunkt/jquery-pjax) - Add page transitions with support for multiple containers / content slots (requires jQuery).
- [MoOx/pjax](https://github.com/MoOx/pjax) - Similar tot jquery-pjax, but without the jQuery dependency.
- [Turbolinks](https://github.com/turbolinks/turbolinks) - Add page transitions with event hooks and cache support. Has adapters to bind to native navigation controls on iOS and Android.
