---
title: "PageSpeed Metrics – Awesome List with 62 resources"
description: "62 curated PageSpeed Metrics resources: Metrics to help understand page speed and user experience."
---

# PageSpeed Metrics

Metrics to help understand page speed and user experience.

!!! info "Source"
    62 resources imported from [csabapalfi/awesome-pagespeed-metrics](https://github.com/csabapalfi/awesome-pagespeed-metrics), dedicated to the public domain ([CC0 / Unlicense](https://creativecommons.org/publicdomain/zero/1.0/)). Thanks to its maintainers and contributors. Part of the [KEEBOX Library](index.md) · Category: **Front-End Development**.

<!-- kb-about:start -->

## About this list

**PageSpeed Metrics** — metrics to help understand page speed and user experience. This page brings together 58 links about PageSpeed Metrics, grouped into 5 sections. The largest sections are **Concepts**, **Rendering metrics**, **Other metrics**, a good place to start if you are exploring the topic for the first time. It belongs to the **Front-End Development** category of the KEEBOX Library; see the related lists at the end of the page for neighbouring topics.

### What you'll find

- **Concepts** — 21 links
- **Rendering metrics** — 13 links
- **Interactivity metrics** — 7 links
- **Network metrics** — 7 links
- **Other metrics** — 10 links

<!-- kb-about:end -->

## Concepts

### Lab Data (Synthetic Measurements)

- [Lighthouse](https://developers.google.com/web/tools/lighthouse/) - A tool built on Google Chrome to audit web pages. You can run it from Chrome DevTools, a Chrome Extension or from the command line (even with headless Chrome).
- [Google PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/) - Free and hosted Lighthouse reporting (and more) by Google.
- [WebpageTest](https://www.webpagetest.org/) - Free and hosted web performance testing (also an open source project).
- [Sitespeed.io](https://www.sitespeed.io/) - A set of open source performance monitoring tools.
- [Calibre](https://calibreapp.com) - Web performance monitoring SaaS.
- [treo.sh](https://treo.sh/) - Web performance monitoring SaaS.
- [SpeedCurve](https://speedcurve.com/) - Web performance monitoring SaaS.
- [AwesomeTechStack](https://awesometechstack.com/) - Website awesomeness monitoring Tool.

### Field Data (Real User Monitoring - RUM)

- [Performance tracking with Google Analytics (GA)](https://philipwalton.com/articles/the-google-analytics-setup-i-use-on-every-site-i-build/#performance-tracking)
- [Chrome User Experience Report (CrUX)](https://developers.google.com/web/tools/chrome-user-experience-report/)
- [Load abandonment](https://developers.google.com/web/updates/2017/06/user-centric-performance-metrics#load_abandonment) - Track  `visibilitychange` to account for survivorship bias.
- [SpeedCurve LUX](https://speedcurve.com/features/lux/) - Real User Monitoring SaaS.
- [Akamai mPulse](https://www.akamai.com/uk/en/products/performance/mpulse-real-user-monitoring.jsp) - Real User Monitoring SaaS.
- [Sematext Experience](https://sematext.com/experience/) - Real User Monitoring SaaS.
- [Perfume.js](https://zizzamia.github.io/perfume/) - Open Source Library to collect Field Data.
- [Web Vitals](https://github.com/GoogleChrome/web-vitals) - Open Source Library to collect Field Data.
- [Vercel Analytics](https://vercel.com/docs/analytics) - Real User Monitoring based on Web Vitals.

### Critical rendering path

- [Critical rendering path](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/)

### Long tasks

- [Spec - Long Tasks](https://w3c.github.io/longtasks/)
- [Blogpost - Tracking CPU with Long Tasks API](https://calendar.perfplanet.com/2017/tracking-cpu-with-long-tasks-api/)

### User-centric metrics

- [Docs - User-centric Performance Metrics - web.dev](https://web.dev/user-centric-performance-metrics/)
- Is it happening? - Did the navigation start successfully? Has the server responded? (e.g [FCP](https://github.com/csabapalfi/awesome-web-performance-metrics/#first-contentful-paint-fcp))
- Is it useful/meaningful? - Has enough content rendered that users can engage with it? (e.g. [LCP](https://github.com/csabapalfi/awesome-web-performance-metrics/#largest-contentful-paint-lcp))
- Is it usable - Can users interact with the page, or is it still busy loading? (e.g [TBT](https://github.com/csabapalfi/awesome-web-performance-metrics/#total-blocking-time-tbt))

## Rendering metrics

### First Contentful Paint (FCP)

- [Docs - FCP - web.dev](https://web.dev/fcp/)
- [Spec - Paint Timing - W3C](https://w3c.github.io/paint-timing/)

### Largest Contentful Paint (LCP)

- [Docs - LCP - web.dev](https://web.dev/largest-contentful-paint/)
- [Spec - LCP - W3C](https://github.com/WICG/largest-contentful-paint#readme)

### Cumulative Layout Shift (CLS)

- [Docs - CLS - web.dev](https://web.dev/cls/)
- [Spec - Layout Instability API - W3C](https://github.com/WICG/layout-instability)

### Visually Complete

- [Docs - Visually Complete - WPT](https://sites.google.com/a/webpagetest.org/docs/using-webpagetest/metrics/speed-index)

### Speed Index

- [Docs - Speed Index - web.dev](https://web.dev/speed-index/)
- [Docs - Speed Index - WPT](https://sites.google.com/a/webpagetest.org/docs/using-webpagetest/metrics/speed-index)
- [Talk - Speed Perception and Lighthouse](https://ldnwebperf.org/sessions/speed-perception-and-lighthouse/)

### (Hero) Element Timing

- [Docs - Last Painted Hero - WPT](https://github.com/WPO-Foundation/webpagetest/blob/master/docs/Metrics/HeroElements.md)
- [Spec - Element Timing API](https://wicg.github.io/element-timing/)
- [Blogpost - Hero Element Timing - SpeedCurve](https://speedcurve.com/blog/web-performance-monitoring-hero-times/)

## Interactivity metrics

### Time to Interactive (TTI)

- [Docs - TTI - web.dev](https://web.dev/tti/)
- [Spec - TTI - Lighthouse](https://docs.google.com/document/d/1GGiI9-7KeY3TPqS3YT271upUVimo-XiL5mwWorDUD4c/edit)
- [Blogpost - TTI](https://blog.dareboost.com/en/2019/05/measuring-interactivity-time-to-interactive/)

### Total Blocking Time (TBT)

- [Docs - TBT - web.dev](https://web.dev/tbt/)

### First Input Delay (FID)

- [Docs - FID - web.dev](https://web.dev/fid/)
- [Polyfill - FID](https://github.com/GoogleChromeLabs/first-input-delay)

### Max Potential First Input Delay

- [Docs - Max Potential FID - web.dev](https://web.dev/lighthouse-max-potential-fid/)

## Network metrics

- [Blogpost - Navigation and Resource Timing](https://developers.google.com/web/fundamentals/performance/navigation-and-resource-timing/)
- [Spec - Navigation Timing](https://www.w3.org/TR/navigation-timing-2/)
- [Spec - Resource Timing](https://www.w3.org/TR/resource-timing-2/)

### TCP and SSL/TLS latency

- Lab: See [Qualys SSL Labs](https://www.ssllabs.com/ssltest/index.html) for an audit

### Transferred bytes

- [Sitespeed.io PageXray](https://www.sitespeed.io/documentation/pagexray/)
- [Lighthouse Performance Budgets](https://developers.google.com/web/tools/lighthouse/audits/budgets)
- [Can You Afford It?: Real-world Web Performance Budgets](https://infrequently.org/2017/10/can-you-afford-it-real-world-web-performance-budgets/)
- [Which third party scripts are most excessive](https://github.com/patrickhulce/third-party-web)

## Other metrics

### Google PageSpeed Insights score

- [About PageSpeed Insights](https://developers.google.com/speed/docs/insights/v5/about)
- [What's in the Google PageSpeed score](https://medium.com/expedia-group-tech/whats-in-the-google-pagespeed-score-a5fc93f91e91)
- [How Google Pagespeed works](https://calibreapp.com/blog/how-pagespeed-works/)

### User Timing

- [Spec - User Timing](https://www.w3.org/TR/user-timing/)

### Server Timing

- [Docs - Server Timing](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Server-Timing)

### Frame rate

- [Docs - Frame Timing API](https://developer.mozilla.org/en-US/docs/Web/API/Frame_Timing_API)
- [Docs - Chrome Devtools - FPS](https://developers.google.com/web/tools/chrome-devtools/evaluate-performance/#analyze_frames_per_second)
- [Docs - Firefox Developer Tools - Frame rate](https://developer.mozilla.org/en-US/docs/Tools/Performance/Frame_rate)

### DOMContentLoaded

- [Docs - `DOMContentLoaded`](https://developer.mozilla.org/en-US/docs/Web/Events/DOMContentLoaded)

### window.load

- [Docs - `window.load`](https://developer.mozilla.org/en-US/docs/Web/Events/load)

<!-- kb-related:start -->

## Related lists

More lists in the **Front-End Development** category of the [KEEBOX Library](index.md):

- [Polymer](polymer.md)
- [Progressive Enhancement](progressive-enhancement.md)
- [Progressive Web Apps](progressive-web-apps.md)
- [Protips](protips.md)
- [MDBootstrap](mdbootstrap.md)
- [Mobile Web Development](mobile-web-development.md)
- [Motion UI Design](motion-ui-design.md)
- [Offline-First](offline-first.md)

<!-- kb-related:end -->
